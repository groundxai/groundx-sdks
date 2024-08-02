# coding: utf-8

import hashlib
import json
import logging
from queue import Queue, Empty
from threading import get_ident, Thread, Event, Lock
import os
from pathlib import Path
import requests
import signal
import time
from typing import Union, List


TRACE_LEVEL_NUM = 5
logging.addLevelName(TRACE_LEVEL_NUM, "TRACE")


def trace(self, message, *args, **kws):
    if self.isEnabledFor(TRACE_LEVEL_NUM):
        self._log(TRACE_LEVEL_NUM, message, args, **kws)


logging.Logger.trace = trace
logger = logging.getLogger(__file__)
logging.basicConfig(
    level=logging.DEBUG,
    format="[groundx] - %(levelname)s - %(message)s",
)


LOCK_FILE = "xray_uploader.lock"
MAX_CALLS_PER_MINUTE = 600
NUM_WORKERS = 5
TOKEN_BUCKET_INTERVAL = 60 / MAX_CALLS_PER_MINUTE
UPLOAD_LOG_FILE = "xray_uploader.log.json"


class XRayUploader:
    def __init__(self, lock_file=None, upload_log_file=None):
        self.lock_file = lock_file or LOCK_FILE
        self.queue = Queue()
        self.token_bucket = Event()
        self.token_bucket.set()
        self.upload_log_file = upload_log_file or UPLOAD_LOG_FILE
        self.uploaded_files = self._load_uploaded_files_log()
        self.token_thread = None
        self.threads = []
        self.stop_event = Event()
        self.exception_lock = Lock()
        self.exception = None

        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGHUP, self._handle_signal)

        self._check_lock_file()

    def _check_lock_file(self):
        if os.path.exists(self.lock_file):
            try:
                with open(self.lock_file, "r") as f:
                    pid = int(f.read().strip())
                os.kill(pid, 0)
            except (ValueError, ProcessLookupError, PermissionError):
                logger.warning(f"Stale lock file found. Removing {self.lock_file}.")
                self._remove_lock_file()

    def _clear_uploaded_files_log(self):
        if os.path.exists(self.upload_log_file):
            try:
                os.remove(self.upload_log_file)
                self.uploaded_files = {}
                logger.trace(f"Cleared log file: {self.upload_log_file}")
            except Exception as e:
                logger.error(f"Error clearing log file: {e}")

    def _compute_file_hash(self, file_path):
        hasher = hashlib.sha256()
        with open(file_path, "rb") as file:
            buf = file.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def _create_lock_file(self):
        if os.path.exists(self.lock_file):
            raise RuntimeError("An X-Ray upload is already in progress.")
        with open(self.lock_file, "w") as f:
            f.write(str(os.getpid()))

    def _get_files_in_directory(self, directory_path):
        file_paths = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_paths.append(os.path.join(root, file))
        return file_paths

    def _get_presigned_url(self, object_name):
        return f"{object_name}"

    def _graceful_shutdown(self):
        logger.debug(f"Graceful shutdown initiated")
        self.stop_event.set()

        for _ in range(NUM_WORKERS):
            self.queue.put(None)

        if self.token_thread and self.token_thread.is_alive():
            self.token_thread.join()

        for thread in self.threads:
            if thread.is_alive():
                thread.join()

        self._remove_lock_file()
        self._save_uploaded_files_log()
        logger.debug("Cleanup complete")

    def _handle_signal(self, signum, frame):
        logger.debug(f"Signal received: {signum}")
        self.stop_event.set()
        self._graceful_shutdown()

    def _load_uploaded_files_log(self):
        if os.path.exists(self.upload_log_file):
            try:
                with open(self.upload_log_file, "r") as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error reading log file: {e}")
        return {}

    def _remove_lock_file(self):
        if os.path.exists(self.lock_file):
            os.remove(self.lock_file)

    def _save_uploaded_files_log(self):
        temp_log_file = f"{self.upload_log_file}.tmp"
        try:
            with open(temp_log_file, "w") as f:
                json.dump(self.uploaded_files, f)
            os.replace(temp_log_file, self.upload_log_file)
        except Exception as e:
            logger.error(f"Error writing log file: {e}")
            if os.path.exists(temp_log_file):
                os.remove(temp_log_file)

    def start(self, file_path: Union[str, List[str], Path, List[Path]]):
        self._create_lock_file()
        try:
            self._upload(file_path)
        except Exception as e:
            logger.error(f"Error during upload: {e}")
            raise e
        finally:
            self._graceful_shutdown()

    def _token_bucket_refill(self):
        while not self.stop_event.is_set():
            self.token_bucket.set()
            time.sleep(TOKEN_BUCKET_INTERVAL)
            if self.queue.empty() and all(
                not thread.is_alive() for thread in self.threads
            ):
                break
        logger.trace("token bucket exiting")

    def _upload(self, file_path: Union[str, List[str], Path, List[Path]]):
        if isinstance(file_path, (str, Path)):
            file_path = [file_path]
        file_path = [str(p) for p in file_path]

        file_paths = []
        for path in file_path:
            if os.path.isfile(path):
                file_paths.append(path)
            elif os.path.isdir(path):
                file_paths.extend(self._get_files_in_directory(path))

        if not file_paths:
            raise Exception("No files found to upload.")

        common_path = os.path.commonpath(file_paths)

        for fp in file_paths:
            self.queue.put(fp)

        self.token_thread = Thread(target=self._token_bucket_refill)
        self.token_thread.start()

        self.threads = []
        for i in range(NUM_WORKERS):
            thread = Thread(
                target=self._worker, args=(common_path,), name=f"WorkerThread-{i+1}"
            )
            thread.start()
            self.threads.append(thread)

        try:
            while not self.stop_event.is_set():
                if self.queue.empty() and all(
                    not thread.is_alive() for thread in self.threads
                ):
                    break
                time.sleep(1)
            if self.exception:
                raise self.exception
        except Exception as e:
            self.stop_event.set()
            raise e

    def _upload_file(self, file_path, presigned_url, file_hash):
        time.sleep(0.1)
        logger.trace(f"upload [{file_path}]")
        return

        try:
            with open(file_path, "rb") as file_data:
                response = requests.put(presigned_url, data=file_data)
                if response.status_code == 200:
                    logger.trace(f"Successfully uploaded {file_path}")
                    self.uploaded_files[file_hash] = {"status": "uploaded"}
                    self._save_uploaded_files_log()
                else:
                    logger.trace(
                        f"Failed to upload {file_path}. Status code: {response.status_code}"
                    )
        except Exception as e:
            with self.exception_lock:
                if not self.exception:
                    self.exception = e
            self.stop_event.set()
            raise

    def _worker(self, common_path):
        logger.trace(f"[{get_ident()}] starting")
        while not self.stop_event.is_set():
            try:
                file_path = self.queue.get(timeout=1)

                if file_path is None:
                    self.queue.task_done()
                    break

                if file_path.endswith(".txt"):
                    raise RuntimeError(f"[{get_ident()}] Simulated crash for testing")

                file_hash = self._compute_file_hash(file_path)
                if file_hash not in self.uploaded_files:
                    while not self.token_bucket.wait(timeout=1):
                        if self.stop_event.is_set():
                            break
                    self.token_bucket.clear()
                    if self.stop_event.is_set():
                        break
                    object_name = os.path.relpath(file_path, common_path)
                    presigned_url = self._get_presigned_url(object_name)
                    self._upload_file(file_path, presigned_url, file_hash)

                logger.debug(f"[{get_ident()}] done [{file_path}]")

                self.queue.task_done()
            except Empty:
                continue
            except Exception as e:
                with self.exception_lock:
                    if not self.exception:
                        self.exception = e
                self.stop_event.set()
                break

        logger.trace(f"[{get_ident()}] exiting")

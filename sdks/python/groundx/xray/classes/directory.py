# coding: utf-8


import hashlib
import json
from queue import Queue, Empty
import os
from pathlib import Path
from threading import get_ident, Event, Lock, Thread
import time
from typing import Any, Dict, List, Optional, Union

from groundx.xray.classes.document import XRayDocument
from groundx.xray.classes.factory import create_xray_document
from groundx.xray.logger import CustomLogger


NUM_WORKERS = 5
MAX_CALLS_PER_MINUTE = 600
TOKEN_BUCKET_INTERVAL = 60 / MAX_CALLS_PER_MINUTE
UPLOAD_LOG_FILE = "xray_uploader.log.json"


class XRayDirectory:
    def __init__(
        self,
        logger: CustomLogger,
        stop_event: Event,
        file_path: Union[str, List[str], Path, List[Path]],
        exclude_list: Optional[List[Union[str, Path]]] = None,
        upload_log_file=None,
    ) -> None:
        self.exclude_list = [str(path) for path in exclude_list] if exclude_list else []
        self.file_path = file_path
        self.logger = logger
        self.stop_event = stop_event

        self.files: List[XRayDocument] = []
        self.threads = []
        self.exception_lock = Lock()
        self.request_queue = Queue()
        self.result_queue = Queue()
        self.token_bucket = Event()
        self.token_bucket.set()
        self.token_lock = Lock()
        self.token_thread = None
        self._total_tokens = 0

        self.exception = None
        self.upload_log_file = upload_log_file or UPLOAD_LOG_FILE
        self.uploaded_files = self._load_uploaded_files_log()

        try:
            self._load()
        except Exception as e:
            self._graceful_shutdown()
            raise e

    def _clear_uploaded_files_log(self) -> None:
        if os.path.exists(self.upload_log_file):
            try:
                os.remove(self.upload_log_file)
                self.uploaded_files = {}
                self.logger.trace(f"Cleared log file: {self.upload_log_file}")
            except Exception as e:
                self.logger.error(f"Error clearing log file: {e}")
                self.uploaded_files = {}

    def _compute_file_hash(self, file_path) -> str:
        hasher = hashlib.sha256()
        with open(file_path, "rb") as file:
            buf = file.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def get_documents(self, sort_by_tokens: bool = False) -> List[XRayDocument]:
        if sort_by_tokens:
            return sorted(self.files, key=lambda doc: doc.tokens, reverse=True)

        return self.files

    def _get_files_in_directory(self, directory_path) -> List[str]:
        file_paths = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if not self._should_exclude(file_path):
                    file_paths.append(file_path)

        return file_paths

    def _get_presigned_url(self, object_name) -> str:
        return f"{object_name}"

    def _graceful_shutdown(self) -> None:
        self.stop_event.set()

        if self.token_thread and self.token_thread.is_alive():
            self.token_thread.join()

        self._load_shutdown()
        self._save_uploaded_files_log()

        self.logger.debug("directory shutdown complete")

    def _load(self) -> None:
        if isinstance(self.file_path, (str, Path)):
            if isinstance(self.file_path, Path):
                file_path = [str(self.file_path)]
            else:
                file_path = [self.file_path]
        file_path = [str(p) for p in file_path]

        file_paths = []
        for path in file_path:
            if os.path.isfile(path) and not self._should_exclude(path):
                file_paths.append(path)
            elif os.path.isdir(path):
                file_paths.extend(self._get_files_in_directory(path))

        if not file_paths:
            raise Exception("No files found to upload.")

        for fp in file_paths:
            self.request_queue.put(fp)

        self.threads = []
        for i in range(NUM_WORKERS):
            thread = Thread(
                target=self._worker_load, args=(), name=f"WorkerThread-{i+1}"
            )
            thread.start()
            self.threads.append(thread)

        while not self.stop_event.is_set():
            if self.request_queue.empty() or all(
                not thread.is_alive() for thread in self.threads
            ):
                break
            time.sleep(1)

        while not self.result_queue.empty():
            self.files.append(self.result_queue.get())

        if self.exception:
            raise self.exception

        self._load_shutdown()

    def _load_shutdown(self) -> None:
        for _ in range(NUM_WORKERS):
            self.request_queue.put(None)

        for thread in self.threads:
            if thread.is_alive():
                thread.join()

    def _load_uploaded_files_log(self) -> Dict:
        if os.path.exists(self.upload_log_file):
            try:
                with open(self.upload_log_file, "r") as f:
                    return json.load(f)
            except Exception as e:
                self.logger.error(f"Error reading log file: {e}")
        return {}

    def _save_uploaded_files_log(self) -> None:
        temp_log_file = f"{self.upload_log_file}.tmp"
        try:
            with open(temp_log_file, "w") as f:
                json.dump(self.uploaded_files, f)
            os.replace(temp_log_file, self.upload_log_file)
        except Exception as e:
            self.logger.error(f"Error writing log file: {e}")
            if os.path.exists(temp_log_file):
                os.remove(temp_log_file)

    def _should_exclude(self, file_path) -> bool:
        return any(exclude in file_path for exclude in self.exclude_list)

    def _token_bucket_refill(self) -> None:
        while not self.stop_event.is_set():
            self.token_bucket.set()
            time.sleep(TOKEN_BUCKET_INTERVAL)
            if self.request_queue.empty() and all(
                not thread.is_alive() for thread in self.threads
            ):
                break
        self.logger.trace("token bucket exiting")

    def total_tokens(self) -> int:
        return self._total_tokens

    def upload(self) -> None:
        if isinstance(self.file_path, (str, Path)):
            if isinstance(self.file_path, Path):
                file_path = [str(self.file_path)]
            else:
                file_path = [self.file_path]
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
            self.request_queue.put(fp)

        self.token_thread = Thread(target=self._token_bucket_refill)
        self.token_thread.start()

        self.threads = []
        for i in range(NUM_WORKERS):
            thread = Thread(
                target=self._worker_upload, args=(common_path,), name=f"WorkerThread-{i+1}"
            )
            thread.start()
            self.threads.append(thread)

        while not self.stop_event.is_set():
            if self.request_queue.empty() or all(
                not thread.is_alive() for thread in self.threads
            ):
                break
            time.sleep(1)
        if self.exception:
            raise self.exception

    def _upload_file(self, file_path, presigned_url, file_hash):
        time.sleep(0.1)
        self.logger.trace(f"upload [{file_path}]")
        return

        """
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
        """

    def _worker_load(self):
        self.logger.trace(f"[{get_ident()}] starting")
        while not self.stop_event.is_set():
            try:
                file_path = self.request_queue.get(timeout=1)

                if file_path is None:
                    self.request_queue.task_done()
                    break

                xray_file = create_xray_document(file_path)
                if xray_file is not None:
                    with self.token_lock:
                        self._total_tokens += xray_file.tokens
                    self.logger.trace(f"added [{file_path}]")
                    self.result_queue.put(xray_file)
                else:
                    self.logger.trace(f"ignored [{file_path}]")

                self.request_queue.task_done()
            except Empty:
                continue
            except Exception as e:
                with self.exception_lock:
                    if not self.exception:
                        self.exception = e
                self.stop_event.set()
                self.logger.error(f"Error processing file {file_path}: {e}")
                break

        self.logger.trace(f"[{get_ident()}] exiting")

    def _worker_upload(self, common_path):
        self.logger.trace(f"[{get_ident()}] starting")
        while not self.stop_event.is_set():
            try:
                file_path = self.request_queue.get(timeout=1)

                if file_path is None:
                    self.request_queue.task_done()
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

                self.logger.debug(f"[{get_ident()}] done [{file_path}]")

                self.request_queue.task_done()
            except Empty:
                continue
            except Exception as e:
                with self.exception_lock:
                    if not self.exception:
                        self.exception = e
                self.stop_event.set()
                break

        self.logger.trace(f"[{get_ident()}] exiting")
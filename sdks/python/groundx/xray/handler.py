# coding: utf-8

from abc import ABC
from pathlib import Path
import signal
from threading import Event
from typing import Any, Iterator, List, Optional, Union
from typing_extensions import TypeAlias

from groundx.apis.tags.customer_api import CustomerApi
from groundx.xray.limits import XRayLimits
from groundx.xray.logger import CustomLogger, setup_custom_logger
from groundx.xray.classes.directory import XRayDirectory
from groundx.xray.interface.base import BaseLoader
from groundx.xray.interface.document import Document


Element: TypeAlias = Any


class XRay(BaseLoader, ABC):
    def __init__(
        self,
        file_path: Union[str, List[str], Path, List[Path]],
        **xray_kwargs: Any,
    ):
        self.file_path = file_path
        self.xray_kwargs = xray_kwargs

        self._load_api_client(xray_kwargs)

        self.directory = None
        self.limits = XRayLimits(self.customer)
        self.logger: CustomLogger = setup_custom_logger(__file__)
        self.stop_event = Event()

        signal.signal(signal.SIGINT, self._handle_signal)
        signal.signal(signal.SIGTERM, self._handle_signal)
        signal.signal(signal.SIGHUP, self._handle_signal)

    def estimate(
        self,
        file_path: Union[str, List[str], Path, List[Path]],
        exclude_list: Optional[List[Union[str, Path]]] = None,
    ):
        try:
            self.file_path = file_path

            self.directory = XRayDirectory(self.logger, self.stop_event, file_path, exclude_list)
        except Exception as e:
            self._graceful_shutdown()
            raise e

    def evaluate(
        self,
    ):
        if self.directory is None:
            raise Exception("directory was not initialized")

        print(self.limits.limits)
        print(f"total tokens: [{self.directory.total_tokens()}]")
        for f in self.directory.get_documents(sort_by_tokens=True):
            print(f"[{f.file_type}] [{f.file_path}] [{f.pages}] [{f.tokens}]")

    def _graceful_shutdown(
        self,
    ):
        self.stop_event.set()

        if self.directory is not None:
            self.directory._graceful_shutdown()

        self.logger.debug("handler shudown complete")

    def _handle_signal(
        self,
        signum,
        frame,
    ):
        self.logger.debug(f"Signal received: {signum}")
        self._graceful_shutdown()

    def lazy_load(
        self,
    ) -> Iterator[Document]:
        try:
            self.limits.update()

            return iter(())
        except Exception as e:
            self._graceful_shutdown()
            raise e

    def _load_api_client(
        self,
        xray_kwargs: dict[str, Any],
    ):
        if xray_kwargs.get("api_client") is None:
            raise TypeError("Missing required argument: 'required_arg'")

        api_client = xray_kwargs.get("api_client")
        self.customer = CustomerApi(api_client)

    def parse(
        self,
        file_path: Union[str, List[str], Path, List[Path]],
        exclude_list: Optional[List[Union[str, Path]]] = None,
    ):
        try:
            self.limits.update()

            self.estimate(file_path, exclude_list)

            self.evaluate()

            return iter(())
        except Exception as e:
            self._graceful_shutdown()
            raise e

        #self.lazy_load()

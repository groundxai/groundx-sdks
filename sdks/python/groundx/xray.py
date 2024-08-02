# coding: utf-8

from abc import ABC
import logging
from pathlib import Path
from typing import Any, Iterator, List, Union
from typing_extensions import TypeAlias

from groundx.xray_uploader import XRayUploader
from groundx.iface.base import BaseLoader
from groundx.iface.document import Document

Element: TypeAlias = Any

logger = logging.getLogger(__file__)


class XRay(BaseLoader, ABC):
    def __init__(
        self,
        file_path: Union[str, List[str], Path, List[Path]],
        **xray_kwargs: Any,
    ):
        self.file_path = file_path
        self.xray_kwargs = xray_kwargs
        self._load_api_client(xray_kwargs)
        self.uploader = XRayUploader()

    def _get_elements(self) -> List[Element]:
        self.uploader.start(self.file_path)

    def _load_api_client(self, xray_kwargs: dict[str, Any]):
        if xray_kwargs.get("api_client") is None:
            raise TypeError("Missing required argument: 'required_arg'")

        self.api_client = xray_kwargs.get("api_client")

    def lazy_load(self) -> Iterator[Document]:
        elements = self._get_elements()
        print(elements)

    def parse(
        self,
        file_path: Union[str, List[str], Path, List[Path]],
    ):
        self.file_path = file_path

        self.lazy_load()

    def process(
        self,
        filename: str,
    ):
        filename = filename.strip()
        if filename is None or filename == "":
            raise ValueError("filename must be set")

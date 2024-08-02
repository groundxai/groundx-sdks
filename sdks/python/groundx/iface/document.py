# coding: utf-8

"""
Abstraction of langchain document methods and classes
"""

from pathlib import PurePath
from typing import Any, List, Literal, Optional, Union

from groundx.iface.serializable import Serializable
from groundx.pydantic_v1 import Field

PathLike = Union[str, PurePath]


class BaseMedia(Serializable):
    id: Optional[str] = None

    metadata: dict = Field(default_factory=dict)


class Document(BaseMedia):
    page_content: str
    type: Literal["Document"] = "Document"

    def __init__(self, page_content: str, **kwargs: Any) -> None:
        super().__init__(page_content=page_content, **kwargs)

    @classmethod
    def is_lc_serializable(cls) -> bool:
        return True

    @classmethod
    def get_lc_namespace(cls) -> List[str]:
        return ["groundx", "lciface"]

    def __str__(self) -> str:
        if self.metadata:
            return f"page_content='{self.page_content}' metadata={self.metadata}"
        else:
            return f"page_content='{self.page_content}'"

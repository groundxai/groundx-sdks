# coding: utf-8

"""
Abstraction of langchain base loader methods and classes
"""

from abc import ABC
from typing import Iterator, List

from groundx.xray.interface.document import Document


class BaseLoader(ABC):
    def load(self) -> List[Document]:
        return list(self.lazy_load())

    def lazy_load(self) -> Iterator[Document]:
        if type(self).load != BaseLoader.load:
            return iter(self.load())
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement lazy_load()"
        )

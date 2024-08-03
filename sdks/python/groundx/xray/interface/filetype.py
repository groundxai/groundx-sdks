# coding: utf-8

"""
Abstraction of unstructured model methods and classes
"""


from __future__ import annotations

import enum
from typing import Iterable, cast


class FileType(enum.Enum):
    _partitioner_shortname: str | None

    _importable_package_dependencies: tuple[str, ...]

    _extra_name: str | None

    _extensions: tuple[str, ...]

    _canonical_mime_type: str

    _alias_mime_types: tuple[str, ...]

    def __new__(
        cls,
        value: str,
        partitioner_shortname: str | None,
        importable_package_dependencies: Iterable[str],
        extra_name: str | None,
        extensions: Iterable[str],
        canonical_mime_type: str,
        alias_mime_types: Iterable[str],
    ):
        self = object.__new__(cls)
        self._value_ = value
        self._partitioner_shortname = partitioner_shortname
        self._importable_package_dependencies = tuple(importable_package_dependencies)
        self._extra_name = extra_name
        self._extensions = tuple(extensions)
        self._canonical_mime_type = canonical_mime_type
        self._alias_mime_types = tuple(alias_mime_types)
        return self

    def __lt__(self, other: FileType) -> bool:
        return self.name < other.name

    @classmethod
    def from_extension(cls, extension: str | None) -> FileType | None:
        if extension in (None, "", "."):
            return None

        for m in cls.__members__.values():
            if extension in m._extensions:
                return m
        return None

    @classmethod
    def from_mime_type(cls, mime_type: str | None) -> FileType | None:
        if mime_type is None:
            return None

        for m in cls.__members__.values():
            if mime_type == m._canonical_mime_type or mime_type in m._alias_mime_types:
                return m
        return None

    @property
    def extra_name(self) -> str | None:
        return self._extra_name

    @property
    def importable_package_dependencies(self) -> tuple[str, ...]:
        return self._importable_package_dependencies

    @property
    def is_partitionable(self) -> bool:
        return bool(self._partitioner_shortname)

    @property
    def mime_type(self) -> str:
        return self._canonical_mime_type

    @property
    def partitioner_function_name(self) -> str:
        if (shortname := self._partitioner_shortname) is None:
            raise ValueError(
                f"`.partitioner_function_name` is undefined because FileType.{self.name} is not"
                f" partitionable. Use `.is_partitionable` to determine whether a `FileType`"
                f" is partitionable."
            )
        return f"partition_{shortname}"

    @property
    def partitioner_module_qname(self) -> str:
        if (shortname := self._partitioner_shortname) is None:
            raise ValueError(
                f"`.partitioner_module_qname` is undefined because FileType.{self.name} is not"
                f" partitionable. Use `.is_partitionable` to determine whether a `FileType`"
                f" is partitionable."
            )
        return f"unstructured.partition.{shortname}"

    @property
    def partitioner_shortname(self) -> str | None:
        return self._partitioner_shortname

    CSV = (
        "csv",
        "csv",
        ["pandas"],
        "csv",
        [".csv"],
        "text/csv",
        [
            "application/csv",
            "application/x-csv",
            "text/comma-separated-values",
            "text/x-comma-separated-values",
            "text/x-csv",
        ],
    )
    DOC = (
        "doc",
        "doc",
        ["docx"],
        "doc",
        [".doc"],
        "application/msword",
        cast(list[str], []),
    )
    DOCX = (
        "docx",
        "docx",
        ["docx"],
        "docx",
        [".docx"],
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        cast(list[str], []),
    )
    JPG = (
        "jpg",
        "image",
        ["unstructured_inference"],
        "image",
        [".jpeg", ".jpg"],
        "image/jpeg",
        cast(list[str], []),
    )
    JSON = (
        "json",
        "json",
        cast(list[str], []),
        None,
        [".json"],
        "application/json",
        cast(list[str], []),
    )
    PDF = (
        "pdf",
        "pdf",
        ["pdf2image", "pdfminer", "PIL"],
        "pdf",
        [".pdf"],
        "application/pdf",
        cast(list[str], []),
    )
    PNG = (
        "png",
        "image",
        ["unstructured_inference"],
        "image",
        [".png"],
        "image/png",
        cast(list[str], []),
    )
    PPT = (
        "ppt",
        "ppt",
        ["pptx"],
        "ppt",
        [".ppt"],
        "application/vnd.ms-powerpoint",
        cast(list[str], []),
    )
    PPTX = (
        "pptx",
        "pptx",
        ["pptx"],
        "pptx",
        [".pptx"],
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        cast(list[str], []),
    )
    TSV = (
        "tsv",
        "tsv",
        ["pandas"],
        "tsv",
        [".tab", ".tsv"],
        "text/tsv",
        cast(list[str], []),
    )
    TXT = (
        "txt",
        "text",
        cast(list[str], []),
        None,
        [
            ".txt",
            ".text",
            ".c",
            ".cc",
            ".cpp",
            ".cs",
            ".cxx",
            ".go",
            ".java",
            ".js",
            ".log",
            ".php",
            ".py",
            ".rb",
            ".swift",
            ".ts",
            ".yaml",
            ".yml",
        ],
        "text/plain",
        [
            "text/yaml",
            "application/x-yaml",
            "application/yaml",
            "text/x-yaml",
        ],
    )
    XLS = (
        "xls",
        "xlsx",
        ["pandas", "openpyxl"],
        "xlsx",
        [".xls"],
        "application/vnd.ms-excel",
        cast(list[str], []),
    )
    XLSX = (
        "xlsx",
        "xlsx",
        ["pandas", "openpyxl"],
        "xlsx",
        [".xlsx"],
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        cast(list[str], []),
    )
    EMPTY = (
        "empty",
        None,
        cast(list[str], []),
        None,
        cast(list[str], []),
        "inode/x-empty",
        cast(list[str], []),
    )

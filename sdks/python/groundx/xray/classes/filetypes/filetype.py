# coding: utf-8


from __future__ import annotations

import enum
from typing import cast, Iterable



class FileType(enum.Enum):
    _accepted_mime_types: tuple[str, ...]
    _file_extensions: tuple[str, ...]
    _mime_type: str
    _name: str
    _should_process: bool

    def __new__(
        cls,
        name: str,
        file_extensions: Iterable[str],
        mime_type: str,
        accepted_mime_types: Iterable[str],
        should_process: bool = True
    ):
        self = object.__new__(cls)
        self._name = name
        self._file_extensions = tuple(file_extensions)
        self._mime_type = mime_type
        self._accepted_mime_types = tuple(accepted_mime_types)
        self._should_process = should_process

        return self

    @classmethod
    def from_extension(cls, extension: str | None) -> FileType | None:
        if extension in (None, "", "."):
            return None

        for m in cls.__members__.values():
            if extension in m._file_extensions:
                return m

        return None

    @classmethod
    def from_mime_type(cls, mime_type: str | None) -> FileType | None:
        if mime_type is None:
            return None

        for m in cls.__members__.values():
            if mime_type == m._mime_type or mime_type in m._accepted_mime_types:
                return m

        return None

    @property
    def name(self) -> str:
        if self._name is None:
            raise ValueError(
                f"`.name` is undefined because FileType.{self.name} is not"
                f" supported. Use `.should_process` to determine whether a `FileType`"
                f" is supported."
            )
        return f"file_{self._name}"

    @property
    def mime_type(self) -> str:
        return self._mime_type

    @property
    def should_process(self) -> bool:
        return self._should_process

    CSV = (
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
    DOCX = (
        "docx",
        [".docx"],
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        cast(list[str], []),
    )
    JPG = (
        "jpg",
        [".jpeg", ".jpg"],
        "image/jpeg",
        cast(list[str], []),
    )
    JSON = (
        "json",
        [".json"],
        "application/json",
        cast(list[str], []),
    )
    PDF = (
        "pdf",
        [".pdf"],
        "application/pdf",
        cast(list[str], []),
    )
    PNG = (
        "png",
        [".png"],
        "image/png",
        cast(list[str], []),
    )
    PPTX = (
        "pptx",
        [".pptx"],
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        cast(list[str], []),
    )
    TSV = (
        "tsv",
        [".tab", ".tsv"],
        "text/tsv",
        cast(list[str], []),
    )
    TXT = (
        "txt",
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
            ".eml",
            ".p7s",
            ".md",
        ],
        "text/plain",
        [
            "text/yaml",
            "application/x-yaml",
            "application/yaml",
            "text/x-yaml",
            "message/rfc822",
            "text/x-markdown",
        ],
    )
    XLSX = (
        "xlsx",
        [".xlsx"],
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        cast(list[str], []),
    )

    UNK = (
        "unknown",
        cast(list[str], []),
        "application/octet-stream",
        cast(list[str], []),
    )

    EMPTY = (
        "empty",
        cast(list[str], []),
        "inode/x-empty",
        cast(list[str], []),
    )
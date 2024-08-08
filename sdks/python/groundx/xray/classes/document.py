# coding: utf-8


import json
import mimetypes
import os
from typing import Optional, Tuple

import filetype
from pydantic import Field
import tiktoken

from groundx.xray.classes.filetypes.constants import MIN_TOKENS, TXT_MODIFIER
from groundx.xray.classes.filetypes.filetype import FileType
from groundx.xray.interface.document import Document


TOKEN_MODEL = "o200k_base"
ENCODING = tiktoken.get_encoding(TOKEN_MODEL)


class XRayDocument(Document):
    file_path: str
    file_data: bytes = Field(default_factory=bytes)
    file_type: Optional[FileType] = None

    pages: int = 0
    tokens: int = 0

    def __init__(self, file_path: str) -> None:
        super().__init__(page_content="", file_path=file_path)

        self.file_data = self._load()
        self.file_type = self._detect_file_type()

    def _detect_file_type(self) -> Optional[FileType]:
        kind = filetype.guess(self.file_path)
        if kind:
            mime_type = kind.mime
            file_type = FileType.from_mime_type(mime_type)
            if file_type is not None:
                return file_type
        
        try:
            ft = FileType.from_mime_type(mime_type)
            if ft is not None:
                return ft
        except Exception:
            pass

        try:
            if self._is_json():
                return FileType.JSON
            if self._is_csv():
                return FileType.CSV
            if self._is_tsv():
                return FileType.TSV
            if self._is_txt():
                return FileType.TXT
        except Exception:
            pass

        mime_type, _ = mimetypes.guess_type(self.file_path)
        if mime_type:
            file_type = FileType.from_mime_type(mime_type)
            if file_type is not None:
                return file_type

        return FileType.from_extension(
            self._get_file_extension(),
        )

    def estimate_size(self) -> Tuple[int, int]:
        pgs, cnt = self._estimate_size()
        if cnt > 0 and cnt < MIN_TOKENS:
            return pgs, MIN_TOKENS

        return pgs, cnt

    def _estimate_size(self) -> Tuple[int, int]:
        if self.file_type == None:
            return 0, 0

        try:
            decoded_data = self.file_data.decode('utf-8', errors='ignore')
            return 1, self._token_count(decoded_data) * TXT_MODIFIER
        except Exception:
            return 0, 0

    def _get_file_extension(self) -> Optional[str]:
        return os.path.splitext(self.file_path)[1].lower()

    def _has_consistent_delimiter(self, delimiter: str) -> bool:
        try:
            decoded_data = self.file_data.decode('utf-8')
            lines = decoded_data.splitlines()
            if len(lines) < 2:
                return False
            delimiter_count = [line.count(delimiter) for line in lines[:10]]
            return len(set(delimiter_count)) == 1 and delimiter_count[0] > 0
        except Exception:
            return False

    def _is_json(self) -> bool:
        try:
            first_line = self.file_data.decode('utf-8').split('\n', 1)[0]
            if first_line:
                if first_line.startswith('{') or first_line.startswith('['):
                    json.loads(self.file_data.decode('utf-8'))
                    return True
            return False
        except json.JSONDecodeError:
            return False

    def _is_csv(self) -> bool:
        return self._has_consistent_delimiter(',')

    def _is_tsv(self) -> bool:
        return self._has_consistent_delimiter('\t')

    def _is_txt(self) -> bool:
        try:
            self.file_data.decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False

    def _load(self) -> bytes:
        with open(self.file_path, 'rb') as file:
            return file.read()

    def read(self):
        raise NotImplementedError("subclasses must implement this method")

    def process(self):
        raise NotImplementedError("subclasses must implement this method")

    def _token_count(self, text: str, sample_size: int = 1000) -> int:
        if len(text) <= sample_size:
            sample_text = text
            sample_token_count = len(ENCODING.encode(sample_text))

            return sample_token_count

        sample_text = text[:sample_size]
        sample_token_count = len(ENCODING.encode(sample_text))
        
        total_length = len(text)
        estimated_total_tokens = (total_length / sample_size) * sample_token_count

        return int(estimated_total_tokens)

    @property
    def name(self):
        return os.path.basename(self.file_path)
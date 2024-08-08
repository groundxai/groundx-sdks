# coding: utf-8


import json
from typing import Tuple

from groundx.xray.classes.document import XRayDocument
from groundx.xray.classes.filetypes.constants import TXT_MODIFIER


class XRayJSON(XRayDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        self.pages, self.tokens = self.estimate_size()

    def _estimate_size(self) -> Tuple[int, int]:
        try:
            data = json.loads(self.file_data.decode('utf-8'))
            flattened_data = self._flat_string(data)

            return 1, self._token_count(flattened_data) * TXT_MODIFIER
        except Exception:
            return 1, 0

    def _flat_string(self, data):
        if isinstance(data, dict):
            items = []
            for key, value in data.items():
                items.append(f'"{key}": {self._flat_string(value)}')
            return '{' + ', '.join(items) + '}'
        elif isinstance(data, list):
            items = [self._flat_string(item) for item in data]
            return '[' + ', '.join(items) + ']'
        elif isinstance(data, str):
            return json.dumps(data)
        else:
            return str(data)
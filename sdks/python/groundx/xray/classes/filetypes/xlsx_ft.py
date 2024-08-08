# coding: utf-8


from typing import Tuple

import openpyxl

from groundx.xray.classes.document import XRayDocument
from groundx.xray.classes.filetypes.constants import TXT_MODIFIER


class XRayXLSX(XRayDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        self.pages, self.tokens = self.estimate_size()

    def _estimate_size(self) -> Tuple[int, int]:
        try:
            workbook = openpyxl.load_workbook(self.file_path)

            full_text = []
            for sheet in workbook.worksheets:
                for row in sheet.iter_rows(values_only=True):
                    for cell in row:
                        if cell is not None:
                            full_text.append(str(cell))

            return len(workbook.worksheets), self._token_count('\n'.join(full_text)) * TXT_MODIFIER
        except Exception as e:
            print(f"error processing XLSX: {e}")
            return 0, 0
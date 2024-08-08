# coding: utf-8


from typing import Optional, Tuple

import fitz

from groundx.xray.classes.document import XRayDocument
from groundx.xray.classes.filetypes.constants import TXT_MODIFIER


class XRayPDF(XRayDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        self.pages, self.tokens = self.estimate_size()

    def _estimate_size(self) -> Tuple[int, int]:
        try:
            doc = fitz.open(stream=self.file_data, filetype="pdf")
            text = ""
            for page in doc:
                text += page.get_textpage().extractText()

            return doc.page_count, self._token_count(text) * TXT_MODIFIER
        except Exception:
            return 0, 0
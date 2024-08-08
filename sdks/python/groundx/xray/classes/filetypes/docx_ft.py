# coding: utf-8


from typing import Tuple

import docx

from groundx.xray.classes.document import XRayDocument
from groundx.xray.classes.filetypes.constants import TXT_MODIFIER


class XRayDOCX(XRayDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        self.pages, self.tokens = self.estimate_size()

    def _estimate_size(self) -> Tuple[int, int]:
        doc = docx.Document(self.file_path)

        full_text = []
        page_count = 0
        for paragraph in doc.paragraphs:
            if paragraph.text == 'Microsoft Word 2010 - Level 2':
                page_count += 1
            else:
                full_text.append(paragraph.text)

        if page_count == 0:
            page_count = 1

        return page_count, self._token_count('\n'.join(full_text)) * TXT_MODIFIER
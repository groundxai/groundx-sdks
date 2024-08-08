# coding: utf-8


from typing import Tuple

from groundx.xray.classes.document import XRayDocument
from groundx.xray.classes.filetypes.constants import IMG_TOKENS


class XRayJPG(XRayDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        self.pages, self.tokens = self.estimate_size()

    def _estimate_size(self) -> Tuple[int, int]:
        return 1, IMG_TOKENS
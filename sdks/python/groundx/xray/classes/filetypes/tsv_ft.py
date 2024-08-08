# coding: utf-8


from typing import Tuple

from groundx.xray.classes.document import XRayDocument
from groundx.xray.classes.filetypes.constants import TABLE_ADD_ON


class XRayTSV(XRayDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        self.pages, self.tokens = self.estimate_size()

    def _estimate_size(self) -> Tuple[int, int]:
        pgs, cnt = super()._estimate_size()

        return pgs, cnt * TABLE_ADD_ON
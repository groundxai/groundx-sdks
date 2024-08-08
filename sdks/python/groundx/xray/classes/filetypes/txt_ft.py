# coding: utf-8


from groundx.xray.classes.document import XRayDocument


class XRayTXT(XRayDocument):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        self.pages, self.tokens = self.estimate_size()
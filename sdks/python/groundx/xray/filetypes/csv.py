# coding: utf-8


class XRayCSV:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def estimate(self):
        print(self.file_path)
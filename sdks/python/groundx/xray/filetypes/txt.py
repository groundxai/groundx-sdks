# coding: utf-8


class XRayTXT:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def count_tokens_in_text(self, text):
        return len(text.split())

    def estimate(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        return self.count_tokens_in_text(text)
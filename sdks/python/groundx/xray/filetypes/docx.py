# coding: utf-8


import docx


class XRayDOCX:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def count_tokens_in_text(self, text: str):
        return len(text.split())

    def estimate(self):
        doc = docx.Document(self.file_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)

        return self.count_tokens_in_text('\n'.join(full_text))
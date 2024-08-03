# coding: utf-8


import fitz


class XRayPDF:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def count_tokens_in_text(self, text):
        return len(text.split())

    def estimate(self, sample_size=5):
        doc = fitz.open(self.file_path)
        total_tokens = 0
        num_pages = len(doc)
        sample_pages = min(sample_size, num_pages)

        for page_num in range(sample_pages):
            page = doc.load_page(page_num)
            text = page.get_text()
            total_tokens += self.count_tokens_in_text(text)

        average_tokens_per_page = total_tokens / sample_pages
        estimated_tokens = average_tokens_per_page * num_pages

        return estimated_tokens
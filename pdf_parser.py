import fitz  # PyMuPDF

class PdfParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        text = ""
        with fitz.open(self.file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text


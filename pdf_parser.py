import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

class PdfParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        text = ""
        with fitz.open(self.file_path) as doc:
            for page in doc:
                text += page.get_text()
        text = self._clean_text(text)
        return text

    def _clean_text(self, text: str) -> str:
        # Remove only empty new lines and trailing spaces
        return '\n'.join(line.rstrip() for line in text.splitlines() if line.strip() != '')

    def chunk_text(self, text: str, chunk_size: int, chunk_overlap: int = 0) -> List[str]:
        """
        Splits the text into chunks using RecursiveCharacterTextSplitter from langchain.
        :param text: The input text to chunk.
        :param chunk_size: The maximum number of characters per chunk.
        :param chunk_overlap: The number of overlapping characters between chunks.
        :return: List of text chunks.
        """
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        return splitter.split_text(text)


from pdf_parser import PdfParser

# Example usage:
if __name__ == "__main__":
    parser = PdfParser("./tests/resources/2A_1.pdf")
    pdf_text = parser.extract_text()
    print(pdf_text)
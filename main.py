from pdf_parser import PdfParser

# Example usage:
if __name__ == "__main__":
    parser = PdfParser("./tests/resources/2A_1.pdf")
    pdf_text = parser.extract_text()
    chunks = parser.chunk_text(pdf_text, chunk_size=500, chunk_overlap=40)

    # print all the chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:\n{chunk}\n{'-' * 40}")
    print(chunks)
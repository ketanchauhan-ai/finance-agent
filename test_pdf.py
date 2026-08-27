from rag.pdf_loader import load_pdf
from rag.text_splitter import split_text

text = load_pdf("annual_report.pdf")

chunks = split_text(text)

print(f"Total Chunks: {len(chunks)}")

print(chunks[0])
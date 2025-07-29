# modules/pdf_extractor.py

import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path: str, output_path: str) -> None:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"[ERROR] PDF not found: {pdf_path}")

    full_text = ""
    doc = fitz.open(pdf_path)

    for page_num, page in enumerate(doc):
        text = page.get_text()
        full_text += f"\n--- Page {page_num + 1} ---\n{text}"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text.strip())

    print(f"✅ Text extracted from '{pdf_path}' and saved to '{output_path}'")

# Test run (optional, remove in production)
if __name__ == "__main__":
    pdf_path = "data/raw_pdfs/os.pdf"
    output_path = "data/extracted_texts/os.txt"
    extract_text_from_pdf(pdf_path, output_path)

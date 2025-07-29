# modules/pdf_extractor.py
import fitz
import os

def extract_text_from_pdf(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text() + "\n"

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print("✅ PDF text extracted.")

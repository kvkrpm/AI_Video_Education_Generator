import fitz
import os
from typing import Optional


def extract_text_from_pdf(pdf_path: str, output_path: str) -> Optional[str]:
    """
    Extracts text from PDF and saves to file
    Args:
        pdf_path: Path to input PDF
        output_path: Path to save extracted text
    Returns:
        Extracted text as string if successful, None otherwise
    """
    try:
        doc = fitz.open(pdf_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text() + "\n\n"  # Extra newlines between pages

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text)
        print(f"✅ PDF text extracted to {output_path}")
        return full_text
    except Exception as e:
        print(f"❌ Error extracting {pdf_path}: {str(e)}")
        return None
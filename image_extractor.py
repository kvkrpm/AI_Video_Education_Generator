import fitz  # PyMuPDF
import os
import shutil
from tqdm import tqdm

# Configuration
PDF_DIR = "data/raw_pdfs"
IMAGE_DIR = "data/extracted_images"
def clean_output_folder():
    """Remove all existing images before processing"""
    if os.path.exists(IMAGE_DIR):
        print(f"🧹 Cleaning existing images in {IMAGE_DIR}...")
        shutil.rmtree(IMAGE_DIR)
    os.makedirs(IMAGE_DIR, exist_ok=True)


def extract_images_from_pdf(pdf_path):
    """Extract all images from a single PDF"""
    try:
        doc = fitz.open(pdf_path)
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        img_count = 0

        for page_num, page in enumerate(doc, start=1):
            for img_index, img in enumerate(page.get_images(full=True), start=1):
                xref = img[0]
                base_image = doc.extract_image(xref)

                # Validate image
                if not base_image["image"]:
                    continue

                # Determine extension (fallback to png)
                ext = base_image.get("ext", "png").lower()
                if ext not in ["jpg", "jpeg", "png", "gif"]:
                    ext = "png"

                # Save image
                img_path = os.path.join(
                    IMAGE_DIR,
                    f"{pdf_name}_p{page_num}_i{img_index}.{ext}"
                )
                with open(img_path, "wb") as f:
                    f.write(base_image["image"])
                img_count += 1

        return img_count

    except Exception as e:
        print(f"❌ Error processing {pdf_path}: {str(e)}")
        return 0


def main():
    # Clean output folder before processing
    clean_output_folder()

    # Process all PDFs
    print(f"🖼️ Extracting images from PDFs in {PDF_DIR}")
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDF files found in the input directory!")
        return

    for pdf_file in tqdm(pdf_files, desc="Processing PDFs"):
        pdf_path = os.path.join(PDF_DIR, pdf_file)
        count = extract_images_from_pdf(pdf_path)
        if count > 0:
            print(f"✅ {pdf_file}: Extracted {count} images")


    print("🏁 Image extraction complete.")


if __name__ == "__main__":
    main()
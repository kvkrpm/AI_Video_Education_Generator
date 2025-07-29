# run_pipeline.py
from pdf_extractor import extract_text_from_pdf
from modules.pdf_extractor import extract_text_from_pdf
from modules.image_extractor import extract_images
from modules.text_cleaner import clean_text
from modules.summarizer import summarize_text
from modules.tts_generator import generate_tts
from modules.video_creator import create_video

pdf_path = "data/raw_pdfs/os.pdf"
text_path = "data/extracted_texts/os.txt"
img_folder = "data/images/os"
summary_path = "data/summaries/os_summary.txt"
audio_path = "data/audio/os_summary.mp3"
video_path = "data/videos/os_summary.mp4"

# Step 1: Extract text and images
extract_text_from_pdf(pdf_path, text_path)
extract_images(pdf_path, img_folder)

# Step 2: Clean text
with open(text_path, "r", encoding="utf-8") as f:
    raw_text = f.read()
cleaned_text = clean_text(raw_text)

# Step 3: Summarize
summary = summarize_text(cleaned_text)
with open(summary_path, "w", encoding="utf-8") as f:
    f.write(summary)

# Step 4: Generate audio
generate_tts(summary, audio_path)

# Step 5: Create video
create_video(summary, audio_path, video_path)

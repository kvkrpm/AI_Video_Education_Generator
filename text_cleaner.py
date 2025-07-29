# modules/text_cleaner.py
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9., ]', '', text)
    text = re.sub(r'Page\s+\d+', '', text, flags=re.IGNORECASE)
    return text.strip()

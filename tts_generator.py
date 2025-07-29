# tts_generator.py

import pyttsx3
import os

def generate_tts(text, output_path):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    print(f"✅ Audio saved to {output_path}")

if __name__ == "__main__":
    summary_path = "data/summaries/os_summary.txt"
    audio_path = "data/audio/os_summary.mp3"

    if not os.path.exists(summary_path):
        print("[❌] Summary file not found.")
    else:
        with open(summary_path, "r", encoding="utf-8") as f:
            summary_text = f.read()

        # Optional: Limit to first 1500 characters if it's too long
        if len(summary_text) > 1500:
            summary_text = summary_text[:1500]

        generate_tts(summary_text, audio_path)

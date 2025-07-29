# summarizer.py

import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize_text(text, sentence_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return "\n".join(str(sentence) for sentence in summary)

def chunk_text(text, max_chars=5000):
    return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]

if __name__ == "__main__":
    input_path = "data/extracted_texts/os.txt"
    output_path = "data/summaries/os_summary.txt"

    if not os.path.exists(input_path):
        print(f"[❌] Input file not found: {input_path}")
        exit()

    with open(input_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    if not raw_text.strip():
        print("[❌] Extracted text is empty.")
        exit()

    print("🔄 Chunking and summarizing...")
    chunks = chunk_text(raw_text, max_chars=5000)

    all_summaries = []
    for idx, chunk in enumerate(chunks):
        print(f"🧠 Summarizing chunk {idx + 1}/{len(chunks)}...")
        summary = summarize_text(chunk, sentence_count=5)
        all_summaries.append(f"--- Summary Chunk {idx + 1} ---\n" + summary)

    final_summary = "\n\n".join(all_summaries)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_summary)

    print(f"✅ Final summary saved to: {output_path}")

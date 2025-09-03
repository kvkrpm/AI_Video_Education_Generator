# Pseudocode for search functionality
def search_extracted_content(query):
    results = []
    for text_file in os.listdir(TEXT_DIR):
        with open(os.path.join(TEXT_DIR, text_file)) as f:
            if query.lower() in f.read().lower():
                matching_image = text_file.replace(".txt", ".png")
                results.append({
                    "text_file": text_file,
                    "image": matching_image,
                    "page": extract_page_number(text_file)
                })
    return results
import re

def split_into_chapters(text, book_name):
    pattern = r"\n\s*(CHAPTER|Chapter)\s+[IVXLC0-9]+\.*.*\n"
    matches = list(re.finditer(pattern, text))

    chapters = []
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunk = text[start:end].strip()

        if len(chunk) > 800:
            chapters.append({
                "chapter_id": i,
                "book": book_name,
                "text": chunk
            })
    return chapters

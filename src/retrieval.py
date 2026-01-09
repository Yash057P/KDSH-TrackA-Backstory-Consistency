import pathway as pw

def build_chapter_table(chapters):
    class ChapterSchema(pw.Schema):
        chapter_id: int
        book: str
        text: str

    # ✅ rows MUST be tuples, in schema order
    rows = [
        (
            ch["chapter_id"],
            ch["book"],
            ch["text"],
        )
        for ch in chapters
    ]

    return pw.debug.table_from_rows(ChapterSchema, rows)


def retrieve_evidence(chapters, claim, top_k=3):
    claim_words = set(claim.lower().split())
    scored = []

    for ch in chapters:
        text_words = set(ch["text"].lower().split())
        score = len(claim_words & text_words)
        scored.append((score, ch["text"]))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [s[1] for s in scored[:top_k]]

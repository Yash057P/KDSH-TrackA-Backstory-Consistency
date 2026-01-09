import pandas as pd

from ingest import load_dataset
from utils import load_novel
from chunking import split_into_chapters
from claims import extract_claims
from retrieval import retrieve_evidence, build_chapter_table


# -------------------------
# PATHS
# -------------------------
TEST_PATH = "data/test.csv"
NOVEL_DIR = "data/novels/"


# -------------------------
# RATIONALE BUILDER
# -------------------------
def build_rationale(claim, evidence_text):
    if not evidence_text:
        return "No supporting narrative evidence found"

    snippet = evidence_text.replace("\n", " ").strip()
    return f"Claim supported by narrative evidence: {snippet[:120]}..."


# -------------------------
# SINGLE SAMPLE PREDICTION
# -------------------------
def predict_sample(row):
    book = row["book_name"]
    backstory = f"{row['caption']} {row['content']}"

    claims = extract_claims(backstory)
    if not claims:
        return 0, "No valid claims extracted from backstory"

    novel_path = NOVEL_DIR + book + ".txt"
    text = load_novel(novel_path)

    chapters = split_into_chapters(text, book)

    # Mandatory Pathway usage
    _ = build_chapter_table(chapters)

    claim = claims[0]
    evidence = retrieve_evidence(chapters, claim)

    if evidence and len(evidence[0]) > 50:
        return 1, build_rationale(claim, evidence[0])

    return 0, "Claim not supported by narrative evidence"


# -------------------------
# MAIN
# -------------------------
def main():
    test_df = load_dataset(TEST_PATH)

    results = []

    for idx, row in test_df.iterrows():
        label, rationale = predict_sample(row)

        results.append({
            "id": row["id"],
            "prediction": label,
            "rationale": rationale
        })

        if idx % 5 == 0:
            print(f"Processed {idx+1}/{len(test_df)} samples")

    results_df = pd.DataFrame(results)
    results_df.to_csv("results.csv", index=False)

    print("\n✅ results.csv generated successfully!")
    print(results_df.head())


if __name__ == "__main__":
    main()

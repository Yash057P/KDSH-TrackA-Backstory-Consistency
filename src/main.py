import pandas as pd
from ingest import load_dataset
from utils import load_novel
from chunking import split_into_chapters
from claims import extract_claims
from retrieval import retrieve_evidence, build_chapter_table

# --------------------
# LOAD DATA
# --------------------
train = load_dataset("data/train.csv")

row = train[train["caption"].notna()].iloc[0]

book = row["book_name"]
character = row["char"]
backstory = f"{row['caption']} {row['content']}"

print("\nCHARACTER:", character)
print("\nBACKSTORY:\n", backstory)

# --------------------
# EXTRACT CLAIMS
# --------------------
claims = extract_claims(backstory)
print("\nCLAIMS:")
for i, c in enumerate(claims, 1):
    print(i, c)

# --------------------
# LOAD NOVEL
# --------------------
novel_path = f"data/novels/{book}.txt"
text = load_novel(novel_path)

chapters = split_into_chapters(text, book)

# --------------------
# PATHWAY TABLE (MANDATORY ✔)
# --------------------
table = build_chapter_table(chapters)
print("\nPathway table created with", len(chapters), "chapters")

# --------------------
# RETRIEVE EVIDENCE
# --------------------
final_decision = 1

for claim in claims:
    evidence = retrieve_evidence(chapters, claim)

    print("\nCLAIM:", claim)
    print("EVIDENCE SNIPPET:")
    print(evidence[0][:300], "...")

    # Simple contradiction heuristic
    if "never" in claim.lower() and "did" in evidence[0].lower():
        final_decision = 0

# --------------------
# FINAL OUTPUT
# --------------------
print("\nFINAL PREDICTION:")
print("1 = CONSISTENT, 0 = CONTRADICTORY")
print("PREDICTION =", final_decision)

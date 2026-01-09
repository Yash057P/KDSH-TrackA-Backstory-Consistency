import pandas as pd

def extract_claims(text):
    if pd.isna(text):
        return []

    text = str(text).strip()
    if len(text) < 40:
        return []

    sentences = text.split(".")
    claims = []

    for s in sentences:
        s = s.strip()
        if len(s) > 20:
            claims.append(s)

    return claims

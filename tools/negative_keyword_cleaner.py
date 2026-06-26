#!/usr/bin/env python3
"""
Clean and deduplicate Arabic/English negative keywords for Google Ads.

Usage:
python tools/negative_keyword_cleaner.py --input templates/negative_keywords_arabic.csv --output cleaned.csv --match phrase
"""

import argparse
import csv
import re
from pathlib import Path

ARABIC_DIACRITICS = re.compile(r"[\u064B-\u065F\u0670]")
MULTISPACE = re.compile(r"\s+")

def normalize_keyword(text: str) -> str:
    text = text.strip().lower()
    text = ARABIC_DIACRITICS.sub("", text)
    text = text.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    text = text.replace("ى", "ي").replace("ة", "ه")
    text = MULTISPACE.sub(" ", text)
    return text

def format_match(keyword: str, match_type: str) -> str:
    if match_type == "exact":
        return f"[{keyword}]"
    if match_type == "phrase":
        return f'"{keyword}"'
    return keyword

def read_keywords(path: Path):
    rows = []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if "keyword" not in reader.fieldnames:
            raise ValueError("Input CSV must contain a 'keyword' column.")
        for row in reader:
            keyword = row.get("keyword", "")
            if keyword.strip():
                rows.append(row)
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input CSV with keyword column")
    parser.add_argument("--output", required=True, help="Output CSV")
    parser.add_argument("--match", choices=["broad", "phrase", "exact", "keep"], default="keep")
    args = parser.parse_args()

    rows = read_keywords(Path(args.input))
    seen = set()
    output_rows = []

    for row in rows:
        normalized = normalize_keyword(row["keyword"])
        if normalized in seen:
            continue
        seen.add(normalized)

        match_type = row.get("match_type", args.match)
        if args.match != "keep":
            match_type = args.match

        output_rows.append({
            "keyword": normalized,
            "google_ads_negative": format_match(normalized, match_type),
            "match_type": match_type,
            "category": row.get("category", ""),
            "reason_ar": row.get("reason_ar", "")
        })

    with Path(args.output).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["keyword", "google_ads_negative", "match_type", "category", "reason_ar"])
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Saved {len(output_rows)} cleaned negative keywords to {args.output}")

if __name__ == "__main__":
    main()

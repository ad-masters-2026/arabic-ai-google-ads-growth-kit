#!/usr/bin/env python3
"""
Generate a simple Search campaign structure CSV from a keyword list.

Usage:
python tools/campaign_structure_generator.py --input examples/sample_keywords.csv --output examples/generated_structure.csv --campaign "Search | Core | AR" --url https://example.com
"""

import argparse
import csv
from pathlib import Path

NEGATIVE_HINTS = [
    "مجاني", "مجانا", "كورس", "دورة", "وظائف", "وظيفة", "شرح", "تحميل", "pdf", "تسجيل دخول", "راتب", "تعلم"
]

def classify(keyword: str) -> str:
    k = keyword.lower()
    if any(h in k for h in NEGATIVE_HINTS):
        return "negative_candidate"
    if "جوجل" in k or "google" in k:
        return "core_google_ads"
    return "general"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--campaign", required=True)
    parser.add_argument("--url", required=True)
    args = parser.parse_args()

    with Path(args.input).open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        keywords = [row["keyword"].strip() for row in reader if row.get("keyword", "").strip()]

    rows = []
    for kw in keywords:
        bucket = classify(kw)
        if bucket == "negative_candidate":
            rows.append([args.campaign, "NEGATIVE_CANDIDATES", kw, "negative_phrase", args.url, "Exclude or review", "Review before adding"])
        elif bucket == "core_google_ads":
            rows.append([args.campaign, "Google Ads Core", kw, "phrase", args.url, "Direct service", "High relevance"])
        else:
            rows.append([args.campaign, "General", kw, "phrase", args.url, "General intent", "Needs review"])

    with Path(args.output).open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["campaign_name","ad_group","keyword","match_type","final_url","ad_angle","notes"])
        writer.writerows(rows)

    print(f"Saved {len(rows)} rows to {args.output}")

if __name__ == "__main__":
    main()

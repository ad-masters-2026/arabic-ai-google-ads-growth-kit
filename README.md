# Arabic AI Google Ads Growth Kit

**An open-source toolkit for Arabic-speaking performance marketers who want to structure, optimize, and scale Google Ads campaigns with practical AI workflows.**

> Not affiliated with Google. This project is community-maintained and focuses on educational templates, checklists, prompts, and lightweight tools for Arabic/MENA performance marketing use cases.

## Why this exists

Most high-quality Google Ads learning resources, templates, and AI workflows are written in English and are not adapted to Arabic search behavior, MENA lead-generation campaigns, Arabic negative keywords, bilingual landing pages, or agency reporting workflows.

This repository provides a practical operating system for:

- Google Search campaign structure
- Performance Max planning and scaling
- AI-assisted keyword research
- Arabic negative keyword expansion
- Ad copy generation and review
- Landing-page message matching
- Conversion tracking and lead-quality scoring
- Scaling decisions based on signals, not guesswork

## Who this helps

- Arabic-speaking media buyers
- Freelancers and agencies in MENA
- Small businesses running Google Ads
- E-commerce teams testing Search, Shopping, and Performance Max
- Students learning paid acquisition with AI support

## What is inside

```text
docs/
  01-ai-google-ads-operating-system.md
  02-search-campaign-structure-ar.md
  03-pmax-scaling-playbook-ar.md
  04-ai-prompt-workflows-ar.md
  05-measurement-conversion-tracking-ar.md
  06-landing-page-message-match-ar.md

templates/
  negative_keywords_arabic.csv
  search_campaign_structure_template.csv
  pmax_asset_group_planner.csv
  lead_quality_scoring_template.csv
  ai_keyword_research_brief.md
  weekly_optimization_report_template.md

prompts/
  google_ads_ai_prompt_library.md

tools/
  negative_keyword_cleaner.py
  campaign_structure_generator.py

examples/
  sample_keywords.csv
  sample_negative_keywords_output.csv
```

## Quick start

1. Clone or download the repository.
2. Open `docs/01-ai-google-ads-operating-system.md`.
3. Use `templates/ai_keyword_research_brief.md` to define the business, offer, market, and landing page.
4. Use the prompt library to generate campaign ideas and negative keyword candidates.
5. Use `tools/negative_keyword_cleaner.py` to clean and deduplicate keyword lists.
6. Use the Search and PMax templates to plan campaigns before launching.

## Example: clean Arabic negative keywords

```bash
python tools/negative_keyword_cleaner.py \
  --input templates/negative_keywords_arabic.csv \
  --output examples/sample_negative_keywords_output.csv \
  --match phrase
```

## Core philosophy

AI should not replace marketing judgment. It should help you:

- Find patterns faster
- Create better hypotheses
- Improve campaign consistency
- Avoid missing obvious exclusions
- Make budget scaling safer
- Document decisions clearly

The media buyer still owns strategy, offer quality, measurement quality, and business results.

## Suggested repository topics

`google-ads` `performance-marketing` `arabic` `mena` `ai-marketing` `negative-keywords` `pmax` `search-ads` `growth-marketing`

## Roadmap

- [ ] Add more Arabic negative keyword categories by industry
- [ ] Add e-commerce PMax feed audit checklist
- [ ] Add GA4 and Google Ads conversion QA checklist
- [ ] Add bilingual landing-page audit prompts
- [ ] Add examples for Saudi, UAE, Egypt, and Kuwait markets
- [ ] Add automated CSV exporter for Google Ads Editor
- [ ] Add community-submitted campaign structures

## Contributing

Contributions are welcome. Please read `CONTRIBUTING.md`.

Useful contributions include:

- Arabic negative keyword lists
- Search campaign structures for specific industries
- PMax asset group examples
- Lead quality scoring logic
- Arabic ad-copy examples
- Measurement QA checklists
- Case-study templates without private client data

## License

MIT License. See `LICENSE`.

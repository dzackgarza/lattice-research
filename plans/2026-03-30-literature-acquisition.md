# Plan: Literature Acquisition for Local Reference Library

**Created**: 2026-03-30 16:03 UTC **Status**: Active **SCHEDULE.md slot**: 17:00-18:00
(preparing early)

## Context

REFERENCES.md lists 13 canonical sources but none are available locally in
machine-parseable form.
GOAL.md Priority 1 emphasizes centralizing canonical literature, and SCHEDULE.md
17:00-18:00 slot specifically tasks ensuring literature is available locally to avoid
repeated fetching.

Current state:
- No papers/ directory exists
- No PDF files in repo
- All 13 sources in REFERENCES.md are external references only

## Goal

Acquire machine-parseable versions (PDFs, extracted markdown) of all obtainable sources
from REFERENCES.md and organize them in a local papers/ directory.

## Phase 1 — Identify obtainable sources [COMPLETE]

Freely available (3 sources):
- [x] Dolgachev & Kondō (2013) - https://arxiv.org/pdf/1201.6093
- [x] AEGS (2023) - https://arxiv.org/pdf/2312.03638
- [x] C. Thas (1994) -
  https://cjhb.site/Files.php/Books/%28Uncategorized%29/2022-23/rational%20sextic.pdf

Restricted access - institutional required (4 sources):
- [x] Friedman (1984) - JSTOR paywall
- [x] Coble (1929) - HathiTrust (login required)
- [x] Coolidge (1931) - HathiTrust (login required)
- [x] Sterk (1991) - Springer paywall

Purchase required (1 source):
- [x] Scattone (1987) - AMS Bookstore

Not found / unavailable (5 sources):
- [x] Coble (1917) - Likely JSTOR paywall, not located
- [x] Nikulin (1979) - Russian original, translation not located
- [x] Nikulin (1980) - Russian original, translation not located
- [x] Garza (2024) - Does not exist as separate publication (dissertation in progress)
- [x] Garza (2026) - Dissertation expected May 2025, not yet published

## Phase 2 — Acquire available sources

Priority order (easiest to hardest):
1. Author's own papers (Garza 2024, 2026)
2. Arxiv papers (AEGS 2023, possibly Dolgachev, Friedman, Nikulin)
3. Archive.org books (Coolidge 1931, Coble 1929)
4. Institutional repositories (Sterk, Scattone)
5. JSTOR/paywalled journals (Coble 1917, C. Thas 1994)

For each acquired source:
- [ ] Download PDF to papers/ directory
- [ ] Use reading-pdfs skill to extract markdown
- [ ] Store extracted markdown in papers/extracted/
- [ ] Update REFERENCES.md with local file paths

## Phase 3 — Document gaps

For sources that remain unavailable:
- [ ] Update GAPS.md with specific blockers (paywall, no open access, etc.)
- [ ] Note which claims depend on unavailable sources
- [ ] Identify workarounds (secondary sources, partial access via Google Books preview,
  etc.)

## Verification

Success: papers/ directory exists with at least 5 obtainable sources in both PDF and
extracted markdown form, REFERENCES.md updated with local paths.

## Notes

- C. Thas (1994) is known to be behind paywall - skip unless user provides institutional
  access
- Coolidge (1931) may have partial Google Books preview - check before attempting full
  acquisition
- Author's own papers (Garza) should be easiest to obtain
- Use reading-pdfs skill (Mistral OCR) for extraction, not ad-hoc tools

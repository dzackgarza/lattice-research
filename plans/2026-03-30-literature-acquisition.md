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

## Phase 1 — Identify obtainable sources

For each source in REFERENCES.md, determine availability:

- [ ] Coble (1917) - American Journal of Mathematics (check JSTOR, arxiv, institutional
  access)
- [ ] C. Thas (1994) - Geometriae Dedicata (KNOWN: behind $39.95 Springer paywall)
- [ ] Coolidge (1931) - Treatise on Algebraic Plane Curves (check archive.org, Google
  Books)
- [ ] Coble (1929) - Algebraic Geometry and Theta Functions (check archive.org, AMS)
- [ ] Dolgachev & Kondō (2013) - check arxiv, author websites
- [ ] Sterk (1991) - check author website, institutional repositories
- [ ] Scattone (1987) - check institutional repositories
- [ ] Friedman (1984) - check author website, arxiv
- [ ] Nikulin (1979) - check author website, institutional repositories, arxiv
- [ ] Nikulin (1980) - check author website, institutional repositories
- [ ] AEGS (2023) - check arxiv (likely available)
- [ ] Garza (2024) - check author's own repository
- [ ] Garza (2026) - check author's own repository

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

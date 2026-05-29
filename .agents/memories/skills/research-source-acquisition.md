---
title: Research Source Acquisition
status: active
date: 2026-05-29
---
# Research Source Acquisition

Use it before adding, auditing, or relying on durable source material under `theory/`.

## Load with this skill

- Load `zotero-api` before querying the local Zotero cache.
- Load `zotero` only when the Zotero write API is needed.
- Load `read-arxiv-paper` when the source is on arXiv.
- Load `pdf-extraction` before invoking MinerU, SSH extraction, MinerU API, or Mistral
  OCR through `~/pdf-extraction`.
- Load `reading-pdfs` when using the local `~/pdfs` cache or Mistral OCR cache path.
- Read `mem:skills/research-proof-auditing` when the source is evidence for a proof,
  theorem, algorithm, or accepted mathematical claim.

## Core invariant

Every durable theory claim needs traceable primary source material.

- Keep bibliographic metadata in `theory/references/references.bib`.
- Keep the source map in `theory/references/index.md`.
- Keep reusable extracted text in `theory/references/literature/`.
- Update `theory/references/claim-map.md` when a source backs a standard definition,
  theorem, algorithm, or implementation-critical claim.
- If mathematical research in chat, plans, specs, or notes relies on an external or web
  source, record the result in a durable mathematical report memory with source links.

## Preferred workflow

- Start inside the repo.
  Check `theory/references/index.md`, `theory/references/references.bib`,
  `theory/references/literature/`, and `theory/references/claim-map.md` before searching
  elsewhere.
- Check Zotero next. Use the local Zotero API cache for metadata, BetterBibTeX citation
  keys, existing PDFs, extracted Markdown attachments, and full-text hits.
- Prefer primary sources over secondary summaries.
- If no reliable extracted text exists, route extraction through `~/pdf-extraction`.
  Prefer MinerU local GPU when available.
- Never fall back to low-quality PDF extraction tools banned by the `pdf-extraction`
  policy.
- Treat extracted Markdown as OCR-derived source material.

## Repository artifacts

- Use stable citation keys from Zotero or BetterBibTeX when available.
- Do not commit large PDFs by default.
- When a source supports implementation or spec work, link it from the relevant plan,
  card, theory note, or category-spec artifact.
- Do not leave web-backed mathematical findings only in chat.

## Completion check

Before treating source acquisition as complete, confirm that the source has:
- A citation record or explicit metadata gap.
- A known source location.
- A known extraction path or reason extraction was unnecessary.
- A trust boundary explaining what was checked directly and what remains OCR-derived.
- Links from the theory, plan, spec, or card that will consume it.

---
name: category-spec-smoke-triage
description: Use when handling category-spec smoke tests, smoke-frontier findings,
  missing constructor coverage, or deciding whether a smoke failure becomes implementation
  work, spec work, research, or a decision.
---

# Category Spec Smoke Triage

Use this skill for smoke-frontier project management.

## Required references

Load `category-spec-workflow` and `category-spec-style` before changing smoke-related cards or specs.

## Rules

- Do not run smoke tests when known design, architecture, layout, or spec violations remain unresolved.
- Smoke status is not the goal; smoke output inventories missing obligations.
- Do not weaken a spec, bypass a constructor, catch away an error, or check shallow implementation detail merely to pass smoke.
- Record smoke findings as Nimbalyst cards, not local triage reports.

## Routing

- Missing methods, smoke failures, and structural blockers go to implementation cards.
- Missing spec surface goes to spec cards.
- Ownership, naming, or admission ambiguity goes to decision cards.
- Evidence gaps go to research cards.
- Vague tangential findings go to `.agents/TODO.md`.

---
title: Category Spec Smoke Triage
status: active
date: 2026-05-29
---
# Category Spec Smoke Triage

Use this skill for smoke-frontier project management.

## Required references

Read `mem:skills/category-spec-workflow` and load `category-spec-style` before changing
smoke-related cards or specs.

## Rules

- Do not run smoke tests when known design, architecture, layout, or spec violations
  remain unresolved.
- Smoke status is not the goal; smoke output inventories missing obligations.
- Do not weaken a spec, bypass a constructor, catch away an error, or check shallow
  implementation detail merely to pass smoke.
- Record smoke findings as Nimbalyst cards, not local triage reports.

## Routing

- Missing methods, smoke failures, and structural blockers go to implementation cards.
- Missing spec surface goes to spec cards.
- Ownership, naming, or admission ambiguity goes to decision cards.
- Evidence gaps go to research cards.
- Vague tangential findings go to `.agents/TODO.md`.

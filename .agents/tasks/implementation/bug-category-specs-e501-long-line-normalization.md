---
trackerStatus:
  type: bug
title: Normalize category_specs Ruff E501 long-line blockers
status: in-progress
priority: medium
planId: SPR-VARIADIC-AUDIT-01KQN9
complexity: 64
progress: 97
created: '2026-05-03'
updated: '2026-05-03'
tags:
  - category-specs
  - implementation
  - bug
  - audit
  - validation
  - quality-control
  - ruff
  - theme-audit-uniformity
---

# Normalize category_specs Ruff E501 long-line blockers

## Summary

Resolve the remaining Ruff `E501` line-length blockers in `category_specs` while
preserving mathematical and public API meaning.

## Source Provenance

- Split from `.agents/tasks/implementation/bug-category-specs-ruff-normalization-blocker.md`.
- Codex Spark triage on 2026-05-03 reported 420 `E501` findings after `just test`
  reached the global QC Ruff normalization stage.
- Representative surfaces include `category_specs/algebras/__init__.py`,
  `category_specs/modules/__init__.py`, `category_specs/rings/__init__.py`,
  `category_specs/rings/subcategories/*.py`, and `category_specs/forms/chain.py`.

## Context

Line length is not a mathematical priority by itself, but it is currently a validation
gate for implementation cards because global QC runs Ruff normalization before the rest
of `just test`. Keep the cleanup mechanical and avoid changing source meaning.

## Complexity And Ownership

- Owner role: implementation cleanup worker with parent review.
- Complexity: 64, high band.
- Rationale: the work is mostly mechanical but spans many files and package surfaces.
  Risk comes from accidentally changing import, lazy-import, or type-aggregation
  semantics while wrapping long expressions.

## Acceptance Criteria

- [x] Reproduce the remaining `E501` findings for `category_specs`.
- [x] Wrap long import, lazy-import, type-alias, docstring, and expression lines in the
  smallest semantics-preserving way.
- [x] Avoid broad rewrites, comment churn, or source-prose edits unrelated to Ruff
  `E501`.
- [x] Do not add local Ruff ignores, bypasses, whitelists, or quality-control
  exceptions.
- [x] Keep public names and import side effects stable.

## Dependencies And Boundaries

- Parent blocker: `.agents/tasks/implementation/bug-category-specs-ruff-normalization-blocker.md`.
- Coordinate with the import-hygiene card if the same package `__init__.py` lines are
  also `F401` or `E402` findings.
- Do not use this card to change mathematical specifications, constructor routing, or
  category ownership.

## Validation Requirements

- Run `just test` after the cleanup attempt.
- If `just test` remains blocked, record the first remaining blocker and representative
  rule families in this card and the parent blocker.

## Work Log

- 2026-05-03: Created from Codex Spark triage of the category-specs Ruff normalization
  blocker.
- 2026-05-03: Reproduced and cleared all `E501` findings in
  `category_specs` via `uvx --from ruff ruff check --select E501 category_specs`,
  resolving the reported 424+ overlong lines to zero.
- 2026-05-03: Reformatted targeted long-line offenders in
  `category_specs/{algebras/forms/modules/rings/**}/**/*.py` and resolved residual
  long-docstring/import line issues manually with minimal wrapping in
  `category_specs/forms/__init__.py` and `category_specs/algebras/__init__.py`.
- 2026-05-03: `python -m compileall category_specs` passed without syntax/runtime compile
  errors.
- 2026-05-03: `just test` now fails at `vulture` dead-code detection stage with
  broad pre-existing unused-code findings (hundreds of hits); no remaining `E501`
  or `Ruff format/check` errors remain from this leaf.

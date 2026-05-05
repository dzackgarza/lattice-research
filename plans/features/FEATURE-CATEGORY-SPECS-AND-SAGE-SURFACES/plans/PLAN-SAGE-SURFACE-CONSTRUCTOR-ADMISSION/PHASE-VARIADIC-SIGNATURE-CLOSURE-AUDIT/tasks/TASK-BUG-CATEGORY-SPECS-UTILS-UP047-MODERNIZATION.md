---
id: TASK-BUG-CATEGORY-SPECS-UTILS-UP047-MODERNIZATION
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Modernize category_specs utils generics for Ruff UP047
status: needs-review
priority: medium
description: Resolve the two Ruff `UP047` findings in `category_specs/utils.py` by using the
  project-supported generic function syntax without changing helper behavior.
successCriteria:
- Reproduce the `UP047` findings in `category_specs/utils.py`.
- Modernize the two generic helper signatures in place.
- Preserve runtime behavior and public helper names.
- Do not bundle unrelated Ruff cleanup into this card.
complexity: 24
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
- category-specs
- audit
- validation
- quality-control
- ruff
- theme-audit-uniformity
- theme-local-cleanup
created: '2026-05-03'
updated: '2026-05-05'
---
# Modernize category_specs utils generics for Ruff UP047

## Summary

Resolve the two Ruff `UP047` findings in `category_specs/utils.py` by using the
project-supported generic function syntax without changing helper behavior.

## Source Provenance

- Split from `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-RUFF-NORMALIZATION-BLOCKER.md`.
- Codex Spark triage on 2026-05-03 reported two `UP047` findings in
  `category_specs/utils.py`, specifically `_fold_nonempty_binary_operation` and
  `foldable_operation`.

## Context

This is a bounded utility modernization needed for the same `just test` QC gate as the
broader Ruff blocker. It is intentionally separate because it does not share the public
package-surface risk of import hygiene or the broad mechanical footprint of `E501`.

## Complexity And Ownership

- Owner role: local implementation worker.
- Complexity: 24, low band.
- Rationale: the affected surface is one utility file and two helper signatures. The
  verification burden is still nonzero because the helpers are generic decorators used
  across category specs.

## Acceptance Criteria

- [x] Reproduce the `UP047` findings in `category_specs/utils.py`.
- [x] Modernize the two generic helper signatures in place.
- [x] Preserve runtime behavior and public helper names.
- [x] Do not bundle unrelated Ruff cleanup into this card.

## Dependencies And Boundaries

- Parent blocker: `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-RUFF-NORMALIZATION-BLOCKER.md`.
- Do not change callers unless the signature modernization reveals a real type/runtime
  incompatibility.

## Validation Requirements

- Run targeted Ruff diagnostics for `category_specs/utils.py`.
- Run `just test` after the cleanup attempt or record the remaining blocker stage if
  broader category-spec Ruff failures still prevent a full pass.

## Work Log

- 2026-05-03: Created from Codex Spark triage of the category-specs Ruff normalization
  blocker.
- 2026-05-03: Reproduced the two `UP047` findings with targeted Ruff, modernized
  `_fold_nonempty_binary_operation` and `foldable_operation` to inline generic
  function syntax, and kept the generic annotations internally consistent after Ruff's
  follow-on type-parameter rename.
- 2026-05-03: Targeted `uvx --from ruff ruff check category_specs/utils.py` and
  `python -m compileall category_specs/utils.py` pass. Full `just test` still fails in
  category-spec Ruff normalization with 532 remaining `F401`/`E402`/`E501` blockers.
- 2026-05-05: Moved to `in-review`; all card-local acceptance criteria and targeted
  validation evidence were already recorded. Remaining global QC blockers are tracked
  on the parent Ruff/vulture cards, not this UP047 leaf.

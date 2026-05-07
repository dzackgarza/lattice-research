---
id: TASK-BUG-CATEGORY-SPECS-RUFF-NORMALIZATION-BLOCKER
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Triage category_specs Ruff normalization blocker for implementation validation
status: needs-review
priority: high
description: '`just test` reaches the global quality-control Ruff normalization stage
  but fails on repo-wide `category_specs` findings. This blocks validation evidence
  for implementation cards even when the implementation diff is narrower than the
  QC backlog.'
successCriteria:
- Reproduce the current `just test` Ruff blocker and preserve a concise failure summary
  in this card.
- Classify remaining findings by owner surface and rule family without weakening global
  QC.
- Split owner-specific cards for independent cleanup surfaces that are not one coherent
  patch.
- Carry forward formatter/linter auto-fixes already produced by repository tooling.
- Either make `just test` pass or record exactly which linked cards remain validation
  blockers.
complexity: 78
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Triage category_specs Ruff normalization blocker for implementation validation

## Summary

`just test` reaches the global quality-control Ruff normalization stage but fails on
repo-wide `category_specs` findings. This blocks validation evidence for implementation
cards even when the implementation diff is narrower than the QC backlog.

## Source Provenance

- Triggered while validating
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-FOUNDATION-KERNEL/PHASE-CATEGORY-OBJECT-SURFACE-UNIFORMIZATION-AND-CONSTRUCTOR-AGGREGATION/tasks/TASK-1777748120649-EQPN1A-ADD-MISSING-FINAL-MARKERS-AND-RETURN-ANNOTATIONS-ON-CAT-METHODS.md`.
- `just test` output on 2026-05-03: Ruff auto-fixed 80 findings, then reported 534
  remaining findings across `category_specs`.
- `.agents/current-goal-phase.md` says QC is a gate for implementation surfaces and
  phase transitions, while incidental QC cleanup should not steer churn-heavy spec
  work.
- Owning plan: `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT`, under `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`.

## Context

The blocker is larger than the Cat final-marker task. The first non-obvious routing
choice is to avoid burying hundreds of Ruff findings inside an unrelated Cat card.
The correct next step is a triage pass that separates validation-blocking cleanup from
spec-phase noise and opens owner-specific work when the findings are not one coherent
fix.

Observed representative finding classes include:

- `E402` import placement findings in package initialization/type aggregation surfaces.
- `F401` re-export/import findings where public re-export intent must be made explicit
  or the import removed.
- `E501` long-line findings across generated or broad subcategory import surfaces.
- `UP047` type-parameter modernization findings in utility helpers.

## Triage Result

Codex Spark read-only triage on 2026-05-03 reproduced the blocker and reported that
the current `just test` normalization pass still fails with 534 Ruff errors after the
previous auto-fixes. The remaining rule-family summary was:

- `E501`: 420 line-length findings.
- `F401`: 87 unused-import findings.
- `E402`: 25 import-placement findings.
- `UP047`: 2 generic-type-parameter modernization findings.

The triage found no single coherent implementation patch. The blocker should be
resolved through these leaf cards:

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-IMPORT-HYGIENE-RUFF-F401-E402.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-E501-LONG-LINE-NORMALIZATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-CATEGORY-SPECS-UTILS-UP047-MODERNIZATION.md`

After resolving the `UP047` utility leaf locally, `just test` still fails in the same
global QC Ruff normalization stage with 532 remaining findings, all in the import
hygiene and long-line cleanup surfaces.

After resolving the import-hygiene leaf, `uvx --from ruff ruff check --select
F401,E402,F821 category_specs` passes. `just test` now reaches the same Ruff
normalization stage and reports 424 remaining `E501` findings, all owned by the linked
long-line normalization card.

After resolving the long-line normalization leaf, the Ruff normalization stage passes.
`just test` now fails later in global vulture dead-code detection; that is tracked
separately in `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-REPO-VULTURE-DEAD-CODE-VALIDATION-BLOCKER.md`.

Current 2026-05-07 validation after the reopened E501 cleanup: `uvx --from ruff ruff
check --select E501 category_specs --output-format json | jq 'length'` reports `0`.
`just test` now passes Python syntax validation and Sage syntax validation, then fails
earlier than Ruff at the global mypy stage with broad existing Sage/pytest import-stub
and category typing errors. The active validation blocker is therefore not a Ruff
normalization blocker. It is a global type-checking/QC issue already noted in adjacent
validation cards, and it does not block DAG-ready spec-phase leaves unless the user is
attempting a QC/phase-transition gate.

## Complexity And Ownership

- Owner role: audit/validation worker, with parent-agent review.
- Complexity: 78, high band.
- Rationale: the work touches many category-spec surfaces and validation policy, but
  the first deliverable is triage plus bounded owner-specific splits, not a single
  repo-wide rewrite. If the triage shows the blocker requires several independent
  cleanups, split those cards before implementation.

## Acceptance Criteria

- [x] Reproduce the current `just test` Ruff blocker and preserve a concise failure
  summary in this card.
- [x] Classify remaining findings by owner surface and rule family without weakening
  global QC.
- [x] Split owner-specific cards for independent cleanup surfaces that are not one
  coherent patch.
- [x] Carry forward formatter/linter auto-fixes already produced by repository tooling.
- [x] Either make `just test` pass or record exactly which linked cards remain
  validation blockers.

## Dependencies And Boundaries

- Do not add project-local QC bypasses, Ruff ignores, local whitelists, or quality-control
  overrides.
- Do not fold this broad cleanup into the Cat final-marker task.
- Do not rewrite mathematical specs only to satisfy formatting if the rewrite changes
  source meaning.
- Use `just test`; do not substitute ad hoc Ruff-only success for full validation.

## Validation Requirements

- Run `just test` after any attempted cleanup.
- If `just test` still fails, record the first blocking stage and representative rule
  families with enough detail to route the next card.

## Work Log

- 2026-05-03: Created after Cat implementation validation exposed a repo-wide Ruff
  normalization blocker.
- 2026-05-03: Codex Spark read-only triage reproduced the blocker, classified the
  remaining findings, and recommended splitting by import hygiene, line-length
  normalization, and `UP047` utility modernization.
- 2026-05-03: Resolved the `UP047` utility leaf locally; targeted Ruff and compileall
  pass for `category_specs/utils.py`. Full `just test` remains blocked by the linked
  import-hygiene and `E501` leaf cards.
- 2026-05-03: Resolved the import-hygiene leaf enough for full category-spec
  `F401`/`E402`/`F821` Ruff diagnostics to pass. Full `just test` remains blocked by
  424 `E501` long-line findings, delegated to Codex Spark under the linked long-line
  leaf card.
- 2026-05-03: Resolved the long-line leaf enough for Ruff format/check to pass inside
  `just test`. Validation now advances to and fails at global vulture dead-code
  detection, so the remaining validation gate is no longer a Ruff-normalization
  blocker.
- 2026-05-07: Re-ran validation after the reopened E501 cleanup. `uvx --from ruff
  ruff check --select E501 category_specs --output-format json | jq 'length'` reports
  `0`. `just test` passes Python and Sage syntax validation, then fails at global
  mypy before Ruff with broad existing Sage/pytest import-stub and category typing
  errors. The Ruff-normalization blocker remains cleared; the current full-QC blocker
  is not phase-local Ruff work.

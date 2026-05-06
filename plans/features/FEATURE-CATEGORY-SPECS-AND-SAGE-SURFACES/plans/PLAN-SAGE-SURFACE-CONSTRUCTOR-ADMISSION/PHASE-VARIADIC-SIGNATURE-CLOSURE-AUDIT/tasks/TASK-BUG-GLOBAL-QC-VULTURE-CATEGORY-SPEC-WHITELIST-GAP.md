---
id: TASK-BUG-GLOBAL-QC-VULTURE-CATEGORY-SPEC-WHITELIST-GAP
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Align global vulture whitelist with category-spec public surfaces
status: blocked
priority: high
description: Prepare an explicit global QC whitelist proposal for category-spec public
  and Sage-dynamic surfaces currently reported by vulture as dead code.
successCriteria:
- Produce a categorized whitelist proposal for intentional category-spec vulture findings.
- Keep the proposal scoped to category-spec public/dynamic surfaces; do not whitelist
  unrelated dead code.
- Request explicit user approval before editing `/home/dzack/ai/quality-control`.
- After approval and implementation, run `just test` and record the next blocker.
complexity: 76
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
---
# Align global vulture whitelist with category-spec public surfaces

## Summary

Prepare an explicit global QC whitelist proposal for category-spec public and
Sage-dynamic surfaces currently reported by vulture as dead code.

## Source Provenance

- Split from `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-REPO-VULTURE-DEAD-CODE-VALIDATION-BLOCKER.md`.
- Codex Spark read-only triage on 2026-05-03 found 762 category-spec vulture findings
  after Ruff normalization passed.
- The global QC vulture recipe reads `/home/dzack/ai/quality-control/vulture_whitelist.py`,
  which already contains category-spec abstract interface names but does not cover the
  current public surface.

## Context

Most category-spec findings are not delete candidates. They are public type aliases,
abstract methods, package re-export variables, and Sage method-provider hooks that are
used dynamically or intentionally exposed for downstream category-spec work. Because the
fix likely changes global QC behavior, it needs explicit user approval before editing
`/home/dzack/ai/quality-control`.

## Complexity And Ownership

- Owner role: global QC triage worker with category-spec parent review.
- Complexity: 76, high band.
- Rationale: this crosses repo-local category-spec semantics and global quality-control
  policy. The work is not hard mechanically, but the approval and classification burden
  is high because an overbroad whitelist can hide real dead code in other projects.

## Acceptance Criteria

- [x] Produce a categorized whitelist proposal for intentional category-spec vulture
  findings.
- [x] Keep the proposal scoped to category-spec public/dynamic surfaces; do not
  whitelist unrelated dead code.
- [ ] Request explicit user approval before editing `/home/dzack/ai/quality-control`.
- [ ] After approval and implementation, run `just test` and record the next blocker.

## Dependencies And Boundaries

- Parent blocker: `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT/tasks/TASK-BUG-REPO-VULTURE-DEAD-CODE-VALIDATION-BLOCKER.md`.
- Do not edit global QC without explicit approval.
- Do not delete category-spec APIs to satisfy vulture.
- Do not add local project bypasses, local whitelist files, or local QC overrides.

## Validation Requirements

- Reproduce the vulture failure before proposing the whitelist update.
- After any approved global QC edit, run `just test`.

## Current Global QC Evidence

- `/home/dzack/ai/quality-control/justfile` already includes Sage-aware vulture
  scanning in `_vulture`: it collects `*.sage` files, preparses them into a temporary
  directory with `sage --preparse`, verifies the generated `.py` files exist, and adds
  those generated files to the `uvx --from vulture vulture` scan surface.
- `/home/dzack/ai/quality-control/vulture_whitelist.py` already contains a large
  category-spec whitelist surface through `_SpecAbstractNames`, including abstract
  method names, Sage method-provider hooks, type-surface names, constructor names, and
  dynamic category names.
- No repo-local vulture whitelist or bypass should be created.

## Categorized Whitelist Proposal

If a fresh public `just test` run reaches vulture and still reports category-spec
false positives, update `/home/dzack/ai/quality-control/vulture_whitelist.py` only
after explicit user approval, using these categories:

- Category-spec abstract API names: abstract methods declared on `ParentMethods`,
  `ElementMethods`, `MorphismMethods`, `SubcategoryMethods`, Hom/End/Aut surfaces, and
  constructor collectors that Sage binds dynamically.
- Standard type-package and public re-export names: names in `category_specs/types.py`
  and package `__init__.py` files that are public vocabulary for downstream specs,
  not locally-called helpers.
- Sage dynamic hooks and provider names: `_element_constructor_`, axiom/category
  selectors, construction-category names, and method-provider hooks that Sage resolves
  through category machinery.
- Explicit non-whitelist bucket: stale backup artifacts, unreachable code,
  non-public local helpers, and source files outside `category_specs` must remain
  repo-local cleanup or follow-up cards, not global whitelist entries.

The global whitelist change should be name-based and category-spec-scoped. It should
not whitelist arbitrary files, directories, or all vulture findings from this repo.

## Blocker

Blocked on a fresh allowed QC path reaching vulture, or explicit user approval to run
and act on a private vulture-only diagnostic. The current public `just test`/commit
hook path fails earlier at repo-wide mypy on pre-existing Sage/stub/type errors, so the
vulture finding set cannot be reproduced through the public QC workflow right now.

## Work Log

- 2026-05-03: Created from read-only vulture triage.
- 2026-05-06: Checked global QC. Sage preparse support for vulture is already present
  in `/home/dzack/ai/quality-control/justfile`, and the shared whitelist already has
  a broad `_SpecAbstractNames` category-spec surface. Recorded a scoped whitelist
  proposal and marked the card blocked pending fresh vulture output through the public
  QC path or explicit approval for private vulture-only diagnostics/global edits.

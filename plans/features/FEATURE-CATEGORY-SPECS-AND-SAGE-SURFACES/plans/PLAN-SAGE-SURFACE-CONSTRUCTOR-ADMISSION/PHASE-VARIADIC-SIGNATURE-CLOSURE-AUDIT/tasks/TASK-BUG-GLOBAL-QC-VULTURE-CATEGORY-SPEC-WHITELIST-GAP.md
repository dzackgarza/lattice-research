---
id: TASK-BUG-GLOBAL-QC-VULTURE-CATEGORY-SPEC-WHITELIST-GAP
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Align global vulture whitelist with category-spec public surfaces
status: unstarted
priority: high
description: Prepare an explicit global QC whitelist proposal for category-spec public and
  Sage-dynamic surfaces currently reported by vulture as dead code.
successCriteria:
- Produce a categorized whitelist proposal for intentional category-spec vulture findings.
- Keep the proposal scoped to category-spec public/dynamic surfaces; do not whitelist unrelated
  dead code.
- Request explicit user approval before editing `/home/dzack/ai/quality-control`.
- After approval and implementation, run `just test` and record the next blocker.
complexity: 76
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
- category-specs
- audit
- validation
- quality-control
- vulture
- theme-audit-uniformity
created: '2026-05-03'
updated: '2026-05-03'
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

- [ ] Produce a categorized whitelist proposal for intentional category-spec vulture
  findings.
- [ ] Keep the proposal scoped to category-spec public/dynamic surfaces; do not
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

## Work Log

- 2026-05-03: Created from read-only vulture triage.

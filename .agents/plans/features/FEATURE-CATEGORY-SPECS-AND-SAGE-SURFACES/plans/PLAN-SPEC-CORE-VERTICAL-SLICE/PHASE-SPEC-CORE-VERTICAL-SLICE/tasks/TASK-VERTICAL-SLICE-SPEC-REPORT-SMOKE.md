---
id: TASK-VERTICAL-SLICE-SPEC-REPORT-SMOKE
trackerStatus:
  type: task
parents:
- '[[PHASE-SPEC-CORE-VERTICAL-SLICE]]'
dependsOn:
- '[[TASK-MODULE-FREE-FINITE-RANK-CONSTRUCTION-WITNESSES]]'
title: Validate the spec report vertical slice
status: needs-agent-review
priority: critical
description: Add focused validation proving the finite `GF(5)^3`, countable `ZZ^2`,
  and missing-obligation report behavior for the spec-core vertical slice.
activityType: validation
workstreamRole: review
claimStatus: computationally-supported
uncertaintyState: none-recorded
successCriteria:
- Focused validation proves the finite `GF(5)^3` report with cardinality `125`.
- Focused validation proves the countable `ZZ^2` report with infinite cardinality
  and inherited enumeration obligation.
- A deliberately incomplete claimant produces a precise missing-obligations report.
- Validation runs through repo `just` recipes or an added focused recipe, not ad hoc
  one-off commands.
complexity: 60
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SPEC-CORE-VERTICAL-SLICE
- PHASE-SPEC-CORE-VERTICAL-SLICE
---
# Validate the spec report vertical slice

## Summary

Add the focused checks that make the pivot measurable. This task proves that the new
spec-core and module witness layers produce inspectable reports for the two admitted
examples and for a failing claimant.

## Source Provenance

- `[[TASK-MODULE-FREE-FINITE-RANK-CONSTRUCTION-WITNESSES]]`
- `[[PLAN-SPEC-CORE-VERTICAL-SLICE]]`
- `tests/category_specs/test_spec_smoke.py`
- `category_specs/modules/smoketest.sage`
- Root `justfile`

## Context

This task is the success metric for the pivot. Broad smoke recovery, full-suite mypy,
and unrelated constructor fixes are not substitutes for focused report output.

## Acceptance Criteria

- [x] The validation artifact checks the exact report fields for `GF(5)^3`: declared
  category, cartesian-power witness, finite cardinality `125`, and provider provenance.
- [x] The validation artifact checks the exact report fields for `ZZ^2`: declared
  category, cartesian-power witness, infinite cardinality, countability, and
  deterministic-enumeration obligation.
- [x] The validation artifact includes a failing claimant or fixture that reports
  missing obligations without broad smoke noise.
- [x] The validation command is exposed through `just` if no existing focused recipe
  covers it.
- [x] The task records why any skipped full-suite checks are non-diagnostic for this
  slice.

## Dependencies And Boundaries

Do not weaken existing smokes to pass this task. Add focused checks or a focused recipe
that answers the slice question directly.

## Complexity And Ownership

Owner role: validation/review agent. Complexity: 60. The work is moderate because it
depends on the preceding implementation tasks, but its validation surface is narrow and
falsifiable.

## Work Log

- Created as the validation leaf of the pivot plan.
- Started after `TASK-MODULE-FREE-FINITE-RANK-CONSTRUCTION-WITNESSES` was accepted
  through merged PR #4.
- Added `just test-spec-core-vertical-slice` as the focused validation command for the
  spec-core report kernel and free finite-rank module witness reports.
- Validation evidence:
  - `just test-spec-core-vertical-slice` passed: 9 tests passed.
- Broad `just test` remains non-diagnostic for this slice while parallel mypy-plugin
  work is active; the focused recipe is the slice acceptance command.

---
id: TASK-VERTICAL-SLICE-SPEC-REPORT-SMOKE
trackerStatus:
  type: task
parents:
- '[[PHASE-SPEC-CORE-VERTICAL-SLICE]]'
dependsOn:
- '[[TASK-MODULE-FREE-FINITE-RANK-CONSTRUCTION-WITNESSES]]'
title: Validate the spec report vertical slice
status: unstarted
priority: critical
description: Add focused validation proving the finite `GF(5)^3`, countable `ZZ^2`,
  and missing-obligation report behavior for the spec-core vertical slice.
activityType: validation
workstreamRole: review
claimStatus: unexamined
uncertaintyState: ordinary-open
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

- [ ] The validation artifact checks the exact report fields for `GF(5)^3`: declared
  category, cartesian-power witness, finite cardinality `125`, and provider provenance.
- [ ] The validation artifact checks the exact report fields for `ZZ^2`: declared
  category, cartesian-power witness, infinite cardinality, countability, and
  deterministic-enumeration obligation.
- [ ] The validation artifact includes a failing claimant or fixture that reports
  missing obligations without broad smoke noise.
- [ ] The validation command is exposed through `just` if no existing focused recipe
  covers it.
- [ ] The task records why any skipped full-suite checks are non-diagnostic for this
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

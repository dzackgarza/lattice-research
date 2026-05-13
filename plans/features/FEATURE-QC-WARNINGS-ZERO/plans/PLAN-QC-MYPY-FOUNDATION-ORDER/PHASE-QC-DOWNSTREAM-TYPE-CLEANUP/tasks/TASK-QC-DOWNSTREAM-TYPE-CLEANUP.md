---
id: TASK-QC-DOWNSTREAM-TYPE-CLEANUP
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-DOWNSTREAM-TYPE-CLEANUP]]'
dependsOn:
- '[[TASK-QC-GENERATE-TYPE-STUBS]]'
title: Clean remaining downstream category type defects
status: unstarted
priority: high
description: 'After basic hygiene, plugin review, and stub generation, fix or split the
  remaining category/type defects from post-stub mypy output.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Post-stub mypy output is collected through the repo-approved validation path or a documented focused equivalent.
- Remaining defects are grouped by real source responsibility, not by aggregate pre-stub error shape.
- Each defect group is fixed or split into executable child tasks.
complexity: 55
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-DOWNSTREAM-TYPE-CLEANUP
---
# Task: Clean Remaining Downstream Category Type Defects

## Summary

Fix or split the remaining mypy defects only after the earlier frontiers are
complete. This task covers defects that remain real after basic hygiene,
dynamic-inheritance plugin review, and stub generation.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`, Category C and D.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`.

## Context

Examples may include incompatible signatures, constructor call mismatches,
remaining `attr-defined` findings, and category-specific type defects, but only
when they survive the earlier phases.

## Acceptance Criteria

- Post-stub validation output identifies remaining defects.
- Each defect is routed to a concrete owner or child task.
- No task in this phase hides or recategorizes earlier-phase work.

## Dependencies And Boundaries

Depends on `TASK-QC-GENERATE-TYPE-STUBS`.

## Work Log

- Created 2026-05-13 as the last mypy cleanup leaf.

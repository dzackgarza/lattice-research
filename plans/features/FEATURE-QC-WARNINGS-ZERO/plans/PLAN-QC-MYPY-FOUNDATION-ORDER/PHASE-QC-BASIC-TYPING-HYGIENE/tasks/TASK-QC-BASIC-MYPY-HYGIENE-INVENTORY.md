---
id: TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-BASIC-TYPING-HYGIENE]]'
dependsOn: []
title: Fix basic mypy missing-type hygiene
status: unstarted
priority: critical
description: 'Run mypy through the approved repo path and fix the missing annotations,
  Any leakage, untyped fixtures, and ordinary local typing hygiene findings directly.
  Plugin, stub-generation, and downstream category typing remain gated.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Current mypy output is collected through the repo-approved `just` path or a documented focused mypy reproduction.
- Missing annotations, Any leakage, untyped fixtures, and ordinary local hygiene findings are fixed in code by disjoint path slices.
- Dynamic-inheritance, stub-generation, and downstream category typing findings remain excluded from this task.
- Validation is rerun after fixes and the remaining frontier is recorded in the handoff.
complexity: 35
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-BASIC-TYPING-HYGIENE
---
# Task: Fix Basic Mypy Missing-Type Hygiene

## Summary

Run mypy through the approved repo path and fix the basic mypy hygiene frontier:
missing return annotations, missing parameter annotations, untyped fixtures,
avoidable `Any` leakage, and ordinary local typing cleanup. Do not classify
`@override`, `@final`, `@abstractmethod`, stub, `.pyi`, `TypeAlias`, or
category-specific downstream typing errors as part of this task.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`: current QC triage categories.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`: dependency order for mypy cleanup.
- User direction from 2026-05-13: focus on one root item at a time; basic hygiene
  comes before plugin, stubs, or downstream type cleanup.

## Context

The aggregate mypy failure count is not the queue, but running mypy is enough to
find the first root frontier. Fix those basic hygiene errors directly by
disjoint file/path slices. Do not create an inventory-only gate.

## Acceptance Criteria

- Basic hygiene findings are fixed by path slice.
- Plugin/dynamic-inheritance errors are explicitly excluded.
- Stub-generation errors are explicitly excluded.
- Downstream category/type defects are explicitly excluded until earlier phases
  are complete.
- Any remaining basic hygiene slice is left as an executable fix target, not an
  inventory-only task.

## Dependencies And Boundaries

No dependencies. This is the first mypy/QC task.

## Work Log

- Created 2026-05-13 to prevent aggregate mypy output from bypassing the root
  QC hygiene frontier.
- Corrected 2026-05-13 after user feedback: this is an execution task, not an
  inventory gate.

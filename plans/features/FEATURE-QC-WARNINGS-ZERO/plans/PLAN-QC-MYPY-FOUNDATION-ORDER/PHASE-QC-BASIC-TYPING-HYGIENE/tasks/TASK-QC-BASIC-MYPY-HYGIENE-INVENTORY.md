---
id: TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-BASIC-TYPING-HYGIENE]]'
dependsOn: []
title: Inventory basic mypy hygiene findings
status: unstarted
priority: critical
description: 'Extract the basic typing hygiene subset from current mypy output and split it
  into executable child tasks before any plugin, stub-generation, or downstream type-cleanup
  work is selected.

  '
activityType: validation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Current mypy output is collected through the repo-approved `just` path or a documented focused mypy reproduction.
- Missing annotations, Any leakage, untyped fixtures, and ordinary local hygiene are listed separately from dynamic-inheritance, stub, and downstream category typing issues.
- Follow-up executable child tasks are created under `PHASE-QC-BASIC-TYPING-HYGIENE` for each basic hygiene slice that is too large to fix immediately.
- The handoff note records the first basic-hygiene child task to pick up next.
complexity: 35
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-BASIC-TYPING-HYGIENE
---
# Task: Inventory Basic Mypy Hygiene Findings

## Summary

Run the repo-approved validation path and extract only the basic mypy hygiene
frontier: missing return annotations, missing parameter annotations, untyped
fixtures, avoidable `Any` leakage, and ordinary local typing cleanup. Do not
classify `@override`, `@final`, `@abstractmethod`, stub, `.pyi`, `TypeAlias`, or
category-specific downstream typing errors as part of this task.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`: current QC triage categories.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`: dependency order for mypy cleanup.
- User direction from 2026-05-13: focus on one root item at a time; basic hygiene
  comes before plugin, stubs, or downstream type cleanup.

## Context

The aggregate mypy failure count is not the queue. This task must produce the
first actionable basic-hygiene queue and split oversized slices into child tasks
under this phase.

## Acceptance Criteria

- Basic hygiene findings are listed by path and error code.
- Plugin/dynamic-inheritance errors are explicitly excluded.
- Stub-generation errors are explicitly excluded.
- Downstream category/type defects are explicitly excluded until earlier phases
  are complete.
- Follow-up child tasks are created only for basic-hygiene slices.

## Dependencies And Boundaries

No dependencies. This is the first mypy/QC task.

## Work Log

- Created 2026-05-13 to prevent aggregate mypy output from bypassing the root
  QC hygiene frontier.

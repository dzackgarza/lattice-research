---
id: TASK-QC-GENERATE-TYPE-STUBS
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-STUB-GENERATION]]'
dependsOn:
- '[[TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
title: Generate or repair static type stubs
status: unstarted
priority: high
description: 'Create or repair Sage/pytest/category static type surfaces after basic hygiene
  and dynamic-inheritance plugin review are complete.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- Stub-generation candidates are drawn from post-plugin mypy output, not pre-plugin aggregate noise.
- Sage, pytest, .pyi, TypeAlias, and generated category-surface needs are separated by source path.
- Generated or handwritten stubs are validated through `just test` or a documented focused equivalent.
- No plugin/base-injection failure is hidden by a stub.
complexity: 55
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-STUB-GENERATION
---
# Task: Generate or Repair Static Type Stubs

## Summary

Create or repair static type surfaces only after the basic hygiene and
dynamic-inheritance plugin frontiers are complete. This includes Sage/pytest
stubs, `.pyi` files, `TypeAlias` intermediaries, and generated representations
of category method surfaces.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`, valid-type and missing-stub sections.
- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`, which makes stub generation out of scope
  for the plugin.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`.

## Context

Pre-plugin aggregate mypy output cannot be used as the stub queue. Stub work
starts from post-basic, post-plugin evidence so it does not mask ordinary type
hygiene or dynamic-inheritance failures.

## Acceptance Criteria

- Stub candidates are listed by path and error shape.
- The plan distinguishes external dependency stubs from repo-generated category
  static surfaces.
- Validation proves the stubs resolve the targeted errors without suppressions.

## Dependencies And Boundaries

Depends on `TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW`. This task does not own
missing annotations, `Any` hygiene, or plugin base injection.

## Work Log

- Created 2026-05-13 as the explicit stub-generation task tree.

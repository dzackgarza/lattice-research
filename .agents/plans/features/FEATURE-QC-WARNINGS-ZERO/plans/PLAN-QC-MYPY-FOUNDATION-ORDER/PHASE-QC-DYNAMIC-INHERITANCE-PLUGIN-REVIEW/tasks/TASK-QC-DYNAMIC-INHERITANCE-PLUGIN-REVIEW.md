---
id: TASK-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW
trackerStatus:
  type: task
parents:
- '[[PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
dependsOn:
- '[[TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY]]'
title: Review dynamic-inheritance mypy plugin findings
status: unstarted
priority: critical
description: 'After basic typing hygiene and plugin completion, classify only override,
  final, abstractmethod, MRO, and base-injection findings as plugin misses or real source
  defects.

  '
activityType: validation
workstreamRole: review
claimStatus: unexamined
uncertaintyState: ordinary-open
successCriteria:
- The basic hygiene phase is complete before this task starts.
- The plugin feature is complete before this task starts.
- Focused mypy reproductions cover each dynamic-inheritance error shape under review.
- Each remaining dynamic-inheritance finding is routed to plugin repair or source repair without including stub-generation issues.
complexity: 45
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
- PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW
---
# Task: Review Dynamic-Inheritance Mypy Plugin Findings

## Summary

Classify only the dynamic-inheritance mypy subset after earlier prerequisites are
complete: `@override`, `@final`, `@abstractmethod`, method-container MRO
projection, base injection, and plugin-loaded QC config behavior.

## Source Provenance

- `SPEC-SAGE-MYPY-CATEGORY-OVERRIDE`.
- `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`.
- `PLAN-QC-MYPY-FOUNDATION-ORDER`.

## Context

This task must not discuss missing annotations, `Any`, generated stubs, invalid
type aliases, or downstream category typing as plugin evidence. Those belong to
other phases.

## Acceptance Criteria

- Dynamic-inheritance findings are reproduced with focused mypy runs.
- Each finding is classified as plugin miss, source defect, or not in this phase.
- Findings outside dynamic inheritance are moved to the correct later phase.

## Dependencies And Boundaries

This task is not selectable until its parent phase dependencies are complete.

## Work Log

- Created 2026-05-13 to narrow plugin-related mypy work to the intended subset.

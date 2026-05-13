---
id: PLAN-QC-MYPY-FOUNDATION-ORDER
trackerStatus:
  type: plan
parents:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
dependsOn: []
title: QC mypy foundation dependency order
status: approved-and-unstarted
priority: critical
description: 'Encode the mypy cleanup queue as a dependency-ordered plan: basic typing
  hygiene first, dynamic-inheritance plugin review second, stub generation third, and
  downstream type cleanup last. Aggregate mypy output is not a selectable work queue.

  '
phases:
- '[[PHASE-QC-BASIC-TYPING-HYGIENE]]'
- '[[PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW]]'
- '[[PHASE-QC-STUB-GENERATION]]'
- '[[PHASE-QC-DOWNSTREAM-TYPE-CLEANUP]]'
successCriteria:
- Basic typing hygiene findings are exhausted or split into executable child tasks before plugin review is selected.
- Dynamic inheritance findings are reviewed only after the basic hygiene frontier is complete.
- Stub-generation work depends on the dynamic-inheritance plugin lane and is not used as a workaround for plugin failures.
- Downstream type cleanup begins only after basic hygiene, plugin review, and stub generation are complete.
tags:
- FEATURE-QC-WARNINGS-ZERO
---
# Plan: QC Mypy Foundation Dependency Order

## Summary

This plan makes the mypy portion of `FEATURE-QC-WARNINGS-ZERO` a dependency
ordered queue rather than a flat error pile. The topological order is:

- basic typing hygiene;
- dynamic-inheritance plugin review;
- stub generation;
- downstream type cleanup.

If a later phase has partially completed work, that progress is irrelevant for
priority until every earlier phase is complete.

## Source Provenance

- `AGENTS.md`: follow the planning DAG literally; priority reports cut at the
  earliest incomplete dependency frontier.
- User direction from 2026-05-13: missing annotations, `Any`, and basic code
  hygiene are the first fundamental QC pass; dynamic inheritance is the narrow
  plugin scope; stub generation is a separate downstream task tree.
- `FEATURE-QC-WARNINGS-ZERO`: repo-wide QC gate and current mypy triage source.
- `FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN`: plugin scope for Sage dynamic
  method-container inheritance.

## Dependency Queue

`PHASE-QC-BASIC-TYPING-HYGIENE` has no mypy predecessor. It owns missing return
annotations, missing parameter annotations, untyped pytest fixtures, ordinary
`Any` leakage, and basic local code hygiene that does not depend on Sage dynamic
method-container inheritance.

`PHASE-QC-DYNAMIC-INHERITANCE-PLUGIN-REVIEW` depends on the basic phase. It owns
only failures whose shape is about Sage dynamic inheritance: `@override`,
`@final`, `@abstractmethod`, method-container MRO projection, base injection, and
plugin-loaded QC config behavior.

`PHASE-QC-STUB-GENERATION` depends on dynamic-inheritance plugin review. It owns
static surface material: Sage/pytest stubs, `.pyi` files, `TypeAlias`
intermediaries, and generated representations of dynamic category surfaces.

`PHASE-QC-DOWNSTREAM-TYPE-CLEANUP` depends on stub generation. It owns remaining
ordinary type defects after the prior frontiers have removed their noise.

## Acceptance Criteria

- `just plan-validate` accepts the plan and sibling phase dependencies.
- `just plan-progress-report` places only the earliest incomplete phase on the
  selectable high-priority frontier.
- Every mypy error discussion cites one of the four phases above before claiming
  an error is a plugin issue, stub issue, or downstream defect.

## Dependencies And Boundaries

This plan does not complete mypy work and does not close the plugin feature. It
only encodes the queue so future work cannot select stubs, plugin review, or
downstream cleanup before the basic typing frontier is finished.

## Work Log

- Created 2026-05-13 to record the corrected mypy/QC dependency order after the
  aggregate plugin review blurred basic hygiene, plugin, stub, and downstream
  categories.

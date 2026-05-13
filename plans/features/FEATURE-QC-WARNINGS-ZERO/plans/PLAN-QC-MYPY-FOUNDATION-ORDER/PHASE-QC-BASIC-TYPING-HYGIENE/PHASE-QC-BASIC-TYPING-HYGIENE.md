---
id: PHASE-QC-BASIC-TYPING-HYGIENE
trackerStatus:
  type: phase
parents:
- '[[PLAN-QC-MYPY-FOUNDATION-ORDER]]'
dependsOn: []
title: Basic mypy typing hygiene
status: unstarted
priority: critical
description: 'First mypy frontier for missing annotations, Any leakage, untyped fixtures,
  and ordinary local typing hygiene. Downstream plugin, stub, and type-cleanup phases are
  not selectable until this phase is complete.

  '
phaseKind: milestone
branchType: implementation
tasks:
- '[[TASK-QC-BASIC-MYPY-HYGIENE-INVENTORY]]'
successCriteria:
- Current basic typing hygiene failures are collected by running mypy through the approved repo path.
- Missing annotations, Any leakage, and untyped fixture failures are fixed directly by disjoint path slices.
- No dynamic-inheritance, stub-generation, or downstream category-typing work is selected before this phase completes.
tags:
- FEATURE-QC-WARNINGS-ZERO
- PLAN-QC-MYPY-FOUNDATION-ORDER
---
# Phase: Basic Mypy Typing Hygiene

## Summary

This is the first selectable mypy frontier. It owns real current-tree defects
that do not require the Sage dynamic-inheritance plugin or generated stubs:
missing return annotations, missing parameter annotations, untyped pytest
fixtures, avoidable `Any` leakage, and ordinary code hygiene.

## Source Provenance

- `FEATURE-QC-WARNINGS-ZERO`, Category B and basic `Any` notes.
- User direction from 2026-05-13: basic code hygiene is a fundamental first pass
  and nothing downstream should proceed until basics are in place.

## Acceptance Criteria

- Basic hygiene findings from current mypy output are fixed directly by
  disjoint path slices.
- Downstream phases remain `unstarted` until this phase is complete.

## Dependencies And Boundaries

This phase excludes Sage dynamic method-container inheritance, generated stubs,
and category-specific downstream type defects. Those are later phases.

## Work Log

- Created 2026-05-13 as the root mypy/QC frontier.

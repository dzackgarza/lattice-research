---
id: PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH
trackerStatus:
  type: phase
parents:
- '[[PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS]]'
dependsOn: []
title: Curve complement and monodromy backend research
status: needs-review
description: 'This phase groups current cards that were previously attached directly
  to `PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS` or to the corresponding legacy `.agents`
  work queue. It is a routing phase: executable work remains in child task cards,
  while definition-heavy work remains in feature-level spec cards.'
successCriteria:
- Child task cards are complete only after blockers are resolved, or after the
  original card is superseded by a linked successor that remains active; blocked child
  cards do not satisfy phase acceptance.
- Any mathematical spec changes cite their source grounding before implementation
  proceeds.
- Follow-up work is filed as tracked cards under root `plans/features/`.
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS
---
# Curve complement and monodromy backend research

## Summary

This phase groups current cards that were previously attached directly to `PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS` or to the corresponding legacy `.agents` work queue. It is a routing phase: executable work remains in child task cards, while definition-heavy work remains in feature-level spec cards.

## Acceptance Criteria

- [ ] Child task cards are complete only after blockers are resolved, or after the
      original card is superseded by a linked successor that remains active; blocked
      child cards do not satisfy phase acceptance.
- [ ] Any mathematical spec changes cite their source grounding before implementation proceeds.
- [ ] Follow-up work is filed as tracked cards under root `plans/features/`.

## Work Log

- 2026-05-06: Started phase execution with
  `[[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]`.

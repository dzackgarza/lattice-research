---
trackerStatus:
  type: task
title: Admit named lattice constructors through lattice meets
status: to-do
priority: high
created: '2026-05-03'
complexity: 55
progress: 0
planId: PLN-LAT-040
tags:
- category-specs
- implementation
- lattices
- phase-plan
- discriminant-groups
- duals
- theme-modules-tensors
---

# Admit named lattice constructors through lattice meets

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-040` is approved.

## Source Provenance

- `plans/PHASE_4_DISCRIMINANT_DESCENT.md`
- Source section: Named lattice constructors and lattice meets
- Parent plan: `PLN-LAT-040`
- Program plan: `PLN-CAT-000`

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/lattices.py`.

## Acceptance Criteria

- [ ] Read the cited source section before implementation.
- [ ] Keep changes inside the named target boundary unless a new card or decision expands scope.
- [ ] Preserve the mathematical semantics from the source plan and category-spec style rules.
- [ ] Record validation commands and results before handoff.
- [ ] Do not mark this card done without human approval.

## Dependencies And Boundaries

Do not execute before the parent phase plan is approved and prerequisite phase cards are resolved. If the source section reveals missing vocabulary or method ownership, stop and file a decision or spec card instead of patching around it.

## Work Log

- Created by corpus-level `plans/` migration on 2026-05-03.

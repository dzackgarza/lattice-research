---
trackerStatus:
  type: task
title: 'Implement concrete bilinear module morphism wrappers'
status: to-do
priority: critical
created: '2026-05-03'
complexity: 65
progress: 0
planId: PLN-LAT-030
tags:
  - category-specs
  - implementation
  - lattices
  - phase-plan
  - morphisms
  - homsets
---

# Implement concrete bilinear module morphism wrappers

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-030` is approved.

## Source Provenance

- `plans/PHASE_3_MORPHISMS.md`
- Source section: Step 3.2: Concrete Morphism Wrappers
- Parent plan: `PLN-LAT-030`
- Program plan: `PLN-CAT-000`

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/morphisms/bilinear.py`.

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

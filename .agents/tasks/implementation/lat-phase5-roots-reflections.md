---
trackerStatus:
  type: task
title: Implement roots and reflections
status: to-do
priority: high
created: '2026-05-03'
complexity: 55
progress: 0
planId: PLN-LAT-050
tags:
- category-specs
- implementation
- lattices
- phase-plan
- orthogonal-groups
- theme-modules-tensors
---

# Implement roots and reflections

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-050` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.5: Roots and Reflections
- Parent plan: `PLN-LAT-050`
- Program plan: `PLN-CAT-000`

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/groups/roots.py`.

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

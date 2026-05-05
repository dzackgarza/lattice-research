---
trackerStatus:
  type: task
title: Implement orthogonal subgroups through ConditionSet composition
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

# Implement orthogonal subgroups through ConditionSet composition

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-050` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.2: Orthogonal Subgroups
- Parent plan: `PLN-LAT-050`
- Program plan: `PLN-CAT-000`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.2),
`category-abc-spec.md`, `forms/docs/MAPPING.md`,
`category_specs/lattices/docs/MAPPING.md`, and `lattice-interface-style-guide.md`.

- Subgroups are predicate-defined refinements of `LatticeOrthogonalGroup` through `LatticeOrthogonalSubgroup`.
- Constructor contracts:
  - `centralizer(g)` adds predicate `f g = g f`.
  - `stabilizer(v)`:
    - if `v in L`, fixes vector (`f(v)=v`);
    - if `v` is a submodule or flagged subobject, preserves its image setwise through
      the subobject inclusion morphism and chosen generators, rather than comparing raw
      ambient coordinates.
  - `stabilizer_of_isotropic_line(v)` applies line-level predicate (`f(v) ∈ {v,-v}`).
  - `kernel_of_discriminant_action()` adds the condition that the induced action on
    `A_L` is identity.
  - `special_orthogonal_subgroup()` is the determinant-one subgroup after the chosen
    matrix realization of `O(L)` is fixed.
- Subgroup operations are via `ConditionSet` intersection/union; no bespoke composition operators.
- Membership semantics remains inherited from ambient orthogonal group and predicate set.

Backend routing:
- Subgroup predicates are in-memory and deterministic.
- For finite subgroup computations (order, Schreier search, stabilizer lifts), prefer
  GAP once a finite matrix-group realization exists.
- For indefinite subgroup membership inherited from `O(L)`, reuse the Indefinite.jl
  ambient group realization rather than introducing subgroup-specific local search.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/groups/orthogonal.py`.

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

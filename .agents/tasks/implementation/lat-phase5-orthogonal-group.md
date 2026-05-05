---
trackerStatus:
  type: task
title: Implement LatticeOrthogonalGroup as morphism-valued parent
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

# Implement LatticeOrthogonalGroup as morphism-valued parent

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-050` is approved.

## Source Provenance

- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`
- Source section: Step 5.1: LatticeOrthogonalGroup
- Parent plan: `PLN-LAT-050`
- Program plan: `PLN-CAT-000`

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.1), `category-abc-spec.md`, `category_specs/lattices/docs/MAPPING.md`, and `forms/docs/MAPPING.md`.

- `orthogonal_group` is `Aut(M,b)` on the formed module category object `(M,b)`.
- `LatticeOrthogonalGroup` is therefore a subgroup of automorphisms of `L` in the form-preserving hom category:
  - elements are lattice morphisms, not matrices.
  - `O(L)` membership filters on object type (`L → L`) plus form preservation predicate from predicates module.
- `from_matrix` and `__call__` are constructor/dispatch layers:
  - both return morphisms in `O(L)` after validation.
  - matrix entry is always interpreted as a representation in the canonical generators, then validated by `is_isometry`.
- `identity`, `gens`, `order`, `__iter__` stay on `LatticeOrthogonalGroup`.
- Required semantics checks:
  - `L.orthogonal_group().lattice() == L`;
  - a raw matrix is not a group element until wrapped by `O(L).from_matrix(...)` or
    `O(L)(...)`;
  - every element of `O(L)` is a morphism in `L.End()` that preserves the form.

Exact backend routing:
- Positive-definite finite matrix-group auxiliaries may use CARAT and GAP through
  backend adapters.
- Indefinite isometry testing routes to Indefinite.jl
  (`INDEF_FORM_TestEquivalence`).
- Indefinite automorphism-group generation routes to Indefinite.jl
  (`INDEF_FORM_AutomorphismGroup`).

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

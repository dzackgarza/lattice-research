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

## Source-Grounded Contract

Source anchors: `pln-lattice-phase-5-orthogonal-groups.md` (Step 5.5),
`category_specs/lattices/docs/MAPPING.md`,
`category_specs/forms/docs/MAPPING.md`,
`category-abc-spec.md`, and `lattice-interface-style-guide.md`.

- Root semantics:
  - a root is an integral lattice element `v` with `b(v,v) in {-2, 2}` in the phase
    convention recorded by the plan and the lattice mapping;
  - `is_root(v)` belongs on lattice elements;
  - `roots()` returns the actual root subset of the lattice, not coordinate vectors.
- Reflection semantics:
  - for a root `v`, the reflection is the orthogonal-group element
    `s_v(w) = w - 2 b(v,w) / b(v,v) * v`;
  - `reflection()` returns a morphism in `O(L)`, not a matrix;
  - `s_v(v) = -v`, `s_v^2 = id`, and containment in `O(L)` are acceptance obligations.
- Ownership:
  - root/reflection construction lives in `src/lattices/groups/roots.py`;
  - orthogonal-group containment and matrix validation still live in the centralized
    predicate and `O(L)` layers.
- Derived objects:
  - `root_sublattice()` is the sublattice spanned by the root set and must return a
    lattice/subobject object with its inclusion morphism, not an ad hoc span matrix.

Backend routing:
- Reflection construction is local once a root is given.
- This card does not own indefinite root enumeration or simple-root search. Hyperbolic
  simple-root discovery belongs to the Vinberg backend path used by the Coxeter/Weyl
  layer.

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

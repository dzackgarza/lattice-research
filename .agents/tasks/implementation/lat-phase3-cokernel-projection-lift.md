---
trackerStatus:
  type: task
title: Implement cokernel projection and lift contract
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
- theme-modules-tensors
---

# Implement cokernel projection and lift contract

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-030` is approved.

## Source Provenance

- `plans/PHASE_3_MORPHISMS.md`
- Source section: Step 3.5: Cokernel Contract
- Parent plan: `PLN-LAT-030`
- Program plan: `PLN-CAT-000`

## Grounded Implementation Contract

- Source anchors:
  - `.agents/plans/phase-01-category-specs/lattice/pln-lattice-phase-3-morphisms-cokernels.md` (Step 3.5)
  - `category_specs/modules/docs/MAPPING.md`
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`
  - `theory/foundations/bilinear-forms-duals-morphisms.md`
- Projection semantics:
  - if `C = f.cokernel()`, then `C.projection()` is the canonical quotient morphism `pi : codomain(f) -> C`;
  - `pi` is a morphism in the relevant formed-module homspace, `pi.is_surjective()` is true, and `ker(pi) = im(f)` as categorical objects.
- Lift semantics:
  - each cokernel element `x_bar in C` may expose `x_bar.lift()` returning some chosen representative `x in codomain(f)` such that `pi(x) = x_bar`;
  - this is representative data for the quotient projection, not a new section or splitting morphism;
  - the implementation may delegate representative choice to the underlying FGP quotient lift, then wrap the representative back into the codomain object.
- Quotient-object surface:
  - invariants, cardinality, generators, and other quotient data belong on the cokernel object `C`, not on the original morphism;
  - `projection()` lives on the quotient object because it is structure of the quotient, while `lift()` lives on quotient elements because it chooses representatives of quotient classes.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/morphisms/bilinear.py`.

## Acceptance Criteria

- [ ] Every cokernel object returned by Phase 3 exposes a canonical projection morphism from the original codomain, and that projection is surjective with kernel equal to the image of the original morphism.
- [ ] `lift()` exists only as quotient-representative selection for cokernel elements and composes with `projection()` to recover the original quotient class.
- [ ] Quotient invariants, generators, and cardinality remain properties of the cokernel object itself rather than ad hoc helpers on the original morphism wrapper.
- [ ] The projection/lift API works for both ordinary quotient modules and the discriminant-style quotient path needed later for `L^#/L`.

## Dependencies And Boundaries

Execute within `src/lattices/morphisms/bilinear.py`, keeping quotient structure on the cokernel object and representative choice on cokernel elements. Do not reinterpret `lift()` as a canonical inverse to the projection.

## Work Log

- Created by corpus-level `plans/` migration on 2026-05-03.

---
id: SPEC-01KQN9J3WVW531PDTHEY094GVG-PRESERVE-ALGEBRA-BASIS-RETURNING-SAGE-HELPERS-AS-OBJECT-RETURNING-PROJEC
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
title: Preserve algebra basis-returning Sage helpers as object-returning project methods
  such as center radical and derivations
status: needs-review
priority: critical
requirement: The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ),
  a module hom-category/forms blocker for DualObjects, and constructor admission gaps.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No new implementation blocker was discovered during this docs/spec pass; recovered
  smoke failures remain unrelated frontiers.
- No algebra category initialization or constructor code changed, so the `algebras/smoketest.sage`
  trigger did not apply in this pass.
- Plain-set `S.algebra(R)` remains routed to `free_module` over `Modules(R)`, not
  to `Algebras(R)`.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Preserve algebra basis-returning Sage helpers as object-returning project methods such as center radical and derivations
## Summary

The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ), a
module hom-category/forms blocker for DualObjects, and constructor admission gaps.

## Source Provenance

- The requested recovery path `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md`
  fails because the file still lived under `plans/category_specs/algebras/docs/TRIAGE.md`
  at that parent commit.
- Exact recovered prior content came from
  `git show 8d1c21c^:plans/category_specs/algebras/docs/TRIAGE.md`.
- Original migrated line: `Preserve algebra basis-returning Sage helpers as object-returning project methods such as center radical and derivations from category_specs/algebras/docs/TRIAGE.md`

## Context

- Algebras(ZZ) raises _SageObject__custom_name while Sage resolves subcategory_class during category initialization.
- Algebras(ZZ).DualObjects() fails while Sage/project axiom inference builds modules.homsets._Forms; this is not an algebra constructor issue.
- Free-construction names may appear as abstract spec targets, but callable implementations require Sage-backed routing and refinement.
- Algebra construction is canonicalized to from_multiplication_tensor(multiplication=mu), where mu is a Tensor in T_R(M)[1,2].
- Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations.

## Grounded Spec Contract

Grounding anchors:

- `category_specs/algebras/docs/MAPPING.md` rows for `basis()`, `one_basis()`,
  `algebra_generators()`, `center_basis()`, `radical_basis()`, `derivations_basis()`,
  and `annihilator_basis(...)`.
- `category_specs/algebras/docs/SAGE_INVENTORY.md`, especially the method rows for
  `AlgebrasWithBasis.ParentMethods` and
  `FiniteDimensionalAlgebrasWithBasis.ParentMethods`.

Grounded owner rule for this leaf:

- Sage basis-returning helpers are inventory evidence, not the public project codomain.
  The public owners stay on the algebra parent surface and return the mathematical
  object named by the helper: `center() -> Algebra`, `radical() -> AlgebraIdeal`,
  `derivations() -> RModule`, and `annihilator(...) -> AlgebraIdeal`.
- Basis data remains structure recoverable from the returned object when that object
  lies in `WithBasis()`. The project does not admit separate public surfaces whose only
  codomain is a distinguished basis list or basis-index family.

Required hypotheses and codomains:

- `center_basis()` grounds `center() -> Algebra`, with the center owned as the
  subalgebra spanned by that basis;
- `radical_basis()` grounds `radical() -> AlgebraIdeal`, with the radical owned as the
  ideal spanned by that basis;
- `derivations_basis()` grounds `derivations() -> RModule`, with any chosen basis
  recovered from the derivation object itself;
- `annihilator_basis(...)` grounds `annihilator(...) -> AlgebraIdeal`;
- `one_basis()` does not create a public basis-index API; it grounds `one() -> AlgebraElement`
  and constructor unit data when the unit happens to be a basis vector.

Rejection/retirement condition:

- reject any spec edit that promotes a Sage basis helper itself to the public return
  object when the mapped mathematical object is an algebra, ideal, module, or element.

## Execution Result

The basis-helper migration is already grounded and preserved:

- `category_specs/algebras/docs/MAPPING.md` maps Sage `center_basis()` to
  `center() -> Algebra`, `radical_basis()` to `radical() -> AlgebraIdeal`,
  `derivations_basis()` to `derivations() -> RModule`, and
  `annihilator_basis(...)` to `annihilator(...) -> AlgebraIdeal`.
- `category_specs/algebras/__init__.py` exposes the object-returning abstract methods
  `center`, `radical`, `derivations`, and `annihilator` on the algebra parent surface.
- `AlgebraIdeal` remains the algebra-ideal object in `Algebras(R).Ideals(A)`, backed by
  module-subobject structure rather than by a bare basis list or a ring ideal alias.
- Sage's basis helpers remain inventory evidence for how to build those objects in a
  later implementation pass; they are not public project codomains.

No code change was required in this pass. The historical `Algebras(ZZ)` and
`DualObjects()` smoke failures are not basis-helper ownership issues.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No new implementation blocker was discovered during this docs/spec pass; recovered smoke failures remain unrelated frontiers.
- [x] No algebra category initialization or constructor code changed, so the `algebras/smoketest.sage` trigger did not apply in this pass.
- [x] Plain-set `S.algebra(R)` remains routed to `free_module` over `Modules(R)`, not to `Algebras(R)`.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Recovered historical algebra triage from
  `plans/category_specs/algebras/docs/TRIAGE.md`, confirmed the object-returning
  `center`, `radical`, `derivations`, and `annihilator` surfaces in mapping/code, and
  marked the basis-helper preservation leaf ready for review without admitting raw
  basis-list codomains.

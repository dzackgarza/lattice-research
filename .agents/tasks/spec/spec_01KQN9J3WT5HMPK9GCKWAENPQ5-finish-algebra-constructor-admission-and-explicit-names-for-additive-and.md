---
trackerStatus:
  type: feature
title: Finish algebra constructor admission and explicit names for additive and table algebra construction routes
status: to-do
priority: critical
planId: SPR-ALG-TENSOR-01KQN9
tags:
- category-specs
- spec
- feature
- constructors
- algebras
- theme-constructor-routing
---

# Finish algebra constructor admission and explicit names for additive and table algebra construction routes
## Summary

The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ), a
module hom-category/forms blocker for DualObjects, and constructor admission gaps.

## Source Provenance

- `category_specs/algebras/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md`.
- Original migrated line: `Finish algebra constructor admission and explicit names for additive and table algebra construction routes from category_specs/algebras/docs/TRIAGE.md`

## Context

- Algebras(ZZ) raises _SageObject__custom_name while Sage resolves subcategory_class during category initialization.
- Algebras(ZZ).DualObjects() fails while Sage/project axiom inference builds modules.homsets._Forms; this is not an algebra constructor issue.
- Free-construction names may appear as abstract spec targets, but callable implementations require Sage-backed routing and refinement.
- Algebra construction is canonicalized to from_multiplication_tensor(multiplication=mu), where mu is a Tensor in T_R(M)[1,2].
- Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations.

## Grounded Spec Contract

Grounding anchors:

- `category_specs/algebras/docs/MAPPING.md`, especially the `Free-Construction Routing`
  and `Multiplication Tensor Constructor` sections and the rows for
  `S.algebra(R, category=AdditiveSemigroups())`,
  `S.algebra(R, category=AdditiveMonoids())`,
  `S.algebra(R, category=AdditiveGroups())`, and
  `FiniteDimensionalAlgebra(k, table, ...)`.
- `category_specs/algebras/docs/SAGE_INVENTORY.md`, especially the constructor rows for
  `Sets.ParentMethods.algebra`, `AlgebraFunctor(base_ring).__call__(G, category=None)`,
  `FreeAlgebra(R, n, names)`, and `FiniteDimensionalAlgebra(k, table, ...)`.
- `category_specs/tensor_algebra_components/docs/MAPPING.md` and
  `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md` for the canonical
  `(1,2)` multiplication-tensor owner and the admitted constructor shapes that feed it.
- `category_specs/modules/docs/MAPPING.md` for the plain-set routing
  `S.free_module(R) -> Modules(R).Constructors().CombinatorialFreeModule(...)`.

Grounded owner rule for this leaf:

- Free algebra constructors on multiplicative or additive source objects are owned by
  `Algebras(R).Constructors()` under explicit source-sensitive names such as
  `free_algebra_from_semigroup`, `free_algebra_from_monoid`,
  `free_algebra_from_group`, `free_algebra_from_additive_semigroup`,
  `free_algebra_from_additive_monoid`, and `free_algebra_from_additive_group`.
- Table- or product-data admission for finite-rank algebras is owned first by
  `TensorAlgebraComponents(R).Constructors()`. The only canonical algebra product input
  is `from_multiplication_tensor(multiplication=mu)` with `mu` a `Tensor` in
  `T_R(M)[1,2]`.

Required hypotheses and codomains:

- additive and multiplicative free-construction routes must name the source category
  whose law supplies multiplication and must return an object in the mapped target
  algebra category (`MagmaticAlgebras(R)`, `AssociativeAlgebras(R)`, or `Algebras(R)`);
- the tensor route requires a tensor with `tensor_type() == (1, 2)` and base module `M`;
  the returned object is an algebra object over `R` whose owner category is determined
  by the proven laws carried by that tensor;
- the plain-set Sage route remains rejected as algebra vocabulary and maps to the
  module constructor path instead.

Rejection/retirement condition:

- reject any algebra constructor proposal that exposes raw Sage `category=` ambiguity,
  list/table/matrix-shaped multiplication data directly on `Algebras(R)`, or routes the
  plain-set `S.algebra(R)` surface into `Algebras(R)` rather than `Modules(R)`.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Run just smoke-file algebras/smoketest.sage after algebra category initialization or constructor changes.
- [ ] Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module over Modules(R).

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

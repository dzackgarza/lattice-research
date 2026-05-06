---
id: TASK-01KQN9J3X25735AND1JQ80C5JT-IMPLEMENT-SAGE-BACKED-ALGEBRA-CONSTRUCTOR-ROUTING-AND-REFINEMENT-FOR-ADM
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Implement Sage-backed algebra constructor routing and refinement for admitted
  constructors
status: needs-review
priority: high
description: The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ),
  a module hom-category/forms blocker for DualObjects, and constructor admission gaps.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just smoke-file algebras/smoketest.sage after algebra category initialization
  or constructor changes.
- Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module
  over Modules(R).
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Implement Sage-backed algebra constructor routing and refinement for admitted constructors
## Summary

The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ), a
module hom-category/forms blocker for DualObjects, and constructor admission gaps.

## Source Provenance

- `category_specs/algebras/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md`.
- Original migrated line: `Implement Sage-backed algebra constructor routing and refinement for admitted constructors from category_specs/algebras/docs/TRIAGE.md`

## Context

- Algebras(ZZ) raises _SageObject__custom_name while Sage resolves subcategory_class during category initialization.
- Algebras(ZZ).DualObjects() fails while Sage/project axiom inference builds modules.homsets._Forms; this is not an algebra constructor issue.
- Free-construction names may appear as abstract spec targets, but callable implementations require Sage-backed routing and refinement.
- Algebra construction is canonicalized to from_multiplication_tensor(multiplication=mu), where mu is a Tensor in T_R(M)[1,2].
- Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file algebras/smoketest.sage after algebra category initialization or constructor changes.
- [ ] Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module over Modules(R).

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06 implementation review: current `category_specs/algebras/__init__.py`
  implements the admitted Sage-backed constructor routes recorded in
  `SPEC-MAPPING-ALGEBRAS`: true free algebras from finite sets use Sage
  `FreeAlgebra`; magma, semigroup, monoid, group, additive-semigroup,
  additive-monoid, and additive-group routes call Sage `S.algebra(R,
  category=...)` only behind named project constructors; multiplication-table
  construction is centralized through `from_multiplication_tensor(mu)`. The
  implementation explicitly rejects the plain-set `S.algebra(R)` route as an
  algebra constructor and leaves that surface to module construction.
- 2026-05-06 validation: `just --justfile category_specs/justfile smoke-file
  algebras/smoketest.sage` passes after the algebra constructor and tensor
  component refinement work in the linked phase. Status moved to
  `needs-review`; this does not mark the card accepted or complete.

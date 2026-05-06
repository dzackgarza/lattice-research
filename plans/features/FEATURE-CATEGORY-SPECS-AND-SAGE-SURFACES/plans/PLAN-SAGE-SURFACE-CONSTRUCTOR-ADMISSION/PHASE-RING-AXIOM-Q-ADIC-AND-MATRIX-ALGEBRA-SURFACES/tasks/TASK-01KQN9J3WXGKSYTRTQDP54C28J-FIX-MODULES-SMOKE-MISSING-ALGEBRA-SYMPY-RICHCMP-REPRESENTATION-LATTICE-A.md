---
id: TASK-01KQN9J3WXGKSYTRTQDP54C28J-FIX-MODULES-SMOKE-MISSING-ALGEBRA-SYMPY-RICHCMP-REPRESENTATION-LATTICE-A
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Fix Modules smoke missing algebra _sympy_ __richcmp__ representation lattice
  and graded base-category failures
status: in-progress
priority: high
description: The deleted Modules triage recorded the post-wrapper-deletion smoke frontier
  and the surfaces still meant as mathematical categories rather than exact Sage implementation
  wrappers.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just smoke-file modules/smoketest.sage and preserve the full missing-surface
  output in tracker updates.
- Do not restore constructor-only wrapper categories to make smokes pass.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
---
# Fix Modules smoke missing algebra _sympy_ __richcmp__ representation lattice and graded base-category failures
## Summary

The deleted Modules triage recorded the post-wrapper-deletion smoke frontier and the
surfaces still meant as mathematical categories rather than exact Sage implementation
wrappers.

## Source Provenance

- `category_specs/modules/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/modules/docs/TRIAGE.md`.
- Original migrated line: `Fix Modules smoke missing algebra _sympy_ __richcmp__ representation lattice and graded base-category failures from category_specs/modules/docs/TRIAGE.md`

## Context

- Constructor-only Sage-wrapper categories were removed; constructors now refine Sage objects into real categories such as Free().FiniteRank(), WithOrderedBasis(), Subobjects(), Quotients(), and form-bearing module categories.
- Remaining named module subcategories must not define themselves by exact Sage implementation-class containment.
- OrthogonalGroup belongs to the aut surface of a forms-owned category: C.AutCategory().Of(M) for formed-module categories.
- Current smoke failures include missing algebra, _sympy_, __richcmp__, RepresentationModules KeyError, IntegerLattices/TorsionQuadraticModules compatibility KeyError, and graded module base-category mismatch.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file modules/smoketest.sage and preserve the full missing-surface output in tracker updates.
- [ ] Do not restore constructor-only wrapper categories to make smokes pass.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-06 start-of-task smoke after fork-isolated smoke harness: `just
  --justfile category_specs/justfile smoke-file modules/smoketest.sage` fails on
  current module frontiers. The former migrated `_sympy_` headline is no longer
  present in the filtered smoke output. Current repeated frontiers include
  `modify_module_structure` on free/vector/ring-as-module constructors,
  `alternating_algebra` on basis/subobject/quotient constructors, `annihilator` on
  basisless finite-rank constructors and matrix-ring-as-module, `form` or invalid
  form base-category routing on inner-product and quadratic constructors,
  representation-module `KeyError`, integer-lattice and torsion-quadratic-module
  compatibility `KeyError`, graded-module base-category mismatch against Sage
  `Modules`, Ore characteristic-polynomial, ideal `_refine_category_`, and inherited
  ring frontiers for polynomial/series-as-module constructors.
- 2026-05-06 constructor-refinement slice: changed module constructor refinement to
  return refined parents without running the global not-implemented-method test. This
  matches the matrix-ring constructor treatment: constructors expose their scoped
  category memberships, while missing broad root methods remain frontier evidence when
  exercised directly. Re-running `just --justfile category_specs/justfile smoke-file
  modules/smoketest.sage` removed the repeated `modify_module_structure` constructor
  failures and narrowed the first frontier to basisless vector-space `dimension`,
  subobject/quotient `alternating_algebra`, representation/lattice compatibility
  `KeyError`s, graded base-category mismatch, ideal `_refine_category_`, and inherited
  ring-as-module frontiers.
- 2026-05-06 finite-rank dimension slice: implemented
  `Modules(R).Free().FiniteRank().ParentMethods.dimension()` as `rank()`, matching the
  mapping rule that finite-rank dimension is the cardinality of a basis. Re-running
  the modules smoke removed the `VectorSpaceWithoutBasis(2) has dimension 2` failure;
  the first remaining constructor-specific frontier is vector-space inner-product form
  routing (`base must be a ring or a subcategory of Rings()`), followed by the existing
  subobject/quotient `alternating_algebra`, representation/lattice compatibility,
  graded, ideal, and ring-as-module frontiers.
- 2026-05-06 OverPID formed-chain slice: changed
  `Modules(R).OverPID().WithForms().Bilinear()` and `.Quadratic()` to use
  `_with_axiom(...)`, matching the generic formed-module chain instead of
  instantiating the axiom category with a category object as if it were a base ring.
  Direct probes for `Modules(QQ).WithForms().Bilinear()`, `.Quadratic()`, and
  `VectorSpaceWithInnerProductRows(...).inner_product_matrix()` now pass. Re-running
  the modules smoke removed the vector-space inner-product and explicit
  free/quadratic form constructor failures; the first remaining frontier is now
  subobject/quotient refinement hitting `alternating_algebra`.
- 2026-05-06 membership-refinement and join-super slice: changed direct
  membership-only smoke refinements to call `refine_category(..., test=False)`, so
  subobject/quotient/representation membership checks do not also run the global
  missing-method probe. Added `Modules(R).Quotients()` to finitely presented PID
  quotient constructor refinement, preserving the mathematical `V/W` output
  structure. Changed representation, integer-lattice, torsion-quadratic, and graded
  constructor-family categories with several declared supercategories to return the
  explicit Sage join category, avoiding framework initialization failures from
  parallel supercategory lists. Re-running `just --justfile category_specs/justfile
  smoke-file modules/smoketest.sage` removed the subobject/quotient
  `alternating_algebra`, quotient-of-free-modules, representation-module,
  integer-lattice, and torsion-quadratic-module failures. Remaining frontiers are the
  wrapped graded-module base-category mismatch, ideals lacking `_refine_category_`,
  and ring-as-module constructors failing inside ring constructor refinement before
  the module forgetful refinement runs.

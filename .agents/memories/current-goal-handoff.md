---
title: Current Goal Handoff
---
# Handoff

## Anchor

Read `mem:repo-purpose-mathematical-research-machine` before any card or plan.

## Current phase

Category-spec vocabulary: building the semantic substrate so downstream lattice/Coble
work has named objects, morphisms, and invariants, not raw matrices.

## Current next action

Continue the Sage-surface inventory and mapping closure for
`category_specs/lattices` from the remaining active cards in
`PHASE-HOM-END-AUT-WORK-QUEUE` plus the broader lattice/subtree completion audit.

Handoff constraints to preserve:

- Keep `SPEC-MAPPING-LATTICES` as the lattice/spec routing source for lattice, module,
  torsion, Homset, and form-adjacent surfaces.
- Treat `invariants()` and `invariant_factors()` as `Modules(R).FinitelyPresented().OverPID()`
  surfaces; lattice and torsion categories only inherit as appropriate.
- Keep `TASK-FORMED-COKERNEL-DESCENDED-FORM` closed until a new source-backed contradiction
  appears; do not reopen it as implementation work.
- Do not add package-level import aliases as new mathematical constructors.
- Treat `BinaryQF`, `BQFClassGroup`, and `TernaryQF` via forms-subtree obligations, not as
  `Lattices(ZZ)` constructors.

Concrete routing state established in this segment:

- Package-level import-route closure is in-scope only:
  - `category_specs/lattices/docs/SAGE_INVENTORY.md`: add `sage/modules/all.py`,
    `sage/quadratic_forms/genera/all.py`, and `sage/geometry/all.py` package routes.
  - `SPEC-MAPPING-LATTICES.md`: map those aliases only to export-boundary status; keep constructor
    ownership with `SPEC-MAPPING-MODULES` for `FreeModule`, `VectorSpace`, `span`,
    `vector`, `free_module_element`, `zero_vector`, `random_vector`, `linear_transformation`,
    `FilteredVectorSpace`, `MultiFilteredVectorSpace`; keep `IntegralLattice`/`TorsionQuadraticForm`
    route ownership unchanged.
  - The handoff must treat `sage.geometry.all` exports outside `ToricLattice` (for example:
    cone/fan/polytope helpers, `PolyhedralComplex`, Voronoi, ribbon graph, hyperplane arrangement)
    as non-lattice routing context.
- Required read-before-edit check for this frontier remains:
  - `category_specs/lattices/docs/SAGE_INVENTORY.md`
  - `SPEC-MAPPING-LATTICES.md`

Current unresolved obligation:

- Final symbol-by-symbol lattice/form/module audit for complete constructor ownership and
  surface admission, with a hard gate that only the lattice subtree can add accepted lattice
  constructor owners.

## Required context

Before the next source edit, load:

- `mem:onboarding`
- `mem:repo-purpose-mathematical-research-machine`
- `mem:category-spec-epistemic-foundation`
- `mem:category-spec-constructor-routes-are-category-owned`
- `mem:category-spec-tests-use-category-api-not-private-classes`
- `mem:category-spec-methods-live-at-most-general-owner`
- `mem:category-spec-rotten-core-indicators`
- `mem:mathematical-sanity-check`
- `mem:skills/category-spec-sage-mapping`
- `mem:skills/category-spec-workflow`
- `category_specs/AGENTS.md`
- `category-spec-style`
- `research-state-machine`

## Constraints

- Mapping and spec surfaces before downstream implementation.
- No invented constructor names.
- No ambient/global mutation as constructor compatibility.
- No broad optional or variadic public APIs.
- No downstream Coble work.
- Methods live at the most general mathematical owner. Downstream objects inherit
  surfaces unless they genuinely add new structure or refine hypotheses.
- No documentation laundering: if a Sage surface is not admitted, classify it as
  backend-only, interop/display/runtime, or an explicit missing-category/spec
  obligation.
- `SPEC-MAPPING-LATTICES` routes the formed-cokernel obligation through
  `TASK-FORMED-COKERNEL-DESCENDED-FORM`, now task-level complete: the quotient object
  with descended bilinear/quadratic form data is specified and reviewed. Do not call
  this partially implemented; runtime implementation is outside the current spec
  workflow.
- The parent feature, `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION`,
  `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION`, and five reopened phases are now
  `in-progress` rather than falsely `complete` because new unstarted child tasks remain.

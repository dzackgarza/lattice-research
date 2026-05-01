# Modules Triage

Source for the current documentation pass: `modules/docs/SAGE_INVENTORY.md`,
`modules/docs/MAPPING.md`, Sage written category docs, and local Sage category source.

This file records the current `modules/smoketest.sage` frontier after the Sage-wrapper
subcategory deletion pass.

## Wrapper-Migration State

The constructor-only Sage-wrapper categories have been removed from module code.
Constructors now refine Sage objects into real category surfaces such as
`Free().FiniteRank()`, `WithOrderedBasis()`, `Subobjects()`, `Quotients()`,
`FinitelyPresented().OverPID()`, and form-bearing module categories.

The remaining named module subcategories in `modules/subcategories/` are intended as
mathematical surfaces, not exact Sage implementation-class wrappers:

- `FreeGradedModules`
- `FinitelyPresentedGradedModules`
- `IntegerLattices`
- `OreModules`
- `RepresentationModules`
- `RingObjectsAsModules`
- `TorsionQuadraticModules`

These surfaces must not use exact Sage implementation class containment as their
definition. Constructor routing may still use exact Sage class matches at the interop
boundary to choose the mathematical refinement.

## Orthogonal-Group Frontier

The mathematical owner of `OrthogonalGroup` is the aut surface of a form-bearing
module category: `C.AutCategory().Of(M)` for `C <= Modules(R).WithForms()`.
`types.py` can therefore alias `OrthogonalGroup` to the module aut parent surface.

A concrete `orthogonal_group()` parent-method stub on every formed module still needs a
follow-up edit to `modules/subcategories/with_forms.py`, which is outside the current
write scope. That method should return `C.AutCategory().Of(self)` for the relevant
formed-module category, not a Sage `Group` wrapper.

## Current Smoke Frontier

`just smoke-file modules/smoketest.sage` now collects the full module constructor
frontier. The deleted wrapper categories are not required to reach these failures.

- Missing `algebra`: standard free, vector-space, quotient, free-quadratic, and Ore
  module constructor paths.
- Missing `_sympy_`: vector-space and module subobject constructor paths.
- Missing `__richcmp__`: combinatorial free modules, finite-rank free modules,
  quotient/subobject refinements, finitely presented PID modules, and polynomial-ring
  objects as modules.
- `RepresentationModules()` currently raises `KeyError: (256, 247)`.
- `IntegerLattices` and `TorsionQuadraticModules` currently raise
  `KeyError: (256, 239)`.
- Graded module constructors currently hit a Sage base-category mismatch between
  `sage.categories.modules.Modules` and `category_specs.modules.Modules`.

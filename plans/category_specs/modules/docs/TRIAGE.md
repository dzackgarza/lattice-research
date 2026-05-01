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

## Current Smoke Frontier

`just smoke-file modules/smoketest.sage` currently stops at the first free-module
constructor:

`AssertionError: Not implemented method: _an_element_from_iterator`

This comes from finite/countable set structure during `refine_category` validation
before the module-wrapper assertions are reached. It is not evidence that a deleted
wrapper category is still required.

## Adjacent Set-Spec Decision

`_an_element_from_iterator` is recorded in `../../NEEDS_DECISIONS.md` as an adjacent
sets-spec decision. The module migration must not hide that failure by weakening module
smokes, deleting set abstract methods, or bypassing `refine_category`.

Once the set decision is resolved, the module smoke should continue exposing the next
real category-surface gap through `Modules(R).Constructors()`.

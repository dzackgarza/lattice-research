# Modules Triage

Source for the current documentation pass: `modules/docs/SAGE_INVENTORY.md`,
`modules/docs/MAPPING.md`, Sage written category docs, and local Sage category source.

This file records the current `modules/smoketest.sage` frontier. The smoke is expected
to fail until the listed missing surfaces and structural blockers are implemented.

## Dynamic Category Key Mismatch

These constructors fail with `KeyError` values such as `(256, 145)` and `(256, 156)`.
The failures happen in Sage/category dynamic-class lookup, so they are not missing
module methods:

- `Modules(Zmod(6)).Constructors().FreeModule(2)`
- `Modules(ZZ['x']).Constructors().FreeModule(2)`
- `Modules(ZZ).Constructors().FreeModule(2)`
- `refine_category(FreeModule(RDF, 2), Modules(RDF).Constructors().RealDoubleVectorSpaces())`
- `refine_category(FreeModule(CDF, 2), Modules(CDF).Constructors().ComplexDoubleVectorSpaces())`
- `refine_category(V.subspace(...), Modules(QQ).Constructors().VectorSubspaces())`
- `refine_category(V.subspace_with_basis(...), Modules(QQ).Constructors().VectorSubspacesWithOrderedGeneratingSet())`
- `refine_category(V.quotient_module(W), Modules(QQ).Constructors().VectorSpaceQuotients())`
- `Modules(QQ).Constructors().CombinatorialFreeModule(['a', 'b'])`
- `Modules(QQ).Constructors().FiniteRankFreeModule(2)`
- `refine_category(M.submodule_with_basis(...), Modules(ZZ).Constructors().FreeModuleSubmodulesWithOrderedGeneratingSet())`
- `refine_category(M.quotient_module(S), Modules(ZZ).Constructors().FreeModuleQuotients())`
- `refine_category(C.submodule([a + b]), Modules(QQ).Constructors().SubmodulesWithOrderedGeneratingSet())`
- `refine_category(C.quotient_module(CS), Modules(QQ).Constructors().QuotientModulesWithOrderedGeneratingSet())`
- `refine_category(SymmetricGroup(3).regular_representation(QQ), Modules(QQ).Constructors().RepresentationModules())`
- `refine_category(M / W, Modules(ZZ).Constructors().FinitelyGeneratedPIDQuotientModules())`

## Form-Axiom Base Mismatch

These constructors fail because bilinear/quadratic form categories are being created
with `Modules` where their axiom category expects `WithForms`:

- `Modules(QQ).Constructors().VectorSpace(2)`
- `Modules(ZZ).Constructors().FreeQuadraticModule(2, [[2, 1], [1, 2]])`
- `Modules(ZZ).Constructors().IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]])`
- `Modules(ZZ).Constructors().TorsionQuadraticForm([[1, 1/2], [1/2, 1]])`

## Graded-module base-category mismatch

These constructors fail with:

`AssertionError: base category class for sage.categories.graded_modules.GradedModules mismatch; expected sage.categories.modules.Modules, got category_specs.modules.Modules`

- `Modules(ExteriorAlgebra(QQ)).Constructors().FreeGradedModule(E, (-1, 3))`
- `Modules(ExteriorAlgebra(QQ)).Constructors().FPModule(E, [0, 1], [[x, 1]])`

This is not a missing-method failure. It is a category-construction mismatch between
Sage's graded-module functorial machinery and the replacement
`category_specs.modules.Modules` root.

## Missing Methods Reached After Refinement

These failures are the next concrete method surfaces exposed by refinement:

- `refine_category(M.submodule(...), Modules(ZZ).Constructors().FreeModuleSubmodules())`
  reaches `AssertionError: Not implemented method: _sympy_`.
- `Modules(GF(5^3)).Constructors().OreQuotientModule(S, X^2 + z)` reaches
  `AssertionError: Not implemented method: _an_element_from_iterator`.
- `Modules(ZZ).Constructors().polynomial_ring_as_module(name='t')` reaches
  `AssertionError: Not implemented method: _sympy_` through the underlying ring
  refinement.

The ring-object-as-module failure comes from refining the underlying polynomial ring
object, not from a module-specific method gap.

## Current Blocker Groups

The module subtree currently has four distinct blockers:

- dynamic category-key mismatches in Sage/category generated class lookup
- form-axiom base-category mismatches for bilinear and quadratic module families
- one functorial-category incompatibility, `GradedModules`
- missing `_sympy_` / `_an_element_from_iterator` surfaces reached after refinement

Do not hide these failures with `pytest.raises` or raw Sage bypasses. The smoke should
continue to expose them through `Modules(R).Constructors()`.

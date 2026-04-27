# Modules Triage

Source for the current documentation pass: `modules/docs/SAGE_INVENTORY.md`,
`modules/docs/MAPPING.md`, Sage written category docs, and local Sage category source.

This file records module-side organizational blockers and the runtime failures already
known from the existing constructor inventory. Runtime failures are not the source of
truth for the organization pass.

## Current Alignment

- Constructor entry points are exposed as `Modules(R).Constructors()`.
- Construction categories are split under `subcategories/constructions/`.
- `Modules(R).NamedModules()` is not part of the forward surface. The canonical
  constructor namespace is `Modules(R).Constructors()`.
- Homsets, endsets, and automorphism sets are explicit category surfaces. Generic
  hom/end/aut behavior belongs to top-level `homsets/`; module-specific linear
  structure belongs to `modules/homsets.py`.
- Axiomatic restrictions are split into one mathematical file per restriction under
  `subcategories/`.
- Sage-backed module families are split into one file per family under
  `subcategories/`.
- Subobjects are submodules in module categories. Quotients, subquotients, tensor
  products, duals, graded modules, and filtered modules are attachable categorical
  constructions, not constructor buckets.

## Audit Conclusions Before Runtime Validation

- Axiomatic module restrictions live in mathematical files such as `free.py`,
  `projective.py`, `finitely_presented.py`, and `over_pid.py`.
- Sage-backed implementation families live in files such as
  `vector_spaces.py`, `free_modules_over_pids.py`,
  `finitely_generated_pid_quotient_modules.py`, and
  `torsion_quadratic_modules.py`.
- Root module method surfaces live in `modules/__init__.py` as `_RModObjects` and
  `_RModElements`, matching the top-level category owner.
- `Modules.from_matrix` delegates matrix cokernel construction to
  `FinitelyPresentedModulesOverPID.from_matrix`, because Smith-form and
  elementary-divisor representations belong to finitely presented modules over PIDs.

## Broad blocker: missing `Aut`

These constructors fail with `AssertionError: Not implemented method: Aut`.

- `Modules(Zmod(6)).Constructors().FreeModule(2)`  
  Category target: `FreeModulesWithStandardBasis`
- `Modules(ZZ['x']).Constructors().FreeModule(2)`  
  Category target: `FreeModulesOverIntegralDomains`
- `Modules(ZZ).Constructors().FreeModule(2)`  
  Category target: `FreeModulesOverPIDs`
- `Modules(QQ).Constructors().VectorSpace(2)`  
  Category target: `VectorSpaces`
- `refine_category(FreeModule(RDF, 2), Modules(RDF).Constructors().RealDoubleVectorSpaces())`
- `refine_category(FreeModule(CDF, 2), Modules(CDF).Constructors().ComplexDoubleVectorSpaces())`
- `refine_category(V.subspace(...), Modules(QQ).Constructors().VectorSubspaces())`
- `refine_category(V.subspace_with_basis(...), Modules(QQ).Constructors().VectorSubspacesWithOrderedGeneratingSet())`
- `refine_category(V.quotient_module(W), Modules(QQ).Constructors().VectorSpaceQuotients())`
- `Modules(ZZ).Constructors().FreeQuadraticModule(2, matrix(ZZ, [[2, 1], [1, 2]]))`
- `Modules(QQ).Constructors().CombinatorialFreeModule(['a', 'b'])`
- `Modules(QQ).Constructors().FiniteRankFreeModule(2)`
- `refine_category(M.submodule(...), Modules(ZZ).Constructors().FreeModuleSubmodules())`
- `refine_category(M.submodule_with_basis(...), Modules(ZZ).Constructors().FreeModuleSubmodulesWithOrderedGeneratingSet())`
- `refine_category(M.quotient_module(S), Modules(ZZ).Constructors().FreeModuleQuotients())`
- `refine_category(C.submodule([a + b]), Modules(QQ).Constructors().SubmodulesWithOrderedGeneratingSet())`
- `refine_category(C.quotient_module(CS), Modules(QQ).Constructors().QuotientModulesWithOrderedGeneratingSet())`
- `refine_category(SymmetricGroup(3).regular_representation(QQ), Modules(QQ).Constructors().RepresentationModules())`
- `refine_category(M / W, Modules(ZZ).Constructors().FinitelyGeneratedPIDQuotientModules())`
- `Modules(GF(5^3)).Constructors().OreQuotientModule(S, X^2 + z)`
- `Modules(ZZ).Constructors().IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]])`
- `Modules(ZZ).Constructors().TorsionQuadraticForm(matrix(QQ, [[1, 1/2], [1/2, 1]]))`

At the moment this single abstract-method gap blocks most of the module subtree from reaching any more specialized validation.

## Graded-module base-category mismatch

These constructors fail with:

`AssertionError: base category class for sage.categories.graded_modules.GradedModules mismatch; expected sage.categories.modules.Modules, got category_specs.modules.Modules`

- `Modules(ExteriorAlgebra(QQ)).Constructors().FreeGradedModule(E, (-1, 3))`
- `Modules(ExteriorAlgebra(QQ)).Constructors().FPModule(E, [0, 1], [[x, 1]])`

This is not a missing-method failure. It is a category-construction mismatch between Sage's graded-module functorial machinery and the replacement `category_specs.modules.Modules` root.

## Ring-object-as-module failure inherited from ring refinement

This constructor fails with `AssertionError: Not implemented method: is_algebraically_closed`.

- `Modules(ZZ).Constructors().polynomial_ring_as_module('t')`

This failure comes from refining the underlying polynomial ring object, not from a module-specific method gap.

## Consequence

The module subtree currently has three distinct blockers:

- one dominant abstract-method gap, `Aut`
- one functorial-category incompatibility, `GradedModules`
- one inherited ring-side gap, `is_algebraically_closed` on ring objects viewed as modules

The `Aut` surface is the first blocker to remove if the goal is to expose the next layer of module-specific missing methods.

## Outstanding Decisions Needed

- Decide how `FinitelyPresentedModulesOverPID` should be wired without recursive
  `FinitelyPresented().OverPID()` registration.
- Decide how topological-module structure inherits from `topological_spaces` and
  topological rings without duplicating method surfaces.

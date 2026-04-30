# Modules Triage

Source for the current documentation pass: `modules/docs/SAGE_INVENTORY.md`,
`modules/docs/MAPPING.md`, Sage written category docs, and local Sage category source.

This file records the current `modules/smoketest.sage` frontier. The smoke is expected
to fail until the listed missing surfaces and structural blockers are implemented.

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

## Consequence

The module subtree currently has four distinct blockers:

- dynamic category-key mismatches in Sage/category generated class lookup
- form-axiom base-category mismatches for bilinear and quadratic module families
- one functorial-category incompatibility, `GradedModules`
- missing `_sympy_` / `_an_element_from_iterator` surfaces reached after refinement

Do not hide these failures with `pytest.raises` or raw Sage bypasses. The smoke should
continue to expose them through `Modules(R).Constructors()`.

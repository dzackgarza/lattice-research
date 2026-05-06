---
id: SPEC-MAPPING-FORMS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track forms mapping spec
status: needs-review
priority: critical
requirement: Convert category_specs/forms/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  bilinear, quadratic, form-codomain, Hom, End, and Aut signatures.
acceptanceCriteria:
- Source paths category_specs/forms/docs/MAPPING.md and category_specs/forms/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 85
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Forms Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/forms/docs/MAPPING.md`.

Source inventory: `category_specs/forms/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/forms/docs/SAGE_INVENTORY.md`.
- Cross-inventory source files checked because the forms inventory is an ownership
  pointer rather than an independent Sage category inventory:
  - `category_specs/modules/docs/SAGE_INVENTORY.md`
  - `category_specs/lattices/docs/SAGE_INVENTORY.md`
  - `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`
- Installed Sage source files checked or named by those inventories for this forms pass:
  - `sage/modules/free_quadratic_module.py`
  - `sage/modules/free_quadratic_module_integer_symmetric.py`
  - `sage/modules/torsion_quadratic_module.py`
  - `sage/tensor/modules/tensor_free_module.py`
  - `sage/tensor/modules/free_module_tensor.py`
  - `sage/quadratic_forms/quadratic_form.py`
  - `sage/quadratic_forms/quadratic_form__automorphisms.py`
  - `sage/quadratic_forms/quadratic_form__genus.py`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the forms
  cross-inventory reconciliation is recorded below, with remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Completeness Reconciliation: Forms Cross-Inventory

The forms inventory names five Sage evidence families: `FreeQuadraticModule_generic`,
`FreeQuadraticModule_integer_symmetric`, `TorsionQuadraticModule`,
`TorsionQuadraticForm(q)`, and `TensorFreeModule` dual components. The converted
mapping assigns all five to explicit forms, modules, lattices, or tensor-component
owners:

- free quadratic modules map to free bilinear or quadratic formed-module structure,
  with Gram, determinant, discriminant, and inner-product surfaces first owned by
  free bilinear modules;
- integral symmetric Sage lattices map through the forms-owned nondegenerate symmetric
  integral chain, with the named `Lattices(R)` endpoint adding only lattice-specific
  specializations;
- torsion quadratic modules map to
  `forms.subcategories.torsion_quadratic_modules.TorsionQuadraticModulesCategory`,
  while the old module route remains constructor compatibility;
- tensor dual components remain tensor-component objects until attached as form data
  to a module;
- symmetric bilinear element divisibility is the pairing-image submodule
  `<b(v, M)> <= S`, not a free-module coordinate-gcd surface.

Negative source finding for a separate Sage forms category:

- Searched: `category_specs/forms/docs/SAGE_INVENTORY.md`, `category_specs/forms/*`,
  `category_specs/modules/docs/SAGE_INVENTORY.md`,
  `category_specs/lattices/docs/SAGE_INVENTORY.md`,
  `category_specs/tensor_algebra_components/docs/SAGE_INVENTORY.md`, installed Sage
  paths matching forms, free-quadratic modules, torsion-quadratic modules, tensor
  modules, and quadratic-form files under `/home/dzack/miniforge3/envs/sage`.
- Found: the local forms inventory intentionally delegates Sage evidence to the
  modules, lattices, and tensor-component inventories; installed Sage exposes the
  relevant form-bearing objects through module, tensor, and quadratic-form sources,
  not through a distinct `sage.categories.forms` owner.
- Conclusion: inference -- this pass found no separate installed Sage forms category
  that should add a new forms-local mapping surface beyond the cross-inventory
  families listed above.
- Confidence: Medium.
- Gaps: Sage upstream issue discussions, unreleased Sage branches, and a full
  method-by-method reconciliation of every quadratic-form algorithm file remain
  outside this forms-local pass and continue under the active completeness task.

## Converted Mapping Content

`FormedModules(R)` is the forms-subtree owner for modules equipped with forms.
It is the named spelling of `Modules(R, dispatch=False).WithForms()`.

## Ownership

| Surface | Owner | Notes |
| --- | --- | --- |
| `Modules(R).WithForms()` | `forms.subcategories.with_forms.FormedModulesCategory` | Modules keeps the Sage-compatible route; forms owns the class and method surface. |
| `Modules(R).WithForms().Bilinear()` | `forms.subcategories.bilinear.BilinearModulesCategory` | Owns bilinear evaluation and generic bilinear predicates. |
| `Modules(R).WithForms().Quadratic()` | `forms.subcategories.quadratic.QuadraticModulesCategory` | Owns quadratic evaluation. |
| Symmetric, alternating, nondegenerate, definite, indefinite, integral, rational bilinear axioms | `forms.subcategories.*` | These are formed-module properties, not lattice-only properties. |
| `divisibility(v)` for symmetric bilinear elements | `forms.subcategories.symmetric.SymmetricBilinearModulesCategory.ElementMethods` | The invariant definition is the pairing-image submodule `<b(v, M)>` of the form codomain `S`; for `S = R`, this is an ideal. |
| Form-preserving morphisms between formed modules | `C.HomCategory().Of(M, N)` for `C <= FormedModules(R)` | A candidate map preserves form data exactly when it is contained in the Hom object of the formed-module category. |
| Isometries of formed modules | `C.HomCategory().Of(M, N)` plus generic isomorphism; automorphism case `C.AutCategory().Of(M)` | Form preservation is already Hom containment. The isometry question is invertibility or isomorphism inside that category. |
| Free bilinear modules | `forms.subcategories.free_bilinear.FreeBilinearModulesCategory` | First tier where Gram matrices, determinant, and discriminant are universally meaningful. |
| Finite-rank free formed-module chain used by `Lattices(R)` | `forms.chain` | Lattices imports this chain and adds only the named `Lattice` endpoint. |
| Finite torsion quadratic modules | `forms.subcategories.torsion_quadratic_modules.TorsionQuadraticModulesCategory` | Modules keeps `TorsionQuadraticModules()` as a compatibility constructor route. |
| `Lattices(R)` | `lattices.LatticesCategory` | Lattice-specific endpoint and lattice construction categories remain in `lattices`. |

## Compatibility Routes

The module and lattice import paths remain valid:

- `category_specs.modules.subcategories.with_forms.FormedModulesCategory`
- `category_specs.modules.subcategories.bilinear.BilinearModulesCategory`
- `category_specs.modules.subcategories.quadratic.QuadraticModulesCategory`
- `category_specs.modules.subcategories.torsion_quadratic_modules.TorsionQuadraticModulesCategory`
- `category_specs.lattices.subcategories.symmetric.SymmetricBilinearModulesCategory`
- analogous lattice paths for alternating, nondegenerate, definite, indefinite,
  integral, rational, and free bilinear categories.

Those files are shims. New specs should import or document formed-module ownership
through `forms`.

## Boundary With Tensor Components

`TensorAlgebraComponents(R)` owns tensor component modules and tensor elements.
A scalar-valued bilinear form may be constructed there as a `(0,2)` tensor. The object
becomes a formed module only when attached as form data to a module category in this
subtree.

## Twisted And Semilinear Form Data

No separate `TwistedForms` category is admitted at this time.

The grounded form-object contract already records the relevant data on the form object:
the tensor-degree source, codomain module, and scalar-action endomorphism `sigma`.
`ModulesWithForms(R)` therefore remains the owner for pairs `(M, f)` with semilinear
form data, while the named forms subcategories own the cases currently admitted by the
mapping:

- bilinear forms use tensor degree `2` and `sigma = id_R`;
- quadratic forms use tensor degree `1` with the current quadratic scalar action;
- alternating, symmetric, integral, rational, finite-torsion, and quotient-valued cases
  refine the existing formed-module chain.

Tensor-component duals remain tensor-component objects until attached as form data to a
module. A future twisted-form subcategory may be admitted only if a concrete public
method or constructor is mathematically wrong without a distinct owner beyond
`FormedModules(R)` plus tensor-component/Hom-category structure.

## Form-Preserving Morphisms And Isometries

For `C <= FormedModules(R)`, the form-preserving maps from `M` to `N` are the elements
of `C.HomCategory().Of(M, N)`. A plain `R`-module morphism belongs to
`Modules(R).HomCategory()` first; it is promoted into the formed-module Hom object only
when it satisfies the defining form-compatibility equation.

Consequences:

- do not introduce a standalone public `is_form_preserving()` predicate as the owner of
  form preservation;
- `is_isometry()` on a formed-module morphism is only a compatibility query for
  isomorphism inside an already form-preserving Hom object;
- `orthogonal_group()` is `C.AutCategory().Of(M)` for the relevant formed-module
  category `C`;
- matrix equations are implementation checks under explicit presentations, not the
  public definition of preservation or isometry.

Metric-space isometries in `TopologicalSpaces().HomCategory()` are a separate surface
and must not be routed through this formed-module owner.

## Symmetric Bilinear Divisibility

For a symmetric bilinear module `(M, b)` with `b: M x M -> S`, the element
divisibility surface is:

`divisibility(v) = < b(v, w) : w in M > <= S`.

This is a submodule of the form codomain `S`. In the scalar-valued case `S = R`, it is
an ideal of `R`. Coordinate gcds, principal generators, or old Sage lattice
presentations are only possible representations after extra hypotheses are recorded;
they are not the mathematical definition and do not create a free-module owner.

## Boundary With Lattices

Lattices are integral, nondegenerate, symmetric, finite-rank free bilinear modules with
the additional named `Lattice` axiom. Formed-module methods such as `b`, `gram_matrix`,
`dual_lattice`, and `orthogonal_group` remain owned by forms. The quotient class map
`L^* -> L^*/L` belongs to `Lattices(R).DualObjects().ElementMethods` because it is
nontrivial on dual-lattice elements and zero on ordinary elements of `L`.
Lattice-specific specializations such as `OverIntegers`, `Even`, `Unimodular`, and
lattice construction categories remain owned by `lattices`.

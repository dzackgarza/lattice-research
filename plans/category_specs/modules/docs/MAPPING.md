# Modules Mapping

This file records the forward target mapping from Sage module surfaces into the local
category-spec hierarchy.

## Constructor Namespace

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| `Modules(R).NamedModules()` | `Modules(R).Constructors()` | Sage constructors create module objects; they are not mathematical subcategories. |
| `FreeModule(R, n)` and `R^n` | `Modules(R).Constructors().FreeModule(n)` refined into `Modules(R).Free()` plus finite-rank and base-ring restrictions | The constructor is concrete; `Free` is an axiomatic restriction attachable to any module subcategory. |
| `VectorSpace(K, n)` | `Modules(K).Constructors().VectorSpace(n)` refined into `Modules(K).Free().FiniteRank().OverField()` | Vector spaces are modules over fields with finite-rank structure when the constructor supplies a dimension. |
| Matrix presentations `f: R^m -> R^n` | `Modules(R).from_matrix(M)` delegating to `FinitelyPresentedModulesOverPID.from_matrix` | A matrix presentation defines `coker(f)`. Smith-form and elementary-divisor normalization are specific to finitely presented modules over PIDs, so the constructor namespace delegates to that subcategory owner. |
| `SubmoduleWithBasis`, free-module submodules, vector subspaces | `Modules(R).Subobjects()` / `Submodules` plus ordered-generating-set refinements | In module categories, subobjects are submodules. |
| Quotient modules and FGP modules | `Modules(R).Quotients()` plus finite-presentation/base-ring refinements | Quotients are construction categories attachable to arbitrary module subcategories. |
| Ring objects viewed as modules | `Modules(R).Constructors().RingObjectAsModule(...)` | The ring object supplies the module structure; ring-specific methods remain in `rings`. |

## Axiomatic Restrictions

`Free`, `Torsion`, `Torsionfree`, `Projective`, `FinitelyGenerated`,
`FinitelyPresented`, and base-ring restrictions are axiomatic restrictions. They must be
attachable to any subcategory `C` of `Modules(R)` through `C.<Axiom>()`. More concrete
categories, such as finitely generated free modules over a PID, can be implementation
targets only when the additional hypotheses make a real algorithmic surface possible.

## Construction Layout

| Current source surface | Target file organization |
| --- | --- |
| Former construction aggregator | `subcategories/constructions/subobjects.py`, `subquotients.py`, `quotients.py`, `isomorphic_objects.py`, `tensor_products.py`, `cartesian_products.py`, and `dual_objects.py`. |
| Axiomatic module restrictions | One mathematical file per axiomatic subcategory under `subcategories/`. |
| Sage-backed module family surface | Constructor namespace plus one mathematical subcategory file per concrete Sage-backed module family. |

## Construction-Category Mapping

| Sage surface | Target surface | Rationale |
| --- | --- | --- |
| `Modules(R).Homsets()` | `modules/homsets.py` and top-level `homsets/` | Module homsets are sets of `R`-linear maps. Sage makes them modules over `R` and gives the parent method `zero()`. |
| `Modules(R).Endsets()` / `Modules(R).Homsets().Endset()` | `modules/homsets.py` plus generic `Endsets` | Module endsets are homsets with equal domain and codomain. Sage's `Modules.Homsets.Endset` adds magmatic-algebra structure over `R`. |
| Project `Modules(R).Autsets()` | generic `Autsets` with module specialization | A module automorphism set is the invertible part of `End(M)`. This belongs in the hom/end/aut hierarchy, not in constructor namespaces. |
| `Modules(R).CartesianProducts()` | `subcategories/constructions/cartesian_products.py` | Cartesian products of modules are direct products with componentwise module operations and common base-ring bookkeeping. |
| `Modules(R).TensorProducts()` | `subcategories/constructions/tensor_products.py` | Tensor products are functorial constructions with `tensor_factors()` and construction data. |
| `Modules(R).DualObjects()` / `dual()` | `subcategories/constructions/dual_objects.py` | Linear duals are covariant functorial construction objects in Sage; graded duals are not separated by the Sage `DualObjects` category. |
| `Modules(R).Subquotients()` | `subcategories/constructions/subquotients.py` | Constructive module subquotients have an ambient module, lift, and retract. Submodules and quotient modules refine this surface. |
| `Modules(R).Subobjects()` / `Submodules` | `subcategories/constructions/subobjects.py` | Subobjects in module categories are submodules. Method signatures should use `Submodule`, not bare `Module`. |
| `Modules(R).Quotients()` | `subcategories/constructions/quotients.py` | Quotient modules are modules modulo submodules and should refine `Subquotients`. |
| `Modules(R).IsomorphicObjects()` | `subcategories/constructions/isomorphic_objects.py` | Transport of module structure along an isomorphism is simultaneously subobject-like and quotient-like in Sage's construction hierarchy. |
| `Modules(R).Graded()` | `subcategories/graded.py` | A graded module is an attachable restriction/construction on any module subcategory. Concrete FP graded modules remain constructor-family objects, not the definition of all graded modules. |
| `Modules(R).Filtered()` | `subcategories/filtered.py` | Filtered modules are attachable restrictions/constructions on module subcategories. Sage notes interaction with `WithBasis`; the project mapping keeps it as its own mathematical file. |
| `Modules(R).FiniteDimensional()` | `subcategories/finite_dimensional.py` | Finite-dimensionality is an axiomatic restriction. Over finite base rings, Sage adds finite-set structure. |
| `Modules(R).FinitelyPresented()` | `subcategories/finitely_presented.py` | Finitely presented modules are an axiomatic restriction. Concrete finitely presented graded/PID modules are implementation families under the constructor namespace. |

## Topological Modules

Topological module structure should inherit the topological-space surface from
`topological_spaces`, the module surface from `modules`, and any ring topology from
`rings`. It should not duplicate topological-space methods locally.

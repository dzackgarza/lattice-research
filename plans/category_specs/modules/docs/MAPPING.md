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

Constructor signatures should expose the structured Sage inputs from
`docs/SAGE_INVENTORY.md`. For example, `FreeModule` takes
`rank_or_basis_keys`, `sparse`, `inner_product_matrix`, `with_basis`, `rank`, and
`basis_keys`; `VectorSpace` takes the analogous dimension/basis-key parameters; and
`FreeQuadraticModule` takes `rank`, `inner_product_matrix`, `sparse`, and
`inner_product_ring`. When upstream Sage implements these surfaces with `*args` or
`**kwds`, the spec should not mirror that plumbing unless the written Sage
documentation proves a genuinely open-ended mathematical input family. The target
surface is the finite documented casework.

Integer-valued module data uses `Integer`, not `int | Integer`: ranks, dimensions,
tensor powers, tensor bidegrees, start indices, graded generator degrees, polynomial
variable counts, and series precisions. The constructor namespace may pass these values
to Sage factories, but the spec surface records the Sage mathematical type.

Type vocabulary should name mathematical objects, not implementation containers.
Generating sets, coordinate vectors, tensor symmetry data, and element-class hooks are
spelled directly as sequences, module elements, tuples, or element classes unless the
name introduces an independent mathematical noun such as `ModuleBasis` or
`Cardinality`.

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
| `Modules(R).Endsets()` / `Modules(R).Homsets().Endset()` | `modules/homsets.py` plus generic `HomsetsOf(Modules(R)).Endset()` | Module endsets are homsets with equal domain and codomain. Sage's `Modules.Homsets.Endset` adds magmatic-algebra structure over `R`, so the project declares `End_R(M)` as an `R`-algebra in addition to the generic endset structure. |
| Project `Modules(R).Autsets()` | generic `HomsetsOf(Modules(R)).Autset()` with module specialization | `Aut_R(M)` is the invertible part of `End_R(M)`. The root homsets layer owns the Autset construction; `modules/homsets.py` declares only module-specific names and extra structure. |
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

## Homset Extra-Structure Decision

`R-Mod` is the first concrete model for hom/end/aut extra structure. The generic layer
declares that `Hom_R(M, N)`, `End_R(M)`, and `Aut_R(M)` are homsets, endsets, and
autsets internal to `Modules(R)`. The module subtree additionally declares that
`Hom_R(M, N)` is an `R`-module and `End_R(M)` is an object of `Algebras(R)`, retaining
Sage's `MagmaticAlgebras(R)` supercategory for upstream compatibility. Autset
construction still comes from the generic layer because `Aut_R(M)` is defined by
invertibility inside `End_R(M)` and dispatched through the module endset category.

## Topological Modules

Topological module structure should inherit the topological-space surface from
`topological_spaces`, the module surface from `modules`, and any ring topology from
`rings`. It should not duplicate topological-space methods locally.

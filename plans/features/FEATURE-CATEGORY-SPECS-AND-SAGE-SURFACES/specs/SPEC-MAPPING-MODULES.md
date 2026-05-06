---
id: SPEC-MAPPING-MODULES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track modules mapping spec
status: needs-review
priority: critical
requirement: Convert category_specs/modules/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  module, subobject, quotient, tensor, dual, basis, and constructor signatures.
acceptanceCriteria:
- Source paths category_specs/modules/docs/MAPPING.md and category_specs/modules/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 90
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Modules Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/modules/docs/MAPPING.md`.

Source inventory: `category_specs/modules/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/modules/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage`
  - `sage/modules/free_module.py`
  - `sage/modules/free_quadratic_module.py`
  - `sage/combinat/free_module.py`
  - `sage/modules/with_basis/subquotient.py`
  - `sage/modules/with_basis/representation.py`
  - `sage/categories/semigroups.py`
  - `sage/modules/fg_pid/fgp_module.py`
  - `sage/modules/free_module_integer.py`
  - `sage/modules/free_quadratic_module_integer_symmetric.py`
  - `sage/modules/torsion_quadratic_module.py`
  - `sage/tensor/modules/finite_rank_free_module.py`
  - `sage/modules/fp_graded/free_module.py`
  - `sage/modules/fp_graded/module.py`
  - `sage/rings/polynomial/ore_polynomial_ring.py`
  - `sage/modules/ore_module.py`
  - `sage/categories/rings.py`
  - `sage/categories/modules.py`
  - `sage/categories/modules_with_basis.py`
  - `sage/modules/free_module_homspace.py`
  - `sage/modules/free_module_morphism.py`
  - `sage/modules/matrix_morphism.py`
  - `sage/modules/fg_pid/fgp_morphism.py`
  - `sage/tensor/modules/free_module_homset.py`
  - `sage/tensor/modules/free_module_morphism.py`
  - `sage/modules/fp_graded/free_homspace.py`
  - `sage/modules/fp_graded/homspace.py`
  - `sage/modules/fp_graded/morphism.py`
  - `sage/modules/ore_module_homspace.py`
  - `sage/modules/ore_module_morphism.py`
  - additional installed source paths listed in `category_specs/modules/docs/SAGE_INVENTORY.md` beyond this ledger limit: 21
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the Modules
  source reconciliation is recorded below, with remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Source Reconciliation Against Installed Sage 10.7

This reconciliation compares the local inventory with installed Sage source under
`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage`. It records
surfaces that were missing, inherited, or easy to mis-own in the converted mapping.
Ownership follows the caller object/category. The category of an output object is
codomain data and does not by itself own the method.

### Reconciled Category And Constructor Surfaces

| Sage surface checked | Source evidence | Mapping outcome |
| --- | --- | --- |
| `Modules(R).__classcall_private__(base_ring)` dispatching fields to vector spaces | `categories/modules.py:120-152` | Runtime dispatch. The project owner remains `Modules(R)`; vector-space output for field bases is a refinement/codomain consequence. |
| `Modules(R).FiniteDimensional()`, `.FinitelyPresented()`, `.Filtered()`, `.Graded()`, `.WithBasis()` | `categories/modules.py:342-493` | Axiomatic or construction restrictions on `Modules(R)`. They are inherited owners for module methods satisfying their hypotheses, not constructor families. |
| `Modules(R).TensorProducts()`, `.DualObjects()`, `.CartesianProducts()`, `.Subquotients()`, `.Subobjects()`, `.Quotients()`, `.IsomorphicObjects()` | `categories/modules.py:246-264`, `:836-980`, inherited construction-category machinery | Construction categories. Methods called on a module, subobject, quotient, tensor product, or dual object stay on that caller surface; the constructed object's category is codomain data. |
| `Modules(R).Homsets()` and `Modules(R).Endsets()` | `categories/modules.py:724-820` | `Modules(R).HomCategory()` and `Modules(R).EndCategory()`. The hom object owns `base_ring()` and `zero()`; module end objects additionally carry algebra structure over `R`. |
| `FreeModule(R, ...)`, `VectorSpace(K, ...)`, `span(...)`, `FreeQuadraticModule(R, ...)`, `QuadraticSpace(K, ...)` | `modules/free_module.py:311-804`, `modules/free_quadratic_module.py:86-220` | Constructor namespace entries on `Modules(R).Constructors()` or the relevant forms-owned constructor route. Positional Sage dispatch remains split into named non-variadic project constructors. |
| `R^n`, `R^(m,n)`, and `R.free_module(...)` | `categories/rings.py:885-906`, `:1622-1686` | Ring-side bridge into module constructors. The ring method is source evidence for preserving Sage syntax; module structure is owned by `Modules(R).Free().FiniteRank()` or by matrix-space module-with-basis structure. |
| `OrePolynomialRing(...).quotient_module(P)` and `OreModule.__classcall_private__` | `rings/polynomial/ore_polynomial_ring.py:1255`, `modules/ore_module.py:322-357`, `categories/ore_modules.py:9-174` | Constructor route into Sage's `OreModules(base, twist)` category. Project ownership remains deferred between a semilinear-operator module owner and a module-over-Ore-algebra owner until the Ore decision is recorded. |
| `FiniteDimensionalAlgebrasWithBasis.ParentMethods.cell_module(mu, **kwds)` | `categories/finite_dimensional_algebras_with_basis.py:1499-1653`, `modules/with_basis/cell_module.py:23-393` | Algebra-side constructor for a cell module. The module object maps to representation/cellular-module owners; the constructor is not owned by generic `Modules(R)`. |

### Reconciled Method Ownership

| Sage method or inherited surface | Highest correct owner | Classification and notes |
| --- | --- | --- |
| `base_ring`, `zero`, additive/scalar operations, `linear_combination` | `Modules(R)` or the relevant `Modules(R).HomCategory()` object when called on a homset | Admitted only as module or hom-object structure. Parent aggregation is not a separate constructor surface. |
| `tensor_square`, `tensor`, `tensor_module`, `tensor_factors`, tensor element `apply_multilinear_morphism` | `Modules(R).TensorProducts()` with `WithBasis()` refinements when basis tensor APIs are used | Tensor-product construction and tensor-product object methods. Representation tensor products refine through representation-module owners. |
| `dual`, `linear_form`, `alternating_form`, `dual_symmetric_power`, `dual_exterior_power` | `Modules(R).DualObjects()` and `Modules(R).HomCategory()` for `Hom_R(M, R)` content; exterior/symmetric owners require finite-rank/free/projective hypotheses | The caller is the module whose dual or tensor construction is being formed. Ordinary linear duals are not forms-owned shortcuts. |
| `basis`, `bases`, `default_basis`, `set_default_basis`, `basis_matrix`, `coordinate_vector`, `coordinates`, `from_vector`, `element_from_coordinates` | `Modules(R).WithBasis()` and `Modules(R).WithOrderedBasis()` where row/order data is meaningful | Basis and coordinate surfaces. Sage state mutation such as `set_default_basis` is interop unless represented as a new presented object plus change-of-basis morphism. |
| `gens`, `gen`, `ngens`, `generator`, `generators`, `generator_degrees` | `WithOrderedGeneratingSet()` or graded-free/finitely-presented graded owners when degrees are part of the structure | Generator access is not evidence for a constructor-family category. Graded degree data stays on graded module surfaces. |
| `monomial`, `term`, `sum_of_monomials`, `sum_of_terms`, `_from_dict`, coefficient/support element methods | `Modules(R).WithBasis().ElementMethods`; ordered leading/trailing methods refine to ordered-basis or term-order owners | Public element construction/readback only when stated as basis-coordinate mathematics. Raw dictionary and private helpers are interop/private. |
| `submodule`, `submodule_with_basis`, `span`, `zero_submodule`, subspace constructors, `ambient`, `lift`, `retract`, `reduce` | `Modules(R).Subobjects()` with `WithBasis()`, `WithOrderedBasis()`, field, PID, or Ore refinements as required | The caller is the ambient module or subobject. Output submodule category is codomain data. |
| `intersection`, `saturation`, `denominator`, `index_in`, `index_in_saturation`, `ambient_vector_space`, `vector_space_span` | Common-ambient subobject owners with integral-domain, PID, or field hypotheses | Admitted only under the algebraic hypotheses in Sage source. Ambient/vector-space conversion is interop unless expressed as scalar extension or subobject data. |
| `quotient`, `quotient_module`, `quotient_abstract`, `__truediv__`, `cover`, `relations`, `free_cover`, `free_relations`, `quotient_map`, `lift_map`, `cokernel_basis_indices` | `Modules(R).Quotients()` and `Modules(R).Subquotients()`, with finite-presentation, PID, field, or basis refinements | The caller is the ambient module, quotient object, or quotient morphism. Quotient normal forms belong to quotient owners, not general basis-bearing modules. |
| `hom`, `_Hom_`, `module_morphism`, `homspace.__call__`, homspace `basis`, `identity`, `zero`, basis-map `on_basis` | `Modules(R).HomCategory()`; `WithBasis().HomCategory()` owns basis-defined constructors | Matrix/image/function constructors are hom-object constructors. Endomorphism specializations refine through `EndCategory()`. |
| Morphism `matrix`, `rank`, `nullity`, `kernel`, `image`, `inverse_image`, `lift`, `restrict_domain`, `restrict_codomain`, `restrict`, injective/surjective/bijective predicates | `Modules(R).HomCategory().ElementMethods`, with field/PID/Ore/graded hypotheses where Sage algorithms require them | These are methods on morphisms. Kernel and image output subobjects are codomain data, not method owners. |
| `inverse`, `side`, `side_switch`, hom arithmetic, `is_identity`, `is_zero`, `is_equal_function` | Hom/end/aut element surfaces | Invertibility promotes membership in the aut surface but does not move the caller-owned method off the morphism/end object. |
| `general_linear_group`, `automorphism`, finite-rank `FreeModuleAutomorphism`, tensor-calculus endomorphism determinant/trace/characteristic polynomial | `Modules(R).AutCategory().Of(M)` and `Modules(R).EndCategory().Of(M)` with finite-rank/free hypotheses | Sage tensor-calculus automorphism classes are implementation witnesses for `Aut_R(M)`, not a separate module family owner. |
| `orthogonal_group` and `automorphisms` on integral lattices or torsion quadratic modules | `C.AutCategory().Of(M)` for the relevant forms-owned category `C` | Orthogonal groups are automorphism objects in a form-preserving category. Lattice/discriminant-form presentations refine the implementation. |
| `determinant`, `discriminant`, `gram_matrix`, `inner_product_matrix`, `_inner_product_is_dot_product`, `_inner_product_is_diagonal`, `inner_product`, `quadratic_product`, `brown_invariant`, `value_module`, `value_module_qf` | Forms-owned bilinear/quadratic module owners | `inner_product_matrix` is Sage wording; public project spelling should be form/Gram/codomain vocabulary. Private diagonal/dot-product helpers stay interop. |
| `dual_lattice`, `discriminant_group`, `signature`, `signature_pair`, `is_even`, `is_primitive`, `orthogonal_complement`, `sublattice`, `overlattice`, `maximal_overlattice`, `genus`, `twist` | Integral-lattice and finite quadratic module owners under forms | Lattice-specific surfaces. They must not be generalized to all modules merely because Sage classes subclass free modules. |
| `LLL`, `BKZ`, `HKZ`, `reduced_basis`, `shortest_vector`, `short_vectors`, `enumerate_short_vectors`, `enumerate_close_vectors`, `voronoi_cell`, `closest_vector`, `babai`, `minimum`, `maximum` | Integral-lattice algorithm surfaces | Algorithmic lattice surfaces. Definite/optional-package limits are implementation caveats, not reasons to weaken the lattice spec. |
| `invariants`, `smith_form_gens`, `gens_to_smith`, `smith_to_gens`, `annihilator`, `additive_order`, finite iteration/list/cardinality | `FinitelyPresentedModulesOverPID` with torsion/finite refinements where applicable | Smith normal form and finite enumeration are PID finite-presentation structure. Element order belongs to torsion/finite PID-module element surfaces. |
| `connectivity`, `suspension`, `minimal_presentation`, `resolution`, `submodule_inclusion`, graded morphism `solve`, `split`, `homology` | `Modules(A).Graded().Free()` or `Modules(A).Graded().FinitelyPresented()` and their hom/subobject/quotient owners | Graded algorithms stay graded; morphism-level algorithms stay on graded hom elements. |
| `semigroup`, `side`, `representation_matrix`, `character`, `brauer_character`, invariant/twisted invariant modules, composition series/factors, Schur/exterior/symmetric representation functors | `Modules(R).WithAction(S, side)` and its representation subobject, quotient, tensor, exterior, symmetric, and Schur construction owners | Representation structure is a module with action. Semigroup/group caller constructors are source evidence for constructor routing only. |
| `cellular_algebra`, `bilinear_form`, `bilinear_form_matrix`, `radical`, `simple_module` on `CellModule` | Deferred cellular-module owner under finite-dimensional algebras with basis, with forms and quotient-module refinements for the bilinear/radical/simple-module surfaces | Not generic module ownership. The caller is a cell module; the constructing caller is the cellular algebra. |
| `ore_ring`, `twisting_morphism`, `twisting_derivation`, `pseudohom`, `multiplication_map`, Ore submodule/quotient morphism restriction/corestriction/quotient/modulo | Deferred Ore owner, plus ordinary inherited free-module, hom, subobject, and quotient surfaces | `categories/ore_modules.py` is present in installed Sage; project naming still needs a decision between semilinear-operator and Ore-algebra ownership. |
| `is_sparse`, `is_dense`, `is_exact`, `some_elements`, `random_element`, `dense_module`, `sparse_module`, `element_class`, display hooks, `_sympy_`, `_magma_init_`, `_macaulay2_`, `_repr_`, `_latex_` | Private/runtime/display/interop | Not public mathematical category surfaces unless a later spec introduces exact-computation or probability-distribution structure with explicit hypotheses. |

### Formal Negative And Corrective Findings

Sage module autset category surface:

- Searched: `category_specs/modules/docs/SAGE_INVENTORY.md`; `sage/categories/modules.py`; recursive source search under installed `sage/modules` and `sage/tensor/modules` for `Autsets`, `AutCategory`, `automorphism`, `general_linear_group`, and `orthogonal_group`.
- Found: no installed `Modules(R).Autsets()` category in the inspected module category source. Sage exposes automorphism behavior through tensor finite-rank `general_linear_group()`/`automorphism()`, matrix-morphism invertibility predicates, and form/lattice `orthogonal_group()` methods.
- Conclusion: inference - the project should own the generic module automorphism surface through `Modules(R).AutCategory()`, with Sage automorphism classes treated as implementation witnesses and specialization evidence.
- Confidence: High.
- Gaps: generated documentation pages and import-resolution aliases outside the inspected installed source tree were not exhausted.

Legacy `NamedModules` surface:

- Searched: `category_specs/modules/docs/SAGE_INVENTORY.md`; `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-MODULES.md`; recursive source search under installed `sage/categories` and `sage/modules` for `NamedModules`, `class NamedModules`, and `def NamedModules`.
- Found: the mapping spec contains the legacy row `Modules(R).NamedModules()`, but the inspected installed Sage source did not expose a `NamedModules` category or method.
- Conclusion: inference - `NamedModules` is a legacy local/wrapper vocabulary item, not a Sage 10.7 source surface; the replacement owner remains `Modules(R).Constructors()`.
- Confidence: High.
- Gaps: historical local deleted files and upstream Sage versions before 10.7 were not inspected in this reconciliation pass.

Cell-module factory ownership:

- Searched: `category_specs/modules/docs/SAGE_INVENTORY.md`; `sage/modules/with_basis/cell_module.py`; installed Sage categories and algebras for `def cell_module` and `cell_module(`.
- Found: `CellModule` is a module class, and `FiniteDimensionalAlgebrasWithBasis.ParentMethods.cell_module(mu, **kwds)` is the visible public factory. No generic module-category `cell_module` constructor was found.
- Conclusion: inference - cell-module construction is algebra-side, while the resulting cell module's module, form, radical, and simple-module methods map to cellular representation/form/quotient owners.
- Confidence: High.
- Gaps: cellular-algebra subclasses outside the searched installed categories/algebras may add specialized wrappers.

Ore module category source:

- Searched: `category_specs/modules/docs/SAGE_INVENTORY.md`; `sage/modules/ore_module.py`; installed `sage/categories/ore_modules.py`; recursive installed-source search for `class OreModules` and `OreModules(`.
- Found: contrary to the local inventory's negative finding, installed Sage 10.7 includes `sage/categories/ore_modules.py` with `class OreModules(Category_over_base_ring)`, and `OreModule.__classcall_private__` references `OreModules(base, twist)`.
- Conclusion: inference - the source-visible Sage category surface is present and must be included in future inventory updates; project ownership is still deferred because the mathematical owner name has not been chosen.
- Confidence: High.
- Gaps: the written Sage manual pages for Ore modules were not separately crawled in this pass.

Free-module element source visibility:

- Searched: Python import location for `sage.modules.free_module_element`; installed `sage/modules/free_module.py` element dispatcher; structural searches for dense vector class names recorded in the local inventory.
- Found: the installed tree exposes `sage/modules/free_module_element.cpython-312-x86_64-linux-gnu.so`, while readable Python source for the base element implementation and several dense vector classes is not present in this environment.
- Conclusion: inference - element-level reconciliation for dense vector internals must rely on visible dispatcher evidence, category element methods, and upstream Cython source acquisition if exact internal behavior is required.
- Confidence: High.
- Gaps: upstream `.pyx` source and generated Cython/C sources were not inspected.

## Converted Mapping Content

This file records the forward target mapping from Sage module surfaces into the local
category-spec hierarchy.

## Constructor Namespace

| Source surface | Target surface | Rationale |
| --- | --- | --- |
| `Modules(R).NamedModules()` | `Modules(R).Constructors()` | Sage constructors create module objects; they are not mathematical subcategories. |
| `FreeModule(R, n)` and `R^n` | `Modules(R).Constructors().FreeModule(n)` refined into `Modules(R).Free()` plus finite-rank and base-ring restrictions | The constructor is concrete; `Free` is an axiomatic restriction attachable to any module subcategory. |
| `CombinatorialFreeModule(R, basis_keys)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys)` refined into `Modules(R).Free()` and `Modules(R).WithOrderedGeneratingSet()` | Combinatorial free modules are a Sage constructor family for free modules with explicit basis keys, not a mathematical subcategory. |
| Plain-set Sage `S.algebra(R)` / `Sets().Algebras(R)` | `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)`, exposed by `S.free_module(R)` | Sage's existing path already constructs the free `R`-module with basis indexed by `S`. The spec routes that Sage source surface here instead of treating it as an algebra constructor. |
| `VectorSpace(K, n)` | `Modules(K).Constructors().VectorSpace(n)` refined into `Modules(K).Free().FiniteRank().OverField()` | Vector spaces are modules over fields with finite-rank structure when the constructor supplies a dimension. |
| Matrix presentations `f: R^m -> R^n` | `Modules(R).from_matrix(M)` delegating to `FinitelyPresentedModulesOverPID.from_matrix` | A matrix presentation defines `coker(f)`. Smith-form and elementary-divisor normalization are specific to finitely presented modules over PIDs, so the constructor namespace delegates to that subcategory owner. |
| `SubmoduleWithBasis`, free-module submodules, vector subspaces | `Modules(R).Subobjects()` / `Submodules` plus ordered-generating-set refinements | In module categories, subobjects are submodules. |
| Quotient modules and FGP modules | `Modules(R).Quotients()` plus finite-presentation/base-ring refinements | Quotients are construction categories attachable to arbitrary module subcategories. |
| Ring objects viewed as modules | `Modules(R).Constructors().RingObjectAsModule(...)` | The ring object supplies the module structure; ring-specific methods remain in `rings`. |
| Square `MatrixRing(R, n)` / `MatrixSpace(R, n, n)` viewed over `R` | The same parent refined into `Modules(R).Free().FiniteRank()` | A square matrix parent is a free finite-rank `R`-module on the matrix-unit basis. This is module structure on the same parent, not a second constructor family. |

Constructor signatures expose the finite Sage input casework as named methods instead
of mirroring Sage's positional dispatch. The canonical rank constructors stay named
`FreeModule(rank=...)`, `VectorSpace(dimension=...)`, and
`FreeQuadraticModule(rank=..., inner_product_matrix=...)`. The other documented Sage
paths are split into `FreeModuleWithBasisKeys`, `FreeModuleWithoutBasis`,
`FreeModuleWithInnerProductRows`, `FreeModuleWithInnerProductEntries`,
`VectorSpaceWithBasisKeys`, `VectorSpaceWithoutBasis`,
`VectorSpaceWithInnerProductRows`, `VectorSpaceWithInnerProductEntries`,
`FreeQuadraticModuleFromRows`, and `FreeQuadraticModuleFromEntries`. Sage's
`inner_product_ring` path is not public because the installed Sage source immediately
raises `NotImplementedError`.

`FPModule(arg0, ...)` splits into `FPModuleFromPresentation(algebra=...)`,
`FPModuleFromCokernelMap(defining_map=...)`, and
`FPModuleFromFreeGradedModule(module=...)`; `FPModule(algebra, generator_degrees, ...)`
is retained only for the presentation case. `IntegerLattice(basis, ...)` splits into
`IntegerLatticeFromBasisMatrix`, `IntegerLatticeFromBasisRows`, and
`IntegerLatticeFromOrderElement`. `TorsionQuadraticForm(q)` splits into matrix and
row-list routes, with the public Sage-compatible name reserved for the matrix case.
Quotient construction similarly splits Sage's `quotient_module` data shapes into
`quotient_by_submodule`, `quotient_by_generators`,
`quotient_by_relation_matrix`, and `quotient_by_relation_rows`.

Ring-as-module constructors mirror the ring constructor split: polynomial
`var_array` admits only one generator-count integer, power-series construction splits
univariate and multivariate routes, and Laurent/Puiseux series expose explicit
constructors from their underlying power/Laurent series rings. When upstream Sage
implements a surface with `*args` or `**kwds`, the spec does not mirror that plumbing
unless the written Sage documentation proves a genuinely open-ended mathematical input
family.

Integer-valued module data uses `Integer`, not `int | Integer`: ranks, dimensions,
tensor powers, tensor types, start indices, graded generator degrees, polynomial
variable counts, and series precisions. The constructor namespace may pass these values
to Sage factories, but the spec surface records the Sage mathematical type.

Type vocabulary should name mathematical objects, not implementation containers.
Generating sets, coordinate vectors, tensor symmetry data, and element-class hooks are
spelled directly as sequences, module elements, tuples, or element classes unless the
name introduces an independent mathematical noun such as `ModuleBasis` or
`Cardinality`.

Sage's `CombinatorialFreeModule(..., **kwds)` keyword bag is not copied as a project
constructor surface. The admitted constructor data is the basis-key set, optional
element class, optional category refinement, prefix, and names. Remaining Sage
keywords are display/provenance options for `IndexedGenerators` (`bracket`,
`latex_bracket`, `latex_names`, old monomial ordering aliases, `key`, and related
print controls). They are recovered through the Sage parent and its
`print_options(...)` API, not through category constructors; basis/order mathematics is
mapped to the basis and ordered-generating-set surfaces below.

## Square Matrix Parent Recovery

Sage's documented split is that rectangular matrix spaces lie in module-with-basis
categories, while square matrix spaces refine further to algebra-with-basis categories.
That algebra refinement does not remove the underlying free finite-rank `R`-module
structure on the square parent.

The project module owner rule is therefore:

| Module surface on a square matrix parent over `R` | Owner | Codomain consequence |
| --- | --- | --- |
| Rank, basis, basis order, coordinate vectors, `from_vector`, submodule and quotient-module structure, module homs | `Modules(R).Free().FiniteRank()` with the usual basis-bearing refinements | The codomain stays the same square matrix parent viewed as an `R`-module. |
| `row_space()` and `column_space()` | Ordinary free-module outputs over `R`, distinct from the square matrix parent itself | These remain separate free modules derived from the matrix parent; they do not replace the parent-as-module surface. |
| Ring multiplication, units, ring ideals | Not owned here | These remain in `rings` and `algebras`. |

Migration consequence: keep matrix-space linear methods in `modules`, including the
square case, and keep the smoke expectation that the square matrix parent refines into
`Modules(R).Free().FiniteRank()` simultaneously with its ring and algebra structure.

## Tensor Component Duals And Forms

`TensorAlgebraComponents(R).DualObjects()` owns integral forms.  If
`N = T_R(M)[p,q]`, then `N.dual()` is the tensor component `T_R(M)[q,p]`.  The
same object is naturally interpretable as `Hom_R(T_R(M)[p,q], R)`, so the hom
category supplies evaluation behavior rather than a separate form identity.

Use these names consistently:

| Surface | Meaning |
| --- | --- |
| `TensorAlgebraComponents(R).DualObjects()` / `dual()` | The dual-component category, a subcategory of `TensorAlgebraComponents(R)`. |
| `tensor_type()` | The tensor type of the object itself: `(p,q)` on `T_R(M)[p,q]`, `(q,p)` on its dual. |
| `Modules(R).HomCategory().Forms()` | Hom-layer interpretation for evaluation against the original component. |

Thus ordinary linear forms are dual tensor components of type `(0,1)`. Bilinear
forms are dual tensor components of type `(0,2)`.
Multiplication structure tensors are not forms on `T_R(M)[1,2]`; they are tensor
elements of type `(1,2)` constructed in `tensor_algebra_components`.

## Combinatorial Free Module Method Surface

`CombinatorialFreeModule` is not a project category. Its constructor builds a free
module with explicit basis keys, and its methods are evidence for existing or missing
mathematical surfaces. Each inventoried method must map independently.

| Sage method surface | Target surface | Rationale |
| --- | --- | --- |
| `rank()` / `dimension()` | `Modules(R).Free().rank()`; finite cases may also satisfy `Modules(R).Free().FiniteRank().dimension()` | The mathematical invariant is the cardinality of a basis. Sage's `dimension()` is a constructor-family alias for rank, not evidence for a `CombinatorialFreeModules` category. |
| `basis()` and `basis().keys()` | Free module basis data, with key access attached to the ordered/indexed basis surface | A basis is structure on a free module. The basis-key set is part of the chosen basis data, not a separate implementation category. |
| `monomial(i)` / `_monomial(i)` / `term(i, coeff)` | Basis-element and term constructors on a free module with a chosen indexed basis | These construct elements from basis indices and coefficients. They belong to the basis-bearing free-module surface, not to the Sage class name. |
| `_sum_of_monomials(indices)` / `sum_of_terms(terms, distinct=...)` | Finite linear-combination constructors for a basis-bearing free module | These are sparse element constructors from basis terms. They should be exposed only through explicit finite linear-combination vocabulary, not through a constructor-family category. |
| `from_vector(vector, order=..., coerce=...)` | Coordinate conversion for a free module with a chosen ordered basis | The operation depends on an ordered basis and a coordinate vector. It belongs with coordinate-vector conversion, not with the constructor that happened to create the module. |
| `set_order(order)` / `get_order()` / `get_order_key()` / `_order_key(x)` | Ordered-basis or term-order surface refining `Modules(R).WithOrderedGeneratingSet()` | Sage lets the chosen basis order drive coordinate and term operations. The project surface should state this as ordered basis data; private order-key helpers stay interop-local. |
| `change_ring(S)` | `Modules(R)` base-change surface, returning an object in `Modules(S)` with compatible free/basis refinements when valid | Base change is a module operation. The constructor family only supplies one implementation. |
| `zero()` | Additive identity inherited from the module/additive-monoid structure | This is not specific to free modules with basis keys. |
| `sum(iter_of_elements)` / `linear_combination(iter_of_elements_coeff, ...)` | No public category method unless the spec admits finite linear-combination constructors | The module laws already give addition and scalar multiplication. Sage implements parent-side aggregation for speed; that implementation detail is not itself mathematical structure. |
| `_element_constructor_`, `_convert_map_from_`, `_coerce_map_from_`, `_from_dict` | Coercion and element-construction interop | These are Sage parent internals. Public project mappings should expose the mathematical constructors above, not raw dictionary or coercion plumbing. |
| `construction()`, `__classcall_private__`, `__init__`, `element_class`, `_element_class`, representation hooks | Constructor/provenance or Python/Sage implementation internals | These surfaces record how Sage builds and displays the object. They are inventory evidence, but they are not mathematical category methods. |
| `is_exact()` | Exact-arithmetic capability predicate, not a module-category predicate | This belongs to a separate exact-computation policy if admitted. It should not be smuggled into module mathematics. |

Inherited `ModulesWithBasis` methods available on a `CombinatorialFreeModule` follow
the same rule:

| Sage method surface | Target surface | Rationale |
| --- | --- | --- |
| `basis()`, `rank()`, `dimension()`, `cardinality()`, `is_finite()` | Free-module and finite-set/cardinality surfaces | These are invariants of the module and its basis-key set. Finite cardinality belongs to set/enumerated-set structure, not to the Sage constructor family. |
| `gens()`, `gen(i)`, `basis()` iteration | `Modules(R).WithOrderedGeneratingSet()` plus basis-bearing free-module structure | These expose the chosen ordered generators or basis elements. |
| `module_morphism(...)` and hom-on-basis constructors | `Modules(R).HomCategory()` with ordered-basis construction helpers where admitted | A basis-defined map is a module homomorphism construction. The hom category owns the morphism object. |
| `submodule(...)`, `quotient_module(...)`, `intersection(...)` | `Modules(R).Subobjects()`, `Modules(R).Quotients()`, and subobject intersections | These are module subobject and quotient operations. Sage's inheritance from `CombinatorialFreeModule` is only implementation reuse. |
| `tensor(...)` and tensor element helpers | `Modules(R).TensorProducts()` | Tensor products are construction objects, not combinatorial-free-module subcategories. |
| `random_element(...)` | No mathematical category method unless a probability distribution is specified | Random sampling is computational API, not module structure. |
| Element coefficient access: `monomial_coefficients()`, `__getitem__`, `coefficient()`, `items()`, `support()`, `support_of_term()`, `monomials()`, `terms()`, `coefficients()` | Element coordinate/support surface for free modules with a chosen basis | These read the finite support of an element in a basis. They belong to the element surface for basis-bearing free modules. |
| Element predicates and size: `is_zero()`, `__len__()`, `length()` | Module element zero/support-size surfaces where mathematically meaningful | Zero is general module-element structure; support length depends on a chosen basis. |
| Leading/trailing term methods and `map_coefficients`, `map_support`, `map_support_skip_none`, `map_item` | Ordered-basis or term-order element surface; otherwise interop-local | These depend on an order or on implementation-level sparse support traversal. Admit only the mathematically stated ordered-basis cases. |

## Rank, Primitive Elements, And Divisibility Boundary

`rank()` is a parent method on `Modules(R).Free()`. Finite-rank free modules may also
expose `dimension()` as a basis-cardinality convention.

Do not admit a free-module element method named `divisibility()` from coordinate gcds,
chosen generators, or a putative divisor relation `v = a*w`. That premise is not a
source-grounded module definition here, and it must not be conflated with lattice/form
divisibility.

The generic module-element predicate `v.is_primitive()` is already routed through the
cyclic submodule inclusion `v.span().inclusion().is_primitive()`, i.e. through the
primitive morphism/submodule notion. It is not a unit-divisibility predicate unless a
later source-grounded proof establishes that equivalence under explicit hypotheses.

The sourced divisibility surface for formed elements belongs in the symmetric bilinear
forms subtree: for `b: M x M -> S`, `divisibility(v)` is the submodule
`<b(v, M)> <= S`; when `S = R`, this is an ideal of `R`.

`CombinatorialFreeModule_Tensor` and `CombinatorialFreeModule_CartesianProduct`
are implementation classes for tensor-product and cartesian-product construction
objects. Their factor accessors and structure maps map to
`Modules(R).TensorProducts()` and `Modules(R).CartesianProducts()`, respectively.
Their representation hooks remain Sage interop.

`SubmoduleWithBasis` and `QuotientModuleWithBasis` inherit from
`CombinatorialFreeModule` in Sage, but their mathematical ownership is subobject and
quotient structure: `Modules(R).Subobjects()` / ordered-generating-set refinements and
`Modules(R).Quotients()` / ordered-generating-set refinements. The inheritance is
implementation evidence only.

Basis-coordinate audit:

| Old or audited surface | Project surface | Rationale |
| --- | --- | --- |
| `Modules(R).WithBasis().linear_combination_of_basis(terms)` | unchanged on `Modules(R).WithBasis().ParentMethods` | A finite sum of indexed basis terms is genuine structure of a module equipped with a specified basis. |
| `Modules(R).WithBasis().cokernel_basis_indices()` | `Modules(R).Quotients().ParentMethods.cokernel_basis_indices()` | These are normal-form basis indices for a quotient/cokernel, not a property of every basis-bearing module. |
| `Modules(R).WithBasis().HomCategory().from_basis_map(f)` | unchanged on `WithBasis().HomCategory().ParentMethods` | A map from basis indices determines a unique module morphism from a basis-bearing domain. The hom object owns the resulting morphism construction. |
| `Modules(R).WithBasis().HomCategory().ElementMethods.on_basis()` | unchanged on `WithBasis().HomCategory().ElementMethods` | This reads the basis-index function determining a basis-defined morphism, so it belongs to the basis-refined hom surface. |

## Sage Wrapper Subcategory Migration Mapping

The old Sage-wrapper files are implementation evidence, not ownership evidence. A
method goes to the weakest mathematical category whose hypotheses make the method
meaningful. Constructor-only Sage families are routed through `Modules(R).Constructors()`
and then refined into those categories.

The mapping below is the phase-one owner table for the wrapper migration.

| Current wrapper | Sage evidence | Constructor owner | Mathematical method owner | Migration result |
| --- | --- | --- | --- | --- |
| `_CombinatorialFreeModules` | `CombinatorialFreeModule` | `Modules(R).Constructors().CombinatorialFreeModule(...)` | `Modules(R).Free()` plus a basis-bearing refinement; ordered APIs refine further to `WithOrderedGeneratingSet()` or an ordered-basis owner | Already deleted. Keep only constructor routing and method mapping. |
| `_FreeModulesWithStandardBasis` | `FreeModule_ambient*` | `FreeModule(R, n)` and `R^n` | finite-rank free modules with a chosen standard ordered basis | Deleted; methods moved to free, ordered-basis, subobject, and quotient owners. |
| `_FiniteRankFreeModules` | tensor-calculus `FiniteRankFreeModule` | `Modules(R).Constructors().FiniteRankFreeModule(...)` | `Modules(R).Free().FiniteRank()` plus tensor, dual, symmetric, exterior, hom, end, and aut construction owners | Deleted; constructor routes directly to `Free().FiniteRank()`. |
| `_FreeModulesOverIntegralDomains` | `FreeModule_generic_domain` | `FreeModule(R, n)` when `R` is an integral domain | `Modules(R).Free().OverIntegralDomain()` and its subobject owner | Deleted; methods moved to integral-domain and subobject owners. |
| `_FreeModulesOverPIDs` | `FreeModule_generic_pid` | `FreeModule(R, n)` when `R` is a PID | `Modules(R).Free().OverPID()`, `Modules(R).Quotients()`, and `FinitelyPresentedModulesOverPID` | Deleted; methods moved to PID and finite-presentation owners. |
| `_VectorSpaces` | `FreeModule_ambient_field` | `VectorSpace(K, n)` and `FreeModule(K, n)` for a field `K` | `Modules(K).OverField().Free().FiniteRank()` plus field-linear subobject and quotient owners | Deleted; methods moved to field/free/subobject/quotient owners. |
| `_RealDoubleVectorSpaces` | `RealDoubleVectorSpace_class` | `VectorSpace(RDF, n)` / `FreeModule(RDF, n)` | the RDF instance of the field-vector-space owner; numeric storage is interop-only | Deleted; coordinates moved to ordered-basis owners. |
| `_ComplexDoubleVectorSpaces` | `ComplexDoubleVectorSpace_class` | `VectorSpace(CDF, n)` / `FreeModule(CDF, n)` | the CDF instance of the field-vector-space owner; numeric storage is interop-only | Deleted; coordinates moved to ordered-basis owners. |
| `_VectorSubspaces` | `FreeModule_submodule_field` | `subspace(...)`, `span(...)`, `V.subspace(...)` | `Modules(K).OverField().Subobjects()` with ambient vector-space structure | Deleted; methods moved to subobject and field-linear owners. |
| `_VectorSubspacesWithOrderedGeneratingSet` | `FreeModule_submodule_with_basis_field` | `subspace_with_basis(...)` | field subobjects with chosen ordered basis/generating set | Deleted; methods moved to ordered-basis subobject owners. |
| `_VectorSpaceQuotients` | `FreeModule_ambient_field_quotient` | `V.quotient_module(W)` for vector spaces | `Modules(K).OverField().Quotients()` | Deleted; methods moved to quotient owners. |
| `_FreeModuleSubmodules` | `FreeModule_submodule_pid` | `M.submodule(...)` for PID free modules | `Modules(R).Free().OverPID().Subobjects()` | Deleted; methods moved to subobject and PID owners. |
| `_FreeModuleSubmodulesWithOrderedGeneratingSet` | `FreeModule_submodule_with_basis_pid` | `M.submodule_with_basis(...)` | PID free subobjects with chosen ordered basis/generating set | Deleted; methods moved to ordered-basis subobject owners. |
| `_SubmodulesWithOrderedGeneratingSet` | `SubmoduleWithBasis` | `M.submodule(...)` for modules with basis | `Modules(R).Subobjects()` refined by basis/ordered-generating-set structure | Deleted; methods moved to subobject and basis owners. |
| `_FreeModuleQuotients` | `QuotientModule_free_ambient` | `M.quotient_module(S)` and `M / S` for free modules | `Modules(R).Free().Quotients()` plus finite-presentation owners when the quotient has PID invariant data | Deleted; methods moved to quotient owners. |
| `_QuotientModulesWithOrderedGeneratingSet` | `QuotientModuleWithBasis` | `M.quotient_module(S)` for modules with basis | `Modules(R).Quotients()` refined by basis/ordered-generating-set structure | Deleted; methods moved to quotient and basis owners. |
| `_FinitelyGeneratedPIDQuotientModules` | `FGP_Module_class` | `FGP_Module(V, W)` and PID quotient syntax | `FinitelyPresentedModulesOverPID`, with torsion and finite refinements as axioms | Deleted; methods moved to `FinitelyPresentedModulesOverPID`. |
| `_FreeQuadraticModules` | `FreeQuadraticModule_*` | `FreeQuadraticModule(R, n, form)` and `QuadraticSpace(K, n, form)` | free modules with bilinear/quadratic form, with PID/field refinements where needed | Deleted; methods moved to forms-owned category surfaces. |
| `_IntegerLattices` | `IntegerLattice` and integral symmetric lattice classes | lattice constructors on `Modules(ZZ).Constructors()` | finite-rank free `ZZ`-modules with symmetric nondegenerate integral bilinear form; algorithmic reduction methods live on the lattice owner | Retained as a real integral-lattice category, not as a Sage-class wrapper. |
| `_TorsionQuadraticModules` | `TorsionQuadraticModule` | `TorsionQuadraticForm(...)` and discriminant-group constructors | finite torsion `ZZ`-modules with bilinear/quadratic form | Moved to `forms`; `Modules(R).TorsionQuadraticModules()` is a compatibility route. |
| `_FreeGradedModules` | `FreeGradedModule` | `FreeGradedModule(algebra, generator_degrees, ...)` | `Modules(A).Graded().Free()` plus basis-bearing refinements | Retained as a real graded-free category surface. |
| `_FinitelyPresentedGradedModules` | `FPModule` | `FPModule(...)` | `Modules(A).Graded().FinitelyPresented()` | Retained as a real graded finitely presented category surface. |
| `_OreModules` | `OreModule`, `OreSubmodule`, `OreQuotientModule` | `OrePolynomialRing(...).quotient_module(P)` and `OreModule(...)` | modules over the relevant Ore-polynomial algebra or a stated semilinear-operator category; coefficient-ring free-module behavior remains inherited | Retained as a real Ore-module category surface. |
| `_RepresentationModules` | `Representation_abstract` and subclasses | semigroup/group representation constructors | modules with an action of a specified semigroup/group/monoid and side | Retained as a real representation-module category surface. |
| `_RingObjectsAsModules` | ring objects exposing module structure | forgetful/constructor bridge from ring or algebra objects | ring methods stay in `rings`; module generators and structure maps live on a forgetful construction or objects-over/under surface | Retained as a real ring-object-as-module category surface. |

### Wrapper Candidate Classification

The recovered wrapper plan at
`plans/category_specs/modules/docs/SAGE_WRAPPER_MIGRATION_PLAN.md` requires every
Sage-wrapper candidate to be classified before deletion. This mapping pass fixes the
classification as follows.

| Classification | Wrapper candidates | Migration consequence |
| --- | --- | --- |
| Constructor-only interop shell | `_CombinatorialFreeModules`, `_FreeModulesWithStandardBasis`, `_FiniteRankFreeModules`, `_FreeModulesOverIntegralDomains`, `_FreeModulesOverPIDs`, `_VectorSpaces`, `_RealDoubleVectorSpaces`, `_ComplexDoubleVectorSpaces`, `_VectorSubspaces`, `_VectorSubspacesWithOrderedGeneratingSet`, `_VectorSpaceQuotients`, `_FreeModuleSubmodules`, `_FreeModuleSubmodulesWithOrderedGeneratingSet`, `_SubmodulesWithOrderedGeneratingSet`, `_FreeModuleQuotients`, `_QuotientModulesWithOrderedGeneratingSet`, `_FinitelyGeneratedPIDQuotientModules` | These wrapper categories are deleted. Exact Sage implementation classes may still be matched at constructor interop boundaries, but public methods route through the constructor, subobject, quotient, basis, ordered-basis, PID, field, hom, tensor, and finite-presentation owners listed above. |
| Forms-owned owner | `_FreeQuadraticModules`, `_TorsionQuadraticModules` | Free quadratic modules and torsion quadratic modules are not module-wrapper categories. Their Gram, bilinear, quadratic, evenness, genus, and orthogonal-group surfaces route through formed-module owners and their aut categories; module paths remain only constructor or compatibility routes. |
| Lattice-owned owner | `_IntegerLattices` | The retained surface is a real integral-lattice/form category: finite-rank free `ZZ`-modules with integral symmetric nondegenerate bilinear form. Reduction, enumeration, gluing, dual, discriminant, and genus methods are lattice-specific surfaces, not generic module methods. |
| Real module-category owner | `_FreeGradedModules`, `_FinitelyPresentedGradedModules`, `_OreModules`, `_RepresentationModules`, `_RingObjectsAsModules` | These retained names describe mathematical module categories or forgetful module surfaces. They are not deletion targets, and their methods stay on graded, Ore, representation, or ring-object-as-module owners with inherited ordinary module behavior. |

Unresolved-owner check:

- Searched: the recovered wrapper plan's class todo list, the current wrapper mapping
  table above, `category_specs/modules/docs/SAGE_INVENTORY.md`, and exact wrapper-name
  matches in `category_specs/modules`.
- Found: no active wrapper candidate is assigned to an unresolved-owner bucket in this
  mapping; deleted wrapper names remain in mapping/provenance docs, while retained code
  names are exactly the real-category rows listed above.
- Conclusion: inference - the wrapper migration mapping has no known unresolved
  candidate classification left for this leaf.
- Confidence: Medium.
- Gaps: this is a documentation and source-map audit, not a fresh exhaustive Sage
  source re-inventory or implementation smoke run.

### Required Immediate Category Owners

The migration needs these mathematical owners before constructors are fully rewired:

| Owner | Role |
| --- | --- |
| `Modules(R).WithBasis()` | Modules equipped with a specified basis. This is the owner for `basis`, basis-key access, monomial/term constructors, support in a basis, and basis-defined morphisms. |
| `Modules(R).WithOrderedBasis()` | Basis-bearing modules whose basis has a specified order. This refines `WithBasis()` and `WithOrderedGeneratingSet()` and owns coordinate vectors, ordered support, leading/trailing term operations, and basis matrices whose row order is meaningful. |
| `C.WithBasis().Subobjects()` / `C.WithOrderedBasis().Subobjects()` | Subobjects equipped with chosen bases or ordered bases, including `SubmoduleWithBasis`, vector subspaces with basis, and PID free submodules with user bases. The construction order uses Sage's covariant machinery so these categories are automatically subcategories of both `C.Subobjects()` and the corresponding basis-bearing category. |
| `C.WithBasis().Quotients()` / `C.WithOrderedBasis().Quotients()` | Quotients equipped with chosen normal-form bases, including `QuotientModuleWithBasis`. The construction order keeps quotient structure functorial over the basis-bearing parent category. |
| `Modules(R).Free().FiniteRank().OverField()` | The vector-space owner for finite-dimensional vector spaces over a field. |
| `Modules(R).Free().OverIntegralDomain()` | The owner for free-module operations requiring an integral domain, including intersection and saturation. |
| `Modules(R).Free().OverPID()` | The owner for free-module operations requiring a PID, including quotient construction and index computations. |
| `FormedModules(R).Bilinear()` / `Modules(R).WithForms().Bilinear()` | Modules equipped with a bilinear form; the class lives in `forms`. |
| `FormedModules(R).Quadratic()` / `Modules(R).WithForms().Quadratic()` | Modules equipped with a quadratic form; the class lives in `forms`. |
| `C.AutCategory().Of(M)` for a form-bearing module category `C` | The orthogonal group of `(M, form)`: automorphisms of `M` in `C`, equivalently module automorphisms that preserve the form. This owner covers integral lattices, rational formed modules, degenerate formed modules, and finite discriminant forms. |
| `Modules(ZZ).Free().FiniteRank().WithForms().Bilinear().Integral().Nondegenerate()` | The forms-owned ambient chain for integral lattices; `lattices` adds the named `Lattice` endpoint. |
| `FinitelyPresentedModulesOverPID(...).Torsion().WithForms().Quadratic()` | The forms-owned finite quadratic module owner for torsion quadratic modules and discriminant groups. |
| `Modules(A).Graded().Free()` | Free graded modules over a graded algebra `A`. |
| `Modules(A).Graded().FinitelyPresented()` | Finitely presented graded modules over a graded algebra `A`. |
| `Modules(R).WithAction(S, side)` | Representation modules: modules over `R` equipped with a specified action of `S` on the given side. |
| `Modules(R).WithOreOperator(...)` or `Modules(OreAlgebra).FiniteRankFree()` | Ore modules, depending on whether the admitted mathematical owner is semilinear-operator data or modules over the Ore algebra. |

### Method Mapping Rules

The same Sage implementation class can expose methods owned by several mathematical
categories. The migration should map each Sage method to a project method signature:
where the project method is defined, its inputs, its hypotheses, and its return type.
Construction categories describe output structure or extra methods on constructed
objects; they do not by themselves determine where an operation is called.

For root module construction signatures, use the tracked spec
`[[SPEC-MODULE-ROOT-METHOD-OWNERSHIP-MAPPING]]`.

| Method group | Project mapping |
| --- | --- |
| `rank`, `dimension`, basis cardinality | `Modules(R).Free()` for rank as basis cardinality; finite-dimensional aliases belong to finite-rank or field-vector owners. |
| `basis`, `basis().keys()`, `monomial`, `term`, `from_vector`, `linear_combination_of_basis` | `WithBasis()`; ordered coordinate variants belong to `WithOrderedBasis()`. |
| `gens`, `gen`, `ngens` | `WithOrderedGeneratingSet()` unless the methods assert basis coordinates, in which case `WithOrderedBasis()`. |
| element `list`, `vector`, `support`, coefficient lookup, leading/trailing term methods | basis or ordered-basis element surfaces; not generic module elements. |
| `degree`, coordinate-ring bookkeeping, dense/sparse conversion, representation hooks, `_sympy_`, `_magma_init_`, `_macaulay2_` | interop or representation details unless a mathematical invariant is explicitly stated. |
| `linear_combination`, parent `sum`, random elements | generic computational helpers; no public category method unless the spec states finite-linear-combination or probability-distribution structure. |
| `submodule`, `submodule_with_basis`, `span`, `zero_submodule` | Construction methods called on an ambient module `M`; they return submodules of `M`. Basis/order/PID/field hypotheses refine the signature and output subobject structure. |
| Submodule comparison and ambient/lift/retract methods | Methods on subobject or ambient-bearing module objects. They require a specified inclusion or ambient relation, not just an abstract module isomorphism. |
| `intersection`, `saturation`, `denominator`, `index_in` | Methods on submodules of a common ambient module, with free/integral-domain/PID hypotheses where the operation or algorithm requires them. |
| `quotient_module`, `__truediv__`, `quotient_abstract`, quotient matrices | Construction methods called on an ambient module `M` with submodule data `N <= M`; they return `M/N`. Field/free/PID/finite-presentation/basis hypotheses refine the signature and output quotient structure. |
| `cover`, `relations`, `free_cover`, `free_relations`, `quotient_map`, `lift_map`, `lift`, `retract` | quotient or subquotient construction owners; `lift`/`retract` for submodules belong to `Subobjects()`. |
| `cokernel_basis_indices` | quotient owners with basis or PID normal-form hypotheses. |
| Smith-form data, `invariant_factors`, `invariants`, `smith_form_gens`, `free_part`, `torsion_part`, `annihilator`, element order | `FinitelyPresentedModulesOverPID` and its torsion/finite refinements. |
| `hom`, `_Hom_`, `module_morphism`, morphism from basis/images/matrices, `on_basis` | the relevant `HomCategory()`; basis-defined constructors refine through `WithBasis().HomCategory()`. |
| `tensor`, `tensor_module`, tensor constructors, tensor factors | Tensor construction methods are called on modules with compatible base/sidedness data and return tensor-product modules; tensor-product objects may have additional factor/construction methods. |
| `dual`, `linear_form`, `alternating_form`, symmetric and exterior powers | `dual()` is called on the module whose dual is being constructed. Linear-form, symmetric, and exterior surfaces require explicit finite-rank/free/projective and sidedness hypotheses before placement. |
| `determinant`, `discriminant`, `gram_matrix`, `inner_product_matrix`, `inner_product`, quadratic product | forms-owned bilinear/quadratic module owners. |
| `is_symmetric`, `is_alternating`, `is_nondegenerate`, `is_integral`, `is_even` | forms-owned axiom owners, not constructor wrappers. |
| lattice reduction and enumeration: `LLL`, `BKZ`, `HKZ`, `shortest_vector`, `voronoi_cell`, `closest_vector`, `babai` | integral-lattice algorithm surface, not generic modules or generic free modules. |
| lattice constructions: `dual_lattice`, `discriminant_group`, `orthogonal_complement`, `overlattice`, `genus` | integral-lattice and finite-quadratic-module owners. |
| `orthogonal_group` / `automorphisms` for a formed module `(M, b)` or `(M, q)` | `C.AutCategory().Of(M)` where `C` is the relevant forms-owned category. The group is `Aut_C(M)`, not a generic Sage group anchor. Lattice and discriminant-form orthogonal groups are specializations of this aut surface; matrix-group, finite-generation, and finite-presentation realizations are later refinements. |
| graded data: `generator_degrees`, homogeneous `basis`, `degree`, `connectivity`, `suspension`, `minimal_presentation`, `resolution` | graded free or graded finitely presented owners. |
| Ore data: `ore_ring`, `twisting_morphism`, `twisting_derivation`, `pseudohom`, Ore matrix, morphism restriction/corestriction/quotient | Ore-algebra or semilinear-operator owner; ordinary free-module operations remain inherited from free finite-rank modules. |
| representation data: `semigroup`, `side`, `representation_matrix`, `character`, invariant/twisted invariant modules, subrepresentation, quotient representation, tensor/exterior/symmetric/Schur functors | parameterized representation-module owner and its subobject, quotient, tensor, exterior, symmetric, and Schur construction owners. |
| ring-as-module data: `structure_ring`, `structure_map`, `module_generators` | forgetful construction from rings/algebras to modules or objects-over/under structure; ring operations remain in `rings`. |

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
| Sage-backed module family surface | Constructor namespace plus mathematical subcategory files only where the family expresses a genuine category restriction. Constructor-only Sage families refine into existing module categories. |

## Construction-Category Mapping

| Sage surface | Target surface | Rationale |
| --- | --- | --- |
| `Modules(R).Homsets()` | `Modules(R).HomCategory()` in `modules/homsets.py` and top-level `homsets/` | Module hom categories have objects `Hom_R(M, N)`, the sets of `R`-linear maps. Sage makes those hom objects modules over `R` and gives the parent method `zero()`. |
| `Modules(R).Endsets()` / `Modules(R).Homsets().Endset()` | `Modules(R).EndCategory()` plus generic `Modules(R).HomCategory().EndCategory()` | Module end categories have objects `End_R(M) = Hom_R(M, M)`. Sage's `Modules.Homsets.Endset` adds magmatic-algebra structure over `R`, so the project declares `End_R(M)` as an `R`-algebra in addition to the generic end-category structure. |
| Sage/project automorphism surfaces | `Modules(R).AutCategory()` with module specialization | `Aut_R(M)` is the invertible part of `End_R(M)`. The root hom category layer owns the aut-category construction; `modules/homsets.py` declares only module-specific names and extra structure. |
| Orthogonal groups of modules with forms | `C.AutCategory().Of(M)` for `C <= FormedModules(R)` | `O(M,b)` is the automorphism group in the category of modules carrying the form. `Modules(R).WithForms()` remains the Sage-compatible spelling, but `forms` owns the category surface. This definition does not require nondegeneracy or a matrix realization; those hypotheses only refine algorithms and concrete presentations. |
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

For `Modules(R).ObjectsOver(M)` and `Modules(R).ObjectsUnder(M)`, the module subtree
owns `structure_module()` and the module morphism `structure_map()`. The old local
`structure_domain()` and `structure_codomain()` methods move to the Cat-owned universal
structure-morphism surface via `structure_morphism().domain()` and
`structure_morphism().codomain()`.

## Hom-Category Extra-Structure Decision

`R-Mod` is the first concrete model for hom/end/aut extra structure. The generic layer
declares that `Modules(R).HomCategory()`, `Modules(R).EndCategory()`, and
`Modules(R).AutCategory()` have objects `Hom_R(M, N)`, `End_R(M)`, and `Aut_R(M)`.
The module subtree additionally declares that `Hom_R(M, N)` is an `R`-module and
`End_R(M)` is an object of `Algebras(R)`, retaining Sage's `MagmaticAlgebras(R)`
supercategory for upstream compatibility. Aut-category construction still comes from
the generic layer because `Aut_R(M)` is defined by invertibility inside `End_R(M)` and
dispatched through the module end category.

For `C <= FormedModules(R)`, preservation of form data is not a separate module-local
boolean predicate. The object `C.HomCategory().Of(M, N)` owns the containment check for
candidate module morphisms, and isometry is isomorphism inside that formed-module Hom
object. In the endomorphism case, `C.AutCategory().Of(M)` is the orthogonal group.
Matrix criteria are implementation witnesses only after a presentation has been fixed.

## Dual Objects As Hom Objects

`Modules(R).DualObjects()` owns linear dual modules. For an object `M in Modules(R)`,
the mathematical meaning is

```text
M^* = Hom_R(M, R).
```

The public construction surface is therefore `M.dual()` as an object lying in
`Modules(R).DualObjects()`, but the category-theoretic content must route through the
module hom layer. The dual object is simultaneously:

- a dual object in `Modules(R).DualObjects()`;
- a hom object in `Modules(R).HomCategory()` with codomain the rank-one module `R`;
- an `R`-module, through the module-hom extra structure.

The implementation target in `subcategories/constructions/dual_objects.py` is to keep
the extra-supercategory chain routed through `Modules(R).HomCategory()`, specifically
the linear integral form surface, instead of shortcutting directly to `Modules(R)`.
This preserves the fact that elements of `M^*` are both module elements and morphisms
`M -> R`.

Migration consequences:

- `RModule.dual()` is a named construction into `Modules(R).DualObjects()`, not a
  separate forms-local helper.
- the dual of a morphism `f: A -> B` belongs to
  `Modules(R).HomCategory().ElementMethods` as `f.dual(): B^* -> A^*`;
- public type aliases for `DualModule` and dual elements must point to the
  `DualObjects` method surfaces, not to plain `RModule` aliases;
- tensor-component duals and semilinear form data may refine the form object attached
  to a module, but they do not replace the module-level linear dual owner. No separate
  `TwistedForms` category is admitted unless the forms mapping records a concrete
  public surface that cannot be expressed through `FormedModules(R)`,
  tensor-component duals, and Hom-category structure.

## Topological Modules

Topological module structure should inherit the topological-space surface from
`topological_spaces`, the module surface from `modules`, and any ring topology from
`rings`. It should not duplicate topological-space methods locally.

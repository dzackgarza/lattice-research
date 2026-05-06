---
id: SPEC-MAPPING-CAT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track cat mapping spec
status: needs-review
priority: critical
requirement: Convert category_specs/cat/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  category-object, Hom, End, Aut, and construction signatures.
acceptanceCriteria:
- Source paths category_specs/cat/docs/MAPPING.md and category_specs/cat/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 80
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Cat Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/cat/docs/MAPPING.md`.

Source inventory: `category_specs/cat/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.
- When a public method has a convention likely to surprise a mathematically literate user,
  its defining docstring must include a diagnostics paragraph naming the condition, the
  convention, and the adjacent method or object that carries the other common meaning.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/cat/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/category.py`
  - `sage/categories/category_singleton.pyx`
  - `sage/categories/category_with_axiom.py`
  - `sage/categories/category_types.py`
  - `sage/categories/objects.py`
  - `sage/categories/homsets.py`
  - `sage/categories/homset.py`
  - `sage/categories/functor.pyx`
  - `sage/categories/pushout.py`
  - `sage/categories/covariant_functorial_construction.py`
  - `sage/categories/subobjects.py`
  - `sage/categories/quotients.py`
  - `sage/categories/subquotients.py`
  - `sage/categories/cartesian_product.py`
  - `sage/categories/isomorphic_objects.py`
  - `sage/categories/dual.py`
  - `sage/categories/tensor.py`
- Source-visibility gaps from inventory tokens requiring follow-up during completeness audit:
  - `sage/sets/__init__.py`
  - checked construction modules are exposed directly as `sage/categories/*.py`,
    not through `sage/categories/constructions/`; see the Cat core negative finding
    below for the search record.
  - checked local slice/coslice selectors remain project-owned construction surfaces;
    see the Cat core negative finding below for the `objects_over.py` and
    `objects_under.py` source search.
- Reconciled source-path corrections:
  - This install exposes
    standard construction classes directly as `sage/categories/subobjects.py`,
    `sage/categories/quotients.py`, `sage/categories/subquotients.py`, and
    `sage/categories/cartesian_product.py`.
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the Cat core
  method reconciliation is recorded in `Completeness Reconciliation: Cat Core` below,
  with remaining gaps routed through `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Converted Mapping Content

This file maps Sage's category and functor machinery to the project `Cat()` subtree.

## Category Objects

Sage `sage.categories.category.Category` instances are the objects of `Cat()`.
For `C = Cat()`, the membership check `X in C` means exactly that `X` is a category
object. A functor is not an object of `Cat()`; it is an element of a functor homset
`A.Hom(B)`.

Consequences:

- Every project top-level category and subcategory should satisfy `C in Cat()`.
- Every category object should get shared category-object operations from
  `Cat.ParentMethods`.
- A homset category is itself a category object, so no separate object-membership
  rule is needed for functor categories.

## Category Order

Sage `Category.is_subcategory(self, c)` is the canonical subcategory relation.

Mapping:

- `C.leq(D)` means `C.is_subcategory(D)`.
- `C.geq(D)` means `D.is_subcategory(C)`.
- `C <= D` and `C >= D` are shorthands for the same relation.
- `Cat().join([C, D, ...])` delegates to Sage `Category.join`.
- `Cat().meet([C, D, ...])` delegates to Sage `Category.meet`, except that the empty
  meet returns `Cat().Constructors().EmptyCategory()`.

This follows Sage's own meaning: `C.is_subcategory(D)` asserts that there is a
natural forgetful functor from `C` to `D`. The comparison shorthands are specified
for ordinary category objects only; `Cat()` itself is the root ambient category in
this spec and does not re-export `leq`, `geq`, `<=`, or `>=`.

## Uniform Category-Object Surface

`Cat.ParentMethods` is the single source of truth for operations every category
object should expose:

- `HomCategory()` / `EndCategory()` / `AutCategory()` for category-level hom, end,
  and aut constructions;
- `Hom(D)` for the object-level functor homspace in `Cat`;
- `leq`, `geq`, `<=`, and `>=` for the Sage category order between ordinary
  category objects;
- containment hooks for categories that need object and morphism membership:
  `_sage_super_categories`, `_sage_object_classes`, and `_sage_morphism_classes`.

Wrapped category instances receive ordinary category-object methods through Sage's
generated classes. The wrapper base layer in `base_category_types.py` is the only
place that flattens `UniversalSubcategoryMethods` into Sage's `SubcategoryMethods`
provider path.

Direct `Hom` ownership is intentionally narrow:

- if `A, B in Cat()`, then `A.Hom(B)` is the object-level functor homspace
  `Hom_{Cat}(A, B)`;
- `A.HomCategory()` is the category-level hom-category construction over objects of
  `A`;
- lower subtrees may refine `HomCategory`, `EndCategory`, and `AutCategory`, but they
  must not define a direct `Hom` method on category objects that changes the meaning
  of `A.Hom(B)` for category objects.

The migration rule is: a subtree-local direct `Hom` method that constructs set maps,
module homomorphisms, ring homomorphisms, continuous maps, or other specialized
morphisms belongs on the subtree hom-category surface, not on the category object
itself. Put such constructors on the relevant `HomCategory().ParentMethods`,
`EndCategory().ParentMethods`, `AutCategory().ParentMethods`, or the concrete
`HomCategory().Of(A, B)` parent. Existing `HomCategory = ...` assignments and nested
`class HomCategory(...)` refinements are admissible when they specialize the
category-level hom construction rather than shadowing `A.Hom(B)`.

As of the 2026-05-04 shadowing audit, direct `def Hom` definitions under
`category_specs/` occur only in `cat/__init__.py` and `cat/base_category_types.py`.
Future lower-subtree direct `Hom` definitions should be filed as implementation
refactor work with this mapping section as the owner/migration source.

## Global Category Diagnostics

The category framework must expose one global diagnostic flag and one category-system
diagnostic logger. The flag is disabled by default. Enabling it must not change return
values, dispatch, containment, coercion, or category refinement; it only permits
background diagnostic messages for conventions that are mathematically correct but easy
to misread.

The diagnostic surface is framework-owned rather than subtree-owned. The concrete API
may be a small `category_specs.cat.diagnostics` module or an equivalent Cat-root
configuration object, but there must be a single source of truth for:

- reading whether category diagnostics are enabled;
- enabling or disabling category diagnostics for the process;
- emitting a category diagnostic message through the category logger;
- silencing or filtering repeated diagnostics without changing mathematical behavior.

Diagnostic messages are appropriate for surprise boundaries such as:

- two standard mathematical meanings sharing a name in nearby software conventions;
- a compatibility spelling whose result is not the object a user might infer from the
  spelling alone;
- inherited Sage behavior that is being preserved as interop evidence, not as a
  mathematical adequacy standard;
- convention-dependent identifications, such as a transported structure that only exists
  after nondegeneracy, freeness, a selected basis, a selected ordering, or another
  recorded hypothesis.

The motivating example is the lattice/module dual boundary. If an implementation
supports a lattice-side compatibility spelling such as `L.dual()`, then for a
degenerate symmetric bilinear object such as a rank-one isotropic sublattice
`L = <e>` inside a hyperbolic plane, diagnostics should be able to warn that the
returned metric dual `L^#` is not the Hom dual `Hom_R(L, R)`. The Hom dual is the
evaluation-bearing dual object; the metric dual is a formed-module construction that
becomes comparable to the Hom dual only through explicit form-induced transport under
the stated hypotheses.

Diagnostic messages are not an error-recovery mechanism. Missing hypotheses,
ill-defined mathematics, failed containment, invalid source grounding, or an
implementation gap should still fail, block the affected spec leaf, or route to a
tracked decision according to the workflow rules.

Any method whose implementation should emit such a diagnostic must say so in the method
definition docstring. The docstring should include:

- the exact condition under which diagnostics should emit;
- the mathematical convention being used;
- the common but different interpretation the user may have expected;
- the method, category, or object that carries that other interpretation when it exists.

## Containment

For an arbitrary category object `C`, `X in C` may mean either:

- `X` is an object of `C`; or
- `X` is a morphism in `C`.

For `C = Cat()`, this specializes to category-object membership only. Functor
membership is expressed by the relevant homset:

- `F in A.Hom(B)` for functors `A -> B`;
- `F in A.Hom(A)` for endofunctors of `A`;
- autofunctors are the invertible elements of `A.Hom(A)`.

## Functors

Sage `Functor` instances are morphisms between category objects.

The project surface records Sage's functor call model:

- `_coerce_into_domain(x)`;
- `_apply_functor(x)`;
- `_apply_functor_to_morphism(f)`;
- `__call__(x)` dispatching through those hooks;
- `domain()` and `codomain()`.

Sage construction functors from `sage.categories.pushout` are still actual functors,
but their extra Sage surface is recorded separately: `pushout`, `merge`, `commutes`,
`expand`, `common_base`, and `coercion_reversed`.

This is distinct from Sage `FunctorialConstructionCategory` classes such as
`SubobjectsCategory` or `QuotientsCategory`. Those are category objects produced by
methods like `C.Subobjects()`, not functors with domains, codomains, and object/morphism
actions.

Sage provides no general computable fixed-point operation for arbitrary endofunctors,
so `fixed_points()` is not a Cat-level functor method surface.

## Standard Constructions

Sage functorial construction categories map directly to category-object methods.  A
selector such as `C.HomCategory()` evaluates the corresponding construction functor at
`C`; the return value is the category object `Hom_C`.

| Sage class | Project method | Local file |
| --- | --- | --- |
| `SubobjectsCategory` | `C.Subobjects()` | `subcategories/constructions/subobjects.py` |
| `QuotientsCategory` | `C.Quotients()` | `subcategories/constructions/quotients.py` |
| `SubquotientsCategory` | `C.Subquotients()` | `subcategories/constructions/subquotients.py` |
| `CartesianProductsCategory` | `C.CartesianProducts()` | `subcategories/constructions/cartesian_products.py` |
| `TensorProductsCategory` | `C.TensorProducts()` where tensor products are defined | `subcategories/constructions/tensor_products.py` |
| `DualObjectsCategory` | `C.DualObjects()` where dual objects are defined | `subcategories/constructions/dual_objects.py` |
| `IsomorphicObjectsCategory` | `C.IsomorphicObjects()` where isomorphic-object transport is defined | `subcategories/constructions/isomorphic_objects.py` |
| Local slice construction | `C.ObjectsOver(T)` | `subcategories/constructions/objects_over.py` |
| Local coslice construction | `C.ObjectsUnder(T)` | `subcategories/constructions/objects_under.py` |
| `HomsetsCategory` | `C.HomCategory()` | `homsets.py` |
| `HomsetsCategory.Endset()` | `C.EndCategory()` | `endsets.py` |
| `HomsetsCategory.Autset()` | `C.AutCategory()` | `autsets.py` |
| `JoinCategory` | `Cat().JoinCategories()` containment | `join_categories.py` |

The universal selectors for `Subobjects`, `Quotients`, `Subquotients`,
`ObjectsOver`, `ObjectsUnder`, and `CartesianProducts` live in
`universal_subcategory_methods.py`. Other standard construction names, such as
`TensorProducts()` and `DualObjects()`, are exposed by the subtrees where the
mathematics is available. Individual category classes still declare their construction
classes, and Sage's `category_of(...)` machinery resolves the specific construction
for the receiver.

For wrapped ordinary category objects, `C.Hom(D)` delegates to Sage's parent homspace
for functors `C -> D`. The category-level construction is `C.HomCategory()`. The
object-level endomorphism functor space is `C.Hom(C)`.

For `Cat()`, `Subobjects` means subcategories, `Quotients` means quotient
categories, `Subquotients` means category-level subquotients, and
`CartesianProducts` means product categories.

## Constructor Aggregation Forwarders

`Cat().Constructors()` is an aggregator over already-scoped constructor namespaces.
The generated forwarding methods in `base_category_types.py` may use Python
`*args`/`**kwargs` internally because they do not define a mathematical constructor
surface. They forward to the owning constructor method, whose signature remains the
single public source of truth.

Mapping rule:

| Implementation hook | Public owner | Consequence |
| --- | --- | --- |
| `_cat_constructor_forwarder(...).forwarded_constructor(self, *args, **kwargs)` | The target subtree constructor, e.g. `Rings().Constructors().PolynomialRing(...)` or `Modules(R).Constructors().FreeModule(...)` | Allowed only as generated private forwarding glue. Do not treat the generated Cat method as evidence that a broad public variadic constructor is admitted. |
| `_CatObjectMixin.__init_subclass__(cls, **kwargs)` and the local `initialize_and_register(self, *args, **kwargs)` wrapper | Python/Sage subclass initialization plumbing | Not a category-spec method surface. The wrapper exists to register constructor owners after Sage/Python initialization and does not create mathematical input casework. |

## Slice and Coslice Categories

Sage does not provide a dedicated installed class for categories over or under a
fixed category in the same way it provides `SubobjectsCategory` and
`QuotientsCategory`. The local mapping is:

- `C.ObjectsOver(T)` means categories `D` equipped with a structure functor
  `D -> T`;
- `C.ObjectsUnder(T)` means categories `D` equipped with a structure functor
  `T -> D`;
- `Slice = ObjectsOver`;
- `Coslice = ObjectsUnder`.

These classes use Sage's `RegressiveCovariantConstructionCategory` plus
`Category_over_base`, so they follow the same `category_of(...)` entry point as
Sage's built-in regressive constructions.

Objects in any slice or coslice construction expose the universal structure-morphism
surface:

- `structure_morphism()` returns the distinguished morphism into or out of the fixed
  object;
- `structure_domain()` is `structure_morphism().domain()`;
- `structure_codomain()` is `structure_morphism().codomain()`.

Set, topological-space, and other lower categories may keep local names such as
`structure_map()` or `structure_functor()` for the category-specific morphism type,
but they do not restate `structure_domain()` or `structure_codomain()`.

## Hom, End, and Aut Categories

`CatHomCategory` is the category of functor categories internal to `Cat()`.  The
functorial construction is `Hom_*: Cat -> Cat`, which sends a category `C` to the
category object `Hom_C`.

Mapping:

- `C.HomCategory()` is the category-level functorial construction whose objects are
  `Hom_C(A, B)` for objects `A, B` of `C`;
- `C.HomCategory().Of(A, B)` is `Hom_C(A, B)`;
- `Cat().HomCategory()` is therefore the category of functor categories;
- `A.Hom(B)` returns Sage's `Hom(A, B, category=Cat())` parent when `A` and `B`
  are category objects;
- `A.Hom(B).category()` is `Cat().HomCategory()`;
- `A.Hom(A)` is the object-level endofunctor parent;
- hom elements are Sage `Functor` instances;
- Sage `ConstructionFunctor` instances have a specialized functor method surface; they
  are not the same object as the construction-category value `Hom_C`.

The repository-level `homsets/` subtree owns generic hom/end/aut vocabulary such as
`domain`, `codomain`, `EndCategory`, and `AutCategory`. The Cat subtree adds only the
functor-specific element surface and the `CatHomCategory`, `CatEndCategory`, and
`CatAutCategory` refinements. These live in separate files:
`cat/homsets.py`, `cat/endsets.py`, and `cat/autsets.py`.

## Constructors

`Constructors` is a plain collection class. A category opts in by defining a
`Constructors` collector that advertises named constructors for objects it owns or
constructs and then refines into its hierarchy. The collector is not a category, not a
functorial construction, and not a subcategory namespace.

`Cat().Constructors()` owns category-object constructor entry points and constructor
collection. It currently exposes:

- `EmptyCategory()`: the bottom category object used by `Cat().meet([])` and by any
  surface that needs the empty category as a category object.

It also exposes constructor discoverability without moving constructor ownership. There
is no public registration call and no separate aggregate object. The declaration is the
existence of an explicit nested `Constructors` class on a category object. During Cat
object initialization, backend code inspects that class and installs deterministic
prefixed forwarding methods on `Cat.Constructors`.

Prefixed names are the category prefix and constructor method name joined by an
underscore. A category-local constructor name must not repeat the category noun in a
`category_from_*` pattern: use `C.Constructors().from_xyz(...)`, so Cat exposes
`cat_prefix_from_xyz(...)`. For example, `Posets().Constructors().from_digraph(...)`
is exposed as `Cat().Constructors().posets_from_digraph(...)`. These methods forward
to the original category-owned constructor collector; they do not move constructor
ownership to `Cat`.

Constructor placement is a style boundary in this spec. Prefer explicit top-level
category collectors because they are easy to audit and collect. Do not enforce that
preference with runtime guards whose only effect is to reject proper subcategories; a
future registered subcategory collector may be valid if it is a deliberate opt-in
surface.

Ordinary category objects are registered by being Sage/project `Category` instances.
Functors are registered by being Sage `Functor` or `ConstructionFunctor` instances and
by lying in the relevant functor homset.

## Completeness Reconciliation: Cat Core

This pass checked the local inventory, the converted mapping body, and the installed
Sage 10.7 category source files listed in the source ledger.

- `Category.__contains__` tests whether `x.category()` is a subcategory of the
  receiver, while `Category.category()` returns `Objects()` for Sage category
  instances. The project `Cat()` membership rule is therefore a deliberate refinement
  of Sage's category-object runtime fact: category instances are the project objects
  of `Cat()`, while arbitrary Sage objects continue to live in their mathematical
  categories such as `Sets()`, `Rings()`, or `Modules(R)`.
- `Category.is_subcategory(self, c)` is source-backed as the category order, with the
  mathematical meaning "there is a natural forgetful functor from `self` to `c`".
  The spec mapping of `leq`, `geq`, `<=`, and `>=` is therefore an order surface on
  category objects, not a morphism-construction surface.
- `Category.join(categories, ...)` is source-backed as Sage's category-lattice join.
  Sage treats the empty join as `Objects()`, so the local `Cat().join([])` behavior
  should remain top-category behavior unless an explicit project decision changes the
  order convention.
- `Category.meet(categories)` is source-backed as Sage's meet for nonempty category
  collections and raises on an empty input. The local mapping that `Cat().meet([])`
  returns `Cat().Constructors().EmptyCategory()` is a project completion of Sage's
  missing bottom-category case, not an upstream Sage behavior claim.
- `JoinCategory` remains a category object that represents an intersection condition
  on objects and morphisms. Mapping it to `Cat().JoinCategories()` containment is
  well-typed: membership is about recognizing join category objects, not about moving
  methods to the constructed join result.
- `Category_singleton` is implemented in this install as `category_singleton.pyx`.
  Singleton status is an implementation/classcall fact for categories such as
  `Sets()` and `Rings()`, not a separate mathematical method surface on `Cat()`.
- `CategoryWithAxiom`, `CategoryWithAxiom_over_base_ring`, and
  `CategoryWithAxiom_singleton` are source-backed as axiom-category implementation
  classes. Their mapping remains style/process guidance for correct wrapper bases;
  an axiom restriction belongs on the category where the axiom is mathematically
  meaningful, not as a generic Cat-level method beyond the category-object machinery.
- `Category_over_base`, `Category_over_base_ring`, `Category_module`, and
  `Category_ideal` are source-backed as parameterized Sage category base classes.
  Their base/base-ring/ambient data are evidence for lower subtree ownership and
  wrapper selection, not extra Cat-level constructors.
- `Functor` is source-backed as a morphism between category objects with domain,
  codomain, object action, morphism action, and domain-coercion hooks. The spec
  mapping to functor homsets is therefore the mathematically coherent owner: functor
  elements live in `A.Hom(B)`, not as objects of `Cat()`.
- `ConstructionFunctor` and `CompositeConstructionFunctor` subclass the Sage functor
  surface and add pushout/coercion-combination methods. The mapped methods
  `pushout`, `merge`, `commutes`, `expand`, `common_base`, and `coercion_reversed`
  remain construction-functor interop surface, not evidence for turning every
  functorial construction category into a functor element.
- `FunctorialConstructionCategory.category_of(category, *args)` is the source-backed
  entry point for categories produced by functorial constructions such as
  `C.Subobjects()` or `C.CartesianProducts()`. These construction categories are
  category objects in the project sense, distinct from `Functor` elements with
  domain/codomain/action.
- `CovariantConstructionCategory.default_super_categories`,
  `RegressiveCovariantConstructionCategory.default_super_categories`,
  `additional_structure`, and `is_construction_defined_by_base` justify the spec's
  inheritance rule for standard construction selectors: a selector method is defined
  on the category where the construction is meaningful, and subcategories inherit the
  resulting method surface through Sage's supercategory machinery.
- `SubobjectsCategory`, `QuotientsCategory`, and `SubquotientsCategory` are installed
  directly under `sage/categories/`. Their source docstrings state that subobjects and
  quotients are subquotients and that regressive constructions keep the constructed
  object in the original category. The mapping to `C.Subobjects()`,
  `C.Quotients()`, and `C.Subquotients()` is therefore a category-object construction
  surface, not an object-local method on the produced subobject or quotient.
- `CartesianProductsCategory` is installed directly under `sage/categories/` and
  exposes idempotent `CartesianProducts()` plus base-ring forwarding. The mapped
  `C.CartesianProducts()` selector is source-backed as a category-level finite product
  construction; product-object operations belong in the owning lower category.
- `IsomorphicObjectsCategory` is source-backed and defaults through subobjects and
  quotients. The project `C.IsomorphicObjects()` selector is well-typed as a
  category-object construction for images under isomorphism; it does not introduce a
  nonmathematical "isomorphic result" owner.
- `DualObjectsCategory` and `TensorProductsCategory` are source-backed Sage
  construction categories, but their mathematical existence depends on the receiver
  category. The Cat spec correctly records these as exposed by lower subtrees where
  duals and tensor products are defined, rather than universal Cat methods.
- `Objects.SubcategoryMethods.Homsets()` and `Endsets()` are source-backed as Sage's
  generated homset/endset category navigation. The Cat mapping to `HomCategory()` and
  `EndCategory()` is a project naming refinement over Sage's plural `Homsets`/
  `Endsets` vocabulary; generic Hom/End/Aut method ownership remains in the
  repository-level homsets spec.
- The prior homsets reconciliation records the negative-finding evidence for Sage's
  generic Autset gap. The Cat `AutCategory()` surface therefore remains a
  project-owned refinement for invertible endomorphisms, with Sage `Homsets.Endset`
  only serving as partial upstream evidence.
- The local `ObjectsOver(T)` and `ObjectsUnder(T)` selectors remain project-owned
  slice/coslice category surfaces. They are mathematically meaningful category-level
  constructions, but not installed Sage standard construction modules in the checked
  source tree.
- `Cat().Constructors()` remains an aggregator over explicit category-owned
  constructor collectors. Generated private forwarders with `*args`/`**kwargs` are
  implementation glue only; they do not create public variadic mathematical
  signatures.

Negative missing-surface finding for this Cat core pass:

- Searched: `category_specs/cat/docs/SAGE_INVENTORY.md`;
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-CAT.md`;
  installed Sage 10.7 files `category.py`, `category_singleton.pyx`,
  `category_with_axiom.py`, `category_types.py`, `objects.py`, `homsets.py`,
  `homset.py`, `functor.pyx`, `pushout.py`,
  `covariant_functorial_construction.py`, `subobjects.py`, `quotients.py`,
  `subquotients.py`, `cartesian_product.py`, `isomorphic_objects.py`, `dual.py`,
  and `tensor.py`; and a direct file search of the installed `sage/categories/`
  root for category, functor, homset, subobject, quotient, cartesian-product,
  tensor, dual, and object/slice construction modules.
- Found: the checked sources support the current Cat mapping surfaces and identify
  two stale source-path assumptions in the ledger: `category_singleton` is a `.pyx`
  source in this installation, and Sage's standard construction modules are direct
  `sage/categories/*.py` files rather than files under `sage/categories/constructions/`.
  I found no additional installed Sage Cat-core public surface in this pass that
  requires a new Cat mapping row beyond the existing category-object, order,
  functor, standard-construction, Hom/End/Aut, and constructor-aggregation sections.
- Conclusion: inference -- for the checked Cat-core Sage category/functor framework
  surface, the converted Cat mapping spec is source-complete modulo lower-subtree
  mathematical audits for tensor products, duals, slice/coslice implementation, and
  generic Aut-category implementation ownership.
- Confidence: Medium.
- Gaps: this pass did not enumerate every mathematical category module under
  `sage/categories/`; those are owned by the domain mapping specs such as sets, rings,
  modules, algebras, posets, topology, tensors, forms, and lattices. It also did not
  search Sage git history, third-party Sage extensions, or unavailable online HTML docs
  beyond the installed source tree.

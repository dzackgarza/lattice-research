# Sets: Sage Category → Spec Hierarchy Mapping

This file records, for each Sage category relevant to `Sets()`, the mathematical
justification for how it maps to our hierarchy.

## Sage `EnumeratedSets` → our `Sets().Countable()`

Sage's `EnumeratedSets` axiom captures: "there exists an explicit enumeration
(iteration) of the set's elements." Countability is equivalent: a set is countable
iff there exists an injection f: X → ℕ, which is precisely an enumeration.
Every Sage enumerated set is countable, and every countable set in our hierarchy
must supply an iterator (via `__iter__`).

Consequence: objects that lie in `SageEnumeratedSets()` are refined to
`Sets().Countable()`. The spec class `_CountableSets` therefore declares
`super_categories = [Sets(), SageEnumeratedSets()]`.

## Sage `FiniteEnumeratedSets` → our `Sets().Countable().Finite()`

Finite enumerated sets are both finite and countable.

## Sage `InfiniteEnumeratedSets` → our `Sets().Countable().Infinite()`

Infinite enumerated sets are countably infinite.

## Sage `FacadeSets` → our `Sets().Facade()`

Facade sets represent their elements as elements of another parent.
Mapping is direct: `SageFacadeSets()` ↔ `Sets().Facade()`.

## Sage `TopologicalSpaces` → our `Sets().Topological()`

Sage's `TopologicalSpaces()` captures topological structure. `RealSet` lives here.
The forward target is the dedicated `topological_spaces` subtree:
`Sets().Topological()` navigates to `TopologicalSpaces()`, and
`Sets().Metric()` navigates to `TopologicalSpaces().Metric()`.

## Sage `FiniteSets` → our `Sets().Finite()`

Direct: `SageFiniteSets()` ↔ `Sets().Finite()`.

## Local Surface → Target Spec Surface

The set subtree maps each Sage-backed or local surface to the target mathematical
subcategory file that owns its spec.

| Source surface | Target destination | Rationale |
| --- | --- | --- |
| Set axiom names | Root `category_specs/axioms.py` plus axiom classes under `sets/subcategories/` | Axiom names have one root registration point; set axiom classes own the mathematical method surfaces. |
| Specialized set-object surfaces | One mathematical subcategory file per Sage concept under `sets/subcategories/` | The file structure follows mathematical vocabulary, not implementation history. |
| Named set constructors | `Sets().Constructors()` on `sets/__init__.py` | Constructors are entry points, not subcategories. |
| `_SetObjects`, `_SetObjectsEnumerated` | `subcategories/set_objects.py` | Wrappers from `sage.sets.set.Set` are set-object concepts. |
| `_FiniteEnumeratedSetObjects` | `subcategories/finite_enumerated_set.py` | Finite enumerated sets have their own Sage-backed method surface. |
| `_IntegerRangeSets` | `subcategories/integer_range.py` | Integer ranges are arithmetic progressions with finite or infinite countable behavior. |
| `_NonNegativeIntegersSets` | `subcategories/non_negative_integers.py` | Nonnegative integers are a named countably infinite subset of `ZZ`. |
| `_PositiveIntegersSets` | `subcategories/positive_integers.py` | Positive integers are a named countably infinite integer range. |
| `_PrimesSets` | `subcategories/primes.py` | `Sets().Primes()` is the one-object category for the full Sage prime set. |
| `_RealSets` | `subcategories/real_set.py` | Real subsets, real open sets, and real intervals require distinct vocabulary in `types.py`. |
| `_RecursivelyEnumeratedSets` | `subcategories/recursively_enumerated.py` | Recursively enumerable sets and forests share the Sage constructor family. |
| `_DisjointUnionEnumeratedSets` | `subcategories/disjoint_union.py` | Disjoint unions are countable coproducts of indexed families. |
| `_CartesianProductSets` | `subcategories/cartesian_product.py` | Cartesian products have parent and element projection surfaces. |
| `_ConditionSets` | `subcategories/condition.py` | Predicate-defined subsets use Sage vocabulary `ambient()` and `arguments()`. |
| `_ImageSets` | `subcategories/image.py` | Images are subobjects under a map. |
| `_TotallyOrderedFiniteSets` | `subcategories/totally_ordered_finite.py` | Finite total orders have parent and element comparison surfaces. |
| `_FiniteSetMapsSets` | `subcategories/finite_set_maps.py` | Finite map sets include finite-set and endomap-monoid behavior. |
| `_FamilySets` | `subcategories/family.py` | Indexed families have finite, lazy, trivial, and enumerated variants. |
| `_EnumeratedSetsFromIterator` | `subcategories/enumerated_from_iterator.py` | Callable-backed enumerated sets expose iterator and cache surfaces. |
| Sage subquotient construction surface | `subcategories/constructions/subquotients.py` | Subobjects and quotients are special cases of constructive subquotients, so the parent construction must be explicit. |
| Sage isomorphic-object construction surface | `subcategories/constructions/isomorphic_objects.py` | Images by isomorphism are both subobjects and quotients in Sage and need their own construction file. |
| Sage realization surface | `subcategories/constructions/with_realizations.py` and `subcategories/constructions/realizations.py` | A set with multiple realizations and its concrete realization parents are construction categories, not named constructors. |
| Sage homset/endset surface | `sets/homsets.py` plus top-level `homsets/` | `Sets().Homsets()` and `Sets().Endsets()` must be explicit category surfaces; automorphism sets derive from endsets at the top level. |
| `SetsWithGrading()` | `subcategories/graded.py`; canonical navigation `Sets().Graded()` with Sage-compatibility alias `Sets().WithGrading()` | A graded set is a set equipped with a grading map to a grading set. Sage's own TODO asks for this to live under `Sets()`, and the project should use the uniform axiomatic name `Graded` while keeping the written Sage phrase available as an alias. |
| `GSets(G)` | `subcategories/group_actions.py`; public navigation `Sets().GSets(G)` | A `G`-set is a set equipped with an action of the fixed group `G`. Sage's category is parameterized by `G` and has `Sets()` as its supercategory. |
| `Posets()`, `LatticePosets()`, `FiniteLatticePosets()` | promoted `posets/` subtree; `sets` docs keep only cross-navigation | Posets have an independent order-theoretic method surface. Lattice posets here are order-theoretic meet/join lattices, not module lattices or quadratic lattices. |

Target subcategory file names follow mathematical vocabulary. Groupings by constructor
history, implementation convenience, or named-object families are not target
subcategory boundaries.

## Sage Category → Project Category Decisions

| Sage category | Project category | Justification | Consequence |
| --- | --- | --- | --- |
| `SetsWithPartialMaps()` | `Sets()` inherited through Sage | Sage places `Sets()` below sets with partial maps. The project does not need a separate public partial-map category for the set-object inventory. | `Sets.super_categories()` keeps `SageSets()`, so Sage's inherited category behavior remains available. |
| `Sets()` | `Sets()` | Base category of parents whose elements support membership and basic element construction. | Root method surface includes operations meaningful for arbitrary sets, including union. Ambient-dependent operations such as intersection, difference, symmetric difference, and complement use `Subset` vocabulary under `Subsets = Subobjects`. |
| `EnumeratedSets()` | `Sets().Countable()` | Sage defines enumerated sets as finite or countable sets/multisets with a canonical enumeration. Countability is the set-level mathematical property; enumeration methods are the computable witness. | Countable sets must declare iterator/rank/unrank/list/tuple/range surfaces inherited from Sage. Multiset caveat remains a documented boundary. |
| `FiniteSets()` | `Sets().Finite()` | Finite sets have finite cardinality independent of enumeration. | `Finite` declares `is_finite() -> True`, cardinality, finite listing, and finite subquotient behavior. |
| `FiniteEnumeratedSets()` | `Sets().Countable().Finite()` | Finite enumerated sets combine finite cardinality with explicit enumeration. | The finite-countable subcategory owns finite enumeration helpers such as `last`, random-by-unrank, cardinality-from-list/iterator, and finite Cartesian product rank/unrank. |
| `InfiniteEnumeratedSets()` | `Sets().Countable().Infinite()` | Infinite enumerated sets are countably infinite, not listable as finite collections. | Infinite-countable declarations should state non-listability methods (`tuple`, `list`, `random_element`) as Sage surfaces without implementing exception logic in the spec. |
| `FacadeSets()` | `Sets().Facade()` | Elements are represented by elements of another parent. | `facade_for`, facade element construction, and facade parent checks belong here. |
| Sage `TopologicalSpaces()` for `RealSet` | `TopologicalSpaces()` / `Sets().Topological()` plus `Sets().Subobjects()` when an ambient real line is present | A `RealSet` is a topological subset of the real line, and a set with a topology is precisely a topological space. | `RealSet` refinement must preserve Sage topological behavior and declare real-line subobject operations. |
| Sage `Set_base` boolean mixins | Root set operations and `Sets().Subobjects()` / `Subsets` | Sage's boolean mixins are implementation artifacts, not mathematical subcategories. A set has union as a set operation. Intersections, differences, symmetric differences, and complements require a common ambient set and therefore live on subsets/subobjects. | Do not introduce a project `WithBooleanOps` axiom. Map Sage mixin methods to the mathematical operation surface they actually represent. |
| `SubobjectsCategory` | `Sets().Subobjects()` / alias `Subsets` | In the category of sets, subobjects are exactly subsets. The same construction must remain attachable to arbitrary set subcategories via Sage's functorial construction/category-of machinery. | The set subtree exposes `Subsets = Subobjects` and uses `Subset` type vocabulary in signatures. Its implementation lives in `subcategories/constructions/subobjects.py`, not a monolithic `constructions.py`. |
| `QuotientsCategory` | `Sets().Quotients()` | Quotient sets are equivalence-class objects. Like subobjects, quotient categories are attachable construction categories, not singleton categories. | `subcategories/constructions/quotients.py` owns the set-specific quotient scaffold and `types.py` exposes `QuotientSet`. |
| `SubquotientsCategory` | `Sets().Subquotients()` | Sage's constructive subquotients are the primitive construction behind quotients and subobjects: an object has an ambient object, a lift, and a retract. | Add `subcategories/constructions/subquotients.py`; `Subobjects`, `Quotients`, and `IsomorphicObjects` should refine this surface rather than restating it. |
| `IsomorphicObjectsCategory` | `Sets().IsomorphicObjects()` | An isomorphic image is simultaneously a subobject and a quotient in Sage. | Add `subcategories/constructions/isomorphic_objects.py` and document the lift/retract convention. |
| `WithRealizationsCategory` / `RealizationsCategory` | `Sets().WithRealizations()` and `Sets().Realizations()` | A parent with realizations is a set whose elements may live in several concrete realization parents; Sage makes it a facade set. | Add construction files for `with_realizations` and `realizations`; do not treat realization names as constructors. |
| `HomsetsCategory` | `SetHomsets`, `SetEndsets`, `SetAutsets` | Morphisms between sets are functions; endomorphisms have equal domain/codomain; automorphisms are bijections. | Generic Autset wiring belongs at the repository top level, but set-specific homset categories should declare function-level methods and delegate Aut construction rather than reimplement condition-set machinery. `Sets().Homsets()` and `Sets().Endsets()` are public category navigation surfaces. |
| `Homsets().Endset()` | `SetEndsets` | Endsets are homsets with equal domain and codomain; Sage makes generic endsets monoids. | `sets/homsets.py` must expose the set-specific endset category and inherit generic endset methods. |
| Sage generic homset/endset surface plus project `Autsets` target | `SetAutsets` backed by generic `Autset` | `Aut(X)` is the subset of `End(X)` consisting of bijections. | This project vocabulary is wired once at the top level and specialized in `sets/homsets.py`; see `TRIAGE.md` for the searched-source note on upstream category naming. |
| `SetsWithGrading()` | `Sets().Graded()` with `Sets().WithGrading()` compatibility alias | A graded set is a disjoint union of graded components indexed by a grading set, with a grading map sending each element to its grade. | `subcategories/graded.py` owns `grading_set`, `graded_component`, optional `subset`, `grading`, `generating_series`, and `_test_graded_components`. |
| `GSets(G)` | `Sets().GSets(G)` | A `G`-set is a set with an action of the fixed group `G`; Sage's source records `GSets(G).super_categories() == [Sets()]`. | `subcategories/group_actions.py` owns the parameterized category. `types.py` needs `GSet` and group-action vocabulary anchored to Sage group/action objects. |
| `Posets()` | top-level `posets/` subtree, cross-linked from `sets` | A poset is a set with a partial order. Sage's required parent method is `le`; it also exposes `lt`, `ge`, `gt`, covers, order ideals, filters, chains, and antichains. | Do not bury this under ordinary set subcategories. The promoted subtree owns order methods and its own finite/lattice refinements. |
| `LatticePosets()` / `FiniteLatticePosets()` | `posets/subcategories/lattice.py` and `posets/subcategories/finite_lattice.py` | These are order-theoretic lattices: posets in which every pair has a meet and join. | Keep separate from module/quadratic-form lattice vocabulary; finite lattice posets add irreducibles and lattice-morphism checks. |

## Constructor Mapping Decisions

| Sage constructor | Project subcategory | Notes |
| --- | --- | --- |
| `Set(X)` | `SetObjects`, `FiniteSetObjects` | `Set_object_enumerated` receives the finite-countable surface. Sage boolean-operation mixins are mapped to root `union` and to `Subsets = Subobjects`, not to a project `WithBooleanOps` category. |
| `FiniteEnumeratedSet(elements)` | `FiniteEnumeratedSetObjects` | Tuple-backed finite facade set. Include `last`, `__call__`, and element construction in the spec. |
| `IntegerRange(...)` | `IntegerRangeSets` | Arithmetic progression of integers. Finite/infinite status depends on bounds; the one-object category should refine through countable facade sets and let Sage/category membership expose finiteness. |
| `NonNegativeIntegers()` | `NonNegativeIntegerSets` | Countably infinite facade subset of `ZZ`. |
| `PositiveIntegers()` | `PositiveIntegerSets` | Positive integer range; inherits most integer-range behavior and supplies Sage's `an_element`/`_sympy_`. |
| `Primes()` | `PrimesSets` | `Sets().Primes()` is the one-object category whose object is Sage's set of prime integers. `PrimeSubset` and `PrimesInArithmeticProgressions` are types of subobjects of that prime set, not separate top-level categories unless Sage exposes distinct parent objects with required methods. |
| `RealSet(...)` | `RealSets` | A real set is a subset of the real line. Real intervals and real open sets are distinct mathematical notions: open intervals are basis elements for the Euclidean topology, while open subsets may be unions such as `(1, 2) ∪ (3, 4)`. |
| `RealSet` static interval constructors | real-subset interval constructors | Sage methods such as `RealSet.open(a, b)` and `RealSet.closed(a, b)` construct interval-shaped real subsets, not arbitrary open or closed real subsets. Static Sage constructors map to `Sets().Constructors()` entries such as `OpenRealInterval`, `ClosedRealInterval`, and `RealLine`; open interval constructors return `RealOpenSet` because an open interval is an open real subset, but a general `RealOpenSet` need not be an interval. |
| `RecursivelyEnumeratedSet(...)` | `RecursivelyEnumeratedSets` | Recursively enumerable countable sets and forests. The forest-specific methods are part of the same Sage constructor family. |
| `DisjointUnionEnumeratedSets(family)` | `DisjointUnionSets` | Countable coproduct/disjoint union of an indexed family. |
| `CartesianProduct(...)` / `cartesian_product(...)` | `CartesianProductSets` | Product of sets; element projections belong to element methods. |
| `ConditionSet(universe, predicates...)` | `PredicateSubsets` or `ConditionSets` | Sage names the ambient set via `ambient()` and predicates via `arguments()`; old `universe()`/`predicates()` names need explicit alias decisions before use. |
| `ImageSubobject(f, X)` | `ImageSets` | Image subobject under a map; must include `ambient`, `lift`, and `retract`. |
| `TotallyOrderedFiniteSet(elements)` | `TotallyOrderedFiniteSets` | Finite set with order relation `le`; element comparison methods are mathematical when elements are non-facade. |
| `FiniteSetMaps(domain, codomain)` | `FiniteSetMapSets` | Finite set of functions. Endomap variants expose monoid identity as `one()`, not only `identity()`. |
| `Family(indices, function)` | `Families` | Indexed family object. Include `items`, `hidden_keys`, `has_key`, and `inverse_family`. |
| `EnumeratedSetFromIterator(f)` | `IteratorEnumeratedSets` | Callable-backed countable set. Include `clear_cache` because caching is part of the Sage-backed parent behavior. |

## Sage Primes Source Note

- Searched: Context7 `/sagemath/documentation`, DeepWiki `sagemath/sage`, hosted Sage docs for `Primes`, and installed source `sage/sets/primes.py`.
- Found: Hosted docs describe prime subsets selected by congruence data (`modulus`, `classes`, and `exceptions`); the installed source at `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/sets/primes.py` exposes only `Primes(proof=True)` for the full set of prime integers.
- Conclusion: I believe the online docs and installed source are version-skewed. Mathematically, congruence-class prime subsets should be represented as subobjects of `Primes()`, with vocabulary such as `PrimesInArithmeticProgressions` only where method signatures require that refinement.
- Confidence: Medium.
- Gaps: I have not searched Sage git history or package metadata for the exact documentation/source version boundary.

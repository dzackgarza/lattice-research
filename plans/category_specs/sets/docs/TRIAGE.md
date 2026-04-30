# Sets Triage

Source for this pass: `sets/docs/SAGE_INVENTORY.md` and `sets/docs/MAPPING.md`.

This triage records the current `sets/smoketest.sage` frontier together with the
documentation audit context needed to interpret those failures.

## Current Alignment

- The set subtree uses one semantic subcategory file per Sage-backed concept under
  `sets/subcategories/`.
- `Sets().Constructors()` is the constructor namespace for Sage set entry points.
- `WithBooleanOps` is not a project axiom or subcategory. Sage boolean mixins are mapped
  to root set `union` and to subset/subobject operations.
- `Subsets = Subobjects` is wired through
  `subcategories/constructions/subobjects.py`, and `Quotients` is wired through
  `subcategories/constructions/quotients.py`.
- Sage `Subquotients`, `IsomorphicObjects`, `WithRealizations`, and `Realizations`
  are split under `subcategories/constructions/`.
- `Homsets`, `Endsets`, and project `Autsets` are explicit through `sets/homsets.py`,
  with generic Autset construction owned by the root `homsets/` subtree.
- Real-line vocabulary distinguishes `RealSubset`, `RealOpenSet`, and `RealInterval`.
  An open interval is an example of a `RealOpenSet`; a general `RealOpenSet` need not be
  an interval.
- Topological and metric surfaces live in `topological_spaces`; `Sets().Topological()`
  and `Sets().Metric()` navigate into that hierarchy.
- `Sets().Primes()` is the one-object category for the full Sage prime set. `PrimeSubset`
  and `PrimesInArithmeticProgressions` are type vocabulary for subobjects of that prime
  set, not separate top-level categories unless Sage exposes distinct parent objects
  with required methods.
- Sage `Set(X)` exists in upstream Sage, but the generic wrapper is not an admitted
  project constructor. It attempts to regard an arbitrary object as a set without a
  mathematical construction that supplies the `Sets()` obligations. Known valid cases
  must be exposed as named constructors with explicit set semantics: `ZZ` is already
  tested as an object of `Sets()`, and finite iterables are routed through
  `Sets().Constructors().from_iterable(elements)`.
- `Sets().Graded()` maps Sage `SetsWithGrading()` to a graded-set axiom.
- `Sets().GSets(G)` is the parameterized category of sets with an action of `G`.
- `Posets()`, `Posets().Lattice()`, and `Posets().Lattice().Finite()` live in the
  promoted `posets/` subtree.

## Audit Conclusions

- Sage set wrappers expose `intersection`, `difference`, and `symmetric_difference`,
  but the wrapper itself is not a valid project category surface. The method surface is
  still mapped: `union` belongs to root sets; `intersection`, `difference`,
  `symmetric_difference`, and complement belong to `Subsets = Subobjects` with
  `Subset` signatures; `__contains__`, `cardinality`, `is_empty`, `is_finite`,
  `subsets`, `subsets_lattice`, and `_sympy_` belong to root sets; and `__iter__`
  belongs to countable sets.
- Cartesian products have two Sage input shapes: the standalone constructor receives a
  sequence or tuple of parent sets, while parent methods support
  `X.cartesian_product(Y, Z, category=..., extra_category=...)`. The
  `Sets().Constructors().cartesian_product` target therefore takes
  `factors: Sequence[Set]`; untyped constructor-level `*args/**kwargs` signatures are
  not justified by the Sage constructor.
- `SetsWithGrading()` maps to `Sets().Graded()`. The required method surface is
  `grading_set`, `graded_component`, optional `subset`, `grading`, `generating_series`,
  and `_test_graded_components`.
- `GSets(G)` maps inside the set subtree as the parameterized subcategory
  `Sets().GSets(G)`. The Sage source gives the mathematical category and base
  parameter; `types.py` now carries `GSet` and group-action vocabulary.
- `Posets`, `LatticePosets`, and `FiniteLatticePosets` are promoted to a `posets`
  subtree. They remain set-structured categories, but their method surfaces are
  independent: posets require order methods; lattice posets require meet and join;
  finite lattice posets add irreducible-element and lattice-morphism methods.
- Rich comparison is split by mathematical meaning and exposed. Sage
  `Set_object.__richcmp__`, `Set_object_enumerated.__richcmp__`, and finite-wrapper
  `issubset`/`issuperset` map to root set-theoretic comparison: equality by elements,
  subset, proper subset, superset, and proper superset. Poset comparisons remain
  `le`, `lt`, `ge`, and `gt` on elements of ordered sets. The spec must not conflate
  set inclusion with poset element order.

## Implemented Structural Changes

- Construction-category files exist for `subquotients.py`, `isomorphic_objects.py`,
  `with_realizations.py`, and `realizations.py`.
- `sets/homsets.py` declares the set-specific Homset, Endset, and Autset method
  surfaces without post-class axiom splicing.
- `subcategories/graded.py` and `subcategories/group_actions.py` specify graded sets
  and `G`-sets.
- The promoted `posets/` subtree specifies posets, lattice posets, and finite lattice
  posets.
- `types.py` carries the corresponding set, subquotient, realization, graded-set,
  `G`-set, and poset vocabulary.
- The generic `Set(X)` wrapper category and `Sets().Constructors().Set` entry point
  were removed from the admitted surface. Upstream `sage.sets.set` remains inventoried
  as a known Sage source whose valid cases must be decomposed into named project
  constructors.
- `Sets.ParentMethods` now exposes the root set methods witnessed by Sage's wrapper
  surface, including set-theoretic rich comparison and subset predicates.
- `Sets().Constructors().from_iterable(elements)` is the named finite iterable
  constructor replacing finite uses of Sage `Set([..])`.

## Current Smoke Frontier

- `sets/smoketest.sage` now exercises `RealSet` with an actual Sage real-interval
  object, matching the admitted `Sets().Constructors().RealSet(intervals=...)` shape.
- `sets/smoketest.sage` documents the `Set(ZZ)` replacement by checking `ZZ in Sets()`
  and documents the `Set([1, 2, 3])` replacement through
  `Sets().Constructors().from_iterable([1, 2, 3])`.
- The smoke still fails on existing abstract-method sentinels, not on tuple/list
  interval data, constructor call-shape mismatches, or arbitrary `Set(X)` wrapping.
- Missing `_element_constructor_`: `RealSet([RealSet.open(0, 1).get_interval(0)])`.
- Missing `_an_element_from_iterator`: `FiniteEnumeratedSet`, `IntegerRange`,
  `RecursivelyEnumeratedSet`, `DisjointUnionEnumeratedSets`, `CartesianProduct`,
  `ImageSubobject`, `TotallyOrderedFiniteSet`, `FiniteSetMaps`, `Family`, and
  categorical `cartesian_product`.
- Missing `__len__`: `NonNegativeIntegers`, `PositiveIntegers`, and
  `EnumeratedSetFromIterator`.
- Missing `__iter__`: `Primes`.
- Missing `algebra`: `ConditionSet(ZZ, even predicate)`.

## Source note: project `Autsets`

- Searched: local Sage `sage/categories/homsets.py`, `sage/categories/homset.py`,
  `sage/categories/sets_cat.py`, Context7 Sage documentation snippets for `Homsets`
  and `Endset`, and DeepWiki category hierarchy answers.
- Found: Sage exposes `Homsets()` and the `Endset` axiom; the searched sources did not
  expose a parallel category named `Autsets`.
- Conclusion: inference -- project `Autsets` should be documented as a project-level
  specialization of endsets by invertibility/bijectivity, not as a Sage category name.
- Confidence: Medium.
- Gaps: full Sage develop-tree grep and Sage git history were not searched for alternate
  automorphism-set naming.

## Source note: prime subsets in arithmetic progressions

- Searched: Context7 `/sagemath/documentation`, DeepWiki `sagemath/sage`, hosted Sage
  docs for `Primes`, and installed source `sage/sets/primes.py`.
- Found: Hosted docs describe prime subsets selected by congruence data (`modulus`,
  `classes`, and `exceptions`); installed source exposes only `Primes(proof=True)` for
  all primes.
- Conclusion: I believe this is a local Sage version/source mismatch. Congruence-class
  prime subsets are subobjects of `Primes()`, with `PrimesInArithmeticProgressions`
  vocabulary only where method signatures require it.
- Confidence: Medium.
- Gaps: Sage git history and package version metadata have not been searched.

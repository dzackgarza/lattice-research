# Sets Triage

Source for this pass: `sets/docs/SAGE_INVENTORY.md` and `sets/docs/MAPPING.md`.

This triage records the documentation audit results before runtime validation. Runtime
smoke output is intentionally not the source of truth for this pass.

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
- `Sets().Graded()` maps Sage `SetsWithGrading()` to a graded-set axiom.
- `Sets().GSets(G)` is the parameterized category of sets with an action of `G`.
- `Posets()`, `Posets().Lattice()`, and `Posets().Lattice().Finite()` live in the
  promoted `posets/` subtree.

## Audit Conclusions

- Sage set wrappers expose `intersection`, `difference`, and `symmetric_difference`
  because those wrappers represent concrete subsets of an implicit ambient universe.
  The project target is to declare `union` on root sets, and declare
  `intersection`, `difference`, `symmetric_difference`, and complement on
  `Subsets = Subobjects` with `Subset` signatures. Concrete `Set_object` wrapper specs
  may redeclare the Sage methods only as wrapper-backed subset operations.
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
- Rich comparison is split by mathematical meaning. `Set_object.__richcmp__` and
  `Set_object_enumerated.__richcmp__` are wrapper/equality and finite-membership
  comparisons; poset comparisons are `le`, `lt`, `ge`, and `gt` on ordered sets. The
  spec should not conflate finite-set rich comparison with partial order.

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

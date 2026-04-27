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
- Sage `Subquotients`, `IsomorphicObjects`, `WithRealizations`, `Realizations`,
  `Homsets`, and `Endsets` are now recorded in the mapping docs as required
  construction-category surfaces. They are not optional runtime conveniences.
- `Autsets` is project vocabulary for automorphism sets. The target is explicit
  top-level wiring specialized by `sets/homsets.py`.
- Real-line vocabulary distinguishes `RealSubset`, `RealOpenSet`, and `RealInterval`.
  An open interval is an example of a `RealOpenSet`; a general `RealOpenSet` need not be
  an interval.
- Topological and metric surfaces live in `topological_spaces`; `Sets().Topological()`
  and `Sets().Metric()` navigate into that hierarchy.
- `Sets().Primes()` is the one-object category for the full Sage prime set. `PrimeSubset`
  and `PrimesInArithmeticProgressions` are type vocabulary for subobjects of that prime
  set, not separate top-level categories unless Sage exposes distinct parent objects
  with required methods.

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
- `SetsWithGrading()` maps to `Sets().Graded()` with `Sets().WithGrading()` as a
  Sage-compatibility alias. The required method surface is `grading_set`,
  `graded_component`, optional `subset`, `grading`, `generating_series`, and
  `_test_graded_components`.
- `GSets(G)` maps inside the set subtree as the parameterized subcategory
  `Sets().GSets(G)`. The Sage source gives the mathematical category and base
  parameter; the project spec should add group-action vocabulary in `types.py` rather
  than treating `G`-sets as named constructors.
- `Posets`, `LatticePosets`, and `FiniteLatticePosets` are promoted to a `posets`
  subtree. They remain set-structured categories, but their method surfaces are
  independent: posets require order methods; lattice posets require meet and join;
  finite lattice posets add irreducible-element and lattice-morphism methods.
- Rich comparison is split by mathematical meaning. `Set_object.__richcmp__` and
  `Set_object_enumerated.__richcmp__` are wrapper/equality and finite-membership
  comparisons; poset comparisons are `le`, `lt`, `ge`, and `gt` on ordered sets. The
  spec should not conflate finite-set rich comparison with partial order.

## Required Spec Changes Identified By The Audit

- Add construction-category files for `subquotients.py`, `isomorphic_objects.py`,
  `with_realizations.py`, and `realizations.py` under the organized construction
  subdirectory.
- Expand `sets/homsets.py` so `Sets().Homsets()`, `Sets().Endsets()`, and the project
  `Autsets` surface are explicit without reading generic category code.
- Add `subcategories/graded.py` and `subcategories/group_actions.py` for graded sets
  and `G`-sets.
- Add or cross-link a promoted `posets/` subtree with files for posets, lattice posets,
  and finite lattice posets.
- Tighten `types.py` with `Subset`, `QuotientSet`, `SetSubquotient`,
  `IsomorphicSetObject`, `SetWithRealizations`, `SetRealization`, `GradedSet`,
  `GSet`, `Poset`, `LatticePoset`, `FiniteLatticePoset`, `SetHomset`, `SetEndset`,
  and `SetAutset` vocabulary anchored to Sage objects or project refinements.

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

## Source note: `_Sets()` in Cartesian-product wiring

- Searched: hosted Sage `develop` URL supplied for `sage/sets/set.py`, raw Sage
  `develop` `sage/sets/cartesian_product.py`, installed
  `sage/sets/cartesian_product.py`, installed `sage/categories/sets_cat.py`, and local
  Probe searches for `_Sets` near Cartesian product and set category code.
- Found: The searched Cartesian-product sources import or use `Sets` directly and expose
  `CartesianProducts` category wiring, but I did not find a local `def _Sets()` in those
  searched locations.
- Conclusion: inference -- I believe the `_Sets()` reference is either in a different
  Sage file/version, in generated/preparsed source not yet searched, or needs a broader
  Sage develop-tree search before it can be mapped.
- Confidence: Low.
- Gaps: full Sage develop repository search, Sage git history, and release-skew
  comparison have not been performed.

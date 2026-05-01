# Needs Decisions

These are design blockers, not mechanical audit findings. Mechanical compliance issues
should be fixed in code; only items that require a human design choice belong here.

## Algebra Constructors

- Name additive-structure algebra constructors. Sage overloads `S.algebra(R,
  category=...)` for additive semigroups, additive monoids, and additive groups; the
  project API must split these into explicit mathematical constructor names.
- Decide the typed input surface for the mapped associative-unital
  finite-dimensional multiplication-table constructor: right-multiplication matrix
  data, basis-name data, and target refinement.
- Define the mathematical type for multiplication-on-basis constructor data: basis
  index set, unit index, and product-on-basis law.
- Decide where nonunital and nonassociative finite-dimensional Sage algebras map once
  the corresponding magmatic or nonunital algebra subtrees exist.

## Topological Spaces

- Choose whether named real-line and real-interval constructors belong to
  `TopologicalSpaces().Constructors()` or to a set/real-subset constructor surface
  whose results refine into `TopologicalSpaces()`.
- Choose whether to keep one explicit flag-bearing interval constructor or require
  named constructors for each endpoint pattern.
- Choose whether metric point methods such as `point.dist(other)` belong in
  `MetricSpacesElement`.
- Choose whether metric homsets are represented as 1-Lipschitz maps, a broader
  Lipschitz-map category, or ordinary continuous maps plus a metric compatibility
  predicate.

## Posets

- Choose the named constructor API for the documented `Poset(...)` input cases:
  elements plus relations, elements plus order predicate, elements plus cover
  predicate, upper-cover dictionary, upper-cover list, acyclic `DiGraph`, and
  existing-poset refinement.
- Choose whether aggregate `meet(x, y=None)` and `join(x, y=None)` become explicit
  overloads, separate finite-fold methods, or Sage compatibility-only behavior.
- Choose project type names for lattice congruences before admitting `congruence`,
  `quotient`, and `congruences_lattice` stubs.
- Decide ownership for graph, plotting, TikZ, polytope, order-complex,
  incidence-algebra, Mobius-algebra, and polynomial invariant surfaces.
- Decide how certificate-returning Sage predicates should appear in project signatures
  without `certificate` boolean overload ambiguity.

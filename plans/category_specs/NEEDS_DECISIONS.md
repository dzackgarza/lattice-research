# Needs Decisions

These are design blockers, not mechanical audit findings. Mechanical compliance issues
should be fixed in code; only items that require a human design choice belong here.

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

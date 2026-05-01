# Topological Spaces Triage

## Current Smoke Frontier

The Sage warning about `Sets.Topological` not being a `CategoryWithAxiom` is still
visible during smoke runs. Under `docs/MAPPING.md`, this is an implementation-frontier
warning for the settled `TopologicalSpaces()` inheritance path, not an unresolved
ownership decision.

## Current Blockers

- `TopologicalSpaces().Constructors()` remains empty by design until the real-line
  constructor namespace is chosen.
- Local `TopologicalSpaces().Metric()` does not yet expose Sage's metric-hom
  distinction.
- Root topological methods now use the ambient-relative shape
  `X.is_open(U: Subset)`, `X.is_closed(U)`, `X.closure(U)`, `X.interior(U)`, and
  `X.boundary(U)`. No implementation or smoke yet proves recovery of Sage
  `RealSet.is_open()`, `RealSet.closure()`, and related subset methods through this
  ambient route.
- Sage `RealSet(*args)` is variadic and accepts manifold-producing keyword paths.
  The future project surface must split this into closed named constructor paths and
  exclude the manifold paths.
- Sage real and complex ball fields are not currently metric spaces in Sage:
  observed `RBF in Sets().Metric()` and `CBF in Sets().Metric()` are both `False`,
  and neither parent exposes `dist`. Their topological recovery belongs through
  topological ring/field work, not through pure topological-space constructors.

## Decisions For Later `NEEDS_DECISIONS.md`

- Choose whether named real-line constructors live under
  `TopologicalSpaces().Constructors()` or under a set/real-subset constructor namespace
  that refines into `TopologicalSpaces()`.
- Choose whether topological subobjects also get convenience methods such as
  `U.is_open()` and `U.closure()`, or whether only ambient methods such as
  `X.is_open(U)` and `X.closure(U)` are required.
- Choose whether to keep one explicit `interval(lower, upper, *, lower_closed,
  upper_closed)` constructor or require only named interval and ray constructors.
- Choose the metric method name: `metric(x, y)`, `metric_function()`, or a deliberately
  documented pair matching Sage's deprecation history.
- Choose whether metric point methods such as `point.dist(other)` belong in
  `MetricSpacesElement`, and keep `abs()` out of pure metric spaces unless the needed
  zero/norm structure is present.
- Choose canonical smoke examples for local `Connected`, `Compact`, and
  `Metric().Complete()` subcategories.

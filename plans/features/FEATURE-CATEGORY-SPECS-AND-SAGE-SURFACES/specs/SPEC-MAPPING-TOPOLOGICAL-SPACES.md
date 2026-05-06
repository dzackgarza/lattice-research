---
id: SPEC-MAPPING-TOPOLOGICAL-SPACES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track topological spaces mapping spec
status: needs-review
priority: critical
requirement: Convert category_specs/topological_spaces/docs/MAPPING.md into a tracked
  spec surface and audit it for Sage-source completeness, mathematical correctness,
  and well-typed topology, metric, connectedness, compactness, ambient, and constructor
  signatures.
acceptanceCriteria:
- Source paths category_specs/topological_spaces/docs/MAPPING.md and category_specs/topological_spaces/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 75
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Topological Spaces Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/topological_spaces/docs/MAPPING.md`.

Source inventory: `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/topological_spaces.py`
  - `sage/categories/metric_spaces.py`
  - `sage/sets/real_set.py`
- Runtime observation route checked by the local inventory:
  - `/home/dzack/miniforge3/envs/sage/bin/sage -c`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the topological
  and metric method reconciliation is recorded below, with remaining gaps routed
  through `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Completeness Reconciliation: Topological And Metric Surface

This pass checked the topological-space inventory against the converted mapping:

- `TopologicalSpaces`, `Sets().Topological()`, connected and compact axioms, and
  Cartesian products are represented by the root `TopologicalSpaces()` surface and its
  construction/axiom refinements;
- `MetricSpaces`, `Sets().Metric()`, complete metric spaces, metric products, and
  metric homsets are represented by `TopologicalSpaces().Metric()` refinements, with
  `metric()` naming the metric map and `dist(x, y)` naming its evaluation;
- `RealSet` topological predicates and transforms are represented by ambient-relative
  topological-space methods on subsets, not by pure set methods or a separate RealSet
  owner;
- named `RealSet` intervals, rays, points, and the real line are routed through
  `Sets().Constructors()` and then refined into topological subobjects;
- the variadic `RealSet(*args)` surface is rejected as public API until its finite
  mathematical cases are expressed as closed named constructors;
- interval and ball fields are recorded as topology-bearing ring/field evidence, not
  topological-space constructors;
- manifolds, schemes, varieties, polyhedra, complexes, hyperbolic models, and related
  structured geometric objects are explicit non-mappings for this subtree because
  their constructors belong to their own mathematical subtrees.

Negative missing-surface finding for this topological pass:

- Searched: `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`, installed Sage
  `sage/categories/topological_spaces.py`, `sage/categories/metric_spaces.py`,
  `sage/sets/real_set.py`, the inventory-recorded Sage runtime observation route, and
  the converted topological mapping rows above.
- Found: every inventoried topological, metric, RealSet, numeric interval/ball, and
  excluded-geometry surface is represented as an admitted topological method/category,
  set-constructor route, ring/field recovery route, interop-only observation, or
  explicit non-mapping in the converted spec.
- Conclusion: inference -- this pass found no additional Sage topological-space
  surface requiring a new public owner inside `topological_spaces`.
- Confidence: Medium.
- Gaps: broader Sage geometry/manifold/scheme/polyhedra sources and unreleased Sage
  branches remain outside this topological-space subtree pass by the inventory's own
  exclusion boundary.

## Converted Mapping Content

Topological spaces are sets with a topology. The target hierarchy therefore has a
dedicated `topological_spaces` subtree, and `Sets().Topological()` is that category,
not a set-local duplicate.

## Category and Method Mapping

| Source concept | Target category or method | Justification | Consequence |
| --- | --- | --- | --- |
| `Sets().Topological()` | `TopologicalSpaces()` | A set with a topology is precisely a topological space. | There is one category surface, exposed from both names. |
| `Sets().Metric()` | `TopologicalSpaces().Metric()` | A metric space is a topological space whose topology is induced by a metric. | Metric methods refine the topological-space surface through the `Metric` axiom. |
| `TopologicalSpaces.CartesianProducts` | `TopologicalSpaces().CartesianProducts()` | Product topology is first true for topological spaces. | Keep this construction category in the subtree. |
| `TopologicalSpaces.Connected()` | `TopologicalSpaces().Connected()` | Connectedness is a topological-space axiom. | Local subcategory stub is `topological_spaces/subcategories/connected.py`. |
| `TopologicalSpaces.Compact()` | `TopologicalSpaces().Compact()` | Compactness is a topological-space axiom. | Local subcategory stub is `topological_spaces/subcategories/compact.py`. |
| `MetricSpaces.Complete()` | `TopologicalSpaces().Metric().Complete()` | Completeness is a metric-space axiom, not a general topological axiom. | Local subcategory stub is `topological_spaces/subcategories/complete.py`. |
| Sage `metric_function()` / deprecated `metric` alias | `MetricSpace.metric() -> SetMorphism` | The metric itself is the map `d: X x X -> RR`, not the evaluated distance. | `dist(x, y)` is the evaluated distance. Do not model `metric` as a binary scalar-valued method. |
| Sage `dist(a, b)` on metric parents | `MetricSpace.dist(x, y)` | Distance between two points is a metric-space method obtained by evaluating the metric map. | Keep as a metric root method. |
| Sage element `dist(b)` | `MetricSpacesElement.dist(other)` delegating to `self.parent().dist(self, other)` | The parent owns the metric; the element API is ergonomic enrichment. | Element methods do not duplicate metric structure. |
| Sage element `abs()` | Structured metric/ring method, not pure topological | Absolute value uses the distinguished zero and additive/ring structure in Sage's default implementation. | Map through topological ring/field or normed additive structure, not the pure topological-space root. |
| Sage metric homsets | `TopologicalSpaces().Metric().HomCategory()` as short maps | The standard category of metric spaces uses distance-nonincreasing maps as morphisms; these are continuous maps with Lipschitz constant at most 1. | The spec records short-map morphisms even though current constructors do not enforce this effectively. Continuous maps remain the root topological hom notion. |
| Sage product metric | `TopologicalSpaces().Metric().CartesianProducts()` | Product metric is the maximum of factor distances in Sage. | Keep metric product behavior in the metric subcategory, separate from product topology. |

Continuous maps inherit set-map inverse-image vocabulary from `Sets().HomCategory()`:
`f.preimage(U)` is the inverse image of a subset under the underlying set map. The
topological refinement is expressed by the ambient topological-space methods on subsets,
not by a second topological-only `preimage` obligation. Endomorphism objects use the
generic end-domain vocabulary: `End_Top(X).domain()` names the underlying space, so
`base_space()` is not a separate abstract method on topological or metric end
categories.

## Root Topological Method Mapping

The root space owns predicates and transforms that take a subset of a space. This is
the surface needed to recover Sage subset methods such as `RealSet.is_open()` without
turning every topological subset constructor into a root constructor.

| Sage subset method | Target topological-space method | Justification | Consequence |
| --- | --- | --- | --- |
| `RealSet.is_open()` | `X.is_open(U: Subset) -> bool` | Openness is a predicate of a subset relative to an ambient topological space. | `U.is_open()` migrates to `U.ambient().is_open(U)` unless a subobject convenience method is separately admitted. |
| `RealSet.is_closed()` | `X.is_closed(U: Subset) -> bool` | Closedness is relative to an ambient topological space. | `U.is_closed()` migrates to `U.ambient().is_closed(U)`. |
| `RealSet.closure()` | `X.closure(U: Subset) -> Subset` | Closure is the smallest closed subset of the ambient space containing `U`. | `U.closure()` migrates to `U.ambient().closure(U)`. |
| `RealSet.interior()` | `X.interior(U: Subset) -> Subset` | Interior is the largest open subset of the ambient space contained in `U`. | `U.interior()` migrates to `U.ambient().interior(U)`. |
| `RealSet.boundary()` | `X.boundary(U: Subset) -> Subset` | Boundary is a subset of the ambient space determined by closure and interior. | `U.boundary()` migrates to `U.ambient().boundary(U)`. |
| `RealSet.is_connected()` as a no-argument category fact | `X.is_connected() -> bool` | Connectedness is a property of the whole topological space. | Keep no-argument connectedness at root. |
| `RealSet.is_compact()` as a no-argument category fact | `X.is_compact() -> bool` | Compactness is a property of the whole topological space. | Keep no-argument compactness at root and add a compact subcategory. |

## RealSet Ambient-Recovery Decision

Real-line subset methods recover through the ambient-relative topological-space surface.
For a real subset `U`, the public route is:

- `U.ambient().is_open(U)` for openness;
- `U.ambient().is_closed(U)` for closedness;
- `U.ambient().closure(U)` for closure;
- `U.ambient().interior(U)` for interior;
- `U.ambient().boundary(U)` for boundary.

The owner remains `TopologicalSpaces().ParentMethods`. `RealSet` compatibility methods
are Sage-backed convenience methods on a topological subobject of the real line; they do
not create a second owner and should not be specified as pure set methods. The return
objects for `closure`, `interior`, and `boundary` are subsets of the same ambient
topological space, refined as real-line subsets when the constructor path is Sage
`RealSet`.

Do not implement category-level wrapper methods on `_RealSets` that merely override
Sage's existing `RealSet` methods before the ambient topological methods have concrete
implementations. The spec obligation is the ownership route and the migration rule:
existing Sage no-argument calls migrate conceptually to the ambient-relative form.

## Constructor Candidate Mapping

`TopologicalSpaces().Constructors()` stays empty for now. Named sets belong under
`Sets().Constructors()` even when they refine into topological spaces or topological
subobjects. This is the current discoverability rule: users first look for named set
objects in `Sets().Constructors()`, and later this can be centralized through aggregate
constructor exposure from subcategories or through `Cat`.

| Sage constructor surface | Candidate path | Mapping status | Reason |
| --- | --- | --- | --- |
| No standalone `TopologicalSpace(...)` constructor found in Sage category source | No generic constructor | Mathematically justified non-mapping | A generic constructor would require arbitrary topology data and is not present in the inventoried Sage category. |
| `RR` / `RealField()` | `Sets().Constructors().RR()` refined into `Sets().Topological()` | Mapped to set constructors | The real line is a named set object with extra structure. It should not force a topological constructor namespace. |
| `RealSet.real_line()` | `Sets().Constructors().RealLine()` | Mapped to set constructors | The real line as a real subset is a topological subobject of itself. |
| `RealSet.open(a, b)` | `Sets().Constructors().OpenRealInterval(lower, upper)` | Mapped to set constructors | Open intervals are named real subsets and topological subobjects of the real line. |
| `RealSet.closed(a, b)` | `Sets().Constructors().ClosedRealInterval(lower, upper)` | Mapped to set constructors | Closed intervals are named real subsets and topological subobjects of the real line. |
| `RealSet.open_closed(a, b)` | `Sets().Constructors().OpenClosedRealInterval(lower, upper)` | Mapped to set constructors | Half-open intervals are named real subsets and topological subobjects of the real line. |
| `RealSet.closed_open(a, b)` | `Sets().Constructors().ClosedOpenRealInterval(lower, upper)` | Mapped to set constructors | Half-open intervals are named real subsets and topological subobjects of the real line. |
| `RealSet.unbounded_below_open(bound)` | `Sets().Constructors().UnboundedBelowOpenRealInterval(bound)` | Mapped to set constructors | Rays are named real subsets and topological subobjects of the real line. |
| `RealSet.unbounded_below_closed(bound)` | `Sets().Constructors().UnboundedBelowClosedRealInterval(bound)` | Mapped to set constructors | Rays are named real subsets and topological subobjects of the real line. |
| `RealSet.unbounded_above_open(bound)` | `Sets().Constructors().UnboundedAboveOpenRealInterval(bound)` | Mapped to set constructors | Rays are named real subsets and topological subobjects of the real line. |
| `RealSet.unbounded_above_closed(bound)` | `Sets().Constructors().UnboundedAboveClosedRealInterval(bound)` | Mapped to set constructors | Rays are named real subsets and topological subobjects of the real line. |
| `RealSet.point(p)` | `Sets().Constructors().RealPoint(p)` | Mapped to set constructors | A singleton is first a finite set/subset and only becomes a topological space relative to an ambient topology. |
| `RealSet.interval(lower, upper, *, lower_closed, upper_closed)` | `Sets().Constructors().RealSetInterval(lower, upper, lower_closed=..., upper_closed=...)` | Mapped to set constructors | This is the universal interval/ray constructor. Named interval and ray constructors call it with fixed endpoint-closure booleans. |
| Variadic `RealSet(*args)` | No catch-all constructor | Mathematically justified non-mapping | Sage accepts finite data shapes, symbolic relations, and manifold objects. The project API requires closed overloads and mathematical names. |
| `RealSet(..., structure='differentiable')`, `ambient=...`, `names=...`, `coordinate=...` | No path in this subtree | Mathematically justified non-mapping | These route to differentiable real manifolds or manifold subsets. |
| `RealIntervalField`, `ComplexIntervalField`, `RealBallField`, `ComplexBallField` constructors | Ring/field constructor paths, with topological methods imported from this subtree | Justified non-mapping as topological-space constructors | These constructors create algebraic/numerical fields or elements, not pure topological spaces. Their topology-bearing behavior should be recovered through topological ring/field categories. |
| Manifolds, varieties, schemes, hyperbolic models, polyhedra, CW complexes, simplicial complexes, and simplicial sets | Their own mathematical subtrees | Justified non-mapping | Each object carries extra structure beyond a bare topology. |

Topological rings, modules, and algebras inherit their topological-space surface from
`topological_spaces` and their algebraic surface from their own subtree. That is how
real intervals, complex intervals, and real or complex balls should recover topological
predicates without becoming topological-space constructors.

## Topological Ring And Field Recovery

The public owner for topological predicates and ambient-relative transforms stays in
`TopologicalSpaces()`, even when the object also lies in a ring or field category. The
existing spec anchors are:

- `category_specs/topological_spaces/__init__.py`, where `TopologicalSpaces()` owns
  `is_open`, `is_closed`, `closure`, `interior`, `boundary`, `is_connected`, and
  `is_compact`;
- `category_specs/rings/subcategories/topological.py`, where `Rings().Topological()`
  records the ring-side topological category edge without redefining those methods.

Accordingly, topological rings and fields recover topological behavior by
inheritance/join:

| Object kind | Entry constructor namespace | Recovered topological surface | Non-topological owner that remains primary for construction |
| --- | --- | --- | --- |
| Real/complex precision fields and their fixed precision objects | `Rings().Constructors()` / field constructor routes | `TopologicalSpaces()` and metric refinements when source-backed | `Rings()` / `Fields()` and precision-field subcategories |
| Interval and ball fields | Ring/field constructor routes in `rings` | `TopologicalSpaces()` through the topological ring/field path | Interval/ball field subcategories in `rings` |
| p-adic and q-adic rings and fields | Ring/field constructor routes in `rings` | `TopologicalSpaces()` through `Rings().Topological()` or field refinements | p-adic and q-adic ring/field subcategories |

Migration consequence:

- `TopologicalSpaces().Constructors()` remains empty for these objects.
- A ring or field constructor keeps returning a ring or field object.
- Once refined into a topological ring/field category, the object inherits
  topological predicates from `TopologicalSpaces()` without duplicating method
  ownership in the ring subtree.

Rejection condition for future edits:

- do not admit interval fields, ball fields, p-adic fields, or other rings/fields as
  pure `TopologicalSpaces().Constructors()` entries;
- do not move constructor ownership away from `rings`;
- do not create ring-local duplicates of the root topological predicates or transforms.

## Resolved Constructor and Metric Decisions

Named set constructors live in `Sets().Constructors()` for now. The result then refines
into every category whose structure it satisfies, including `TopologicalSpaces()` and
`TopologicalSpaces().Subobjects()` for real-line subsets. `TopologicalSpaces()` owns
the topological method surface, not the named-constructor namespace.

The interval API keeps both the universal endpoint/closure constructor and named
constructors for the common endpoint patterns. The universal constructor is
unambiguous because two endpoints and two closure booleans determine the subset of the
real line. Named constructors are discoverable spellings over that universal shape.

Metric spaces expose `metric()` for the metric map and `dist(x, y)` for its evaluation.
Metric elements expose `x.dist(y)` as delegation to the parent metric space. Metric
homsets are the short-map homsets; ordinary continuous maps remain the homsets of the
root topological category.

## Canonical Smoke Examples

Use these examples for the first topological smoke assertions:

| Target | Canonical object | Constructor owner | Witness |
| --- | --- | --- | --- |
| `TopologicalSpaces().Connected()` | `Sets().Constructors().OpenRealInterval(0, 1)` | `Sets().Constructors()` via `RealSet.open(0, 1)` | Sage refines `(0, 1)` into connected topological spaces; the project constructor also refines into `TopologicalSpaces().Connected()`. |
| `TopologicalSpaces().Compact()` | `Sets().Constructors().ClosedRealInterval(0, 1)` | `Sets().Constructors()` via `RealSet.closed(0, 1)` | Sage refines `[0, 1]` into compact topological spaces; the project constructor also refines into `TopologicalSpaces().Compact()`. |
| `TopologicalSpaces().Metric().Complete()` | `Sets().Constructors().RR()` / Sage `RR` | `Sets().Constructors()` for the named set object; ring ownership stays in `Rings().Constructors()` | Local Sage observation shows `RR.category()` is a join containing complete metric spaces. Project smoke should wait for the topological ring/field recovery path to refine `RR` through `TopologicalSpaces().Metric().Complete()`. |

Do not use `RealIntervalField`, `ComplexIntervalField`, `RealBallField`, or
`ComplexBallField` as complete-metric smoke examples in this subtree. The inventory
records them as topology-bearing ring/field evidence, not as Sage metric-space parents.
Their recovery belongs to the topological ring/field cards.

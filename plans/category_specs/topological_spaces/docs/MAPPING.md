# Topological Spaces Mapping

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
| Sage `metric_function()` | `MetricSpace.metric_function()` or `MetricSpace.metric()` decision | Sage has both names, with `metric` as a deprecated alias. The mathematical noun is the metric. | Needs a naming decision before editing metric stubs; do not preserve both names by aliasing blindly. |
| Sage `dist(a, b)` on metric parents | `MetricSpace.dist(x, y)` | Distance between two points is a metric-space method. | Keep as a metric root method. |
| Sage element `dist(b)` | Element-level metric method | The receiver is a point in a metric space. | Needs a decision whether point-distance belongs in `MetricSpacesElement` or remains recovered through the parent method. |
| Sage element `abs()` | Structured metric/ring method, not pure topological | Absolute value uses the distinguished zero and additive/ring structure in Sage's default implementation. | Map through topological ring/field or normed additive structure, not the pure topological-space root. |
| Sage metric homsets | `TopologicalSpaces().Metric().HomCategory()` refinement | Sage describes metric maps as Lipschitz maps with constant 1. | Needs a hom-category decision: continuous maps live at topological root; metric maps require a stricter metric-hom subcategory. |
| Sage product metric | `TopologicalSpaces().Metric().CartesianProducts()` | Product metric is the maximum of factor distances in Sage. | Keep metric product behavior in the metric subcategory, separate from product topology. |

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

## Constructor Candidate Mapping

`TopologicalSpaces().Constructors()` must remain small. It must not collect every Sage
constructor for every object with a topology.

| Sage constructor surface | Candidate path | Mapping status | Reason |
| --- | --- | --- | --- |
| No standalone `TopologicalSpace(...)` constructor found in Sage category source | No generic constructor | Mathematically justified non-mapping | A generic constructor would require arbitrary topology data and is not present in the inventoried Sage category. |
| `RealSet.real_line()` | `TopologicalSpaces().Constructors().real_line()` | Concrete future candidate | The real line is a pure topological space and also the ambient for real subsets. |
| `RealSet.open(a, b)` | `TopologicalSpaces().Constructors().open_interval(lower, upper)` | Concrete future candidate | Open intervals are pure subspaces of the real line when manifold keywords are absent. |
| `RealSet.closed(a, b)` | `TopologicalSpaces().Constructors().closed_interval(lower, upper)` | Concrete future candidate | Closed intervals are compact connected real-line subspaces when bounded. |
| `RealSet.open_closed(a, b)` | `TopologicalSpaces().Constructors().open_closed_interval(lower, upper)` | Concrete future candidate | Half-open intervals are pure real-line subspaces. |
| `RealSet.closed_open(a, b)` | `TopologicalSpaces().Constructors().closed_open_interval(lower, upper)` | Concrete future candidate | Half-open intervals are pure real-line subspaces. |
| `RealSet.unbounded_below_open(bound)` | `TopologicalSpaces().Constructors().open_ray_below(bound)` | Concrete future candidate | This is a pure ray in the real line. |
| `RealSet.unbounded_below_closed(bound)` | `TopologicalSpaces().Constructors().closed_ray_below(bound)` | Concrete future candidate | This is a pure ray in the real line. |
| `RealSet.unbounded_above_open(bound)` | `TopologicalSpaces().Constructors().open_ray_above(bound)` | Concrete future candidate | This is a pure ray in the real line. |
| `RealSet.unbounded_above_closed(bound)` | `TopologicalSpaces().Constructors().closed_ray_above(bound)` | Concrete future candidate | This is a pure ray in the real line. |
| `RealSet.point(p)` | `Sets().Constructors()` or `TopologicalSpaces().Constructors().singleton_subspace(p)` | `NEEDS_DECISIONS` | A singleton is first a finite set and only becomes a topological space relative to an ambient topology. |
| `RealSet.interval(lower, upper, *, lower_closed, upper_closed)` | Closed overload family over the named interval/ray constructors | `NEEDS_DECISIONS` | The closure flags are explicit, but the target API should choose whether to keep a flag-bearing constructor or force named interval constructors only. |
| Variadic `RealSet(*args)` | No catch-all constructor | Mathematically justified non-mapping | Sage accepts finite data shapes, symbolic relations, and manifold objects. The project API requires closed overloads and mathematical names. |
| `RealSet(..., structure='differentiable')`, `ambient=...`, `names=...`, `coordinate=...` | No path in this subtree | Mathematically justified non-mapping | These route to differentiable real manifolds or manifold subsets. |
| `RealIntervalField`, `ComplexIntervalField`, `RealBallField`, `ComplexBallField` constructors | Ring/field constructor paths, with topological methods imported from this subtree | Justified non-mapping as topological-space constructors | These constructors create algebraic/numerical fields or elements, not pure topological spaces. Their topology-bearing behavior should be recovered through topological ring/field categories. |
| Manifolds, varieties, schemes, hyperbolic models, polyhedra, CW complexes, simplicial complexes, and simplicial sets | Their own mathematical subtrees | Justified non-mapping | Each object carries extra structure beyond a bare topology. |

Topological rings, modules, and algebras inherit their topological-space surface from
`topological_spaces` and their algebraic surface from their own subtree. That is how
real intervals, complex intervals, and real or complex balls should recover topological
predicates without becoming topological-space constructors.

## Concrete Future Decisions

These decisions should move to root `NEEDS_DECISIONS.md` in a later interactive pass.

| Decision | Options | Why it blocks constructor admission |
| --- | --- | --- |
| Real-line constructor owner | Put named real-line constructors under `TopologicalSpaces().Constructors()`, or keep them under `Sets().Constructors()` / a real-subset subtree and only refine into `TopologicalSpaces()`. | `RealSet` is simultaneously a set, subobject, and topological space. The constructor namespace determines the future smoke labels. |
| Subset convenience methods | Require only ambient methods such as `X.is_open(U)`, or also add convenience methods such as `U.is_open()` on topological subobjects. | Sage exposes subset methods, while the mathematical root method is ambient-relative. |
| `RealSet.interval` flags | Keep one explicit flag-bearing constructor, or require named constructors for each endpoint pattern. | The no-variadic rule allows explicit named arguments, but named endpoint constructors are easier to smoke and migrate. |
| Metric name | Use `metric(x, y)` only, or also expose `metric_function()` because Sage uses it and deprecates `metric` as an alias. | This changes the metric method surface and regression mapping. |
| Metric element methods | Add `point.dist(other)` and possibly `point.abs()`, or require parent-mediated `X.dist(x, y)` only. | Sage exposes both parent and element methods; `abs()` depends on additional algebraic structure. |
| Complete metric examples | Use Sage's `RR.cartesian_product(RR)`, a local constructor, or another canonical metric-space object for future smokes. | The local subcategory exists, but no constructor example has been admitted. |

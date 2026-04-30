# Topological Spaces Mapping

Topological spaces are sets with a topology. The target hierarchy therefore has a
dedicated `topological_spaces` subtree, and `Sets().Topological()` is that category,
not a set-local duplicate.

| Source concept | Target category | Justification | Consequence |
| --- | --- | --- | --- |
| `Sets().Topological()` | `TopologicalSpaces()` | A set with a topology is precisely a topological space. | There is one category surface, exposed from both names. |
| `Sets().Metric()` | `TopologicalSpaces().Metric()` | A metric space is a topological space whose topology is induced by a metric. | Metric methods refine the topological-space surface through the `Metric` axiom. |
| `RealSet` topology | `TopologicalSpaces()` plus `Sets().Subobjects()` | A real subset inherits topology from the real line and is also a subobject of that ambient line. | Real-line methods use `RealSubset`, `RealOpenSet`, and `RealInterval` vocabulary. |
| Metric balls | `MetricBall` type vocabulary | In any metric space, an open ball is an open subset of the underlying set. | `ball(center, radius)` returns `MetricBall`, not a generic set. |

Topological rings, modules, and algebras inherit their topological-space surface from
`topological_spaces` and their algebraic surface from their own subtree. The remaining
open work is constructor inventory and wiring, not mathematical ownership of the
topological methods.

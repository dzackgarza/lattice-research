# Topological Spaces Mapping

Topological spaces are sets with a topology. The target hierarchy therefore has a
dedicated `topological_spaces` subtree while preserving navigation from `Sets()`.

| Source concept | Target category | Justification | Consequence |
| --- | --- | --- | --- |
| `Sets().Topological()` | `TopologicalSpaces()` | A set with a topology is precisely a topological space. | Set-backed topological objects use the topological-space method surface, not a set-local duplicate. |
| `Sets().Metric()` | `TopologicalSpaces().Metric()` | A metric space is a topological space whose topology is induced by a metric. | Metric methods refine the topological-space surface. |
| `RealSet` topology | `TopologicalSpaces()` plus `Sets().Subobjects()` | A real subset inherits topology from the real line and is also a subobject of that ambient line. | Real-line methods use `RealSubset`, `RealOpenSet`, and `RealInterval` vocabulary. |

# Topological Spaces Sage Inventory

Source for this initial pass: the existing set subtree topological surface and Sage
`Sets().Topological()` / `Sets().Metric()` navigation.

| Sage surface | Target category | Method surface to represent |
| --- | --- | --- |
| `SageSets().Topological()` | `TopologicalSpaces()` = `Sets().Topological()` | `is_connected`, `closure`, `interior`, `boundary`, `is_open`, `is_closed`, `is_compact`. |
| `SageSets().Metric()` | `TopologicalSpaces().Metric()` = `Sets().Metric()` | `metric`, `ball`, `dist`, plus the inherited topological-space surface. |

## Inventory Gaps

- Sage topological-space constructors beyond set-backed objects have not yet been
  inventoried.
- Interactions with topological rings, modules, and algebras need a later pass after
  those subtrees are reorganized.

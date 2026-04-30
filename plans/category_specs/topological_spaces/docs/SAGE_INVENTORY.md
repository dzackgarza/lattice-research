# Topological Spaces Sage Inventory

Source for this initial pass: the existing set subtree topological surface and Sage
`Sets().Topological()` / `Sets().Metric()` navigation.

| Sage surface | Sage meaning | Method surface |
| --- | --- | --- |
| `SageSets().Topological()` | Sage topological refinement under `Sets()` | `is_connected`, `closure`, `interior`, `boundary`, `is_open`, `is_closed`, `is_compact`. |
| `SageSets().Metric()` | Sage metric refinement under `Sets()` | `metric`, `ball`, `dist`, plus the inherited topological-space surface. |

## Inventory Gaps

- Sage topological-space constructors beyond set-backed objects have not yet been
  inventoried.
- Sage topological ring, module, and algebra category surfaces are not inventoried in
  this file.

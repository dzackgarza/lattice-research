---
trackerStatus:
  type: task
title: Split boolean and optional return-shape signatures
---
# Split boolean and optional return-shape signatures
Source: pasted backlog 2026-05-02.

Task: split the mixed boolean|None and T|None return-type signatures on Category and Map classes into explicit @overload declarations.

## Complexity Justification
- Owner: C55
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Split boolean and optional return-shape signatures
- Why this specific score:
  - This is a typed-API refactor scoped to category/map methods, but it touches many call signatures and forces coherent overload behavior across public methods. The risk is concentrated (typing correctness) rather than runtime behavior, matching a moderate complexity window.
- Item-specific evidence:
  - The task is tightly scoped to `Category` and `Map` return-shape changes and calls out `bool|None` / `T|None` unbundling, indicating a coordinated but bounded interface contract clean-up.
  - No additional files are named, so validation burden is mostly static typing consistency and downstream method callsites.

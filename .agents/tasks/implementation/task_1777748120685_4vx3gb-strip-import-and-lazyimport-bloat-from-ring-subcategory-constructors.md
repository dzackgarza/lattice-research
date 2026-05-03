---
trackerStatus:
  type: task
title: Strip import and LazyImport bloat from ring subcategory constructors
status: to-do
priority: high
planId: PLN-SAGE-000
progress: 0
tags:
- category-specs
- implementation
- task
- constructors
- rings
- imports
- theme-constructor-routing
---

# Strip import and LazyImport bloat from ring subcategory constructors
Source: pasted backlog 2026-05-02.

Task: strip import and LazyImport bloat from the ring subcategory constructors, fix the public surface to use canonical constructors.

## Complexity Justification
- Owner: C58
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Strip import and LazyImport bloat from ring subcategory constructors
- Why this specific score:
  - This is a focused cleanup in the ring subcategory constructor path with moderate coupling: import/lazy-import shape and canonical constructor exposure both affect module load behavior and API consistency, but only within a bounded surface.\n  - The item is not about novel algorithmic behavior, keeping the work in the mid band.
- Item-specific evidence:
  - The file states a concrete cleanup boundary (`ring subcategory constructors`) and a specific end-state (`canonical constructors`), giving a constrained verification target.
  - The evidence suggests deterministic refactoring rather than speculative implementation changes.

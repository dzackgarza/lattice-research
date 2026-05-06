---
id: TASK-1777748120685-4VX3GB-STRIP-IMPORT-AND-LAZYIMPORT-BLOAT-FROM-RING-SUBCATEGORY-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Strip import and LazyImport bloat from ring subcategory constructors
status: unstarted
priority: high
description: Strip import and LazyImport bloat from ring subcategory constructors
successCriteria:
- Strip import and LazyImport bloat from ring subcategory constructors is resolved
  according to the body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
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

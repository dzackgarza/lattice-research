---
trackerStatus:
  type: task
title: Move nontrivial algebra construction out of category constructors
status: to-do
priority: high
planId: PLN-SAGE-000
progress: 0
tags:
- category-specs
- implementation
- task
- constructors
- algebras
- theme-constructor-routing
---

# Move nontrivial algebra construction out of category constructors
Source: pasted backlog 2026-05-02.

Task: move nontrivial algebra construction (Zmod, Cyclotomic, NumberField, etc.) out of category constructors, restrict to lightweight wrapper logic.

## Complexity Justification
- Owner: C77
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Move nontrivial algebra construction out of category constructors
- Why this specific score:
  - This task is high-coupling by design: lifting substantial algebra-construction behavior out of category constructors affects constructor semantics, import layering, and initialization pathways across multiple algebra families (Zmod, Cyclotomic, NumberField).
- Item-specific evidence:
  - The text explicitly calls out nontrivial constructions (`Zmod`, `Cyclotomic`, `NumberField`) and a hard behavior boundary (`lightweight wrapper logic`), which increases migration and compatibility risk.
  - Complexity is validated by expected downstream behavior shifts rather than small typed annotation edits.

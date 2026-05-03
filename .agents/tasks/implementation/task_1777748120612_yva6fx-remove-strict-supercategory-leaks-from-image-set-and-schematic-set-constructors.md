---
trackerStatus:
  type: task
title: Remove strict-supercategory leaks from image-set and schematic-set constructors
status: to-do
priority: critical
planId: PLN-SAGE-000
progress: 0
tags:
- category-specs
- implementation
- task
- constructors
- sets
- theme-audit-uniformity
---

# Remove strict-supercategory leaks from image-set and schematic-set constructors
Source: pasted backlog 2026-05-02.

Task: remove strict-supercategory leakage from diagram-set/image-set/schematic-set constructors, restrict inputs to the correct base category.

## Complexity Justification
- Owner: C61
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Remove strict-supercategory leaks from image-set and schematic-set constructors
- Why this specific score:
  - This task likely edits multiple constructor categories (`diagram-set`, `image-set`, `schematic-set`) and their inheritance constraints. Tightening category restrictions can break typed and runtime assumptions across callers, so coupling and verification cost are high but still localized to category wiring.
- Item-specific evidence:
  - The task statement directly names supercategory leak removal as the mechanism, implying non-local effect on constructor input validation paths rather than only one function.
  - The explicit owner 61 maps cleanly to this high-but-bounded migration risk.

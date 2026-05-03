---
trackerStatus:
  type: task
title: Remove Sage option bags from number-field and rational-field constructors
status: to-do
priority: critical
planId: PLN-SAGE-000
progress: 0
tags:
- category-specs
- implementation
- task
- constructors
- sage
- signatures
- theme-audit-uniformity
---

# Remove Sage option bags from number-field and rational-field constructors
Source: pasted backlog 2026-05-02.

Task: excise Sage option bags from number-field and rational-field constructors, use explicit keyword arguments on the new public surface.

## Complexity Justification
- Owner: C55
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Remove Sage option bags from number-field and rational-field constructors
- Why this specific score:
  - This is a public constructor cleanup across number/rational field entry points, with compatibility risk at constructor callsites but a bounded module surface. The work is mostly API hygiene plus argument-shape migration, which is moderately coupled and verification-heavy enough to stay in 41-60.
- Item-specific evidence:
  - The file explicitly targets constructor semantics rather than runtime algorithms, so complexity is driven by argument migration and downstream ripple through calling code.
  - No new test or acceptance list is embedded, which means the task’s own evidence focuses on implementation breadth more than checklist-driven branching.

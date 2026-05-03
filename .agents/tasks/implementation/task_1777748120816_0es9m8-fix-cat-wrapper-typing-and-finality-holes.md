---
trackerStatus:
  type: task
title: Fix Cat wrapper typing and finality holes
---
# Fix Cat wrapper typing and finality holes
Source: pasted backlog 2026-05-02.

Task: fix Cat wrapper typing (explicit type parameters, correct variance), fill finality holes on concrete Cat subclasses, and excise Sage option bags from the public surface.

## Complexity Justification
- Owner: C70
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Fix Cat wrapper typing and finality holes
- Why this specific score:
  - This item explicitly spans typing semantics (`explicit type parameters`, variance) and class contract enforcement (`@final` gaps) on concrete Cat subclasses, so it touches both static and inheritance behavior in the wrapper layer.
- Item-specific evidence:
  - Multiple coupled remediation vectors are listed in one task, indicating higher coordination than isolated method edits.
  - The coupling to wrapper surfaces justifies the high band because regressions can propagate through consumers of category wrappers.

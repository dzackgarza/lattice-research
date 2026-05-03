---
trackerStatus:
  type: task
title: Add missing final markers and return annotations on Cat methods
---
# Add missing final markers and return annotations on Cat methods
Source: pasted backlog 2026-05-02.

Task: add missing @final markers to concrete Cat methods, annotate return types, and excise Sage option bags from the public surface.

## Complexity Justification
- Owner: C57
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Add missing final markers and return annotations on Cat methods
- Why this specific score:
  - The task combines two intertwined quality gates (`@final` markers and return annotations), both affecting multiple Cat methods. This is broader than a signature-only change because enforcement affects inheritance contracts and static interface guarantees, but it remains a targeted API-hardening pass.
- Item-specific evidence:
  - It directly lists multiple change vectors in one line item (annotations, finality, option-bag removal), which raises coupling while still keeping scope within public Cat method surfaces.
  - The work is implementation-safe but verification-sensitive due to inheritance and type-surface consistency checks.

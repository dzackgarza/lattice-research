---
trackerStatus:
  type: task
title: Audit standard type-package aliases after concrete Cat migration
status: to-do
priority: critical
planId: PLN-CAT-100
progress: 0
tags:
- category-specs
- implementation
- task
- cat
- types
- audit
- theme-audit-uniformity
---

# Audit standard type-package aliases after concrete Cat migration
Source: pasted backlog 2026-05-02.

Task: audit standard type-package aliases (Set, Matrix, etc.) and ensure they point to the new project types after the concrete Cat migration.

## Complexity Justification
- Owner: C54
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Audit standard type-package aliases after concrete Cat migration
- Why this specific score:
  - This is a consistency audit across the naming layer (`Set`, `Matrix`, etc.) after migration. The work is moderate because it is less about introducing new behavior and more about verifying and realigning alias mappings across the project boundary.
- Item-specific evidence:
  - The file explicitly anchors scope to post-migration alias audit, which typically has hidden dependency impacts but a bounded surface if executed as verification-heavy pass.

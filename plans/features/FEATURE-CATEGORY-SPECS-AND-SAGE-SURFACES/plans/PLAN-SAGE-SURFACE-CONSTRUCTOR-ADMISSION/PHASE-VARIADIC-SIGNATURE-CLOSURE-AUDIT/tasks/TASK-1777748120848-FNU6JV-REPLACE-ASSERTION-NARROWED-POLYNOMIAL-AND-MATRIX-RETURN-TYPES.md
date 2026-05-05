---
id: TASK-1777748120848-FNU6JV-REPLACE-ASSERTION-NARROWED-POLYNOMIAL-AND-MATRIX-RETURN-TYPES
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Replace assertion-narrowed polynomial and matrix return types
status: unstarted
priority: high
description: Replace assertion-narrowed polynomial and matrix return types
successCriteria:
- Replace assertion-narrowed polynomial and matrix return types is resolved according to the
  body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
- category-specs
- task
- matrix
- types
- theme-rings-algebras
---
# Replace assertion-narrowed polynomial and matrix return types
Source: pasted backlog 2026-05-02.

Task: replace assertion-narrowed polynomial and matrix return types (via result of isinstance checks) with proper static union types using X|None patterns.

## Complexity Justification
- Owner: C55
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Replace assertion-narrowed polynomial and matrix return types
- Why this specific score:
  - The complexity is moderate because this is primarily a type-system replacement task with explicit static behavior (`isinstance`-based narrowing -> explicit union types). It is broader than a pure annotation tweak, but avoids cross-module architectural redesign.
- Item-specific evidence:
  - The mention of `polynomial`, `matrix`, and `X|None` patterns defines precise implementation targets in return-type APIs.
  - No external acceptance checklist is embedded, so the cost is localized to type-correctness migration across the named return surfaces.

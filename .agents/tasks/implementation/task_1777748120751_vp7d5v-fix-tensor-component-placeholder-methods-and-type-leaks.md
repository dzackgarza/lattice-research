---
trackerStatus:
  type: task
title: Fix tensor-component placeholder methods and type leaks
status: to-do
priority: critical
planId: SPR-ALG-TENSOR-01KQN9
progress: 0
tags:
- category-specs
- implementation
- task
- tensors
- types
- theme-audit-uniformity
---

# Fix tensor-component placeholder methods and type leaks
Source: pasted backlog 2026-05-02.

Task: fix tensor-component placeholder methods that incorrectly return self or return None, add missing @final markers, and excise Sage option bags from the public surface.

## Complexity Justification
- Owner: C69
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Fix tensor-component placeholder methods and type leaks
- Why this specific score:
  - The task spans tensor-component behavior, return-type correctness, and constructor-surface hygiene simultaneously. Placeholder return fixes (`self`/`None`) can silently affect call contracts, so this carries higher impact than pure signature cleanup and justifies a high band.
- Item-specific evidence:
  - It names concrete risk vectors (`type leaks`, `@final` markers, `Sage option bags`) rather than a single-file rename, so validation must cover both runtime and typing expectations.

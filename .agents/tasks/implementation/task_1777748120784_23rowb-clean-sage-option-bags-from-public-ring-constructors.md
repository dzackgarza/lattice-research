---
trackerStatus:
  type: task
title: Clean Sage option bags from public ring constructors
---
# Clean Sage option bags from public ring constructors
Source: pasted backlog 2026-05-02.

Task: clean Sage option bags from public ring constructors (MatrixSpace, VectorSpace, etc.), use explicit keyword arguments.

## Complexity Justification
- Owner: C56
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Clean Sage option bags from public ring constructors
- Why this specific score:
  - This is a constrained API migration touching public ring constructors (`MatrixSpace`, `VectorSpace`, etc.). The work is moderately complex because it replaces loosely typed option-bag passing with explicit keywords while preserving constructor behavior.
- Item-specific evidence:
  - The explicit constructor list gives a bounded set of callsites, with no new domain boundaries beyond public interface normalization.
  - The owner reflects moderate risk: more than typing-only edits, but less than cross-subsystem redesign.

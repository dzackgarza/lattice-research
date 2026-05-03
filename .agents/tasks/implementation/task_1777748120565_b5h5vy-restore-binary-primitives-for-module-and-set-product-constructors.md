---
trackerStatus:
  type: task
title: Restore binary primitives for module and set product constructors
status: to-do
priority: high
planId: PLN-SAGE-000
progress: 0
tags:
- category-specs
- implementation
- task
- constructors
- modules
- sets
- theme-constructor-routing
---

# Restore binary primitives for module and set product constructors
Source: pasted backlog 2026-05-02.

Task: restore the binary-only variants of the module and set product constructors, deprecate the n-ary forms, and add missing @final markers to the concrete implementations.

## Complexity Justification
- Owner: C58
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Restore binary primitives for module and set product constructors
- Why this specific score:
  - This work is confined to product-constructor APIs, but it enforces deprecation and behavior-preserving API transitions (`binary` vs `n-ary`) across module/set surfaces plus concrete implementation markers. That creates more than a trivial signature edit but not architecture-wide dependency spread.
- Item-specific evidence:
  - The task text explicitly constrains the scope to module and set product constructors and states both API migration steps and concrete `@final` enforcement.
  - There is a clear deprecation path and no explicit multi-file implementation plan, which narrows the verification burden to compatibility and consistency checks.

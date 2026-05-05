---
id: TASK-1777748120529-YQJMY7-SPLIT-MIXED-SET-CONSTRUCTOR-INPUT-SHAPES-INTO-NAMED-ALTERNATIVES
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Split mixed set-constructor input shapes into named alternatives
status: unstarted
priority: high
description: Split mixed set-constructor input shapes into named alternatives
successCriteria:
- Split mixed set-constructor input shapes into named alternatives is resolved according to
  the body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
- category-specs
- task
- constructors
- sets
- theme-constructor-routing
---
# Split mixed set-constructor input shapes into named alternatives
Source: pasted backlog 2026-05-02.

Task: split the mixed input shapes on set constructors (objects, collection, and single object) into explicit alternatives using @overload.

## Complexity Justification
- Owner: C56
- Complexity band: Moderate (41-60)
- Tracker type: task-work
- Title: Split mixed set-constructor input shapes into named alternatives
- Why this specific score:
  - The task touches multiple constructor overload surfaces for set creation, which is broader than a single method edit but still bounded to API typing. The complexity is moderate because behavior should remain same while call-shape space is decomposed, requiring careful static compatibility checks.
- Item-specific evidence:
  - The description explicitly names three constructor input alternatives (`objects`, `collection`, `single object`) and thus defines a clear but non-trivial decomposition scope.
  - Scope is explicit enough to avoid architecture-level uncertainty.

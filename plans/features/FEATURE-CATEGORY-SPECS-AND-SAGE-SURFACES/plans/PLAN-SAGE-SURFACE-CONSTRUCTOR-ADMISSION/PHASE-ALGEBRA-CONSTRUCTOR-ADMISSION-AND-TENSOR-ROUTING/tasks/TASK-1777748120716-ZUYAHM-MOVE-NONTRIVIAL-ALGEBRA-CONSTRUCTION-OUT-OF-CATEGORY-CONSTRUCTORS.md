---
id: TASK-1777748120716-ZUYAHM-MOVE-NONTRIVIAL-ALGEBRA-CONSTRUCTION-OUT-OF-CATEGORY-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING]]'
dependsOn: []
title: Move nontrivial algebra construction out of category constructors
status: needs-review
priority: high
description: Move nontrivial algebra construction out of category constructors
successCriteria:
- Move nontrivial algebra construction out of category constructors is resolved according
  to the body acceptance criteria.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-ALGEBRA-CONSTRUCTOR-ADMISSION-AND-TENSOR-ROUTING
---
# Move nontrivial algebra construction out of category constructors
Source: pasted backlog 2026-05-02.

Task: move nontrivial algebra construction (Zmod, Cyclotomic, NumberField, etc.) out of category constructors, restrict to lightweight wrapper logic.

## Complexity Justification
- Owner: C77
- Complexity band: High (61-80)
- Tracker type: task-work
- Title: Move nontrivial algebra construction out of category constructors
- Why this specific score:
  - This task is high-coupling by design: lifting substantial algebra-construction behavior out of category constructors affects constructor semantics, import layering, and initialization pathways across multiple algebra families (Zmod, Cyclotomic, NumberField).
- Item-specific evidence:
  - The text explicitly calls out nontrivial constructions (`Zmod`, `Cyclotomic`, `NumberField`) and a hard behavior boundary (`lightweight wrapper logic`), which increases migration and compatibility risk.
  - Complexity is validated by expected downstream behavior shifts rather than small typed annotation edits.

## Work Log

- 2026-05-06 implementation review: the current algebra constructor surface does
  not directly construct `Zmod`, cyclotomic fields, number fields, or comparable
  nontrivial algebra parents inside category constructors. It keeps category
  constructors to named routing/refinement logic over Sage-backed objects:
  `FreeAlgebra`, source-category `S.algebra(R, category=...)`, and
  `FiniteDimensionalAlgebra` reached only after tensor-component construction.
  This matches the boundary in `SPEC-MAPPING-ALGEBRAS` that nontrivial raw
  constructor shapes are not public algebra category constructors.
- 2026-05-06 validation: `just --justfile category_specs/justfile smoke-file
  algebras/smoketest.sage` passes. Status moved to `needs-review`; this does
  not mark the card accepted or complete.

## Negative Finding

- Searched: `rg -n "Zmod|Cyclotomic|NumberField" category_specs/algebras`;
  `category_specs/algebras/__init__.py`; `SPEC-MAPPING-ALGEBRAS`.
- Found: no direct algebra-constructor implementation route for `Zmod`,
  cyclotomic fields, or number fields in `category_specs/algebras`; the code and
  spec route constructor work through named lightweight Sage-backed routes and
  refinement.
- Conclusion: inference based on the checked algebra subtree and canonical
  mapping spec: the current algebra constructor surface satisfies this card's
  boundary by keeping these heavy constructors out of category constructors.
- Confidence: High.
- Gaps: other subtrees may still mention these constructors for their own module,
  ring, or field surfaces; that is outside this algebra-constructor card.

---
id: TASK-1777748120784-23ROWB-CLEAN-SAGE-OPTION-BAGS-FROM-PUBLIC-RING-CONSTRUCTORS
trackerStatus:
  type: task
parents:
- '[[PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT]]'
dependsOn: []
title: Clean Sage option bags from public ring constructors
status: needs-review
priority: critical
description: Clean Sage option bags from public ring constructors
successCriteria:
- Matrix-ring constructor surface is explicit.
- Matrix element constructor split is explicit and documented.
- VectorSpace ownership is recorded as module-owned, not ring-owned.
- Current public ring constructors have no generic Sage option bag in code.
- Human review accepts the audit and closes the card.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT
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

## Implementation Result

- Current `Rings().Constructors().MatrixRing(base_ring, n, sparse=False, implementation=None)`
  already exposes explicit parameters and delegates internally to Sage
  `MatrixSpace(base_ring, n, n, sparse=sparse, implementation=implementation)`.
- Current square-matrix element construction is split in
  `category_specs/rings/matrix_algebras.py` into
  `zero_matrix()`, `matrix_from_matrix(matrix, *, coerce=True)`,
  `matrix_from_entries(entries, *, coerce=True)`,
  `matrix_from_rows(rows, *, coerce=True)`, and
  `scalar_matrix(scalar, *, coerce=True)`.
- Current `VectorSpace` construction is not ring-owned. It is explicitly mapped and
  implemented under `Modules(K).Constructors()` as `VectorSpace(dimension, sparse=False,
  *, inner_product_matrix=None)` plus named basis/inner-product variants.
- Updated `category_specs/rings/docs/MAPPING.md` so the `MatrixSpace.matrix` split
  records the concrete public method signatures and states that Sage's option bag is
  not public.

## Audit Evidence

- Searched: this task card, `category_specs/rings/__init__.py`,
  `category_specs/rings/matrix_algebras.py`, `category_specs/rings/docs/MAPPING.md`,
  `category_specs/rings/tests/regression/matrix_rings.sage`,
  `category_specs/rings/smoketest.sage`, `category_specs/modules/__init__.py`,
  `category_specs/modules/docs/MAPPING.md`, and textual searches for `MatrixRing`,
  `MatrixSpace`, `VectorSpace`, `zero_matrix`, `matrix_from`, `scalar_matrix`, `*args`,
  `**kwargs`, `kwds`, `opts`, and `options` under the rings/modules/algebras category
  surfaces.
- Found: no current public ring constructor body exposes `*args`, `**kwargs`, `kwds`,
  or a generic option bag. Remaining `kwds` / option-bag text in adjacent docs belongs
  to Sage source inventory or non-ring cards, not to the public ring constructor
  surface covered here.
- Conclusion: inference - the current implementation surface already satisfies this
  card; the durable correction is the updated ring mapping plus this owner-split audit.
- Confidence: High.
- Gaps: this pass did not close separate algebra option-bag or module wrapper cards.

## Acceptance Criteria

- [x] Matrix-ring constructor surface is explicit.
- [x] Matrix element constructor split is explicit and documented.
- [x] VectorSpace ownership is recorded as module-owned, not ring-owned.
- [x] Current public ring constructors have no generic Sage option bag in code.
- [ ] Human review accepts the audit and closes the card.

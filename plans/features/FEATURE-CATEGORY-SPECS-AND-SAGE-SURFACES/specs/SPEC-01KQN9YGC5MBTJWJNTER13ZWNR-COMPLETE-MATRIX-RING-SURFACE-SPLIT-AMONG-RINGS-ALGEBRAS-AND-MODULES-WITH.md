---
id: SPEC-01KQN9YGC5MBTJWJNTER13ZWNR-COMPLETE-MATRIX-RING-SURFACE-SPLIT-AMONG-RINGS-ALGEBRAS-AND-MODULES-WITH
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
title: Complete matrix ring surface split among rings algebras and modules without weakening
  the matrix smoke
status: needs-review
priority: critical
requirement: 'The deleted Rings triage recorded ring smoke blockers: nested axiom category
  identity mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
  split.'
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in the relevant
  MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No new implementation blocker was discovered during this docs/spec pass; the existing implementation
  proof remains the matrix smoke frontier.
- No ring constructor or axiom code changed, so the `rings/smoketest.sage` trigger did not
  apply in this pass.
- Constructor membership assertions were not weakened; the docs now preserve simultaneous
  ring/algebra/module refinement as the smoke expectation.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- category-specs
- smoke
- modules
- rings
- algebras
- matrix
- theme-rings-algebras
updated: '2026-05-05'
---
# Complete matrix ring surface split among rings algebras and modules without weakening the matrix smoke
## Summary

The deleted Rings triage recorded ring smoke blockers: nested axiom category identity
mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
split.

## Source Provenance

- The requested recovery path `git show 8d1c21c^:category_specs/rings/docs/TRIAGE.md`
  fails because the file still lived under `plans/category_specs/rings/docs/TRIAGE.md`
  at that parent commit.
- Exact recovered prior content came from
  `git show 8d1c21c^:plans/category_specs/rings/docs/TRIAGE.md`.
- Original migrated line: `Complete matrix ring surface split among rings algebras and modules without weakening the matrix smoke from category_specs/rings/docs/TRIAGE.md`
- Sage written-doc and source anchors used for this leaf:
  `https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_space.html`,
  `https://doc.sagemath.org/html/en/reference/modules/sage/modules/free_module.html`,
  `https://doc.sagemath.org/html/en/reference/rings/sage/rings/ring.html`,
  `category_specs/modules/docs/SAGE_INVENTORY.md`,
  and the current mapping docs in `rings`, `algebras`, and `modules`.

## Context

- ZZ, field constructors, p-adic constructors, and q-adic constructors fail through nested axiom category class-identity mismatches.
- IntegerModRing, PolynomialRing, PowerSeriesRing, LaurentSeriesRing, PuiseuxSeriesRing, and MatrixRing refine far enough to expose missing _sympy_.
- MatrixRing stays reachable from Rings().Constructors(), but the result must refine into Algebras(R) and Modules(R).Free().FiniteRank().
- The matrix smoke must not be moved or weakened to hide the surface split.

## Grounded Spec Contract

Grounding anchors:

- `category_specs/rings/docs/MAPPING.md`, especially the rows for `MatrixRing`,
  `MatrixSpace.matrix(...)`, and the `Matrix ring/algebra surface` organization rule.
- `category_specs/rings/docs/SAGE_INVENTORY.md`, especially the constructor-family row
  for `MatrixRing` and `MatrixSpace` when square.
- `category_specs/algebras/docs/MAPPING.md`, especially the row stating that
  matrix-ring algebra methods belong in `Algebras(R)` plus matrix-algebra
  subcategories.
- `category_specs/modules/docs/MAPPING.md`, especially the owner table for
  `Modules(R).Free().FiniteRank()` and the rule that vector-space/free-module structure
  stays in `modules`.

Grounded owner rule for this leaf:

- `Rings().Constructors().MatrixRing(...)` remains the constructor entry point because
  it creates the ambient square-matrix ring object.
- The constructed parent must refine simultaneously into the ring surface,
  the algebra surface over its base ring, and the free finite-rank module surface over
  that base ring.
- Method placement follows that split: ring operations stay in `rings`, algebra
  operations in `algebras`, and rank/basis/module operations in `modules`.

Required hypotheses and codomains:

- the object under discussion is a square matrix parent over a base ring `R`;
- the ring codomain is the matrix ring parent itself;
- the algebra codomain is the same parent viewed in `Algebras(R)` or the matrix-algebra
  refinement;
- the module codomain is the same parent viewed in `Modules(R).Free().FiniteRank()`.

Rejection/retirement condition:

- reject any spec move that collapses the owner split by relocating all matrix methods
  into one subtree, or that weakens matrix smoke expectations to avoid proving the same
  parent refines into rings, algebras, and modules simultaneously.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No new implementation blocker was discovered during this docs/spec pass; the existing implementation proof remains the matrix smoke frontier.
- [x] No ring constructor or axiom code changed, so the `rings/smoketest.sage` trigger did not apply in this pass.
- [x] Constructor membership assertions were not weakened; the docs now preserve simultaneous ring/algebra/module refinement as the smoke expectation.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Recovered the removed rings triage wording from
  `plans/category_specs/rings/docs/TRIAGE.md` at `8d1c21c^` after broadening the path
  search.
- Recorded the owner split in the mapping docs: `Rings().Constructors().MatrixRing(...)`
  remains the constructor owner; the returned square matrix parent simultaneously
  refines into `Rings()`, `Algebras(R)`, and `Modules(R).Free().FiniteRank()`.
- Kept the matrix smoke requirement intact: no constructor relocation and no weakening
  of simultaneous refinement expectations.

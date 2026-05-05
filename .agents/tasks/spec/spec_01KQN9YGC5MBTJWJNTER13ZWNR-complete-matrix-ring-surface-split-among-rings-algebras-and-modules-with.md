---
trackerStatus:
  type: feature
title: Complete matrix ring surface split among rings algebras and modules without weakening the matrix smoke
status: to-do
priority: critical
planId: SPR-RINGS-PADIC-01KQN9
tags:
- category-specs
- spec
- feature
- smoke
- modules
- rings
- algebras
- matrix
- theme-rings-algebras
---

# Complete matrix ring surface split among rings algebras and modules without weakening the matrix smoke
## Summary

The deleted Rings triage recorded ring smoke blockers: nested axiom category identity
mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
split.

## Source Provenance

- `category_specs/rings/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/rings/docs/TRIAGE.md`.
- Original migrated line: `Complete matrix ring surface split among rings algebras and modules without weakening the matrix smoke from category_specs/rings/docs/TRIAGE.md`

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

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Run just smoke-file rings/smoketest.sage after ring constructor or axiom changes.
- [ ] Confirm failures are reduced without weakening constructor membership assertions.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

---
id: TASK-01KQN9YGCKBZM1PG5YYQW5A8M6-IMPLEMENT-MATRIX-RING-REFINEMENT-INTO-ALGEBRAS-R-AND-MODULES-R-FREE-FINI
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Implement matrix-ring refinement into Algebras(R) and Modules(R).Free().FiniteRank()
  while keeping ring-only routing in rings
status: unstarted
priority: high
description: 'The deleted Rings triage recorded ring smoke blockers: nested axiom category
  identity mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
  split.'
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken smokes
  or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with exact
  failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only
  categories.
- Run just smoke-file rings/smoketest.sage after ring constructor or axiom changes.
- Confirm failures are reduced without weakening constructor membership assertions.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
- category-specs
- modules
- rings
- algebras
- matrix
- theme-constructor-routing
---
# Implement matrix-ring refinement into Algebras(R) and Modules(R).Free().FiniteRank() while keeping ring-only routing in rings
## Summary

The deleted Rings triage recorded ring smoke blockers: nested axiom category identity
mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
split.

## Source Provenance

- `category_specs/rings/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/rings/docs/TRIAGE.md`.
- Original migrated line: `Implement matrix-ring refinement into Algebras(R) and Modules(R).Free().FiniteRank() while keeping ring-only routing in rings from category_specs/rings/docs/TRIAGE.md`

## Context

- ZZ, field constructors, p-adic constructors, and q-adic constructors fail through nested axiom category class-identity mismatches.
- IntegerModRing, PolynomialRing, PowerSeriesRing, LaurentSeriesRing, PuiseuxSeriesRing, and MatrixRing refine far enough to expose missing _sympy_.
- MatrixRing stays reachable from Rings().Constructors(), but the result must refine into Algebras(R) and Modules(R).Free().FiniteRank().
- The matrix smoke must not be moved or weakened to hide the surface split.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file rings/smoketest.sage after ring constructor or axiom changes.
- [ ] Confirm failures are reduced without weakening constructor membership assertions.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

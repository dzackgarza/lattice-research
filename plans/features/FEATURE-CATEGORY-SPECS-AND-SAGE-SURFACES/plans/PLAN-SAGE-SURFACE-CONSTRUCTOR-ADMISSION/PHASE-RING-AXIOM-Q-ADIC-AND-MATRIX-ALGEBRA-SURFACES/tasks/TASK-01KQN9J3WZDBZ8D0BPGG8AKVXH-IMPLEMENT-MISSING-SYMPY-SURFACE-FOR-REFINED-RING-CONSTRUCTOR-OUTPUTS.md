---
id: TASK-01KQN9J3WZDBZ8D0BPGG8AKVXH-IMPLEMENT-MISSING-SYMPY-SURFACE-FOR-REFINED-RING-CONSTRUCTOR-OUTPUTS
trackerStatus:
  type: task
parents:
- '[[PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES]]'
dependsOn: []
title: Implement missing _sympy_ surface for refined ring constructor outputs
status: needs-review
priority: high
description: 'The deleted Rings triage recorded ring smoke blockers: nested axiom
  category identity mismatches, missing _sympy_ methods on refined parents, and the
  matrix-ring surface split.'
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just smoke-file rings/smoketest.sage after ring constructor or axiom changes.
- Confirm failures are reduced without weakening constructor membership assertions.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-RING-AXIOM-Q-ADIC-AND-MATRIX-ALGEBRA-SURFACES
---
# Implement missing _sympy_ surface for refined ring constructor outputs

## Summary

The deleted Rings triage recorded ring smoke blockers: nested axiom category identity
mismatches, missing _sympy_ methods on refined parents, and the matrix-ring surface
split.

## Source Provenance

- `category_specs/rings/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/rings/docs/TRIAGE.md`.
- Original migrated line: `Implement missing _sympy_ surface for refined ring constructor outputs from category_specs/rings/docs/TRIAGE.md`

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
- 2026-05-06: Audited the current ready leaf against the regenerated DAG and current
  `rings/smoketest.sage` output. The cited `category_specs/rings/docs/TRIAGE.md` path
  was not present at `8d1c21c^`, and a broader search found no live `_sympy_` failure
  in the current ring smoke frontier. The current failures are earlier or separate
  surfaces: `hilbert_polynomial`, finite-ring `ideal_monoid`, complex interval/ball
  `algebraic_closure`, p-adic `_change_print_mode`, deferred q-adic precision-cap
  constructors, series-ring `cardinality`/`completion`, and matrix algebra/module MRO
  refinement.
- 2026-05-06: No implementation patch was made for this card because the named
  `_sympy_` target is no longer present in current ring smoke output. This is not a
  blocked dependency state; it is a stale migrated leaf whose current smoke frontier is
  already represented by neighboring ring, matrix-ring, q-adic, and topological-ring
  tracker items. Moved to `needs-review` so a reviewer can decide whether to retire or
  merge the stale migrated card into those successor items.

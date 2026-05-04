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

## Definition Grounding Required Before Spec Edit

This migrated card is executable for source mining and decision capture, but it does not by itself authorize a mathematical spec edit. Before moving, deleting, admitting, or generalizing any public category, method, constructor, predicate, invariant, Hom/End/Aut surface, or return type, record the canonical source path, exact definition, owner category, hypotheses, codomain/return object, and any invariance or equivalence proof obligation.

Use the subtree `MAPPING.md` and `SAGE_INVENTORY.md` files, Sage written docs/source, `theory/references/index.md` for literature-backed claims, and relevant repo `theory/` or skill-local sources. If the term is ambiguous or only supported by migrated backlog text, split to source-mining or decision work before editing specs.

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


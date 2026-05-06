---
id: TASK-01KQN9YGCHDRNXNEYEH2P134JD-IMPLEMENT-TOPOLOGICAL-RING-AND-FIELD-REFINEMENTS-FOR-TOPOLOGY-BEARING-RI
trackerStatus:
  type: task
parents:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
dependsOn: []
title: Implement topological ring and field refinements for topology-bearing ring
  objects without duplicating topological-space methods
status: revision-required
priority: high
description: Rings mapping records constructor namespace decisions, split p-adic and
  q-adic precision routes, matrix-ring ownership, topological ring inheritance, and
  deferred q-adic lattice-precision gaps.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- For q-adic precision items, preserve the five-field negative finding format when
  updating evidence.
- For topological ring work, check both ring and topological-space category membership.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
---
# Implement topological ring and field refinements for topology-bearing ring objects without duplicating topological-space methods
## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
lattice-precision gaps.

## Source Provenance

- `category_specs/rings/docs/MAPPING.md`
- Original migrated line: `Implement topological ring and field refinements for topology-bearing ring objects without duplicating topological-space methods from category_specs/rings/docs/MAPPING.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- ZqWithPrecisionCaps and QqWithPrecisionCaps are retained admitted split names but remain deferred frontiers because installed Sage lacks a working unramified q-adic extension path with split lattice caps.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Acceptance Criteria

- [x] The retained implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [x] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The retained precision-field change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] No q-adic precision evidence was changed; existing q-adic five-field findings remain in the mapping/frontier cards.
- [ ] Topological ring membership remains blocked on a design-preserving implementation path for inherited topological-space methods.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Preflighted with
  `just --justfile category_specs/justfile smoke-file rings/smoketest.sage`. The smoke
  fails before topological membership assertions because topology-bearing ring
  constructors such as `RR`, `CC`, `RDF`, `CDF`, `RIF`, `RealField(100)`,
  `ComplexField(100)`, and `RealBallField(100)` refine into a topological surface with
  abstract topological methods such as `boundary` still unimplemented. The same smoke
  also reports unrelated ring-frontier failures (`hilbert_polynomial`, `ideal_monoid`,
  q-adic deferred frontiers, and matrix-ring MRO). This finding is leaf-local evidence
  for the topological ring implementation card and is not a global blocker for other
  approved phase-01 leaves.
- 2026-05-06: Added source-backed `change_precision` implementations for real and
  complex precision-field categories. `RealField`, `RealDoubleField`,
  `RealIntervalField`, `ComplexField`, `ComplexDoubleField`, and
  `ComplexIntervalField` use Sage's `to_prec`; `RealBallField` and
  `ComplexBallField` use their source-backed constructor route with the new
  precision.
- 2026-05-06: Rejected and reversed an attempted topological-root implementation that
  removed abstract obligations from `TopologicalSpaces().ParentMethods` and delegated
  ambient-relative methods only for Sage `RealSet` subsets. That would have weakened
  the ideal topological-space surface to make a ring smoke frontier disappear.
- Current revision finding: topology-bearing ring objects still refine into
  `TopologicalSpaces()` and hit abstract root obligations such as `boundary`.
  Implementing those methods directly in ring files would duplicate topological
  method ownership; removing abstractness at the topological root weakens the spec.
  This leaf needs design-preserving rework for how concrete topological-space behavior
  is supplied to topology-bearing ring objects while preserving the root owner
  obligations. This is rework for this task, not a `blocked` status.
- Verification:
  - `python -m py_compile category_specs/rings/subcategories/real_precision_field.py category_specs/rings/subcategories/complex_precision_field.py` passed.
  - `git diff --check -- category_specs/rings/subcategories/real_precision_field.py category_specs/rings/subcategories/complex_precision_field.py` passed.
  - `just --justfile category_specs/justfile smoke-file topological_spaces/smoketest.sage` passed.
  - `just --justfile category_specs/justfile smoke-file rings/smoketest.sage` remains
    blocked by the topological-space `boundary` obligation for topology-bearing ring
    constructors after preserving the abstract topological owner. Other ring-frontier
    failures observed in the same smoke include `hilbert_polynomial`,
    `algebraic_closure` for complex interval/ball fields, `ideal_monoid`, q-adic
    deferred extension constructors, p-adic `_change_print_mode`, power-series
    `cardinality`, Laurent/Puiseux `completion`, matrix-ring module MRO, and
    quadratic-field `alternating_form`.

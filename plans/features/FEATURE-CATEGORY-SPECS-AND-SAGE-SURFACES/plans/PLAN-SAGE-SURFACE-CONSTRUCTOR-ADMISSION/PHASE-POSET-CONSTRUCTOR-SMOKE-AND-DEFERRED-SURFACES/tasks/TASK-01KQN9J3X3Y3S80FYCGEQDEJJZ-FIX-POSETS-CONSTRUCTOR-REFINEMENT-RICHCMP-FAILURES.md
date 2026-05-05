---
id: TASK-01KQN9J3X3Y3S80FYCGEQDEJJZ-FIX-POSETS-CONSTRUCTOR-REFINEMENT-RICHCMP-FAILURES
trackerStatus:
  type: task
parents:
- '[[PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES]]'
dependsOn: []
title: Fix Posets constructor refinement __richcmp__ failures
status: needs-review
priority: high
description: The deleted Posets triage recorded settled order-theoretic mapping items, a concrete
  design decision about equivalence relations/set partitions, and evidence gaps around semilattice
  category introspection.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken smokes
  or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with exact
  failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only
  categories.
- Run just smoke-file posets/smoketest.sage after poset constructor or method changes.
- Use the five-field negative-finding format for further Sage semilattice evidence gaps.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES
- category-specs
- constructors
- richcmp
- sets
- posets
- theme-constructor-routing
updated: '2026-05-05'
---
# Fix Posets constructor refinement __richcmp__ failures
## Summary

The deleted Posets triage recorded settled order-theoretic mapping items, a concrete
design decision about equivalence relations/set partitions, and evidence gaps around
semilattice category introspection.

## Source Provenance

- `category_specs/posets/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/posets/docs/TRIAGE.md`.
- Original migrated line: `Fix Posets constructor refinement __richcmp__ failures from category_specs/posets/docs/TRIAGE.md and posets smoketest frontier`

## Context

- Poset constructors are named non-variadic adaptations; acyclic DiGraph is the canonical finite-poset constructor.
- Meet and join expose binary operations plus sequence folds, not optional-argument aggregate signatures.
- Lattice congruences use set-theoretic vocabulary: EquivalenceRelation and SetPartition, with congruence_generated_by(blocks).
- certificate=True Sage paths map to separately named witness-returning certificate methods.
- Sage semilattice category evidence remains incomplete because local Sage imports failed before category introspection.

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [x] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] Run just smoke-file posets/smoketest.sage after poset constructor or method changes.
- [ ] Use the five-field negative-finding format for further Sage semilattice evidence gaps.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Resolved the poset constructor smoke frontier without weakening
  constructor assertions. Root `Posets()` methods backed by Sage
  `sage.categories.posets.Posets.ParentMethods` were made final concrete project
  methods where the local abstract surface had shadowed Sage's implementation:
  `directed_subset`, principal order ideal/filter, order-ideal toggles, and
  order-ideal/order-filter/chain/antichain predicates.
- 2026-05-05: Resolved finite-poset constructor refinement failures by wiring
  Sage-backed final methods for `height_certificate`, `width_certificate`,
  `meet_semilattice_certificate`, `join_semilattice_certificate`,
  `is_poset_morphism`, and `order_ideals_lattice`.
- 2026-05-05: Resolved the finite join-semilattice smoke frontier by adding the
  `subjoinsemilattice` join-closure construction to the mathematically correct
  `Posets().JoinSemilattice().Finite()` owner. Source grounding:
  `category_specs/posets/docs/MAPPING.md` maps `subjoinsemilattice` there, while
  Sage source places the construction in
  `sage/combinat/posets/lattices.py`.
- 2026-05-05 validation: `just --justfile category_specs/justfile smoke-file
  posets/smoketest.sage` passed; `just --justfile category_specs/justfile
  check-abstract-redefinitions` passed; `git diff --check` passed.

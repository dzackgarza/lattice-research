---
trackerStatus:
  type: feature
title: Map poset deferred graph polytope order-complex algebra polynomial Coxeter
  display and raw-interop surfaces to final owners
---
# Map poset deferred graph polytope order-complex algebra polynomial Coxeter display and raw-interop surfaces to final owners
## Summary

Posets mapping owns constructor names, finite surface methods, certificate method split,
deferred non-core surface ownership, and slice/coslice structure methods.

## Source Provenance

- `plans/category_specs/posets/docs/MAPPING.md`
- Original migrated line: `Map poset deferred graph polytope order-complex algebra polynomial Coxeter display and raw-interop surfaces to final owners from plans/category_specs/posets/docs/MAPPING.md`

## Context

- Graph, plotting, TikZ, polytope, order-complex, algebra, polynomial, and Coxeter surfaces are deferred mapping work, not open design decisions.
- Boolean predicates remain boolean; certificate variants become separately named certificate methods.
- Slice and coslice posets use structure_poset and structure_map, with domain/codomain inherited through Cat-owned structure_morphism.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] When closing deferred surface mapping, place each method by target mathematical object or display/interop status.
- [ ] Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


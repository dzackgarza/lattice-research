---
trackerStatus:
  itemId: impl_01KQN9J3X3Y3S80FYCGEQDEJJZ
  title: Fix Posets constructor refinement __richcmp__ failures
  type: implementation-work
  status: to-do
  priority: high
  assignee: null
  tags:
  - cat
  - category-specs
  - implementation-work
  - posets
  - sets
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Fix Posets constructor refinement __richcmp__ failures

## Summary

The deleted Posets triage recorded settled order-theoretic mapping items, a concrete
design decision about equivalence relations/set partitions, and evidence gaps around
semilattice category introspection.

## Source Provenance

- `plans/category_specs/posets/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/posets/docs/TRIAGE.md`.
- Original migrated line: `Fix Posets constructor refinement __richcmp__ failures from plans/category_specs/posets/docs/TRIAGE.md and posets smoketest frontier`

## Context

- Poset constructors are named non-variadic adaptations; acyclic DiGraph is the canonical finite-poset constructor.
- Meet and join expose binary operations plus sequence folds, not optional-argument aggregate signatures.
- Lattice congruences use set-theoretic vocabulary: EquivalenceRelation and SetPartition, with congruence_generated_by(blocks).
- certificate=True Sage paths map to separately named witness-returning certificate methods.
- Sage semilattice category evidence remains incomplete because local Sage imports failed before category introspection.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file posets/smoketest.sage after poset constructor or method changes.
- [ ] Use the five-field negative-finding format for further Sage semilattice evidence gaps.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


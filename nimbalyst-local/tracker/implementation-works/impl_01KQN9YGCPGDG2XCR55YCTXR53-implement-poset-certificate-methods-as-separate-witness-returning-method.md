---
trackerStatus:
  itemId: impl_01KQN9YGCPGDG2XCR55YCTXR53
  title: Implement poset certificate methods as separate witness-returning methods
    while keeping boolean predicates boolean
  type: implementation-work
  status: to-do
  priority: medium
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

# Implement poset certificate methods as separate witness-returning methods while keeping boolean predicates boolean

## Summary

Posets mapping owns constructor names, finite surface methods, certificate method split,
deferred non-core surface ownership, and slice/coslice structure methods.

## Source Provenance

- `plans/category_specs/posets/docs/MAPPING.md`
- Original migrated line: `Implement poset certificate methods as separate witness-returning methods while keeping boolean predicates boolean from plans/category_specs/posets/docs/MAPPING.md`

## Context

- Graph, plotting, TikZ, polytope, order-complex, algebra, polynomial, and Coxeter surfaces are deferred mapping work, not open design decisions.
- Boolean predicates remain boolean; certificate variants become separately named certificate methods.
- Slice and coslice posets use structure_poset and structure_map, with domain/codomain inherited through Cat-owned structure_morphism.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] When closing deferred surface mapping, place each method by target mathematical object or display/interop status.
- [ ] Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


---
trackingStatus:
  itemId: impl_01KQN9J3X04R2PWJADC8B4EF9A
  title: Fix Sets root containment refined-constructor __richcmp__ Primes iteration
    RealSet element-constructor and topological axiom warning
  type: implementation-work
  status: to-do
  priority: high
  assignee: null
  tags:
  - cat
  - category-specs
  - implementation-work
  - sets
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Fix Sets root containment refined-constructor __richcmp__ Primes iteration RealSet element-constructor and topological axiom warning

## Summary

The deleted Sets triage recorded the mapped enumeration smoke surface and current
failures for containment, rich comparison, Primes iteration, RealSet element
construction, and topological axiom resolution.

## Source Provenance

- `plans/category_specs/sets/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/sets/docs/TRIAGE.md`.
- Original migrated line: `Fix Sets root containment refined-constructor __richcmp__ Primes iteration RealSet element-constructor and topological axiom warning from plans/category_specs/sets/docs/TRIAGE.md`

## Context

- sets/smoketest.sage uses indexed access, rank, iteration, cardinality, and Python conversion protocols rather than Sage first/next/unrank/list/tuple helpers.
- ZZ in Sets() currently fails at the root containment statement.
- Most refined set constructors expose missing __richcmp__; Primes() exposes missing __iter__.
- RealSet interval input exposes missing _element_constructor_.
- SetPartitions(s) maps to Sets().Partitioned(), while SetPartitions() remains countable-only because it lacks a fixed powerset ambient.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file sets/smoketest.sage after set constructor or comparison changes.
- [ ] Preserve the mapped enumeration vocabulary and do not reintroduce Sage fallback helper names.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


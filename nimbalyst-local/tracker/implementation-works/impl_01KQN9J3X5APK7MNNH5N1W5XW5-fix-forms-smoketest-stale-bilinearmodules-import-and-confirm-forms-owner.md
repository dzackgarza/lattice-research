---
trackingStatus:
  itemId: impl_01KQN9J3X5APK7MNNH5N1W5XW5
  title: Fix forms smoketest stale _BilinearModules import and confirm forms owner
    identity through compatibility paths
  type: implementation-work
  status: to-do
  priority: medium
  assignee: null
  tags:
  - cat
  - category-specs
  - forms
  - implementation-work
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Fix forms smoketest stale _BilinearModules import and confirm forms owner identity through compatibility paths

## Summary

The deleted Forms triage recorded ownership separation: formed-module category classes
live in forms, while module and lattice paths preserve compatibility re-exports.

## Source Provenance

- `plans/category_specs/forms/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/forms/docs/TRIAGE.md`.
- Original migrated line: `Fix forms smoketest stale _BilinearModules import and confirm forms owner identity through compatibility paths from plans/category_specs/forms/docs/TRIAGE.md`

## Context

- FormedModules(R) names the forms owner while preserving Modules(R).WithForms().
- forms/smoketest.sage checks owner identity through module and lattice compatibility paths.
- Axiom registration remains centralized in axioms.py.
- IntegerLattices remains a module constructor-route surface until lattice constructors move behind Lattices(R).Constructors().

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file forms/smoketest.sage after forms ownership changes.
- [ ] Keep forms-owned category classes in forms rather than module or lattice wrapper paths.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


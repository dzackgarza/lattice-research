---
trackingStatus:
  itemId: impl_01KQN9YGCD23ZSZDA3VT3BJ92E
  title: Implement RealSet named constructors and smoke recovery through ambient-relative
    topological methods
  type: implementation-work
  status: to-do
  priority: high
  assignee: null
  tags:
  - cat
  - category-specs
  - implementation-work
  - topological-spaces
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Implement RealSet named constructors and smoke recovery through ambient-relative topological methods

## Summary

The deleted Topological Spaces triage recorded settled topological constructor placement
and remaining smoke design work for RealSet ambient recovery and metric examples.

## Source Provenance

- `plans/category_specs/topological_spaces/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/topological_spaces/docs/TRIAGE.md`.
- Original migrated line: `Implement RealSet named constructors and smoke recovery through ambient-relative topological methods from plans/category_specs/topological_spaces/docs/TRIAGE.md`

## Context

- TopologicalSpaces().Constructors() remains empty by design; named set constructors live under Sets().Constructors() and refine into topological categories.
- Root topological methods use ambient-relative shape: X.is_open(U), X.is_closed(U), X.closure(U), X.interior(U), and X.boundary(U).
- RealSet variadic/manifold-producing paths are excluded; admitted real-line subset construction uses named Sets().Constructors() paths.
- Real and complex ball fields are not Sage metric spaces; topological recovery belongs through topological ring/field work.
- Canonical smoke examples are still needed for Connected, Compact, and Metric().Complete().

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file topological_spaces/smoketest.sage after topological-space work.
- [ ] Prove RealSet method recovery through the ambient-relative route, not by adding pure topological constructors.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


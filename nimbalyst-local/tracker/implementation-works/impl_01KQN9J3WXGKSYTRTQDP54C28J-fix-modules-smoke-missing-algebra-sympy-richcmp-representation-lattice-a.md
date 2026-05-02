---
trackingStatus:
  itemId: impl_01KQN9J3WXGKSYTRTQDP54C28J
  title: Fix Modules smoke missing algebra _sympy_ __richcmp__ representation lattice
    and graded base-category failures
  type: implementation-work
  status: to-do
  priority: high
  assignee: null
  tags:
  - cat
  - category-specs
  - implementation-work
  - modules
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Fix Modules smoke missing algebra _sympy_ __richcmp__ representation lattice and graded base-category failures

## Summary

The deleted Modules triage recorded the post-wrapper-deletion smoke frontier and the
surfaces still meant as mathematical categories rather than exact Sage implementation
wrappers.

## Source Provenance

- `plans/category_specs/modules/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/modules/docs/TRIAGE.md`.
- Original migrated line: `Fix Modules smoke missing algebra _sympy_ __richcmp__ representation lattice and graded base-category failures from plans/category_specs/modules/docs/TRIAGE.md`

## Context

- Constructor-only Sage-wrapper categories were removed; constructors now refine Sage objects into real categories such as Free().FiniteRank(), WithOrderedBasis(), Subobjects(), Quotients(), and form-bearing module categories.
- Remaining named module subcategories must not define themselves by exact Sage implementation-class containment.
- OrthogonalGroup belongs to the aut surface of a forms-owned category: C.AutCategory().Of(M) for formed-module categories.
- Current smoke failures include missing algebra, _sympy_, __richcmp__, RepresentationModules KeyError, IntegerLattices/TorsionQuadraticModules compatibility KeyError, and graded module base-category mismatch.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file modules/smoketest.sage and preserve the full missing-surface output in tracker updates.
- [ ] Do not restore constructor-only wrapper categories to make smokes pass.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


---
trackingStatus:
  itemId: spec_01KQN9YGCA0D25CR40N85EHYZ5
  title: Review subtree direct Hom methods that shadow Cat category-object Hom and
    specify the uniform owner
  type: spec-work
  status: to-do
  priority: medium
  assignee: null
  tags:
  - cat
  - category-specs
  - spec-work
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Review subtree direct Hom methods that shadow Cat category-object Hom and specify the uniform owner

## Summary

The deleted Cat triage recorded structural Cat smoke scope and future uniformization
work for category-object Hom behavior and functor/autofunctor modeling.

## Source Provenance

- `plans/category_specs/cat/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/cat/docs/TRIAGE.md`.
- Original migrated line: `Review subtree direct Hom methods that shadow Cat category-object Hom and specify the uniform owner from plans/category_specs/cat/docs/TRIAGE.md`

## Context

- Some subtree classes define direct Hom methods that may shadow Cat-level category-object Hom at runtime.
- Natural transformations are not modeled; the current Cat morphism surface is Sage functors and construction functors.
- Generic Sage functors do not provide a uniform invertibility certificate, so concrete autofunctor membership is a future refinement.
- The Cat smoke is structural: Cat instantiation, category-object membership, functor HomCategory instantiation, and standard construction navigation.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Run just smoke-file cat/smoketest.sage after any Cat or category-object surface change.
- [ ] Check that direct subtree Hom methods do not hide the Cat-owned category-object operation.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


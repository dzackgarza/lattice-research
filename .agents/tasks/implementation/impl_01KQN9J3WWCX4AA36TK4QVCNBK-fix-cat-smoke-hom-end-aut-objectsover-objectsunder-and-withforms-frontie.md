---
trackerStatus:
  type: feature
title: Fix Cat smoke Hom End Aut ObjectsOver ObjectsUnder and WithForms frontier
status: to-do
priority: critical
planId: PLN-CAT-100
tags:
- category-specs
- implementation
- feature
- smoke
- hom-end-aut
- cat
- forms
- theme-category-core
---

# Fix Cat smoke Hom End Aut ObjectsOver ObjectsUnder and WithForms frontier
## Summary

The deleted Cat triage recorded structural Cat smoke scope and future uniformization
work for category-object Hom behavior and functor/autofunctor modeling.

## Source Provenance

- `category_specs/cat/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/cat/docs/TRIAGE.md`.
- Original migrated line: `Fix Cat smoke Hom End Aut ObjectsOver ObjectsUnder and WithForms frontier from category_specs/cat/docs/TRIAGE.md`

## Context

- Some subtree classes define direct Hom methods that may shadow Cat-level category-object Hom at runtime.
- Natural transformations are not modeled; the current Cat morphism surface is Sage functors and construction functors.
- Generic Sage functors do not provide a uniform invertibility certificate, so concrete autofunctor membership is a future refinement.
- The Cat smoke is structural: Cat instantiation, category-object membership, functor HomCategory instantiation, and standard construction navigation.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] Run just smoke-file cat/smoketest.sage after any Cat or category-object surface change.
- [ ] Check that direct subtree Hom methods do not hide the Cat-owned category-object operation.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


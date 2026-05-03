---
trackerStatus:
  type: feature
title: Design and scaffold TwistedForms as the form-object category for modules with
  forms
status: to-do
priority: critical
planId: PLN-CAT-100
phasePlan: PLN-LAT-020
tags:
- category-specs
- spec
- feature
- modules
- forms
- theme-modules-tensors
---

# Design and scaffold TwistedForms as the form-object category for modules with forms
## Summary

The source backlog identifies category-spec design work around dual objects as Hom
objects, method ownership generalization, centralized type aliases, and a TwistedForms
category.

## Source Provenance

- `plans/todo.md`
- Original migrated line: `Design and scaffold TwistedForms as the form-object category for modules with forms from plans/todo.md`

## Context

- Dual objects should route through Homsets: M* = Hom_R(M, R), so dual-object category wiring must not bypass the hom-category surface.
- Methods should move to the most general category where they make mathematical sense, rather than remaining on forms-specific wrappers.
- types.py should own standard mathematical aliases for module objects, elements, Hom/End/Aut objects, dual modules, forms, and scalar categories.
- TwistedForms should be a real form-object category rather than ad hoc form handling inside ModulesWithForms.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Review the affected public type aliases and category methods against plans/todo.md before closing.
- [ ] Run the relevant category_specs smoke file for any changed subtree.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


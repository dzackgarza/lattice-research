---
trackerStatus:
  type: feature
title: Centralize remaining category hierarchy type aliases in types.py
status: to-do
priority: critical
planId: SPR-CAT-SURFACE-01KQN9
tags:
- category-specs
- spec
- feature
- types
- theme-audit-uniformity
---

# Centralize remaining category hierarchy type aliases in types.py
## Summary

The source backlog identifies category-spec design work around dual objects as Hom
objects, method ownership generalization, centralized type aliases, and a TwistedForms
category.

## Source Provenance

- `plans/todo.md`
- Original migrated line: `Centralize remaining category hierarchy type aliases in types.py from plans/todo.md`

## Context

- Dual objects should route through Homsets: M* = Hom_R(M, R), so dual-object category wiring must not bypass the hom-category surface.
- Methods should move to the most general category where they make mathematical sense, rather than remaining on forms-specific wrappers.
- types.py should own standard mathematical aliases for module objects, elements, Hom/End/Aut objects, dual modules, forms, and scalar categories.
- TwistedForms should be a real form-object category rather than ad hoc form handling inside ModulesWithForms.

## Definition Grounding Required

Type alias centralization is not just import cleanup. Before adding or moving any alias,
record the mathematical noun, its owner category/module, and the Sage or project class
that anchors it. Use `category_specs/*/docs/MAPPING.md`,
`category_specs/*/docs/SAGE_INVENTORY.md`, `category_specs/types.py`, and
`category-spec-style` standard type-package rules.

Aliases for Hom/End/Aut, dual modules, forms, scalar categories, discriminant groups,
or lattices must cite the category surface that owns the object. Do not create a name
because a Sage class or software role exists if the corresponding mathematical noun is
not grounded.

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

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

## Grounded Spec Contract

This card owns alias centralization only where the owner category is already grounded in
the current mapping docs and style rules.

- Standard type-package names live in `types.py` and follow
  `.agents/skills/category-spec-style/references/style.md`: each public category
  package names the category, object, element, morphism, Hom, End, and Aut surfaces it
  actually owns.
- Category-object and functor-category aliases must follow
  `category_specs/cat/docs/MAPPING.md` and `category_specs/homsets/docs/MAPPING.md`:
  `Hom`, `End`, and `Aut` names belong to the category whose objects and morphisms they
  classify, and subtree aliases must refine rather than shadow the generic hom/end/aut
  hierarchy.
- Dual-object aliases for modules must reflect the hom routing recorded in
  `category_specs/modules/docs/MAPPING.md` and
  `.agents/skills/category-framework-design/references/homsets-structural-core.md`:
  a dual module is the grounded `Hom_R(M, R)` object, not an independent wrapper role.
- Formed-module and lattice aliases must use the owner split from
  `category_specs/forms/docs/MAPPING.md`,
  `category_specs/lattices/docs/MAPPING.md`, and
  `.agents/skills/lattice-redesign/references/category-abc-spec.md`: forms own
  `WithForms`, bilinear/quadratic, and generic dual/discriminant semantics; lattices
  add only the named lattice endpoints and lattice-specific construction categories.
- Discriminant-group, lattice, and scalar-category aliases may be centralized only when
  the owning subtree already exposes the mathematical noun in its mapping doc. If an
  alias candidate still depends on an unmapped owner or unresolved export surface, keep
  that alias out of `types.py` and record the concrete blocker in this card.

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

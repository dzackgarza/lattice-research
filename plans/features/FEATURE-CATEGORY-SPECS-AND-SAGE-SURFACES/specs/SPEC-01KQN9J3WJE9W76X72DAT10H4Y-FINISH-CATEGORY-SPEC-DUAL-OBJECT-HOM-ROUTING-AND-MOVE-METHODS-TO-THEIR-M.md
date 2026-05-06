---
id: SPEC-01KQN9J3WJE9W76X72DAT10H4Y-FINISH-CATEGORY-SPEC-DUAL-OBJECT-HOM-ROUTING-AND-MOVE-METHODS-TO-THEIR-M
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-HOM-END-AUT-WORK-QUEUE]]'
title: Finish category-spec dual-object Hom routing and move methods to their most
  general mathematical owners
status: unstarted
priority: critical
requirement: The source backlog identifies category-spec design work around dual objects
  as Hom objects, method ownership generalization, centralized type aliases, and a
  TwistedForms category.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance.
- Review the affected public type aliases and category methods against plans/todo.md
  before closing.
- Run the relevant category_specs smoke file for any changed subtree.
complexity: 85
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Finish category-spec dual-object Hom routing and move methods to their most general mathematical owners
## Summary

The source backlog identifies category-spec design work around dual objects as Hom
objects, method ownership generalization, centralized type aliases, and a TwistedForms
category.

## Source Provenance

- `plans/todo.md`; recover deleted source with `git show f3c2a1b^:plans/todo.md`.
- Original migrated line: `Finish category-spec dual-object Hom routing and move methods to their most general mathematical owners from plans/todo.md`

## Context

- Dual objects should route through Homsets: M* = Hom_R(M, R), so dual-object category wiring must not bypass the hom-category surface.
- Methods should move to the most general category where they make mathematical sense, rather than remaining on forms-specific wrappers.
- types.py should own standard mathematical aliases for module objects, elements, Hom/End/Aut objects, dual modules, forms, and scalar categories.
- TwistedForms should be a real form-object category rather than ad hoc form handling inside ModulesWithForms.

## Definition-Grounded Split Policy

This parent card is not definition authority. Each child leaf must carry its own
grounding record before spec edits:

- source path/reference;
- exact mathematical definition and owner category;
- hypotheses and base-ring/codomain conditions;
- return object or public surface;
- proof obligations for equivalences, presentation choices, or Sage-compatibility
  translations.

If a child leaf cannot state those fields, it is blocked only for that leaf and must be
split into source-mining or decision work. Do not execute this parent directly.

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

## Split Outcome

This card is not an atomic execution leaf. The recovered `plans/todo.md` source bundles
four independent outcomes:

- dual objects as Hom objects;
- method ownership generalization;
- centralized type aliases;
- a future `TwistedForms` category.

The dual-object/Hom owner rule is now recorded in
`category_specs/modules/docs/MAPPING.md`. The remaining work is represented by the
following active leaves:

- `spec_20260504_forms_symmetric_bilinear_divisibility_owner.md`
- `spec_20260504_forms_isometry_hom_containment_owner.md`
- `spec_01KQN9J3WKCASMD9XVMGT6JP8K-centralize-remaining-category-hierarchy-type-aliases-in-types-py.md`
- `spec_01KQN9J3WM2ASPH06AKRJQ8G82-design-and-scaffold-twistedforms-as-the-form-object-category-for-modules.md`

This parent card is blocked on those leaves. Do not execute it directly as if it were
minimal in the dependency poset.

## Complexity And Ownership

- Owner/role: category-spec planning/spec agent for Hom/End/Aut and module/form
  ownership.
- Complexity: `85` (plan-scale after preflight).
- Rationale: the recovered source combines dual-object Hom routing, method migration,
  public type aliases, and TwistedForms design. Those are independent outcomes with
  different owners and validation surfaces.
- Split/promote note: this card has been decomposed into the active leaves listed in
  `Split Outcome`; keep it blocked until those leaves are resolved or superseded by
  human-approved plan changes.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-04: Recovered deleted source from `git show f3c2a1b^:plans/todo.md` and
  preflighted the card as non-atomic.
- 2026-05-04: Added the dual-object Hom-routing rule to
  `category_specs/modules/docs/MAPPING.md`.
- 2026-05-04: Split remaining method-owner work into
  `spec_20260504_forms_symmetric_bilinear_divisibility_owner.md` and
  `spec_20260504_forms_isometry_hom_containment_owner.md`; existing type-alias and
  TwistedForms cards already cover the other independent outcomes.
- 2026-05-04: Corrected the divisibility leaf after human review rejected the
  free-module coordinate/content premise; the active leaf now owns
  symmetric-bilinear pairing-image divisibility.

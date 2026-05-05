---
trackerStatus:
  type: feature
title: Design and scaffold TwistedForms as the form-object category for modules with forms
status: to-do
priority: critical
planId: PLN-LAT-020
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

## Source-Mining Contract

This leaf is intentionally source-mining and decision capture, not implementation.
The deliverable is a grounded admission decision for whether `TwistedForms` is a real
form-object category or should be retired as an alias/helper idea.

Current local source anchors:

- `.agents/skills/lattice-redesign/references/category-abc-spec.md`: `ModuleForm`
  already has `domain()`, `codomain()`, `tensor_degree()`,
  `scalar_action_endomorphism()`, and `evaluate(...)`; `ModulesWithForms(R)` owns
  pairs `(M, f)` with bilinear and quadratic branches.
- `theory/foundations/bilinear-forms-duals-morphisms.md`: base-change morphisms of
  bilinear-form objects are triples with scalar-ring, module, and coefficient maps.
- `category_specs/forms/docs/MAPPING.md`: formed modules are owned by `forms`, while
  tensor components become forms only when attached as form data to a module.
- `category_specs/tensor_algebra_components/docs/MAPPING.md`: tensor components own
  `T_R(M)[p,q]`, tensor duals, and scalar-valued tensor-form construction data.

The grounded decision must state:

- object data: source tensor component or quotient, codomain module, tensor degree, and
  scalar-action/semilinearity twist;
- owner category: whether this belongs as a `forms` subcategory, a tensor-component
  dual-object refinement, or no new category at all;
- morphism condition: how Hom containment compares source tensor data, codomain maps,
  and scalar twists;
- relation to existing branches: bilinear, quadratic, alternating, symmetric, and
  quotient-valued discriminant forms;
- admission test: one public method or constructor that would be mathematically wrong
  without a distinct `TwistedForms` owner.

If no such public method or constructor exists after source review, the correct outcome
is to reject or retire `TwistedForms` as unnecessary indirection rather than scaffold a
compatibility layer.

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

---
id: DECISION-ALGEBRA-STANDARD-INVOLUTION-OWNER
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide algebra standard-involution method owner
status: unstarted
chosen: ''
options:
- name: Quaternion-algebra refinement owner
  pros:
  - Matches the Sage source note that the visible algorithm is quaternion-specific.
  - Avoids admitting basis-dependent quaternion behavior on arbitrary algebras.
  cons:
  - Requires mining quaternion-algebra sources before implementation can expose the
    method.
- name: Algebra-with-involution refinement owner
  pros:
  - Captures the general mathematical structure of an algebra equipped with a chosen
    involution.
  - Leaves quaternion algebras as one implementation-backed subclass.
  cons:
  - Requires defining the project algebra-with-involution category and its relation
    to Sage's standard-involution predicate.
- name: Reject as public project method for now
  pros:
  - Keeps the inventory free of a weakly grounded Sage compatibility predicate.
  - Allows future admission after a source-backed owner exists.
  cons:
  - Defers a Sage-visible surface that may be important for quaternion algebra
    interoperability.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide algebra standard-involution method owner

## Summary

Decide whether `has_standard_involution()` belongs to a quaternion-algebra refinement,
an algebra-with-involution refinement, or no public project surface yet.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-ALGEBRAS.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md`
- `category_specs/algebras/docs/SAGE_INVENTORY.md`
- `category_specs/algebras/docs/MAPPING.md`

## Context

The literal method inventory originally admitted `has_standard_involution()` as an
`Algebras(R).ParentMethods` row. Independent review found this unsafe: the canonical
algebra mapping records the predicate as unresolved, and the checked Sage evidence says
the visible implementation is quaternion-specific and basis-dependent.

The project must not treat a Sage compatibility method as a generally grounded algebra
method until the owner category, hypotheses, and codomain semantics are source-backed.

## Acceptance Criteria

- Choose whether the public owner is a quaternion-algebra refinement,
  algebra-with-involution refinement, or no admitted project method yet.
- Record the exact Sage source paths and mathematical definition checked.
- Update `SPEC-MAPPING-ALGEBRAS.md` and
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY.md` with the chosen owner,
  hypotheses, codomain, and implementation-routing status.
- Keep `has_standard_involution()` out of general `Algebras(R)` until this decision is
  settled.

## Dependencies And Boundaries

- This decision blocks only general public admission of `has_standard_involution()`.
  It does not block unrelated algebra method-inventory rows.
- Do not infer the owner from Sage method placement alone.
- If the checked sources show that "standard involution" is not a stable project
  mathematical name, reject the public spelling and record the replacement surface.

## Work Log

- 2026-05-07: Created from the Gate 1 review finding on
  `[[TASK-CATEGORY-METHOD-INVENTORY-ALGEBRA-MODULES]]`.

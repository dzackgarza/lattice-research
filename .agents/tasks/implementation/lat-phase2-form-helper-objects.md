---
trackerStatus:
  type: task
title: Implement bilinear and quadratic form helper objects
status: to-do
priority: high
created: '2026-05-03'
complexity: 55
progress: 0
planId: PLN-LAT-020
tags:
- category-specs
- implementation
- lattices
- phase-plan
- theme-modules-tensors
---

# Implement bilinear and quadratic form helper objects

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-020` is approved.

## Source Provenance

- `plans/PHASE_2_CORE_OBJECTS.md`
- Source section: Step 2.3: Form Helper Objects
- Parent plan: `PLN-LAT-020`
- Program plan: `PLN-CAT-000`

## Grounded Implementation Contract

- Helper objects are plain data-validated wrappers for form semantics, not competing category
  constructors:
  - `BilinearForm` stores `(domain, codomain: FormCodomain, gram_matrix)` where
    `domain` is a `ModulesWithForms` object, `codomain` is an actual module parent, and
    `gram_matrix` realizes the bilinear map on a chosen presentation basis.
  - `QuadraticForm` stores `(domain, codomain: FormCodomain, gram_matrix)` and the same
    evaluation contract, with a quadratic evaluation path and associated polar form.
- Required method-level behavior in `core/forms.py`:
  - `domain()`, `codomain()`, `matrix()`, `evaluate(left, right) / b(left,right)`.
  - `quadratic_form(v)` and `bilinear_form(v,w)` entry points for the bilinear branch.
  - `to_matrix()` and `with_codomain(...)` constructors that preserve form object identity.
  - `polar_form()` on `QuadraticForm` producing the associated `BilinearForm`.
- Branch-specific codomain invariants:
  - Bilinear path uses scalar-valued pairing in the codomain parent `S`.
  - Quadratic path computes in the same codomain family and satisfies `q(v+w)-q(v)-q(w)=b(v,w)` via
    `polar_form`.
- Method ownership:
  - `form` objects own no base-change, homs, spans, or lattice-specific invariants.
  - `ModulesWithForms(...).ElementMethods` and `ParentMethods` own evaluation call paths.
- Acceptance checks:
  - `BilinearForm`/`QuadraticForm` must coerce raw evaluations into `S = codomain.codomain()`.
  - `QuadraticForm.polar_form()` returns a `BilinearForm` on same domain with codomain branch.
  - Calling `evaluate` on vectors from the same parent but wrong coordinate rank raises input-shape
    validation.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/core/forms.py`.

## Acceptance Criteria

- [ ] Read the cited source section before implementation.
- [ ] Keep changes inside the named target boundary unless a new card or decision expands scope.
- [ ] Preserve the mathematical semantics from the source plan and category-spec style rules.
- [ ] Record validation commands and results before handoff.
- [ ] Do not mark this card done without human approval.

## Dependencies And Boundaries

Do not execute before the parent phase plan is approved and prerequisite phase cards are resolved. If the source section reveals missing vocabulary or method ownership, stop and file a decision or spec card instead of patching around it.

## Work Log

- Created by corpus-level `plans/` migration on 2026-05-03.

---
id: TASK-LAT-PHASE3-KERNEL-IMAGE
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS]]'
dependsOn: []
title: Implement kernel and image construction as categorical objects
status: unstarted
priority: critical
description: Leaf implementation card derived from the old phase plan. This card is executable
  only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS` is approved.
successCriteria:
- '`kernel()` returns a formed subobject of the domain, not a raw relation matrix or ambient
  subspace, and its form is literally the restriction of the domain form.'
- '`image()` returns a formed subobject of the codomain, not only generator images, and its
  form is the codomain form restricted to `im(f)`.'
- Free/torsion/integral/rational predicates on kernel and image are inherited through the
  relevant meets of `ModulesWithForms(R)` rather than hard-coded by wrapper class name.
- Zero-kernel and full-image cases agree with the morphism predicates `is_injective()` and
  `is_surjective()` used elsewhere in Phase 3.
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS
- category-specs
- lattices
- phase-plan
- morphisms
- homsets
- theme-modules-tensors
created: '2026-05-03'
---
# Implement kernel and image construction as categorical objects

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS` is approved.

## Source Provenance

- `plans/PHASE_3_MORPHISMS.md`
- Source section: Step 3.3: Kernel and Image
- Parent plan: `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

- Source anchors:
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`
  - `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
  - `category_specs/forms/docs/MAPPING.md`
  - `category_specs/lattices/docs/MAPPING.md`
- Kernel contract:
  - For `f: M → N` in `ModulesWithForms(R).Bilinear()`, `f.kernel()` is the categorical object `ker(f) ⊆ M`.
  - `ker(f)` inherits the source form via restriction:
    `β_{ker}(x, y) = β_M(x, y)` for `x, y ∈ ker(f)`.
  - Returned category must be the meet of source predicates (free/torsion/integral/rational as applicable).
- Image contract:
  - `f.image()` is `im(f) ⊆ N` with form inherited from the codomain:
    `β_{im}(f(x), f(y)) = β_N(f(x), f(y))`.
  - Image construction must use the underlying FGP image and then wrap as a formed module in the same parent family.
- Structural boundary:
  - `kernel()` and `image()` are object-level constructions, not raw subspaces.
  - `kernel()==` and `image()==` comparisons are against formed-module category zeros in the respective coefficient families.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/morphisms/bilinear.py`.

## Acceptance Criteria

- [ ] `kernel()` returns a formed subobject of the domain, not a raw relation matrix or ambient subspace, and its form is literally the restriction of the domain form.
- [ ] `image()` returns a formed subobject of the codomain, not only generator images, and its form is the codomain form restricted to `im(f)`.
- [ ] Free/torsion/integral/rational predicates on kernel and image are inherited through the relevant meets of `ModulesWithForms(R)` rather than hard-coded by wrapper class name.
- [ ] Zero-kernel and full-image cases agree with the morphism predicates `is_injective()` and `is_surjective()` used elsewhere in Phase 3.

## Dependencies And Boundaries

Execute within `src/lattices/morphisms/bilinear.py`, using the underlying FGP kernel/image constructors only as backend data. Public results must stay categorical objects in the formed-module hierarchy.

## Work Log

- Created by corpus-level `plans/` migration on 2026-05-03.

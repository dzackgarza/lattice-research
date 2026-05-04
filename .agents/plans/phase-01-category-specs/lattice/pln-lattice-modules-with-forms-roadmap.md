---
trackerStatus:
  type: plan
title: Lattice and ModulesWithForms roadmap
status: approved
planId: PLN-LAT-000
planType: implementation-roadmap
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
parentPlan: PLN-CAT-100
tags:
- category-specs
- plan
- lattices
- modules
- forms
- theme-modules-tensors
- theme-category-core
---

# Lattice and ModulesWithForms roadmap

## Objective

Organize the lattice redesign around the actual dependency chain: Sage/module prerequisites, category core, morphisms and cokernels, lattice/dual/discriminant descent, then orthogonal and Coxeter structures.

## Source corpus

- `plans/CATEGORY_ABC_SPEC.md`
- `plans/LATTICE_STYLE_GUIDE.md`
- `plans/lattice_redesign_corrections_spec.md`
- `plans/PHASE_0_SAGE_PATCHES.md`
- Deleted superseded crosswalk: `plans/PHASE_1_BILINEAR_MODULES.md`
- `plans/PHASE_2_CORE_OBJECTS.md`
- `plans/PHASE_3_MORPHISMS.md`
- `plans/PHASE_4_DISCRIMINANT_DESCENT.md`
- `plans/PHASE_5_ORTHOGONAL_GROUPS.md`

## Phase tree

- `PLN-LAT-010`: Phase 0 Sage patch prerequisites.
- `PLN-LAT-020`: Phase 2 ModulesWithForms core category and carriers.
- `PLN-LAT-030`: Phase 3 morphisms, homsets, kernels, images, and cokernels.
- `PLN-LAT-040`: Phase 4 lattice meets, duals, and discriminant descent.
- `PLN-LAT-050`: Phase 5 orthogonal groups, roots, Weyl, Eichler, and Coxeter.

## Structural rule

Phase 1 is gone as an active unit. It was a crosswalk from the old monolithic plan into Phases 2-5. The active graph is Phase 0 -> Phase 2 -> Phase 3 -> Phase 4 -> Phase 5.

## Acceptance Criteria

- [ ] Phase 0 prerequisites are complete before Phase 2 implementation starts.
- [ ] Category vocabulary and method ownership from `PLN-CAT-100` are settled before dependent implementation.
- [ ] Phase 3 cokernels exist before Phase 4 discriminant descent.
- [ ] Phase 4 lattice/discriminant objects exist before Phase 5 group theory.
- [ ] Every executable item links to exactly one phase or foundation plan.

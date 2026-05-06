---
id: PLAN-CATEGORY-SPEC-PROGRAM
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Category-spec program organization and work graph
status: approved-and-unstarted
priority: critical
owner: Zack
description: 'Make the `plans/` corpus navigable as one Nimbalyst-backed work graph:
  source specifications feed high-level plans, high-level plans split into subplans,
  and subplans own leaf task, research, bug, feature, and decision cards.'
successCriteria:
- No new work is added to loose root `plans` TODO files.
- New work is filed as `.agents` cards under the owning plan.
- Category vocabulary and method ownership cards are resolved before dependent implementation
  work proceeds.
- Sage/source-map claims are researched before constructor admission or implementation.
- Completed cards are retired rather than retained as a permanent backlog.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Category-spec program organization and work graph

## Objective

Make the `plans/` corpus navigable as one Nimbalyst-backed work graph: source specifications feed high-level plans, high-level plans split into subplans, and subplans own leaf task, research, bug, feature, and decision cards.


## Definition Grounding Requirements

This category-core plan coordinates spec work; it does not authorize definitions by
itself. Each child card must ground any category, axiom, Hom/End/Aut surface,
constructor, method, predicate, type alias, or mapping decision before spec edits.

Required sources include the relevant `category_specs/*/docs/MAPPING.md`,
`category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, local category-spec
skills, and `theory/references/index.md` when a standard mathematical claim is involved.
The card must record exact definition, owner category, hypotheses, codomain/return
object, and proof obligations for equivalence or Sage translation.

## Corpus-level analysis

The old `plans/` tree was not one backlog. It contained six different things:

- Canonical source specifications: `CATEGORY_ABC_SPEC.md`, `LATTICE_STYLE_GUIDE.md`, and `lattice_redesign_corrections_spec.md`.
- Operative phase plans: `PHASE_0_SAGE_PATCHES.md`, `PHASE_2_CORE_OBJECTS.md`, `PHASE_3_MORPHISMS.md`, `PHASE_4_DISCRIMINANT_DESCENT.md`, and `PHASE_5_ORTHOGONAL_GROUPS.md`.
- Superseded provenance: `PHASE_1_BILINEAR_MODULES.md`, now deleted because the active split is Phases 2-5 and the crosswalk is captured here and in the phase plans.
- Sage/source maps: `CATEGORY_REFINEMENT_PHASES.md`, `RING_INTEGRATION.md`, `SET_SPEC.md`, `autset_categories_path.md`, `autset_integration_plan.md`, `axioms_with_generators_finitely_presented.md`, `category_creation_notes.md`, and `homsets_structural_core.md`.
- Executable spec files and tool support: `test_spec.sage`, `test_spec2.sage`, `test_spec3.sage`, and `vulture_whitelist.py`.
- Loose process holders and generated debris: `todo.md`, `category_specs/TODO.md`, `category_specs/NEEDS_DECISIONS.md`, `.ruff_cache/`, and `__pycache__/`. These have been removed or folded into tracked cards.

## Plan tree

- `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION`: source maps, constructor routing, and admission research.
- `PLAN-CATEGORY-FOUNDATION-KERNEL`: category foundation kernel and method ownership.
- `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION`: smoke, audit, and uniformity stabilization.

Leaf task ownership is encoded by `parents` containment. Parent plans own phase cards;
phase cards own executable tasks.

## Operating rule

The old flat planning directory has been retired. Active work is represented by root
`plans/features/` cards; reusable doctrine lives in skills; executable specs live under
`tests/`; category-spec source lives under `category_specs/`.

## Source mapping

| Old material | New owner | Disposition |
| --- | --- | --- |
| `CATEGORY_ABC_SPEC.md` | `lattice-redesign` skill and `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP` | Migrated, old copy removed |
| `LATTICE_STYLE_GUIDE.md` | `lattice-redesign` skill and `PLAN-SMOKE-AUDIT-UNIFORMITY-STABILIZATION` | Migrated, old copy removed |
| `lattice_redesign_corrections_spec.md` | `lattice-redesign` skill | Migrated, old copy removed |
| `PHASE_0_SAGE_PATCHES.md` | `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` | Decomposed into leaf cards |
| `PHASE_1_BILINEAR_MODULES.md` | `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP` | Superseded crosswalk, deleted |
| `PHASE_2_CORE_OBJECTS.md` | `PHASE-LATTICE-02-CORE-CATEGORY-AND-CARRIERS` | Decomposed into leaf cards |
| `PHASE_3_MORPHISMS.md` | `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS` | Decomposed into leaf cards |
| `PHASE_4_DISCRIMINANT_DESCENT.md` | `PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT` | Decomposed into leaf cards |
| `PHASE_5_ORTHOGONAL_GROUPS.md` | `PHASE-LATTICE-05-ORTHOGONAL-GROUPS-ROOTS-WEYL-EICHLER-AND-COXETER` | Decomposed into leaf cards |
| `CATEGORY_REFINEMENT_PHASES.md` | `PLAN-STATIC-CATEGORY-REFINEMENT-ORDER` | Decomposed into category-refinement subplan |
| `autset_categories_path.md`, `autset_integration_plan.md` | `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` | Decomposed into Hom/End/Aut subplan |
| `axioms_with_generators_finitely_presented.md`, `category_creation_notes.md`, `homsets_structural_core.md` | `PLAN-CATEGORY-FOUNDATION-KERNEL`, `PLAN-STATIC-CATEGORY-REFINEMENT-ORDER`, `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION` | Source maps for foundation cards |
| `RING_INTEGRATION.md`, `SET_SPEC.md` | `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` | Source maps for constructor and family admission |
| `test_spec.sage`, `test_spec2.sage`, `test_spec3.sage` | `tests/sage_spec/category_*` | Migrated executable specs |
| `vulture_whitelist.py` | `/home/dzack/ai/quality-control/vulture_whitelist.py` | Migrated tooling support |
| `todo.md` | Existing critical cards under `PLAN-CATEGORY-FOUNDATION-KERNEL` and `PHASE-LATTICE-03-MORPHISMS-HOMSETS-KERNELS-IMAGES-AND-COKERNELS` | Folded and deleted |
| `category_specs/TODO.md`, `category_specs/NEEDS_DECISIONS.md` | `.agents/TODO.md` and `plans/features/*/decisions/` policy | Empty/stale holders deleted |

## Acceptance Criteria

- [ ] No new work is added to loose root `plans` TODO files.
- [ ] New work is filed as `.agents` cards under the owning plan.
- [ ] Category vocabulary and method ownership cards are resolved before dependent implementation work proceeds.
- [ ] Sage/source-map claims are researched before constructor admission or implementation.
- [ ] Completed cards are retired rather than retained as a permanent backlog.

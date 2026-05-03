---
trackerStatus:
  type: plan
title: Phase 01 category specs and semantic vocabulary
status: needs-approval
planId: PLN-PHASE-01
planType: phase-plan
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
parentPlan: PLN-RESEARCH-000
tags:
  - plan
  - phase-control
  - category-specs
  - spec
---

# Phase 01 category specs and semantic vocabulary

## Objective

Specify a Sage-compatible categorical language for downstream research: sets, modules,
Hom/End/Aut objects, modules with forms, lattices, and preliminary geometry interfaces.
The goal is a constrained mathematical DSL where later code constructs typed objects and
morphisms rather than manipulating raw matrices, vectors, and equations directly.

## Current plan groups

- `category-core/`: category foundation, refinement order, Hom/End/Aut admission, Sage source maps, constructor admission, and smoke/audit stabilization.
- `lattice/`: ModulesWithForms and lattice roadmap plans currently expressed as spec-phase dependency plans.
- `geometry/`: geometric category expansion planning for later scheme, variety, curve, surface, and family vocabulary.
- `sprints/`: existing sprint-plan files migrated from category-spec triage work.

## Exit criteria

- [ ] Core categorical vocabulary is specified enough to express later implementation cards.
- [ ] Lattice specs can state Picard, discriminant, isometry, Hom, End, Aut, base-change, and morphism semantics without raw matrix fallbacks.
- [ ] Backend/source gaps are filed as research cards rather than hidden inside implementation work.
- [ ] Future phase plans have enough prerequisites to block premature downstream work.

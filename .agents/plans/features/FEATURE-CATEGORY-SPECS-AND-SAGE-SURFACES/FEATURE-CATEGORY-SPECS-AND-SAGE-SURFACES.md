---
id: FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
trackerStatus:
  type: feature
parents: []
dependsOn: []
plans:
- '[[PLAN-CATEGORY-SPEC-PROGRAM]]'
- '[[PLAN-SPEC-CORE-VERTICAL-SLICE]]'
- '[[PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION]]'
- '[[PLAN-STATIC-CATEGORY-REFINEMENT-ORDER]]'
- '[[PLAN-CATEGORY-FOUNDATION-KERNEL]]'
- '[[PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION]]'
- '[[PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION]]'
- '[[PLAN-CATEGORY-OBLIGATION-EXAMPLES]]'
title: Category specs and Sage surface admission
status: in-progress
priority: critical
description: 'Specify a Sage-compatible categorical language for downstream research:
  sets, modules, Hom/End/Aut objects, modules with forms, lattices, and preliminary
  geometry interfaces. The goal is a constrained mathematical DSL where later code
  constructs typed objects and morphisms rather than manipulating raw matrices, vectors,
  and equations directly.'
---
# Phase 01 category specs and semantic vocabulary

## Objective

Specify a Sage-compatible categorical language for downstream research: sets, modules,
Hom/End/Aut objects, modules with forms, lattices, and preliminary geometry interfaces.
The goal is a constrained mathematical DSL where later code constructs typed objects and
morphisms rather than manipulating raw matrices, vectors, and equations directly.

## Current Pivot Gate

The active success metric is `[[PLAN-SPEC-CORE-VERTICAL-SLICE]]`: a narrow typed
spec-core and construction-witness slice proving that finite/countable cartesian
products satisfy inherited set obligations for free finite-rank modules. Broad category
expansion, broad category-obligation repair, or mypy/QC routing is not progress for the current
pivot unless it directly changes the slice reports for `GF(5)^3`, `ZZ^2`, or a
missing-obligation claimant.

## Definition Grounding Control

Approved plans and migrated cards are routing artifacts, not mathematical definition
authority. Before any spec edit changes a mathematical category, method, predicate,
constructor, invariant, Hom/End/Aut surface, or mapping decision, the executing card
must record:

- the canonical source path or reference;
- the exact definition and owner category;
- the hypotheses under which the definition is valid;
- the codomain or return object;
- proof obligations for choice-independence or equivalence with another notion.

If that grounding is missing, the next action is source mining, a decision card, or a
split prerequisite, not speculative spec editing. This hard stop is local to the
affected leaf; it does not block other approved phase-01 spec leaves.

## Current Plan Groups

- `PLAN-SPEC-CORE-VERTICAL-SLICE`: current pivot gate and next executable success
  metric; proves the spec-core, provider, witness, and report contract on the
  finite/countable free finite-rank module slice.
- `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION`: Sage/source mapping and admission discipline.
- `PLAN-CATEGORY-FOUNDATION-KERNEL` and `PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION`: core category vocabulary and ownership; static refinement-order policy lives in the `category-framework-design` skill and source-backed child cards.
- `PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION` and `PLAN-CATEGORY-OBLIGATION-EXAMPLES`: constructor admission, failed-assertion classification, and audit stabilization.
- `PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP` and the geometry feature plans: cross-feature spec-phase dependencies.

The connected plan spine is `GOAL.md` -> `.agents/current-goal-phase.md` -> active feature plans; active phase-01 tasks are contained by phase cards under their owning plans.

Reopened 2026-05-10 on the Hom/End/Aut path after runtime auditing showed that the
current generic `HomCategory.parent_class` chain does not inherit Sage's concrete
`sage.categories.homset.Homset` parent surface even though `SPEC-MAPPING-HOMSETS`
records `domain()`, `codomain()`, `identity()`, and `is_endomorphism_set()` as
Sage-backed generic homset behavior. Follow-up now lives under the Hom/End/Aut plan
and the linked ownership decision.

## Exit criteria

- [x] The spec-core vertical slice reports `GF(5)^3` through a finite
  cartesian-power witness with cardinality `125` and `ZZ^2` through a countable
  cartesian-power witness with inherited enumeration obligations.
  (29 vertical-slice tests pass as of 2026-05-20; `just test-spec-core-vertical-slice` → 29 passed)
- [x] Core categorical vocabulary is specified enough to express later implementation cards.
  (All 8 plans complete: PLAN-CATEGORY-SPEC-PROGRAM, PLAN-SPEC-CORE-VERTICAL-SLICE,
  PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION, PLAN-STATIC-CATEGORY-REFINEMENT-ORDER,
  PLAN-CATEGORY-FOUNDATION-KERNEL, PLAN-HOM-END-AUT-STRUCTURAL-ADMISSION,
  PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION, PLAN-CATEGORY-OBLIGATION-EXAMPLES)
- [x] Lattice specs can state Picard, discriminant, isometry, Hom, End, Aut, base-change, and morphism semantics without raw matrix fallbacks.
  (`category_specs/lattices/homsets.py` has Hom/End/Aut categories; `category_specs/forms/subcategories/free_bilinear.py` has discriminant, base_change_to; `LatticeAutomorphisms.is_isometry()` in homsets; all return typed project aliases not raw matrices)
- [x] Active mathematical spec leaves either contain a definition-grounding record or
  are explicitly blocked/split on the missing source, decision, or proof obligation.
  (All source-mining tasks complete; poset-aut surfaces explicitly rejected with evidence)
- [x] Backend/source gaps are filed as research cards rather than hidden inside implementation work.
  (poset aut group surface and Sage-support research cards all filed)
- [x] Future phase plans have enough prerequisites to block premature downstream work.
  (QC and ModulesWithForms features have proper DAG blocks; Coble features gated on all prerequisites)

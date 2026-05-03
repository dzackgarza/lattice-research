---
trackerStatus:
  type: plan
title: 'Category-spec source maps constructor routing and admission research'
status: needs-approval
planId: PLN-CAT-010
planType: research-plan
priority: critical
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 10
tags:
  - category-specs
  - plan
  - research
  - sage
  - constructors
  - theme-research-sources
  - theme-constructor-routing
---

# Category-spec source maps constructor routing and admission research

## Objective

Preserve and route the non-lattice root `plans` source maps into an approved research/admission workflow before they drive implementation.

## Current State

Several root plan files are source maps or design notes rather than executable implementation plans. They are valuable, but they should not remain free-floating planning authorities outside Nimbalyst.

## Source Provenance

- `plans/CATEGORY_REFINEMENT_PHASES.md`
- `plans/RING_INTEGRATION.md`
- `plans/SET_SPEC.md`
- `plans/autset_categories_path.md`
- `plans/autset_integration_plan.md`
- `plans/axioms_with_generators_finitely_presented.md`
- `plans/category_creation_notes.md`
- `plans/homsets_structural_core.md`

## Scope

This plan owns research and admission around:

- Static category hierarchy and method-surface phases.
- Ring construction entry points and constructor routing.
- Set category hierarchy and concrete set implementation surfaces.
- Autset admission as an axiom/refinement below Endsets.
- WithGenerators, FinitelyPresented, Dedekind/PID module axioms, and structural patterns.
- Category creation and `_refine_category_` mechanics.
- Homsets as the structural core for modules, duals, endsets, and autsets.

## Non-goals

- Do not implement directly from source-map notes.
- Do not convert every source-map heading into a card.
- Do not create duplicate cards when active category-spec tasks already cover the work.

## Acceptance Criteria

- [ ] The human approves this source-map plan before decomposition.
- [ ] Each source map is classified as canonical reference, research input, phase dependency, or retired provenance.
- [ ] Work that blocks vocabulary or method ownership becomes critical or high-priority cards.
- [ ] External/Sage-source claims cite source paths or docs before implementation.
- [ ] Constructor admission cards identify the mathematical owner and the Sage constructor surface separately.

## Decomposition Boundary

After approval, split into research cards for source-map verification and decision cards for unresolved ownership or admission choices. Only create implementation cards after the relevant vocabulary and ownership are fixed.

## Visual Window

See `.agents/visuals/category-spec-plan-hierarchy.mmd` for the current plan hierarchy and dependency sketch.

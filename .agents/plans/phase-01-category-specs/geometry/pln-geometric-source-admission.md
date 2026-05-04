---
trackerStatus:
  type: plan
title: Geometric category source admission research
status: approved
planId: PLN-GEO-010
parentPlan: PLN-GEO-000
planType: research-plan
priority: high
owner: Zack
created: '2026-05-03'
updated: '2026-05-03'
progress: 0
tags:
  - category-specs
  - plan
  - research
  - geometry
  - theme-geometric-categories
---

# Geometric category source admission research

## Objective

Organize the geometry category research cards that identify source-backed category
vocabulary for schemes, varieties, manifolds, polytopes, and toric interfaces before
any implementation card is created.

## Source Provenance

- Parent plan: `PLN-GEO-000`.
- Active child cards are identified by `planId: PLN-GEO-010`.
- Current phase boundary: phase-01 category specs and semantic vocabulary only.

## Context

This is a leaf plan. Its child cards are research tasks, not implementation work. They
must return source evidence, Sage or backend surface findings, ownership decisions, and
follow-up cards when the category vocabulary is concrete enough to execute.

## Acceptance Criteria

- [ ] Every child card cites the exact sources searched and separates evidence from inference.
- [ ] Geometry vocabulary is admitted only after mathematical owner, Sage surface, and public category boundary are explicit.
- [ ] Toric-variety work records its dependency on the lattice category surface before implementation.
- [ ] Follow-up implementation or decision work is tracked as new cards rather than left in research prose.

## Dependencies And Boundaries

- Depends on `PLN-CAT-010` for source-map and admission discipline.
- Does not authorize phase-06 geometry/Coble implementation.
- Does not replace source-backed mapping docs or future category specs.

## Work Log

- 2026-05-03: Created as a leaf plan during tracker poset reorganization.

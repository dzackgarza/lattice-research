---
id: PLAN-GEOMETRIC-SOURCE-ADMISSION
trackerStatus:
  type: plan
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn: []
title: Geometric category source admission research
status: approved-and-unstarted
priority: high
owner: Zack
description: Organize the geometry category research cards that identify source-backed
  category vocabulary for schemes, varieties, manifolds, polytopes, and toric interfaces
  before any implementation card is created.
successCriteria:
- Every child card cites the exact sources searched and separates evidence from inference.
- Geometry vocabulary is admitted only after mathematical owner, Sage surface, and
  public category boundary are explicit.
- Toric-variety work records its dependency on the lattice category surface before
  implementation.
- Follow-up implementation or decision work is tracked as new cards rather than left
  in research prose.
phases:
- '[[PHASE-GEOMETRIC-SOURCE-ADMISSION-RESEARCH]]'
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Geometric category source admission research

## Objective

Organize the geometry category research cards that identify source-backed category
vocabulary for schemes, varieties, manifolds, polytopes, and toric interfaces before
any implementation card is created.


## Mathematical Grounding Requirements

This geometry plan is source-admission work, not a license for ad hoc algebraic-geometry
interfaces. Each child card must cite the relevant literature, Sage/Singular/Macaulay2/
Oscar documentation, or local theory note before admitting a category, constructor,
backend, invariant, or morphism.

The grounding record must state the geometric object, morphism or construction,
hypotheses, return object, and backend evidence. If the software only exposes raw
polynomials, matrices, or option bags, the child card must translate them into project
category vocabulary or split a source/backend decision first.

## Source Provenance

- Parent feature: `FEATURE-GEOMETRY-CATEGORY-INTERFACES`.
- Active child cards are contained by this plan's phase cards.
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

- Depends on `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` for source-map and admission discipline.
- Does not authorize phase-06 geometry/Coble implementation.
- Does not replace source-backed mapping docs or future category specs.

## Work Log

- 2026-05-03: Created as a leaf plan during tracker poset reorganization.

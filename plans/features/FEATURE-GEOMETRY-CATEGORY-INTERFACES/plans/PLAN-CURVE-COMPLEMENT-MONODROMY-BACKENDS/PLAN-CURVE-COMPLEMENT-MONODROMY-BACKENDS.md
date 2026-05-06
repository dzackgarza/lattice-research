---
id: PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS
trackerStatus:
  type: plan
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn: []
title: Curve complement and monodromy backend research
status: approved-and-unstarted
priority: high
owner: Zack
description: Group the curve-complement, Riemann-surface, Sirocco, ore_algebra, Picard-Fuchs,
  and monodromy research cards under one leaf plan so backend evidence is collected
  before geometry-facing implementation work is proposed.
successCriteria:
- Each child card records exact sources searched, backend capabilities, mathematical
  inputs, and mathematical outputs.
- Negative findings use the repository five-field format.
- Any backend admission consequence is linked to a spec, decision, or implementation
  card.
- No child card introduces a public backend wrapper before ownership and source evidence
  are reviewed.
phases:
- '[[PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH]]'
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Curve complement and monodromy backend research

## Objective

Group the curve-complement, Riemann-surface, Sirocco, ore_algebra, Picard-Fuchs, and
monodromy research cards under one leaf plan so backend evidence is collected before
geometry-facing implementation work is proposed.


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
- Related phase boundary: phase-01 source and vocabulary research only.

## Context

This plan collects backend investigations that inform later curve, surface, family,
and monodromy category surfaces. It must not become a shortcut into downstream Coble
experimentation.

## Acceptance Criteria

- [ ] Each child card records exact sources searched, backend capabilities, mathematical inputs, and mathematical outputs.
- [ ] Negative findings use the repository five-field format.
- [ ] Any backend admission consequence is linked to a spec, decision, or implementation card.
- [ ] No child card introduces a public backend wrapper before ownership and source evidence are reviewed.

## Dependencies And Boundaries

- Depends on `PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION` for source-map and constructor admission discipline.
- Blocks premature phase-06 implementation until backend capability and vocabulary are explicit.
- Does not authorize Coble orbit, Picard, or surface computations.

## Work Log

- 2026-05-03: Created as a leaf plan during tracker poset reorganization.

---
trackerStatus:
  type: plan
title: Curve complement and monodromy backend research
status: approved
planId: PLN-GEO-020
parentPlan: PLN-GEO-000
planType: backend-research-plan
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
  - backend
  - theme-research-sources
---

# Curve complement and monodromy backend research

## Objective

Group the curve-complement, Riemann-surface, Sirocco, ore_algebra, Picard-Fuchs, and
monodromy research cards under one leaf plan so backend evidence is collected before
geometry-facing implementation work is proposed.

## Source Provenance

- Parent plan: `PLN-GEO-000`.
- Active child cards are identified by `planId: PLN-GEO-020`.
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

- Depends on `PLN-CAT-010` for source-map and constructor admission discipline.
- Blocks premature phase-06 implementation until backend capability and vocabulary are explicit.
- Does not authorize Coble orbit, Picard, or surface computations.

## Work Log

- 2026-05-03: Created as a leaf plan during tracker poset reorganization.

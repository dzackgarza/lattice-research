---
trackerStatus:
  type: plan
title: Geometric category expansion research program
status: approved
planId: PLN-GEO-000
planType: research-program
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
- theme-research-sources
parentPlan: PLN-CAT-010
---

# Geometric category expansion research program

## Objective

Group the high-priority geometric category research cards so schemes, varieties, manifolds, polytopes, toric varieties, and related categories enter the system through source-backed vocabulary and dependency-aware planning.

## Subplans

- `PLN-GEO-010`: geometric category source admission research.
- `PLN-GEO-020`: curve complement and monodromy backend research.

Leaf task ownership is encoded by child cards' `planId` values.

## Dependency intuition

Definitions and vocabulary come first: schemes and varieties precede specialized complex algebraic categories; lattice integration must precede toric-variety constructor decisions; manifolds and complex manifolds should not be forced through algebraic-variety vocabulary unless the source research justifies it.

## Acceptance Criteria

- [ ] Each geometric category has source-backed Sage and mathematical vocabulary before implementation.
- [ ] Dependencies are recorded before implementation cards are created.
- [ ] Toric varieties explicitly route through the lattice category integration decision.

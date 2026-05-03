---
trackerStatus:
  type: plan
title: 'Geometric category expansion research program'
status: needs-approval
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
---

# Geometric category expansion research program

## Objective

Group the high-priority geometric category research cards so schemes, varieties, manifolds, polytopes, toric varieties, and related categories enter the system through source-backed vocabulary and dependency-aware planning.

## Owned existing cards

- `integrate-schemes-category.md`
- `integrate-varieties-category.md`
- `integrate-complex-varieties-category.md`
- `integrate-polytopes-category.md`
- `integrate-polyhedra-2d-polytopes-category.md`
- `integrate-smooth-manifolds-category.md`
- `integrate-complex-manifolds-category.md`
- `integrate-complex-algebraic-curves-category.md`
- `integrate-complex-algebraic-surfaces-category.md`
- `integrate-families-of-varieties-category.md`
- `integrate-toric-varieties-with-lattice-category.md`

## Dependency intuition

Definitions and vocabulary come first: schemes and varieties precede specialized complex algebraic categories; lattice integration must precede toric-variety constructor decisions; manifolds and complex manifolds should not be forced through algebraic-variety vocabulary unless the source research justifies it.

## Acceptance Criteria

- [ ] Each geometric category has source-backed Sage and mathematical vocabulary before implementation.
- [ ] Dependencies are recorded before implementation cards are created.
- [ ] Toric varieties explicitly route through the lattice category integration decision.

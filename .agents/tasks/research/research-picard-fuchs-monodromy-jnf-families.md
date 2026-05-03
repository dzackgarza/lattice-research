---
trackerStatus:
  type: task
title: Research Picard-Fuchs and monodromy JNF computations for families
status: to-do
priority: low
tags:
- category-specs
- research
- todo-migration
- external-integration
created: '2026-05-03'
complexity: 35
progress: 0
---

# Research Picard-Fuchs and monodromy JNF computations for families

## Summary

Research how to compute Jordan normal forms of monodromy operators for families of curves and surfaces, including Picard-Fuchs operator routes.

## Source Provenance

Migrated from `specs/TODO.md`: "Computations of the JNF of a monodromy operator of a family of curves f(x,y,t) and a family of surfaces f(x,y,z,t)" and note about Picard-Fuchs operators and Singular `foliation.lib` in `https://github.com/movasati/NoetherLefschetz/tree/master`.

## Context

This card should clarify the mathematical/computational route before any implementation: Sage, Singular, ore_algebra, or another exact backend. It likely feeds future families-of-varieties category work.

## Acceptance Criteria

- Read the referenced Noether-Lefschetz/Singular material enough to understand the Picard-Fuchs route.
- Identify required backend tools and what each certifies.
- State the exact mathematical inputs/outputs for curve-family and surface-family cases.
- Create follow-up cards for backend decisions, category specs, and implementation tasks if warranted.

## Dependencies And Boundaries

Do not implement monodromy or Picard-Fuchs computation in this card. Do not claim exactness or correctness without proof-audit-ready evidence.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.

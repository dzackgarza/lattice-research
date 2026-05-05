---
id: TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS
trackerStatus:
  type: task
parents:
- '[[PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH]]'
dependsOn: []
title: Research Sirocco integration for curve-complement fundamental groups
status: unstarted
priority: low
description: Research whether and how `sirocco2` should be integrated for computing or representing
  fundamental groups of curve complements.
successCriteria:
- Read the upstream Sirocco repository and any available documentation.
- 'Identify the exact mathematical object(s) exposed: curve complements, fundamental groups,
  monodromy, or related structures.'
- Decide whether integration requires a spec card, implementation card, decision card, or
  rejection note.
- Record any required follow-up as tracked cards rather than inline TODOs.
complexity: 35
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
- PLAN-CURVE-COMPLEMENT-MONODROMY-BACKENDS
- PHASE-CURVE-COMPLEMENT-MONODROMY-BACKEND-RESEARCH
- category-specs
- todo-migration
- external-integration
- theme-research-sources
created: '2026-05-03'
---
# Research Sirocco integration for curve-complement fundamental groups

## Summary

Research whether and how `sirocco2` should be integrated for computing or representing fundamental groups of curve complements.

## Source Provenance

Migrated from `specs/TODO.md`: "Integrate sirocco: https://github.com/miguelmarco/sirocco2" and note "Used to define pi_1 of curve complements."

## Context

This is exploratory category-spec research. The output should determine whether Sirocco belongs in the project vocabulary, whether it should be wrapped, and what category/spec cards or decisions are needed before implementation.

## Acceptance Criteria

- Read the upstream Sirocco repository and any available documentation.
- Identify the exact mathematical object(s) exposed: curve complements, fundamental groups, monodromy, or related structures.
- Decide whether integration requires a spec card, implementation card, decision card, or rejection note.
- Record any required follow-up as tracked cards rather than inline TODOs.

## Dependencies And Boundaries

Do not implement a wrapper in this card. Do not assume Sirocco semantics without reading upstream source/docs. Do not add a dependency until a separate implementation card or decision approves the integration path.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.

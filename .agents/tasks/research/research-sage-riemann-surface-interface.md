---
trackerStatus:
  type: task
title: Research Sage Riemann surface interface integration
status: to-do
priority: low
tags:
- category-specs
- research
- todo-migration
- external-integration
- theme-research-sources
created: '2026-05-03'
complexity: 35
progress: 0
planId: PLN-GEO-020
---

# Research Sage Riemann surface interface integration

## Summary

Research how Sage Riemann surface functionality should map into the category-spec vocabulary and whether it warrants wrapper, constructor, or method cards.

## Source Provenance

Migrated from `specs/TODO.md`: "Wrap and interface with https://doc.sagemath.org/html/en/reference/curves/sage/schemes/riemann_surfaces/riemann_surface.html".

## Context

This should survey the Sage Riemann surface API, identify the finite set of relevant constructors and methods, and map them to existing or missing category-spec concepts.

## Acceptance Criteria

- Read the Sage Riemann surface documentation and relevant source.
- List candidate constructors, methods, and mathematical nouns relevant to category specs.
- Identify required decisions about ownership, naming, and allowed wrapper boundaries.
- Create follow-up cards for any implementation or decision work that is concrete enough to execute.

## Dependencies And Boundaries

Do not design a variadic or convenience wrapper. Do not implement code. Do not treat Sage method names as project vocabulary without mapping them through category-spec style rules.

## Work Log

- 2026-05-03: Created as a research card during `specs/TODO.md` migration and category-integration carding.

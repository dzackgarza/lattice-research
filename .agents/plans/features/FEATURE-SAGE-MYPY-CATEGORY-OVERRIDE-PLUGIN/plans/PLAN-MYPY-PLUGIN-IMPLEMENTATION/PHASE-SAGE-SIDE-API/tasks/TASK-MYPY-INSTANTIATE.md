---
id: TASK-MYPY-INSTANTIATE
trackerStatus:
  type: task
parents:
- '[[PHASE-SAGE-SIDE-API]]'
dependsOn:
- '[[TASK-MYPY-PARSER]]'
title: Implement instantiate_category_from_source_path
status: needs-review
priority: high
description: 'Given a parsed CategoryMethodContainer, instantiate the corresponding Sage category
  using an_instance() chaining. Handles singleton, nested (Homsets), and axiom (Finite) paths.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- "Rings \u2192 an_instance() returns Rings()"
- "Objects.Homsets \u2192 Objects.an_instance().Homsets() returns category"
- "Monoids.Finite \u2192 Monoids.an_instance().Finite() returns axiom category"
- Fails cleanly with diagnostic for unresolvable paths
complexity: 20
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-SAGE-SIDE-API
---
# Task: Implement Category Instantiation

## Summary

Implement `instantiate_category_from_source_path` that takes the module and
category path from the parser and returns a live Sage category instance.

## Context

Uses `Category.an_instance()` (not `Category()`) as the preferred instantiation
method per Sage convention. Chains attribute access for nested/axiom paths.

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`: "Category Instantiation Rule"

## Acceptance Criteria

- Singleton: import module, get class, call `an_instance()`, return category
- Nested: chain `.Homsets()`, `.CartesianProducts()`, etc.
- Axiom: chain `.Finite()`, `.WithBasis()`, etc.
- Parameterized: `an_instance()` may return a default; documented as best-effort
- Import errors caught and surfaced as diagnostics

## Current Status

Ready for review. This card's implementation is exercised by the full Sage mypy category plugin suite, verified on 2026-05-10 with `just test`: `24 passed, 3 warnings`, no skipped tests.

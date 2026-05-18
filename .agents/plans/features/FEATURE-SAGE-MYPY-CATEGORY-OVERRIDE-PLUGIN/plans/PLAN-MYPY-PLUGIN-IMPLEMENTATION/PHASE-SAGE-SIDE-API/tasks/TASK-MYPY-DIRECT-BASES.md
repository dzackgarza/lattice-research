---
id: TASK-MYPY-DIRECT-BASES
trackerStatus:
  type: task
parents:
- '[[PHASE-SAGE-SIDE-API]]'
dependsOn:
- '[[TASK-MYPY-INSTANTIATE]]'
title: Implement method_container_direct_bases, dependencies, and debug oracle
status: needs-agent-review
priority: high
description: 'Implement the core projection: given a method container fullname, instantiate
  the Sage category, read its dynamic class __bases__, map each base back to a source container,
  return the ordered list. Also implement module_method_container_dependencies and debug_projection.

  '
activityType: implementation
workstreamRole: implementation
claimStatus: unexamined
uncertaintyState: none-recorded
successCriteria:
- method_container_direct_bases returns correct list for a known Sage category
- uses __bases__ not mro()
- module_method_container_dependencies returns correct ancestor modules
- debug_projection prints expected output shape
complexity: 30
tags:
- FEATURE-SAGE-MYPY-CATEGORY-OVERRIDE-PLUGIN
- PLAN-MYPY-PLUGIN-IMPLEMENTATION
- PHASE-SAGE-SIDE-API
---
# Task: Implement Direct Bases Projection

## Summary

Implement the three remaining functions in the introspection module:
`method_container_direct_bases`, `module_method_container_dependencies`,
and `debug_projection`.

## Context

The algorithm from the technical addendum:
1. Parse fullname → module, category_path, method_kind
2. Instantiate category
3. Get dynamic class (parent_class / element_class / morphism_class / subcategory_class)
4. Read `dynamic_class.__bases__`
5. Map each base back to source container via `all_super_categories()` lookup table
6. Return `type(D).method_kind` fullnames in order

Critical: uses `__bases__` not `mro()`. Mypy computes transitive MRO from the injected direct bases.

## Source Provenance

- `~/ai/quality-control/planning/override-sage-categories.md`:
  "Sage-Side Helper: Direct Dynamic-Base Projection" (full algorithm),
  "Debug Oracle"

## Acceptance Criteria

- `method_container_direct_bases("sage.categories.rings.Rings.ParentMethods")` returns non-empty list
- Uses `__bases__` (verify with code review)
- Non-category runtime bases (object, etc.) are skipped
- Bases without source containers are skipped (optionally diagnosed)
- `debug_projection` prints: source fullname, dynamic class, dynamic bases, injected static bases

## Current Status

Ready for review. This card's implementation is exercised by the full Sage mypy category plugin suite, verified on 2026-05-10 with `just test`: `24 passed, 3 warnings`, no skipped tests.

---
id: TASK-CATEGORY-METHOD-INVENTORY-SETS-TOPOLOGY
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS]]'
title: Write set topology and metric method ownership rows
status: needs-review
priority: critical
owner: Zack
description: Mine set, finite-set, enumerated-set, subobject, image-set, topological,
  and metric inventories into literal method-owner rows.
successCriteria:
- The target method-inventory spec contains set, finite, countable/enumerated, subobject,
  image-object, topological, and metric method tables.
- '`len(X)` / `__len__` is recorded as finite-set or finite-enumeration protocol ownership,
  not a root `Sets()` method.'
- Every set operation row states whether the owner is root `Sets()`, countable or
  enumerated sets, finite sets, subobjects, image subobjects, topological spaces,
  or metric spaces.
- Sage wrapper and RealSet methods are either admitted with owner and codomain, mapped
  to named constructor or subobject routes, or rejected as interop/display/private
  behavior.
complexity: 70
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Write set topology and metric method ownership rows

## Summary

Write the literal method-owner rows for sets and topology. This task should produce
actual tables in `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY` or split
trackable spec cards when the table becomes too large.

## Source Provenance

- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/sets/docs/MAPPING.md`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`
- `category_specs/topological_spaces/docs/MAPPING.md`
- Existing partition follow-up spec:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER.md`

## Context

The seed rows include:

- root set surface: `__contains__`, `an_element`, `some_elements`, `cardinality`,
  `is_empty`, `is_finite`, `subsets`, `subsets_lattice`, `union`, set comparison,
  `_sympy_`;
- countable/enumerated surface: `__iter__`, `rank`, `unrank`, `__getitem__`,
  iterator ranges, `first`, `next`, `random_element`;
- finite surface: `len(X)`, `__len__`, `list(X)`, `tuple(X)`, finite conversion
  protocols and caches;
- subobject surface: `intersection`, `difference`, `symmetric_difference`,
  `complement`, subset comparisons requiring a common ambient;
- image/subquotient surface: `ambient`, `lift`, `retract`;
- set-to-algebra routes: `free_module(R)` and `free_algebra(R)` with module or algebra
  constructor owners, not generic Sage `S.algebra(R)` ownership;
- RealSet and topology surface: `closure`, `interior`, `boundary_points`, `contains`,
  interval/ray/real-line constructor methods, connectedness and compactness refinements;
- metric surface: `metric_function`, `metric`, `dist`, element distance delegation,
  product metric, complete metric refinement.

## Complexity And Ownership

- Owner/role: category-spec sets/topology spec writer.
- Complexity: `70` (high).
- Rationale: this touches root set semantics, Python protocols, finite/countable
  distinctions, subobject operations, RealSet topology, and metric refinements.
- Split/promote note: if the set and topology tables exceed one readable spec section,
  split into separate set and topology spec cards while keeping this task as the
  coordinating leaf.

## Acceptance Criteria

- [x] The target method-inventory spec contains set, finite, countable/enumerated, subobject, image-object, topological, and metric method tables.
- [x] `len(X)` / `__len__` is recorded as finite-set or finite-enumeration protocol ownership, not a root `Sets()` method.
- [x] Every set operation row states whether the owner is root `Sets()`, countable or enumerated sets, finite sets, subobjects, image subobjects, topological spaces, or metric spaces.
- [x] Sage wrapper and RealSet methods are either admitted with owner and codomain, mapped to named constructor or subobject routes, or rejected as interop/display/private behavior.

## Dependencies And Boundaries

- Do not expose Sage `Set(X)` as a generic public constructor.
- Do not collapse real intervals, open subsets, finite point sets, and general
  topological spaces into one constructor owner.
- Do not admit Python export methods such as `set()` or `frozenset()` as mathematical
  set methods unless a new source-grounded decision says otherwise.
- When Sage places a method on a concrete wrapper, map it to the minimal mathematical
  category or reject it as wrapper state.

## Work Log

- 2026-05-05: Created as the sets/topology leaf for the literal method ownership inventory phase.
- 2026-05-06: Wrote the set/topology/metric method rows into
  `SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY`, including finite `len(X)`
  ownership and rejected Sage wrapper/export surfaces. Moved this task to
  needs-review.

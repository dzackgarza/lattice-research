---
title: Sage Set Implementations Reference
status: active
date: 2026-05-29
---
# SageMath Set Implementations: Comprehensive Reference

## Category Hierarchy

Three layers: actual containment graph, SubcategoryMethods (restriction methods),
shortcut methods (named conveniences on `Sets()`).

Actual hierarchy: Sets → FiniteSets, InfiniteSets, CountableSets (FiniteEnumeratedSets,
InfiniteEnumeratedSets, RecursivelyEnumeratedSets), FacadeSets, PartiallyOrderedSets
(TotallyOrderedSets), TopologicalSets (MetricSets, CompleteMetricSets).

## Concrete Set Implementations

Key implementations:
- `Set` — generic set
- `FiniteSet` — explicitly listed finite sets
- `InfiniteSet` — marker for infinite sets
- `Set_object` — base class for set objects
- `RealSet` — unions of intervals: `.open(a,b)`, `.closed(a,b)`, `.open_closed(a,b)`,
  `.closed_open(a,b)`
- `ImageSet` / `ImageSubobject` — images of maps
- `ConditionSet` — predicate-defined sets
- Enumerated sets with cardinality

## RealSet Operations

`union`, `intersection`, `difference`, `symmetric_difference`, `complement`,
`is_subset`, `is_empty`. RealSet refines into TopologicalSets, MetricSets,
CompleteMetricSets.

## Topology, Metric, Complete

Sets with topological structure: `TopologicalSpaces()`, `MetricSpaces()`,
`CompleteMetricSpaces()`. Methods: `is_open`, `is_closed`, `closure`, `interior`,
`boundary`.

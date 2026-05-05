---
trackerStatus:
  type: decision
title: Decide how partition element methods override Sage list-returning methods
status: to-do
tags:
- category-specs
- decision
- sets
- partitions
- sage
- implementation
- needs-decision
- theme-decisions
planId: SPR-POSETS-PART-01KQN9
---

# Decide how partition element methods override Sage list-returning methods

## Summary

The partition refinement implementation card requires `refinements()`,
`coarsenings()`, and `strict_coarsenings()` to return project finite set objects.
Installed Sage already defines those concrete methods on the `SetPartition` element
class and returns Python lists. Ordinary category `ElementMethods` refinement cannot
override concrete methods already present on the Sage element class.

## Source Provenance

- Blocking card:
  `.agents/tasks/implementation/impl_01KQN9YGCG1916T40B7XTZX9MH-implement-partition-refinements-coarsenings-and-strict-coarsenings-as-fi.md`
- Spec leaf:
  `.agents/tasks/spec/spec_01KQN9YGC8WM34SAME35N4VGX5-specify-partition-refinements-coarsenings-and-strict-coarsenings-as-fini.md`
- Mapping anchors:
  - `category_specs/sets/docs/MAPPING.md`, rows for `refinements()`,
    `coarsenings()`, and `strict_coarsenings()`
  - `category_specs/sets/subcategories/partitioned.py`
- Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/combinat/set_partition.py`

## Context

`Sets().Partitioned().ElementMethods` records the project surface, but Sage's concrete
`SetPartition` element class already owns the same method names. A direct probe after
refining the fixed-base parent still shows:

```text
type(C.SetPartitions(3)([[1,3],[2]]).refinements()) == list
```

That means a normal category-method patch would document the desired surface but not
change runtime behavior.

## Decision Grounding Required

Before moving this decision to `decided`, choose the implementation route and record
the effect on public partition-element vocabulary:

- whether to introduce a true project `SetPartition` element wrapper/subclass and have
  fixed-base parents construct wrapped elements;
- whether to keep Sage names list-returning for interop and add project finite-set
  names such as `refinement_set()` / `coarsening_set()`;
- whether a localized monkeypatch of Sage `SetPartition` is acceptable in this spec
  layer; or
- whether the mapping/spec should be revised because the runtime surface cannot safely
  claim the Sage method names with different codomains.

## Acceptance Criteria

- [ ] The chosen route states whether public method names stay
  `refinements()`, `coarsenings()`, and `strict_coarsenings()` or move to separate
  project names.
- [ ] The decision records how element construction through
  `Sets().Constructors().SetPartitions(...)` preserves Sage membership and parent
  behavior.
- [ ] The decision forbids hidden monkeypatching unless the rationale and audit
  surface are explicitly accepted.
- [ ] The implementation card can either resume with a concrete write path or be
  revised/superseded without weakening the partition mapping silently.

## Dependencies And Boundaries

- Do not expose a generic Sage `Set(X)` constructor.
- Do not make `strict_coarsenings()` mean ordinary proper coarsening; Sage's method is
  reflexive and order-dependent.
- Do not treat this as a blocker for unrelated approved phase-01 leaves.

## Work Log

- 2026-05-05: Created after implementation preflight showed Sage concrete
  `SetPartition` methods shadow category `ElementMethods` and still return Python
  lists after parent refinement.

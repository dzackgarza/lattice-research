---
trackerStatus:
  type: feature
title: Admit finite totally ordered base-set owner for partitioned-set subclass predicates
status: in-review
priority: critical
planId: SPR-POSETS-PART-01KQN9
tags:
- category-specs
- spec
- feature
- sets
- partitions
- theme-constructor-routing
complexity: 65
progress: 90
created: '2026-05-05'
updated: '2026-05-05'
---

# Admit finite totally ordered base-set owner for partitioned-set subclass predicates

## Summary

Admit the category owner needed before noncrossing, nonnesting, or atomic partition
subclasses can become axiomatic subcategories. The prerequisite is a source-grounded
partitioned-set owner that records a fixed finite totally ordered base set, rather than
only a fixed base set.

## Source Provenance

- Parent decision card: `.agents/tasks/spec/spec_01KQN9YGC7HDGCSFP6JETA3ZZG-specify-partitioned-set-subclass-predicates-crossings-nestings-noncrossi.md`.
- Mapping source: `category_specs/sets/docs/MAPPING.md`, section `Set Partitions / Partitioned Sets`.
- Spec source: `category_specs/sets/subcategories/partitioned.py`.
- Local finite-order owners: `category_specs/sets/subcategories/totally_ordered.py` and `category_specs/sets/subcategories/totally_ordered_finite.py`.
- Sage reference: `https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/set_partition.html`.

## Context

The partition-subclass predicate decision admits `crossings()`, `nestings()`,
`is_noncrossing()`, `is_nonnesting()`, and `is_atomic()` as element methods on
`Sets().Partitioned()`. It rejects immediate global axiom admission because Sage's
crossing/nesting definitions use an arc diagram on an ordered finite ground set, and
atomicity uses the same standard ordered-set convention.

The next concrete spec task is to decide and implement the owner for partitions of a
fixed finite totally ordered base set. Only after that owner exists can a later pass
safely admit `Noncrossing`, `Nonnesting`, or `Atomic` as axiomatic subcategories or
predicate-defined subobjects with the correct hypotheses.

## Complexity And Ownership

- Owner/role: category-spec sets/partition spec implementer.
- Complexity: `65` (high).
- Rationale: this changes public category semantics for partitioned sets and controls
  whether downstream subclass predicates become axioms, subobjects, or element-only
  predicates. Mistakes can poison constructor routing and poset/partition subclass work.
- Split/promote note: keep this card limited to the finite totally ordered base-set
  owner. Do not admit `Noncrossing`, `Nonnesting`, or `Atomic` categories here unless
  the owner decision itself forces the exact axiom registration shape.

## Acceptance Criteria

- [x] The mapping docs state the exact category owner for partitions of a fixed finite totally ordered base set.
- [x] The spec surface records the owner without weakening the existing `Sets().Partitioned()` fixed-base-set meaning.
- [x] The decision states whether this owner is an axiom on `Sets().Partitioned()`, a meet with existing finite/totally ordered set owners, or a predicate-defined subobject route.
- [x] Any later `Noncrossing`, `Nonnesting`, or `Atomic` admission path is stated as a follow-up implementation/spec task with exact prerequisites, not hidden in prose.

## Dependencies And Boundaries

- Depends on the grounded partition-subclass predicate decision in the parent card.
- Do not expose a generic Sage `Set(X)` constructor.
- Do not admit noncrossing, nonnesting, or atomic partition global axioms without the finite total-order hypothesis encoded in the category graph.
- Do not use raw Python ordering as a substitute for a category-owned finite total order.

## Validation Requirements

- Re-read the Sage `SetPartition` docs and local set-order subcategory specs before editing.
- Run `rg -n "Noncrossing|Nonnesting|Atomic|crossings|nestings|totally ordered" category_specs/sets .agents/tasks/spec -g '*.md' -g '*.py'` after changes.
- Skip global QC unless the user explicitly asks for QC or a phase transition is being prepared.

## Grounded Decision

Sources reviewed for this owner decision:

- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/subcategories/partitioned.py`
- `category_specs/sets/subcategories/totally_ordered.py`
- `category_specs/sets/subcategories/totally_ordered_finite.py`
- Sage reference manual:
  `https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/set_partition.html`
- DeepWiki summary against `sagemath/sage` for `SetPartitions(X)` and order-dependent
  set-partition methods

Owner decision:

- The exact owner is `Sets().Partitioned().FiniteTotallyOrderedBase()`.
- This owner is an axiom on `Sets().Partitioned()`, implemented in
  `category_specs/sets/subcategories/partitioned.py` as
  `FiniteTotallyOrderedBasePartitionedSetsCategory`.
- It is not a meet with `Sets().TotallyOrdered()`. The total order belongs to the
  fixed base set returned by `base_set()`, not to the partition parent itself. A set
  of partitions is not thereby a totally ordered set.
- The owner also refines through `Sets().Countable().Finite()` because partitions of a
  fixed finite base set form a finite set.

Source basis for the distinction:

- Sage models `SetPartitions(X)` as partitions of a fixed base set `X`, matching the
  existing `Sets().Partitioned()` meaning.
- Sage's `crossings()`, `nestings()`, `is_noncrossing()`, and `is_nonnesting()`
  explicitly use the arc-diagram picture obtained by placing the ground-set elements in
  order on a line.
- Sage's `is_atomic()` uses the same order-sensitive standard-set-partition
  convention: order blocks by their minimal element and test pipe-indecomposability.

Follow-up shape fixed by this decision:

- Any future `Noncrossing`, `Nonnesting`, or `Atomic` owner must sit over
  `Sets().Partitioned().FiniteTotallyOrderedBase()`, not over bare
  `Sets().Partitioned()`.
- If a later pass needs subclass objects before axiom admission is finalized, the safe
  intermediate route is a predicate-defined subobject of a fixed parent already in
  `Sets().Partitioned().FiniteTotallyOrderedBase()`.

## Work Log

- 2026-05-05: Created as the concrete prerequisite exposed by the partition-subclass predicate decision.
- 2026-05-05: Recorded the owner as
  `Sets().Partitioned().FiniteTotallyOrderedBase()`, updated the sets mapping, and
  added the corresponding partitioned-set axiom surface without admitting
  `Noncrossing`, `Nonnesting`, or `Atomic`.

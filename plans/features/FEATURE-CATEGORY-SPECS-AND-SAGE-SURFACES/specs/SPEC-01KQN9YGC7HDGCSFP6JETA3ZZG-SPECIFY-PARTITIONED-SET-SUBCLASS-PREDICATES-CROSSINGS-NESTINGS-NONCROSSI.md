---
id: SPEC-01KQN9YGC7HDGCSFP6JETA3ZZG-SPECIFY-PARTITIONED-SET-SUBCLASS-PREDICATES-CROSSINGS-NESTINGS-NONCROSSI
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES]]'
title: Specify partitioned-set subclass predicates crossings nestings noncrossing
  nonnesting and atomic only after subcategory admission
status: needs-review
priority: critical
requirement: Sets mapping is the source of truth for set constructors, rich comparison,
  partitioned sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut
  ownership.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in
  the relevant MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No implementation blocker was discovered during this spec pass; the remaining finite-total-order
  prerequisite is represented as a separate spec item.
- When implementing a set item, cite the exact mapping row and prove behavior through
  project category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Specify partitioned-set subclass predicates crossings nestings noncrossing nonnesting and atomic only after subcategory admission
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Specify partitioned-set subclass predicates crossings nestings noncrossing nonnesting and atomic only after subcategory admission from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Source-Mining Contract

This leaf is truly source-mining because the mapping records the surfaces but does not
yet admit the governing subcategories.

Exact source anchors to mine:

- `category_specs/sets/docs/MAPPING.md:194-216`, especially row `:213`, which records
  `crossings`, `nestings`, `is_noncrossing`, `is_nonnesting`, and `is_atomic` as
  partitioned-set surfaces reserved for future axiomatic subcategory admission.
- `category_specs/sets/docs/MAPPING.md:209-214`, which fixes the surrounding object as
  an ordered finite set partition with arc-diagram and restriction/standardization
  methods on the same partition element surface.
- `.agents/skills/category-spec-style/references/style.md:1160-1169`, which governs how
  any admitted axiomatic subcategory must register `_base_category_class_and_axiom`.
- `.agents/skills/category-spec-style/references/style.md:1229-1242`, which requires
  the final methods and predicates to be placed at the highest mathematically valid
  owner category.

Decision this source-mining pass must produce:

- Object/method/constructor decision: separate the witness-valued surfaces
  `crossings()` and `nestings()` from the boolean/predicate surfaces
  `is_noncrossing()`, `is_nonnesting()`, and `is_atomic()`, and state whether the
  booleans remain element predicates, induce admitted axiomatic subcategories, or both.
- Owner category decision: identify the exact owner under `Sets().Partitioned()` for
  each surface, including any future admitted subcategories such as noncrossing,
  nonnesting, or atomic partitioned sets.
- Hypotheses: record the exact domain assumptions needed for each notion, including
  whether the predicate requires a finite partition, a linearly ordered base set, and
  the arc-diagram interpretation fixed by the partition mapping.
- Return object/codomain: `crossings()` and `nestings()` must land in witness lists of
  crossing/nesting arc pairs, not scalar counts; `is_noncrossing()`,
  `is_nonnesting()`, and `is_atomic()` must land in boolean predicates or in admitted
  axiomatic subcategory membership with the boolean witness spelled out.

Retire this card only when the cited sources produce a grounded owner decision and, if
subcategory admission is chosen, the exact admitted axiom names and registration shape.
Reject this leaf if source review shows these notions should remain only as combinatorial
element methods with no subcategory admission at all.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No implementation blocker was discovered during this spec pass; the remaining
  finite-total-order prerequisite is represented as a separate spec item.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Grounded Decision

Sources reviewed for this decision:

- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- `category_specs/sets/subcategories/partitioned.py`
- `category_specs/sets/subcategories/condition.py`
- `category_specs/sets/subcategories/totally_ordered.py`
- `category_specs/sets/subcategories/totally_ordered_finite.py`
- Sage reference manual:
  `https://doc.sagemath.org/html/en/reference/combinat/sage/combinat/set_partition.html`

Owner and codomain decision:

- `crossings()` and `nestings()` are `Sets().Partitioned().ElementMethods` surfaces.
  Sage defines them on `SetPartition` elements and returns witness lists of pairs of
  arcs, not counts and not parent-level data.
- `is_noncrossing()`, `is_nonnesting()`, and `is_atomic()` are also
  `Sets().Partitioned().ElementMethods` surfaces. They are boolean predicates on a
  single partition element, not constructors and not parent/category predicates.
- `crossings_iterator()` and `nestings_iterator()` stay implementation helpers, not
  primary project method names. The spec surface keeps the finite witness lists and the
  booleans built from them.

Hypotheses and admission consequence:

- `crossings()`, `nestings()`, `is_noncrossing()`, and `is_nonnesting()` require the
  finite base set to be totally ordered. Sage's definition is the arc-diagram picture
  obtained by placing ground-set elements in order on a line and connecting consecutive
  elements within each block.
- `is_atomic()` is not an arc-count notion. Sage defines it by pipe-indecomposability
  of a nonempty standard set partition: order the blocks by minimal element and ask
  whether the partition splits as `B | C`.
- Because the current `Sets().Partitioned()` axiom captures only "partitions of a
  fixed base set", these predicates are not admitted yet as axiomatic subcategories
  such as `Sets().Partitioned().Noncrossing()`, `.Nonnesting()`, or `.Atomic()`. The
  missing owner is a source-grounded category that records the required finite total
  order on the base set.
- If the project later needs subclass objects before that owner exists, the first
  admissible constructor is a predicate-defined subobject of a fixed partition parent
  via the existing `Sets().Subobjects().Of(...)` / `condition_subset(...)` route, not a
  new global partition axiom.

Acceptance consequence for implementation:

- `category_specs/sets/subcategories/partitioned.py` should carry abstract element
  methods for `crossings()`, `nestings()`, `is_noncrossing()`, `is_nonnesting()`, and
  `is_atomic()`, with the finite totally ordered base-set hypothesis stated in the
  docstrings.
- A future admission card is still required before adding `_base_category_class_and_axiom`
  registrations for noncrossing, nonnesting, or atomic partition categories.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Grounded the owner decision against Sage's `SetPartition` docs and the
  local partitioned-set mapping. Recorded that the five surfaces belong on
  `Sets().Partitioned().ElementMethods` now, while axiom admission remains blocked on a
  category that records finite totally ordered base sets. That prerequisite is now
  tracked in `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-20260505-PARTITIONED-FINITE-TOTALLY-ORDERED-BASE-OWNER.md`.

---
trackerStatus:
  type: feature
title: Specify partitioned-set subclass predicates crossings nestings noncrossing nonnesting and atomic only after subcategory admission
status: to-do
priority: critical
planId: SPR-POSETS-PART-01KQN9
tags:
- category-specs
- spec
- feature
- sets
- partitions
- theme-constructor-routing
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

- Object/method/constructor decision: separate the count-valued surfaces
  `crossings()` and `nestings()` from the boolean/predicate surfaces
  `is_noncrossing()`, `is_nonnesting()`, and `is_atomic()`, and state whether the
  booleans remain element predicates, induce admitted axiomatic subcategories, or both.
- Owner category decision: identify the exact owner under `Sets().Partitioned()` for
  each surface, including any future admitted subcategories such as noncrossing,
  nonnesting, or atomic partitioned sets.
- Hypotheses: record the exact domain assumptions needed for each notion, including
  whether the predicate requires a finite partition, a linearly ordered base set, and
  the arc-diagram interpretation fixed by the partition mapping.
- Return object/codomain: `crossings()` and `nestings()` must land in an integer-valued
  codomain; `is_noncrossing()`, `is_nonnesting()`, and `is_atomic()` must land in
  boolean predicates or in admitted axiomatic subcategory membership with the boolean
  witness spelled out.

Retire this card only when the cited sources produce a grounded owner decision and, if
subcategory admission is chosen, the exact admitted axiom names and registration shape.
Reject this leaf if source review shows these notions should remain only as combinatorial
element methods with no subcategory admission at all.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [ ] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

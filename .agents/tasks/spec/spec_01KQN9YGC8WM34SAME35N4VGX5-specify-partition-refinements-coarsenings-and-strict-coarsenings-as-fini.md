---
trackerStatus:
  type: feature
title: Specify partition refinements coarsenings and strict coarsenings as finite subsets refining through set constructors
status: to-do
priority: critical
planId: SPR-POSETS-PART-01KQN9
tags:
- category-specs
- spec
- feature
- constructors
- sets
- partitions
- theme-constructor-routing
---

# Specify partition refinements coarsenings and strict coarsenings as finite subsets refining through set constructors
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Specify partition refinements coarsenings and strict coarsenings as finite subsets refining through set constructors from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Grounded Spec Contract

Source anchors for this leaf are already concrete enough to authorize the spec edit:

- `category_specs/sets/docs/MAPPING.md:194-216`, especially the `SetPartition`
  method row at `:215`, which fixes `refinements()`, `coarsenings()`, and
  `strict_coarsenings()` as finite subsets of partition elements.
- `category_specs/sets/docs/MAPPING.md:196-208`, which fixes the same object as a
  fixed-base partition element in the refinement lattice and locates the lattice
  operations on `Partitioned.ElementMethods`.
- `.agents/skills/category-spec-style/references/style.md:1139-1149`, which makes
  `MAPPING.md` the canonical owner/migration source for subtree method placement.
- `.agents/skills/category-spec-style/references/style.md:1229-1242`, which requires
  the method to live at the highest category where it is universally well-defined and
  forbids restating inherited behavior at lower levels without new mathematics.

Concrete contract for the spec edit:

- Owner category: `Sets().Partitioned()` on the partition element surface, with the
  finite-base Sage `SetPartition` object as the source-backed witness.
- Public methods to specify: `refinements()`, `coarsenings()`, and
  `strict_coarsenings()` as partition-element methods.
- Hypotheses: the input object is a partition of a finite fixed base set, so the
  refinement lattice neighborhood determined by these methods is finite.
- Return object/codomain: a finite set object of partition elements, routed through set
  constructors rather than a raw Python container or an untyped Sage iterator.
- Migration consequence: do not remap these methods to poset constructors, graph
  surfaces, or free-floating helper functions; they stay attached to partition
  elements and refine through the canonical set-constructor vocabulary.

Retire or reject this leaf only if a cited mapping row is superseded by a source-backed
owner change showing that one of these methods is not a partition-element method or does
not return a finite set object.

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

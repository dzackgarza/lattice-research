---
id: SPEC-01KQN9YGC8WM34SAME35N4VGX5-SPECIFY-PARTITION-REFINEMENTS-COARSENINGS-AND-STRICT-COARSENINGS-AS-FINI
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-POSET-CONSTRUCTOR-SMOKE-AND-DEFERRED-SURFACES]]'
title: Specify partition refinements coarsenings and strict coarsenings as finite
  subsets refining through set constructors
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
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance.
- When implementing a set item, cite the exact mapping row and prove behavior through
  project category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
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

- Owner category for the project finite-set wrappers of Sage `refinements()` and
  `coarsenings()`:
  `Sets().Partitioned()` on the partition element surface, with the fixed finite-base
  Sage `SetPartition` object as the source-backed witness.
- Owner category for the project finite-set wrapper of Sage's `strict_coarsenings()`:
  `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods`, because Sage's
  definition compares ordered blocks using `max(part) < min(other)`.
- Public project methods to specify: `refinement_set()`, `coarsening_set()`, and
  `ordered_coarsening_closure()` as partition-element methods at those split owners.
  Sage's concrete `refinements()`, `coarsenings()`, and `strict_coarsenings()` names
  remain list-returning compatibility methods on Sage `SetPartition` elements.
- Hypotheses: the input object is a partition of a finite fixed base set, so the
  refinement lattice neighborhoods determined by `refinements()` and `coarsenings()`
  are finite. Sage-compatible `strict_coarsenings()` additionally requires the finite
  totally ordered base-set owner.
- Return object/codomain: a finite set object of partition elements, routed through set
  constructors rather than a raw Python container or an untyped Sage iterator.
- Migration consequence: do not remap these methods to poset constructors, graph
  surfaces, or free-floating helper functions; they stay attached to partition elements
  and refine through the canonical set-constructor vocabulary. Project finite-set
  wrappers use separate names because Sage already owns the concrete list-returning
  names. Do not treat Sage's `strict_coarsenings()` as ordinary proper coarsenings:
  Sage defines a reflexive closure and includes `self`.

Retire or reject this leaf only if a cited mapping row is superseded by a source-backed
owner change showing that one of these methods is not a partition-element method or does
not return a finite set object.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Split the owner decision after checking Sage behavior and source:
  `refinements()` and `coarsenings()` live on `Sets().Partitioned().ElementMethods`;
  Sage-compatible `strict_coarsenings()` lives on
  `Sets().Partitioned().FiniteTotallyOrderedBase().ElementMethods`, returns a finite
  set object in the project spec, and is not ordinary proper coarsening.
- 2026-05-05: Updated public method names after
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-20260505-PARTITION-ELEMENT-METHOD-SHADOWING.md` decided that
  Sage's concrete list-returning names must remain compatibility methods. The project
  finite-set methods are now `refinement_set()`, `coarsening_set()`, and
  `ordered_coarsening_closure()`.

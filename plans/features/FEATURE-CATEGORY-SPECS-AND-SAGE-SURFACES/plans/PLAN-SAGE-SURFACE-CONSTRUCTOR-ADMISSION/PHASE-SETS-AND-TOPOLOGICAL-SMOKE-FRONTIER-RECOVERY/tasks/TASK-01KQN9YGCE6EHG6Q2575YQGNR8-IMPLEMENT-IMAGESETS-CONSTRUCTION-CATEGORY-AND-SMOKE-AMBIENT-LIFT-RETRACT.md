---
id: TASK-01KQN9YGCE6EHG6Q2575YQGNR8-IMPLEMENT-IMAGESETS-CONSTRUCTION-CATEGORY-AND-SMOKE-AMBIENT-LIFT-RETRACT
trackerStatus:
  type: task
parents:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
dependsOn: []
title: Implement ImageSets construction category and smoke ambient lift retract and
  image-subobject membership
status: needs-review
priority: high
description: Sets mapping is the source of truth for set constructors, rich comparison,
  partitioned sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut
  ownership.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- When implementing a set item, cite the exact mapping row and prove behavior through
  project category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
---
# Implement ImageSets construction category and smoke ambient lift retract and image-subobject membership
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Implement ImageSets construction category and smoke ambient lift retract and image-subobject membership from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [x] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Commit `983a058` completed the smoke-facing ImageSubobject implementation
  against the `category_specs/sets/docs/MAPPING.md` image-subobject rows: the constructor
  remains the typed `Sets().Constructors().ImageSubobject(f, domain_subset)` route,
  the result refines through `ImageSets`, subobjects, and subquotients, and finite image
  subobjects now recover membership and cardinality in the Sets smoke without exposing
  generic Sage `Set(X)` as a public constructor.
- 2026-05-05: Validation evidence from `983a058`: `just --justfile
  category_specs/justfile smoke-file sets/smoketest.sage` passed; `just --justfile
  category_specs/justfile check-abstract-redefinitions` passed; `git diff --check`
  passed. This card is moved to `in-review`; human acceptance is still required for
  closure.

## Review Log

### Review - 2026-05-07

Outcome: review gap found and repaired; card remains `needs-review` for a fresh review
and human acceptance.

- Gate 2 initially lacked direct smoke evidence for the ambient/lift/retract part of
  the card title. The existing smoke covered finite-image membership and cardinality
  for a Python callable whose Sage codomain is `None`.
- Added a focused smoke witness using a set morphism
  `IntegerRange(3) -> IntegerRange(5)` so `ImageSubobject.ambient()` is a real
  codomain rather than Sage's callable fallback.
- Added smoke assertions for `ambient()`, `lift()`, and `retract()` on that codomain
  witness while preserving the existing membership/cardinality assertions.

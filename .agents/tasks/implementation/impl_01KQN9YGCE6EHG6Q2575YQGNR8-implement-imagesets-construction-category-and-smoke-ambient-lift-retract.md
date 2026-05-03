---
trackerStatus:
  type: feature
title: Implement ImageSets construction category and smoke ambient lift retract and
  image-subobject membership
---
# Implement ImageSets construction category and smoke ambient lift retract and image-subobject membership
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `plans/category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Implement ImageSets construction category and smoke ambient lift retract and image-subobject membership from plans/category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [ ] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


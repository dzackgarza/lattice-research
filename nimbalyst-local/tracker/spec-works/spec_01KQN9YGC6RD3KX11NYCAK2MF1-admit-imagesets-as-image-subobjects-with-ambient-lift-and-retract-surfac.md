---
trackerStatus:
  itemId: spec_01KQN9YGC6RD3KX11NYCAK2MF1
  title: Admit ImageSets as image subobjects with ambient lift and retract surface
  type: spec-work
  status: to-do
  priority: medium
  assignee: null
  tags:
  - cat
  - category-specs
  - sets
  - spec-work
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Admit ImageSets as image subobjects with ambient lift and retract surface

## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `plans/category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Admit ImageSets as image subobjects with ambient lift and retract surface from plans/category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

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


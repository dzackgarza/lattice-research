---
trackerStatus:
  type: feature
title: Implement partition refinements coarsenings and strict coarsenings as finite-set constructor outputs
status: blocked
priority: high
planId: SPR-POSETS-PART-01KQN9
progress: 10
updated: '2026-05-05'
tags:
- category-specs
- implementation
- feature
- constructors
- sets
- partitions
- theme-constructor-routing
---

# Implement partition refinements coarsenings and strict coarsenings as finite-set constructor outputs
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Implement partition refinements coarsenings and strict coarsenings as finite-set constructor outputs from category_specs/sets/docs/MAPPING.md`

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

## Path-Local Blocker

Blocked on `.agents/decisions/dec_20260505_partition_element_method_shadowing.md`.

Preflight evidence:

- Sage source defines concrete `SetPartition.refinements()`,
  `SetPartition.coarsenings()`, and `SetPartition.strict_coarsenings()` in
  `sage/combinat/set_partition.py`.
- After refining the fixed-base parent through project constructors,
  `C.SetPartitions(3)([[1,3],[2]]).refinements()` still returns a Python `list`.
- Therefore adding ordinary category `ElementMethods` with the same method names would
  not change runtime behavior; Sage's element-class methods shadow the category method
  provider.

This blocks only this finite-set-output leaf. It does not block other approved
partition/spec work.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Preflighted the implementation route and found a Sage concrete-method
  shadowing issue. Created
  `.agents/decisions/dec_20260505_partition_element_method_shadowing.md` and blocked
  this leaf until the project chooses wrapper, renamed project methods, monkeypatch, or
  spec-revision strategy.

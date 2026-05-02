---
trackingStatus:
  itemId: dec_01KQN9YGCTP85RXF1F56D8S08X
  title: Decide whether partitioned-set combinatorial subclasses such as noncrossing
    and atomic become axiomatic subcategories in the current set-partition pass or
    a later pass
  type: design-decision
  status: needs-decision
  priority: medium
  assignee: null
  tags:
  - cat
  - category-specs
  - design-decision
  - sets
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Decide whether partitioned-set combinatorial subclasses such as noncrossing and atomic become axiomatic subcategories in the current set-partition pass or a later pass

## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `plans/category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Decide whether partitioned-set combinatorial subclasses such as noncrossing and atomic become axiomatic subcategories in the current set-partition pass or a later pass from plans/category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Acceptance Criteria

- [ ] The decision record lists the alternatives, selected outcome, rationale, consequences, and affected tracker items.
- [ ] If the decision changes category ownership, the relevant MAPPING.md is updated in the same work or a linked spec-work item.
- [ ] The decision status moves from needs-decision to decided only after the consequence is explicit enough for implementation.
- [ ] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [ ] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


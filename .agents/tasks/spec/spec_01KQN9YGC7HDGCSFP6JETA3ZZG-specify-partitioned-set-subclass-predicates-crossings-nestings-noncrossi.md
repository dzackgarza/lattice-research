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

## Definition Grounding Required Before Spec Edit

This migrated card is executable for source mining and decision capture, but it does not by itself authorize a mathematical spec edit. Before moving, deleting, admitting, or generalizing any public category, method, constructor, predicate, invariant, Hom/End/Aut surface, or return type, record the canonical source path, exact definition, owner category, hypotheses, codomain/return object, and any invariance or equivalence proof obligation.

Use the subtree `MAPPING.md` and `SAGE_INVENTORY.md` files, Sage written docs/source, `theory/references/index.md` for literature-backed claims, and relevant repo `theory/` or skill-local sources. If the term is ambiguous or only supported by migrated backlog text, split to source-mining or decision work before editing specs.

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


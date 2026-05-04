---
trackerStatus:
  type: decision
title: Decide whether equivalence relations and set partitions need a first-class set subtree or remain centralized Sage-backed type aliases
status: to-do
tags:
- category-specs
- decision
- sage
- sets
- partitions
- set-partitions
- types
- needs-decision
- theme-decisions
planId: SPR-POSETS-PART-01KQN9
---

# Decide whether equivalence relations and set partitions need a first-class set subtree or remain centralized Sage-backed type aliases

## Summary

The deleted Posets triage recorded settled order-theoretic mapping items, a concrete
design decision about equivalence relations/set partitions, and evidence gaps around
semilattice category introspection.

## Source Provenance

- `category_specs/posets/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/posets/docs/TRIAGE.md`.
- Original migrated line: `Decide whether equivalence relations and set partitions need a first-class set subtree or remain centralized Sage-backed type aliases from category_specs/posets/docs/TRIAGE.md`

## Context

- Poset constructors are named non-variadic adaptations; acyclic DiGraph is the canonical finite-poset constructor.
- Meet and join expose binary operations plus sequence folds, not optional-argument aggregate signatures.
- Lattice congruences use set-theoretic vocabulary: EquivalenceRelation and SetPartition, with congruence_generated_by(blocks).
- certificate=True Sage paths map to separately named witness-returning certificate methods.
- Sage semilattice category evidence remains incomplete because local Sage imports failed before category introspection.

## Acceptance Criteria

- [ ] The decision record lists the alternatives, selected outcome, rationale, consequences, and affected tracker items.
- [ ] If the decision changes category ownership, the relevant MAPPING.md is updated in the same work or a linked spec-work item.
- [ ] The decision status moves from needs-decision to decided only after the consequence is explicit enough for implementation.
- [ ] Run just smoke-file posets/smoketest.sage after poset constructor or method changes.
- [ ] Use the five-field negative-finding format for further Sage semilattice evidence gaps.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

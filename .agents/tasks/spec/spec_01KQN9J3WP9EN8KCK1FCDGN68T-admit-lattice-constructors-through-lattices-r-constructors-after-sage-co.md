---
trackerStatus:
  type: feature
title: Admit lattice constructors through Lattices(R).Constructors after Sage constructor
  inventory mapping
status: blocked
priority: critical
planId: PLN-LAT-040
tags:
- category-specs
- spec
- feature
- constructors
- sage
- lattices
- mapping
- theme-constructor-routing
- theme-modules-tensors
---

# Admit lattice constructors through Lattices(R).Constructors after Sage constructor inventory mapping
## Summary

The deleted Lattices triage recorded the top-level lattice subtree admission, current
smoke coverage, constructor admission boundary, and DiscriminantGroupAut blocker.

## Source Provenance

- `category_specs/lattices/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/lattices/docs/TRIAGE.md`.
- Original migrated line: `Admit lattice constructors through Lattices(R).Constructors after Sage constructor inventory mapping from category_specs/lattices/docs/TRIAGE.md`

## Context

- Lattice smokes cover Cat registration, the ambient module chain, Hom/End/Aut construction, Subobjects, DualObjects/DualLattices vocabulary, and Even predicate surface.
- Constructor admission remains outside the current smoke surface and must enter through Lattices(R).Constructors() after Sage constructor inventory mapping.
- LatticeOrthogonalGroup is Lattices(R).AutCategory().Of(L), specializing the formed-module aut surface.
- DiscriminantGroupAut export is blocked until discriminant_groups.py defines Hom, End, and Aut standard names.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Run just smoke-file lattices/chain_smoketest.sage and just smoke-file lattices/smoketest.sage for lattice-surface changes.
- [ ] Do not admit lattice constructors without completing Sage constructor inventory mapping.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

- 2026-05-04: Marked `status: blocked` because the card body already records the DiscriminantGroupAut prerequisite; continue other approved phase-01 leaves until that prerequisite is available.

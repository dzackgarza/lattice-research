---
trackerStatus:
  type: feature
title: Define DiscriminantGroup Hom End Aut standard names so DiscriminantGroupAut
  can be exported
status: in-review
priority: critical
planId: PLN-CAT-120
phasePlan: PLN-LAT-040
progress: 90
tags:
- category-specs
- spec
- feature
- hom-end-aut
- theme-category-core
---

# Define DiscriminantGroup Hom End Aut standard names so DiscriminantGroupAut can be exported
## Summary

The deleted Lattices triage recorded the top-level lattice subtree admission, current
smoke coverage, constructor admission boundary, and DiscriminantGroupAut blocker.

## Source Provenance

- `category_specs/lattices/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/lattices/docs/TRIAGE.md`.
- Original migrated line: `Define DiscriminantGroup Hom End Aut standard names so DiscriminantGroupAut can be exported from category_specs/lattices/docs/TRIAGE.md`

## Context

- Lattice smokes cover Cat registration, the ambient module chain, Hom/End/Aut construction, Subobjects, DualObjects/DualLattices vocabulary, and Even predicate surface.
- Constructor admission remains outside the current smoke surface and must enter through Lattices(R).Constructors() after Sage constructor inventory mapping.
- LatticeOrthogonalGroup is Lattices(R).AutCategory().Of(L), specializing the formed-module aut surface.
- DiscriminantGroupAut export is blocked until discriminant_groups.py defines Hom, End, and Aut standard names.

## Grounded Review Outcome

Grounded target for this card:

- Source anchors:
  - `category_specs/lattices/docs/MAPPING.md`;
  - `category_specs/homsets/docs/MAPPING.md`;
  - `.agents/skills/lattice-redesign/references/category-abc-spec.md`;
  - `theory/foundations/bilinear-forms-duals-morphisms.md`;
  - `theory/references/index.md` for literature-backed discriminant-form claims.
- Mathematical object: for a lattice `L`, the discriminant object is the quotient
  `A_L = L^*/L`, with the descended quotient-valued bilinear or quadratic form when the
  ambient formed-module data provides one.
- Hom/End/Aut contract: `DiscriminantGroupHom`, `DiscriminantGroupEnd`, and
  `DiscriminantGroupAut` name the morphism, endomorphism, and automorphism parents for
  form-preserving morphisms of `A_L`; they classify categorical morphisms, not raw
  generators, matrices, or Sage torsion backends.
- Concrete dependency: this leaf is blocked on the discriminant-group owner file
  defining the standard Hom/End/Aut type package and export surface consistent with the
  generic hom/end/aut hierarchy. Until that owner exists, do not export
  `DiscriminantGroupAut` from the lattice subtree.
- Work this card can still do while blocked: pin the exact names, object definition,
  preservation law, and migration consequence against the mapping docs so the eventual
  owner implementation is a direct wiring task rather than another definition-mining
  pass.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance. No new implementation blocker was discovered; the recorded blocker was stale.
- [ ] Run just smoke-file lattices/chain_smoketest.sage and just smoke-file lattices/smoketest.sage for lattice-surface changes.
- [ ] Do not admit lattice constructors without completing Sage constructor inventory mapping.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

- 2026-05-04: Marked `status: blocked` because the card body already records the DiscriminantGroupAut prerequisite; continue other approved phase-01 leaves until that prerequisite is available.
- 2026-05-05: Rechecked `category_specs/lattices/subcategories/constructions/discriminant_groups.py`
  and `category_specs/types.py`; the standard Hom/End/Aut names already exist and are
  exported. Added the missing mapping note to `category_specs/lattices/docs/MAPPING.md`
  and moved this card to `in-review` because the prior blocker is stale. This was a
  mapping/card update only; lattice smoke commands were not run because no code surface
  changed.

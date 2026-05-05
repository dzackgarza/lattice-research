---
id: SPEC-01KQN9YGC6RD3KX11NYCAK2MF1-ADMIT-IMAGESETS-AS-IMAGE-SUBOBJECTS-WITH-AMBIENT-LIFT-AND-RETRACT-SURFAC
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
title: Admit ImageSets as image subobjects with ambient lift and retract surface
status: needs-review
priority: critical
requirement: Sets mapping is the source of truth for set constructors, rich comparison, partitioned
  sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in the relevant
  MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No implementation blocker was discovered during this spec pass.
- When implementing a set item, cite the exact mapping row and prove behavior through project
  category vocabulary.
- Do not expose generic Sage Set(X) as a public project constructor.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- category-specs
- sets
- imagesets
- theme-sets-topology
updated: '2026-05-05'
---
# Admit ImageSets as image subobjects with ambient lift and retract surface
## Summary

Sets mapping is the source of truth for set constructors, rich comparison, partitioned
sets, ImageSets, Primes version skew, RealSet routing, and set/hom/end/aut ownership.

## Source Provenance

- `category_specs/sets/docs/MAPPING.md`
- Original migrated line: `Admit ImageSets as image subobjects with ambient lift and retract surface from category_specs/sets/docs/MAPPING.md`

## Context

- ImageSets are image subobjects and must expose ambient, lift, and retract surface.
- Fixed-base SetPartitions(s) refines through Sets().Partitioned(); all finite partitions without a fixed base remain countable-only.
- Set rich comparison is set-theoretic inclusion and equality, not Sage wrapper comparison behavior.
- Partitioned-set predicates such as crossings, nestings, noncrossing, nonnesting, and atomic are mapped for future axiomatic subcategory admission.
- Primes documentation and installed source are version-skewed; congruence-class prime subsets need further evidence before admission.

## Grounded Spec Contract

Canonical source anchors for this card are:

- `category_specs/sets/docs/MAPPING.md`:
  - local-surface row
    `| _ImageSets | subcategories/image.py | Images are subobjects under a map. |`
  - constructor decision row
    `| ImageSubobject(f, X) | ImageSets | Image subobject under a map; must include ambient, lift, and retract. |`
  - subobject-routing rows for `ConditionSet` and constructive subobjects
- `category_specs/sets/docs/SAGE_INVENTORY.md` if additional Sage surface detail is
  needed for `ImageSubobject`
- `category_specs/topological_spaces/docs/MAPPING.md` only if a future example uses
  image subsets inside a topological ambient; it is not owner authority for the image
  notion itself

Spec decision fixed by those sources:

- owner category: `Sets().Subobjects()` with explicit refinement through
  `Sets().Subquotients()` owns the image notion
- admitted object: `ImageSets` is the public image-subobject category for images of a
  map, not a generic wrapper around arbitrary Sage `Set(X)` values
- required public surface on the image object is `ambient`, `lift`, and `retract`

Required hypotheses and return/codomain obligations:

- input data must include a map `f` and an ambient/source object `X` sufficient to form
  the image subobject
- `ambient()` returns the ambient set containing the image subobject
- `lift(...)` returns an image element viewed in the ambient codomain
- `retract(...)` returns the corresponding image-side object or element when an
  ambient element is in the image, matching the constructive subobject contract
- any further topological or algebraic refinement is inherited from the ambient object;
  it does not redefine the set-level image owner
- Sage's arbitrary callable wrapping and non-parent `Set(X)` fallback are interop
  details; the project constructor surface stays typed as `SetMorphism` plus
  `Subset`

Rejection or retirement condition:

- reject any edit that exposes generic Sage `Set(X)` as the public constructor, drops
  any of `ambient`/`lift`/`retract`, or relocates image ownership away from the
  subobject construction surface without a new mapped source anchor

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No implementation blocker was discovered during this spec pass.
- [x] When implementing a set item, cite the exact mapping row and prove behavior through project category vocabulary.
- [x] Do not expose generic Sage Set(X) as a public project constructor.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Admitted `_ImageSets` as a constructive image subobject/subquotient
  surface, recorded the `ambient`/`lift`/`retract` obligations in mapping docs and
  `image.py`, and rejected Sage's generic callable/`Set(X)` fallback as public project
  API.

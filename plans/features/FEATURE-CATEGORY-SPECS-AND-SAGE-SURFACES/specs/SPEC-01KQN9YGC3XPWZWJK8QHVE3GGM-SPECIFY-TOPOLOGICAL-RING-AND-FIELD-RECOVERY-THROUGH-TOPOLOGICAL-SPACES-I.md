---
id: SPEC-01KQN9YGC3XPWZWJK8QHVE3GGM-SPECIFY-TOPOLOGICAL-RING-AND-FIELD-RECOVERY-THROUGH-TOPOLOGICAL-SPACES-I
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
title: Specify topological ring and field recovery through topological_spaces inheritance
  rather than pure topological constructors
status: needs-review
priority: critical
requirement: Rings mapping records constructor namespace decisions, split p-adic and q-adic
  precision routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
  lattice-precision gaps.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in the relevant
  MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No implementation blocker was discovered during this spec pass.
- For q-adic precision items, preserve the five-field negative finding format when updating
  evidence.
- For topological ring work, check both ring and topological-space category membership in
  the existing public spec anchors.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- category-specs
- constructors
- rings
- topology
- theme-constructor-routing
updated: '2026-05-05'
---
# Specify topological ring and field recovery through topological_spaces inheritance rather than pure topological constructors
## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
lattice-precision gaps.

## Source Provenance

- `category_specs/rings/docs/MAPPING.md`
- `category_specs/topological_spaces/docs/MAPPING.md`
- Pre-migration triage content recovered from `git show 8d1c21c^:plans/category_specs/topological_spaces/docs/TRIAGE.md`
- Original migrated line: `Specify topological ring and field recovery through topological_spaces inheritance rather than pure topological constructors from category_specs/rings/docs/MAPPING.md and category_specs/topological_spaces/docs/TRIAGE.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- ZqWithPrecisionCaps and QqWithPrecisionCaps are retained admitted split names but remain deferred frontiers because installed Sage lacks a working unramified q-adic extension path with split lattice caps.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Grounded Spec Contract

Canonical source anchors for this card are:

- `category_specs/rings/docs/MAPPING.md`:
  - `## Topological Rings`
  - constructor-namespace guidance keeping ring/field constructors in
    `Rings().Constructors()`
  - the construction-category ownership rows showing ring-side ownership for ring
    homsets, endsets, automorphisms, products, subobjects, quotients, and realizations
- `category_specs/topological_spaces/docs/MAPPING.md`:
  - `Sets().Topological() -> TopologicalSpaces()`
  - `Sets().Metric() -> TopologicalSpaces().Metric()`
  - constructor-candidate rows explicitly excluding pure
    `TopologicalSpaces().Constructors()` admission for interval/ball/field objects
- `category_specs/rings/subcategories/topological.py`:
  - `super_categories()` keeping the ring-side topological edge at
    `SageRings().Topological()` and `Rings()`
- `category_specs/topological_spaces/__init__.py`:
  - `TopologicalSpaces().ParentMethods` ownership for `is_open`, `is_closed`,
    `closure`, `interior`, `boundary`, `is_connected`, and `is_compact`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`:
  - numeric interval and ball surfaces showing these objects as topology-bearing
    evidence, not pure topological-space constructors

Spec decision fixed by those sources:

- topological predicates and transforms are owned by `TopologicalSpaces()` and its
  refinements
- ring and field operations remain owned by `Rings()` and downstream ring/field
  subcategories
- recovery path: a topological ring or field is specified by inheritance/join of the
  algebraic subtree with the topological-space subtree, not by admitting duplicate
  constructors or ring-local copies of topological methods

Required hypotheses and return/codomain obligations:

- every candidate object must first be admitted through the ring/field constructor
  namespace or an already grounded Sage ring/field object
- topological methods inherited into a ring or field keep the same codomain contracts
  recorded in `topological_spaces`: boolean predicates return `bool`; closure/interior
  /boundary-style operations return subsets of the same ambient topological object
- no spec edit may change the object returned by a ring constructor into a pure
  topological-space object detached from its ring/field owner

Rejection or retirement condition:

- reject any edit that introduces `TopologicalSpaces().Constructors()` entries for
  rings, fields, interval fields, or ball fields, or that duplicates topological-space
  method ownership inside a ring-only file rather than inheriting it

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No implementation blocker was discovered during this spec pass.
- [x] For q-adic precision items, preserve the five-field negative finding format when updating evidence.
- [x] For topological ring work, check both ring and topological-space category membership in the existing public spec anchors.

## Grounded Recovery Decision

Decision: topological rings and fields recover their topological predicates and
ambient-relative transforms through the `TopologicalSpaces()` public surface, while
construction stays in `Rings().Constructors()` and downstream ring/field constructor
routes.

This pass records:

- ring-side topological membership is expressed by `Rings().Topological()` in
  `category_specs/rings/subcategories/topological.py`;
- topological predicate ownership remains in
  `category_specs/topological_spaces/__init__.py` on
  `TopologicalSpaces().ParentMethods`;
- mapping docs now state that real/complex precision fields, interval fields, ball
  fields, and p-adic/q-adic rings and fields recover topological behavior by
  inheritance/join instead of by `TopologicalSpaces().Constructors()` admission.

Migration consequence:

- the constructor namespace for these objects remains ring/field-owned;
- inherited topological methods keep the codomain obligations already fixed in
  `topological_spaces`;
- no ring-only file becomes a second owner for `is_open`, `is_closed`, `closure`,
  `interior`, `boundary`, `is_connected`, or `is_compact`.

Validation note: runtime smoke/QC execution was intentionally skipped for this bounded
phase-01 spec leaf. The source check here is document/spec-level only.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Recorded the topological ring/field inheritance route in ring and
  topological-space mapping docs, using the existing `Rings().Topological()` and
  `TopologicalSpaces()` public spec anchors rather than introducing new constructors
  or duplicate method owners.

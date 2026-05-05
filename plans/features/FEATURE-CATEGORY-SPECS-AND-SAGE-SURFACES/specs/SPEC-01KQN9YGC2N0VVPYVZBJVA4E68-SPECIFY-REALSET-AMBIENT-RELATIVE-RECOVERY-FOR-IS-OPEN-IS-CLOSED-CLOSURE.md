---
id: SPEC-01KQN9YGC2N0VVPYVZBJVA4E68-SPECIFY-REALSET-AMBIENT-RELATIVE-RECOVERY-FOR-IS-OPEN-IS-CLOSED-CLOSURE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
title: Specify RealSet ambient-relative recovery for is_open is_closed closure interior and
  boundary through TopologicalSpaces
status: needs-review
priority: critical
requirement: The deleted Topological Spaces triage recorded settled topological constructor
  placement and remaining smoke design work for RealSet ambient recovery and metric examples.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in the relevant
  MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- No implementation blocker was discovered during this spec pass.
- Run just smoke-file topological_spaces/smoketest.sage after topological-space work.
- Prove RealSet method recovery through the ambient-relative route, not by adding pure topological
  constructors.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- category-specs
- sets
- realset
- topology
- theme-sets-topology
updated: '2026-05-05'
---
# Specify RealSet ambient-relative recovery for is_open is_closed closure interior and boundary through TopologicalSpaces
## Summary

The deleted Topological Spaces triage recorded settled topological constructor placement
and remaining smoke design work for RealSet ambient recovery and metric examples.

## Source Provenance

- `category_specs/topological_spaces/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/topological_spaces/docs/TRIAGE.md`.
- Original migrated line: `Specify RealSet ambient-relative recovery for is_open is_closed closure interior and boundary through TopologicalSpaces from category_specs/topological_spaces/docs/TRIAGE.md`

## Context

- TopologicalSpaces().Constructors() remains empty by design; named set constructors live under Sets().Constructors() and refine into topological categories.
- Root topological methods use ambient-relative shape: X.is_open(U), X.is_closed(U), X.closure(U), X.interior(U), and X.boundary(U).
- RealSet variadic/manifold-producing paths are excluded; admitted real-line subset construction uses named Sets().Constructors() paths.
- Real and complex ball fields are not Sage metric spaces; topological recovery belongs through topological ring/field work.
- Canonical smoke examples are still needed for Connected, Compact, and Metric().Complete().

## Grounded Spec Contract

Canonical source anchors for this spec are already present:

- `category_specs/topological_spaces/docs/MAPPING.md`, `Root Topological Method Mapping`
  rows for:
  - `RealSet.is_open() -> X.is_open(U: Subset) -> bool`
  - `RealSet.is_closed() -> X.is_closed(U: Subset) -> bool`
  - `RealSet.closure() -> X.closure(U: Subset) -> Subset`
  - `RealSet.interior() -> X.interior(U: Subset) -> Subset`
  - `RealSet.boundary() -> X.boundary(U: Subset) -> Subset`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md` rows for:
  - `RealSet.is_open`
  - `RealSet.is_closed`
  - `RealSet.closure`
  - `RealSet.interior`
  - `RealSet.boundary`
  - `RealSet.ambient`
- `category_specs/sets/docs/MAPPING.md` and
  `category_specs/topological_spaces/docs/MAPPING.md` constructor-routing rows keeping
  named real-line subset constructors under `Sets().Constructors()`

Spec decision fixed by these sources:

- owner category: `TopologicalSpaces()` owns the public surfaces
  `is_open`, `is_closed`, `closure`, `interior`, and `boundary`
- subject shape: each method is ambient-relative, taking a subset `U` of an ambient
  topological space `X`; the public recovery route for a `RealSet` subset is
  `U.ambient().method(U)`
- constructor ownership stays in `Sets().Constructors()`; this card must not introduce
  `TopologicalSpaces().Constructors()` or a direct pure-topology `RealSet` constructor

Required hypotheses and return/codomain obligations:

- hypothesis: `U` is a subobject/subset of the ambient topological space `X`
- `X.is_open(U)` and `X.is_closed(U)` return `bool`
- `X.closure(U)`, `X.interior(U)`, and `X.boundary(U)` return subsets of the same
  ambient space `X`, not bare Python containers and not detached set objects
- any convenience method on subset objects must be explicitly documented as delegation,
  not as a second owner for the topological notion

Rejection or retirement condition:

- reject any spec edit from this card that reassigns ownership to `Sets()`, introduces
  a pure topological constructor namespace, or treats `RealSet` no-argument methods as
  definition authority independent of their ambient space

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] No implementation blocker was discovered during this spec pass.
- [ ] Run just smoke-file topological_spaces/smoketest.sage after topological-space work.
- [x] Prove RealSet method recovery through the ambient-relative route, not by adding pure topological constructors.

## Grounded Recovery Decision

Decision: RealSet topological methods recover through the ambient-relative
`TopologicalSpaces()` surface.

For a real subset `U`, the migration route is:

- `U.is_open()` becomes `U.ambient().is_open(U)`;
- `U.is_closed()` becomes `U.ambient().is_closed(U)`;
- `U.closure()` becomes `U.ambient().closure(U)`;
- `U.interior()` becomes `U.ambient().interior(U)`;
- `U.boundary()` becomes `U.ambient().boundary(U)`.

This pass recorded that route in `category_specs/topological_spaces/docs/MAPPING.md`
and documented the compatibility boundary in `category_specs/sets/subcategories/real_set.py`.
No `TopologicalSpaces().Constructors()` path or direct pure-topology `RealSet`
constructor was admitted. No `_RealSets` wrapper methods were added, because overriding
Sage's existing no-argument RealSet methods before the ambient methods have concrete
implementations would create a fragile compatibility layer rather than a mathematical
owner.

Validation note: global QC and smoke execution were skipped under the current
user-authorized skip-verification workflow for spec checkpoints.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Recorded the RealSet ambient-relative recovery route in topological-space
  mapping and the real-set spec docstring. Kept Sage no-argument RealSet methods as
  compatibility methods rather than adding overriding wrappers.

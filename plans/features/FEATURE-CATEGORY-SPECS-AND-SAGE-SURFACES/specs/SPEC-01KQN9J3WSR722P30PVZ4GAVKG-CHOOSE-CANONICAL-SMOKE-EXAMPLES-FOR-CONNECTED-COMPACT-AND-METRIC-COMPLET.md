---
id: SPEC-01KQN9J3WSR722P30PVZ4GAVKG-CHOOSE-CANONICAL-SMOKE-EXAMPLES-FOR-CONNECTED-COMPACT-AND-METRIC-COMPLET
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
title: Choose canonical smoke examples for Connected Compact and Metric Complete topological
  subcategories
status: needs-review
priority: critical
requirement: The deleted Topological Spaces triage recorded settled topological constructor
  placement and remaining smoke design work for RealSet ambient recovery and metric examples.
acceptanceCriteria:
- The mathematical owner, public surface, and migration consequence are recorded in the relevant
  MAPPING.md or category spec file.
- No new subtree-local TRIAGE or process document is created; follow-up work is represented
  as tracker items.
- Any implementation blocker discovered during spec work is split into an implementation-work
  item with source provenance.
- Run just smoke-file topological_spaces/smoketest.sage after topological-space work.
- Prove RealSet method recovery through the ambient-relative route, not by adding pure topological
  constructors.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- category-specs
- smoke
- topology
- theme-sets-topology
updated: '2026-05-05'
---
# Choose canonical smoke examples for Connected Compact and Metric Complete topological subcategories
## Summary

The deleted Topological Spaces triage recorded settled topological constructor placement
and remaining smoke design work for RealSet ambient recovery and metric examples.

## Source Provenance

- `category_specs/topological_spaces/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/topological_spaces/docs/TRIAGE.md`.
- Original migrated line: `Choose canonical smoke examples for Connected Compact and Metric Complete topological subcategories from category_specs/topological_spaces/docs/TRIAGE.md`

## Context

- TopologicalSpaces().Constructors() remains empty by design; named set constructors live under Sets().Constructors() and refine into topological categories.
- Root topological methods use ambient-relative shape: X.is_open(U), X.is_closed(U), X.closure(U), X.interior(U), and X.boundary(U).
- RealSet variadic/manifold-producing paths are excluded; admitted real-line subset construction uses named Sets().Constructors() paths.
- Real and complex ball fields are not Sage metric spaces; topological recovery belongs through topological ring/field work.
- Canonical smoke examples are still needed for Connected, Compact, and Metric().Complete().

## Source-Mining Contract

This leaf is source-mining and decision capture, not a free-form spec gate. The output
of this card must be a bounded example-selection record for the three smoke targets
already admitted by the mapping docs:

- `TopologicalSpaces().Connected()`
- `TopologicalSpaces().Compact()`
- `TopologicalSpaces().Metric().Complete()`

Required source anchors for the decision:

- `category_specs/topological_spaces/docs/MAPPING.md`:
  - `TopologicalSpaces.Connected() -> TopologicalSpaces().Connected()`
  - `TopologicalSpaces.Compact() -> TopologicalSpaces().Compact()`
  - `MetricSpaces.Complete() -> TopologicalSpaces().Metric().Complete()`
  - root ambient-relative recovery rows for `is_open`, `is_closed`, `closure`,
    `interior`, and `boundary`
  - constructor-routing rows keeping named examples under `Sets().Constructors()`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`:
  - `RealSet.__init__` category assignment
  - named constructors `RealSet.point`, `RealSet.closed`, `RealSet.real_line`
  - category surfaces for `TopologicalSpaces`, `MetricSpaces`, and
    `MetricSpaces.SubcategoryMethods.Complete()`
- `category_specs/sets/docs/MAPPING.md`:
  - RealSet constructor-routing rows admitting named real-line subset constructors
    through `Sets().Constructors()`

Decision this card must produce:

- exact canonical smoke objects, one per target where possible, or a minimal shared set
  of objects if one example witnesses multiple subcategories
- owner category for each asserted fact:
  - connectedness and compactness under `TopologicalSpaces()`
  - completeness under `TopologicalSpaces().Metric()`
  - constructor ownership under `Sets().Constructors()`
- the precise witness being exercised for each example:
  - object membership in the target subcategory
  - any ambient-relative topological operation needed to justify the example
  - whether the example is Sage-backed today or only mapped/provenanced for future spec

Hypotheses and return-object expectations to record:

- each example must be constructible from an admitted named constructor path or from an
  existing Sage-backed parent named in the inventory
- each topological subset example must have an explicit ambient space
- if a metric example is used, record the metric parent and the subcategory
  codomain being witnessed (`TopologicalSpaces().Metric().Complete()`)

Rejection or retirement condition:

- retire or rewrite this card if the only candidate examples depend on excluded
  variadic `RealSet(...)` shapes, manifold-producing paths, or ring/field topology that
  has not yet been grounded through the ring mapping

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Run just smoke-file topological_spaces/smoketest.sage after topological-space work.
- [x] Prove RealSet method recovery through the ambient-relative route, not by adding pure topological constructors.

## Grounded Example Decision

Decision: use two real-line subset constructors and the Sage real field as the canonical
smoke examples.

| Target | Canonical object | Owner and witness |
| --- | --- | --- |
| `TopologicalSpaces().Connected()` | `Sets().Constructors().OpenRealInterval(0, 1)` | Constructor owner is `Sets().Constructors()` through `RealSet.open(0, 1)`. The witness is object membership in `TopologicalSpaces().Connected()`. |
| `TopologicalSpaces().Compact()` | `Sets().Constructors().ClosedRealInterval(0, 1)` | Constructor owner is `Sets().Constructors()` through `RealSet.closed(0, 1)`. The witness is object membership in `TopologicalSpaces().Compact()`. |
| `TopologicalSpaces().Metric().Complete()` | `Sets().Constructors().RR()` / Sage `RR` | The Sage witness is `RR.category()` lying in complete metric spaces. Project implementation is routed through the existing topological ring/field recovery cards before this becomes a live smoke assertion. |

Source observations used in this pass:

- `RealSet.open(0, 1)` lies in Sage connected topological spaces and not compact spaces.
- `RealSet.closed(0, 1)` lies in Sage connected and compact topological spaces.
- `RR.category()` is a join containing complete metric spaces; `RR in Sets().Metric().Complete()` is true in local Sage.
- `RealSet` examples are not Sage metric spaces, so they are not complete-metric smoke
  candidates.

Migration consequence:

- Connected and compact smoke examples can be added once the topological smoke file is
  updated for named `Sets().Constructors()` real intervals.
- Complete metric smoke should be held to the topological ring/field recovery path,
  already tracked by
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC3XPWZWJK8QHVE3GGM-SPECIFY-TOPOLOGICAL-RING-AND-FIELD-RECOVERY-THROUGH-TOPOLOGICAL-SPACES-I.md`
  and
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION/PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY/tasks/TASK-01KQN9YGCHDRNXNEYEH2P134JD-IMPLEMENT-TOPOLOGICAL-RING-AND-FIELD-REFINEMENTS-FOR-TOPOLOGY-BEARING-RI.md`.
- Do not use real/complex interval or ball fields as complete-metric smoke examples in
  this subtree; they remain ring/field topology evidence.

Validation note: the local Sage observation command was used for source confirmation.
The topological smoke file itself was not run under the current user-authorized
skip-verification workflow.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Selected `OpenRealInterval(0, 1)`, `ClosedRealInterval(0, 1)`, and
  `RR`/`Sets().Constructors().RR()` as the connected, compact, and complete-metric
  smoke examples. Recorded the complete-metric implementation dependency on
  topological ring/field recovery.

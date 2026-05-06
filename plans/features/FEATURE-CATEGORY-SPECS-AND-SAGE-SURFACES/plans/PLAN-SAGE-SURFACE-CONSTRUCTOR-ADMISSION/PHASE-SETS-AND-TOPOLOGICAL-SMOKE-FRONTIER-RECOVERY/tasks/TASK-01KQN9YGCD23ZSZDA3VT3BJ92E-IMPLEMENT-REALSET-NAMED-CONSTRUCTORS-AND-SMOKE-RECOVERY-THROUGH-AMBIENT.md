---
id: TASK-01KQN9YGCD23ZSZDA3VT3BJ92E-IMPLEMENT-REALSET-NAMED-CONSTRUCTORS-AND-SMOKE-RECOVERY-THROUGH-AMBIENT
trackerStatus:
  type: task
parents:
- '[[PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY]]'
dependsOn: []
title: Implement RealSet named constructors and smoke recovery through ambient-relative
  topological methods
status: needs-review
priority: high
description: The deleted Topological Spaces triage recorded settled topological constructor
  placement and remaining smoke design work for RealSet ambient recovery and metric
  examples.
successCriteria:
- The implementation changes only the scoped category-spec surface and does not weaken
  smokes or mapping decisions to make failures disappear.
- Relevant smoke output is updated in this task body or a linked tracker item, with
  exact failing surfaces preserved when work remains.
- The change uses project category vocabulary rather than Sage fallback helper names
  or wrapper-only categories.
- Run just smoke-file topological_spaces/smoketest.sage after topological-space work.
- Prove RealSet method recovery through the ambient-relative route, not by adding
  pure topological constructors.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-SAGE-SURFACE-CONSTRUCTOR-ADMISSION
- PHASE-SETS-AND-TOPOLOGICAL-SMOKE-FRONTIER-RECOVERY
---
# Implement RealSet named constructors and smoke recovery through ambient-relative topological methods
## Summary

The deleted Topological Spaces triage recorded settled topological constructor placement
and remaining smoke design work for RealSet ambient recovery and metric examples.

## Source Provenance

- Canonical RealSet/topological recovery specs:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9YGC2N0VVPYVZBJVA4E68-SPECIFY-REALSET-AMBIENT-RELATIVE-RECOVERY-FOR-IS-OPEN-IS-CLOSED-CLOSURE.md`
  and
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-01KQN9J3WSR722P30PVZ4GAVKG-CHOOSE-CANONICAL-SMOKE-EXAMPLES-FOR-CONNECTED-COMPACT-AND-METRIC-COMPLET.md`.
- Constructor mapping:
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`,
  especially the `RealSetFromIntervals`, `RealSetInterval`, named interval/ray/point,
  and real-line rows.
- Source inventory:
  `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`.
- `category_specs/topological_spaces/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/topological_spaces/docs/TRIAGE.md`.
- Original migrated line: `Implement RealSet named constructors and smoke recovery through ambient-relative topological methods from category_specs/topological_spaces/docs/TRIAGE.md`

## Context

- TopologicalSpaces().Constructors() remains empty by design; named set constructors live under Sets().Constructors() and refine into topological categories.
- Root topological methods use ambient-relative shape: X.is_open(U), X.is_closed(U), X.closure(U), X.interior(U), and X.boundary(U).
- RealSet variadic/manifold-producing paths are excluded; admitted real-line subset construction uses named Sets().Constructors() paths.
- Real and complex ball fields are not Sage metric spaces; topological recovery belongs through topological ring/field work.
- Canonical smoke examples are still needed for Connected, Compact, and Metric().Complete().

## Acceptance Criteria

- [x] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [x] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [x] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [x] Run just smoke-file topological_spaces/smoketest.sage after topological-space work.
- [x] Prove RealSet method recovery through the ambient-relative route, not by adding pure topological constructors.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Commit `983a058` implemented the admitted RealSet constructor surface
  without restoring the rejected catch-all `Constructors().RealSet`: `RealSetFromIntervals`
  is the finite interval-union route, named interval/ray/point constructors refine
  through `Sets().Constructors()`, and RealSet compactness/category refinement is based
  on the closed-bounded real-line subset predicate. The implementation also leaves
  `TopologicalSpaces().Constructors()` empty and keeps ambient-relative topological
  ownership in the spec/mapping.
- 2026-05-06 scope clarification: commit `983a058` also contained broader Sets smoke
  integration work for iterator-backed sets, recursive sets, families, image sets,
  totally ordered finite sets, Cartesian products, subobjects, and audit-card routing.
  Those edits are shared integration context and are not claimed as this RealSet
  leaf's scoped implementation evidence. This card's scoped evidence is limited to
  the RealSet constructor/refinement rows, the topological constructor non-admission,
  and the RealSet/topological smoke assertions named above.
- 2026-05-05: Validation evidence from `983a058`: `just --justfile
  category_specs/justfile smoke-file topological_spaces/smoketest.sage` passed;
  `just --justfile category_specs/justfile smoke-file sets/smoketest.sage` passed
  while still emitting Sage's inherited `Sets.Topological` warning on the original
  Sage `RealSet` category join; `just --justfile category_specs/justfile
  check-abstract-redefinitions` passed; `git diff --check` passed. This card is moved
  to `in-review`; human acceptance is still required for closure.

## Review Log

### Review 2026-05-06 (Kant)

**Gates passed:** Gate 1
**Gates failed:** Gate 2 Acceptance Criteria
**Outcome:** revision-required, then reworked within this card's scope

#### Gate 2 Finding: Scope Evidence

- The card claimed the implementation changed only the scoped category-spec surface,
  but cited commit `983a058`, which also included broad Sets smoke-frontier work across
  iterator-backed sets, recursively enumerated sets, families, image sets, totally
  ordered finite sets, Cartesian products, subobjects, audit tracker files, and another
  implementation card.
- Validation evidence existed, but did not cure the scope mismatch.

#### Rework

- Added canonical RealSet/topological source provenance.
- Clarified that the broad `983a058` commit is shared integration context and is not
  claimed as this card's scoped implementation evidence.
- Limited this card's evidence to the admitted RealSet constructor/refinement rows,
  topological constructor non-admission, and RealSet/topological smoke assertions.

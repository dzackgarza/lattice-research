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
- 2026-05-05: Validation evidence from `983a058`: `just --justfile
  category_specs/justfile smoke-file topological_spaces/smoketest.sage` passed;
  `just --justfile category_specs/justfile smoke-file sets/smoketest.sage` passed
  while still emitting Sage's inherited `Sets.Topological` warning on the original
  Sage `RealSet` category join; `just --justfile category_specs/justfile
  check-abstract-redefinitions` passed; `git diff --check` passed. This card is moved
  to `in-review`; human acceptance is still required for closure.

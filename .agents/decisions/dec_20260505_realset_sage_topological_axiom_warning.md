---
trackerStatus:
  type: decision
title: Decide how to handle Sage RealSet inherited Sets.Topological axiom warning
status: to-do
tags:
- category-specs
- decision
- sets
- realset
- topology
- smoke
- needs-decision
- theme-decisions
planId: SPR-SETS-TOPO-01KQN9
---

# Decide how to handle Sage RealSet inherited Sets.Topological axiom warning

## Summary

`just --justfile category_specs/justfile smoke-file sets/smoketest.sage` now passes, but
the RealSet rows still emit Sage's warning:
`Expecting Sets.Topological to be a subclass of CategoryWithAxiom ... got
sage.categories.topological_spaces.TopologicalSpaces`.

The functional smoke frontier is clear. The remaining decision is how the project
should treat the original Sage `RealSet` category provenance when refining RealSet
objects into the local topological hierarchy.

## Source Provenance

- Blocking card:
  `.agents/tasks/implementation/impl_01KQN9J3X04R2PWJADC8B4EF9A-fix-sets-root-containment-refined-constructor-richcmp-primes-iteration-r.md`
- Implementation commit: `983a058`
- Tracker synchronization commit: `f606652`
- Mapping anchors:
  - `category_specs/sets/docs/MAPPING.md`
  - `category_specs/topological_spaces/docs/MAPPING.md`
  - `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`

## Context

The warning is not a failed smoke assertion. It is emitted by Sage category machinery
while RealSet objects carry their original Sage `TopologicalSpaces()` category join.
Local attempts to remove direct Sage topological supercategory references and override
project topological construction-category joins reduced warning exposure in
`topological_spaces/smoketest.sage`, but the Sets smoke still reaches the warning
through the original Sage `RealSet` category provenance.

## Decision Grounding Required

This decision cannot be settled by hiding the warning or by weakening the smoke. Before
moving to `decided`, record:

- exact Sage source path and call stack for the warning;
- whether project refinement may replace or strip an object's original Sage category
  provenance without losing necessary Sage parent methods;
- whether local construction-category joins should special-case Sage's non-axiom
  `TopologicalSpaces()` category;
- whether the warning should instead be accepted and documented as inherited Sage
  behavior until owned RealSet carriers exist.

Negative findings must use the five-field search format.

## Options

- Replace or strip the original Sage `RealSet` category during refinement.
- Patch local construction-category joins to avoid applying the `Topological` axiom to
  Sage `Sets()` supercategories reached through original RealSet provenance.
- Accept and document the warning as inherited Sage behavior while keeping functional
  smoke passing until the owned categorical implementation phase.

## Acceptance Criteria

- [ ] The decision lists the chosen option, rationale, and affected implementation or
  documentation cards.
- [ ] The decision states whether the root Sets smoke card can move from `blocked` to
  `in-review` with the warning documented, or whether a concrete implementation card
  must clear the warning.
- [ ] Any implementation consequence preserves the admitted RealSet constructor surface
  and does not reintroduce catch-all `Constructors().RealSet`.
- [ ] Any accepted warning is documented in the owning card or mapping docs rather than
  buried in chat.

## Dependencies And Boundaries

- Do not use this decision to add a pure `TopologicalSpaces().Constructors()` namespace.
- Do not weaken or remove RealSet smoke rows.
- Do not treat this as a blocker for unrelated approved phase-01 spec, research,
  implementation, or audit leaves.

## Work Log

- 2026-05-05: Created after commit `983a058` cleared functional Sets smoke failures but
  left Sage's inherited `Sets.Topological` warning on the RealSet path.

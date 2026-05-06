---
id: TASK-LAT-PHASE0-MODULE-ENRICHMENT
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES]]'
dependsOn: []
title: Implement enriched finitely generated module surface
status: unstarted
priority: critical
description: Leaf implementation card derived from the old phase plan. This card is
  executable only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.
successCriteria:
- Read the cited source section before implementation.
- Keep changes inside the named target boundary unless a new card or decision expands
  scope.
- Preserve the mathematical semantics from the source plan and category-spec style
  rules.
- Record validation commands and results before handoff.
- Do not mark this card done without human approval.
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES
---
# Implement enriched finitely generated module surface

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.

## Source Provenance

- `plans/PHASE_0_SAGE_PATCHES.md`
- Source section: module_enrichment.py -- ZZ^n as enriched FGP module
- Parent plan: `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

### Canonical sources
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md`
- `theory/backends/software-capability-map.md`

### Public owner and target category
- Owner: `src/sage_patches/module_enrichment.py`.
- Public object owners:
  - free modules: `Modules(R).Free().FiniteRank()`
  - FGP modules: `Modules(R).FinitelyPresented()`
- Enriched construction entry remains `R^n` and module base-change operations in
  existing Sage categories.

### Definitions and hypotheses
- For supported target PID rings, `R^n` is a mathematically free module parent in
  `Modules(R)` (not an ambient vector span).
- `+` on enriched module parents denotes direct-sum in the designed API, not span in
  an ambient module.
- `M * N` (parent-level) denotes tensor product; module element `*` is not addressed in
  this leaf.
- `M / (n*M)` is an FGP quotient module object; equality may be tested through
  isomorphic FGP presentation equality (or native equality once verified).

### Return objects / codomains
- `R^n` returns an enriched module parent in `Modules(R)` with `n >= 0`.
- `M ⊕ N` via `M + N` returns an enriched module parent in `Modules(R)`.
- `M.tensor(S)` and `M * S` return enriched modules over the tensor-rank target:
  - mixed tensor `ZZ^n ⊗ (ZZ/p)` ⇒ `Mod(ZZ/p)` object.
- `M.base_change(S)` returns base-changed enriched module with the same structural
  categories (`Free`/`FGP` where valid).
- `M / H` for submodule/image-like `H` returns FGP quotient parent in `Modules` of base ring.

### Concrete implementation work
- Patch enriched module behavior on native parents used for free and FGP modules:
  - `is_free`, `is_torsionfree`, `is_torsion` predicates,
  - `dual()` as `Hom(ZZ)`-based construction,
  - parent-level tensor helper via `__mul__` and `tensor`,
  - `base_change` routed through tensor with ring parent,
  - `__add__` as direct sum and `__pow__` as repeated sum for direct-sum expansion,
  - `__truediv__` producing FGP quotient parent.
- Preserve compatibility by confining new behavior to refined parents and using
  `super()` for all upstream behavior before category refinement.
- Ensure ring-power path (`__pow__` for ring object and constructors) is stable under
  both class-call and power-call entry points.

### Acceptance checks
- `[ ]` `M = ZZ^3`; `M in Modules(ZZ)` and `M.rank() == 3`.
- `[ ]` `M == ZZ + ZZ + ZZ` and `M * M == M.tensor(M)`.
- `[ ]` `M.dual() == M.Hom(ZZ)` and `M.base_change(Z2) == M.tensor(Z2)`.
- `[ ]` `M / (2*M) == M.tensor(ZZ/2)` in whichever equality notion is chosen
  for FGP-presentations.
- `[ ]` `M.is_free()`, `M.is_torsionfree()`, and `not M.is_torsion()` are stable across
  ring-level and direct-sum constructions.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/sage_patches/module_enrichment.py`.

## Acceptance Criteria

- [ ] Read the cited source section before implementation.
- [ ] Keep changes inside the named target boundary unless a new card or decision expands scope.
- [ ] Preserve the mathematical semantics from the source plan and category-spec style rules.
- [ ] Record validation commands and results before handoff.
- [ ] Do not mark this card done without human approval.

## Dependencies And Boundaries

Do not execute before the parent phase plan is approved and prerequisite phase cards are resolved. If the source section reveals missing vocabulary or method ownership, stop and file a decision or spec card instead of patching around it.

## Work Log

- Created by corpus-level `plans/` migration on 2026-05-03.

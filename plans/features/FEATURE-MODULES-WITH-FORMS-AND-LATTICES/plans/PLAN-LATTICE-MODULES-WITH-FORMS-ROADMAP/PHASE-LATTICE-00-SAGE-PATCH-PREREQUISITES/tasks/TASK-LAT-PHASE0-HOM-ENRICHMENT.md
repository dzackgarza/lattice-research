---
id: TASK-LAT-PHASE0-HOM-ENRICHMENT
trackerStatus:
  type: task
parents:
- '[[PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES]]'
dependsOn: []
title: Implement Hom spaces as enriched modules and morphism constructors
status: unstarted
priority: critical
description: Leaf implementation card derived from the old phase plan. This card is executable
  only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.
successCriteria:
- Read the cited source section before implementation.
- Keep changes inside the named target boundary unless a new card or decision expands scope.
- Preserve the mathematical semantics from the source plan and category-spec style rules.
- Record validation commands and results before handoff.
- Do not mark this card done without human approval.
complexity: 65
tags:
- FEATURE-MODULES-WITH-FORMS-AND-LATTICES
- PLAN-LATTICE-MODULES-WITH-FORMS-ROADMAP
- PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES
- category-specs
- lattices
- phase-plan
- sage
- modules
- theme-modules-tensors
created: '2026-05-03'
---
# Implement Hom spaces as enriched modules and morphism constructors

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES` is approved.

## Source Provenance

- `plans/PHASE_0_SAGE_PATCHES.md`
- Source section: hom_enrichment.py -- Hom spaces as modules, morphism construction
- Parent plan: `PHASE-LATTICE-00-SAGE-PATCH-PREREQUISITES`
- Program plan: `PLAN-CATEGORY-SPEC-PROGRAM`

## Grounded Implementation Contract

### Canonical sources
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
- `category_specs/homsets/docs/MAPPING.md`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/forms/docs/MAPPING.md`
- `theory/backends/software-capability-map.md`

### Public owner and target category
- Owner: `src/sage_patches/hom_enrichment.py`.
- Public hom-space owner: `Modules(R).HomCategory()` and derived homset objects
  (`Hom`, `End`, `Aut` surfaces).
- Morphism owner: module morphism classes backing Sage hom objects.

### Definitions and hypotheses
- `Hom(M, N)` is the set of `R`-linear maps with fixed domain/range and composition.
- A morphism is in the hom object iff it preserves module structure; no ad hoc
  element-wise side channels.
- `is_primitive()` on hom is defined as torsion-free cokernel over PID bases.
- `cokernel()` of a morphism returns a module object in `Modules(codomain.base_ring())`
  with canonical projection map.

### Return objects / codomains
- `H.from_dict`, `H.from_images`, `H.from_matrix` return homset elements in
  `Hom(M, N)`.
- `f.to_matrix()` / `f.to_dict()` round-trip element data in the domain generator basis.
- `f.base_change(S)` returns morphism in `Hom(M ⊗ S, N ⊗ S)`.
- `M.End()` is alias for `M.Hom(M)`.
- `M.Aut()` is a condition-set subgroup of endomorphisms with inverse present; codomain
  remains group object (`Groups`).
- `cokernel().projection()` returns surjective quotient map into the quotient object.

### Concrete implementation work
- On homset objects (`FreeModuleHomspace`, `FGP_Homset_class`), implement:
  - `from_dict`, `from_images`, `from_matrix`, `element_from_function`,
  - `natural_map`, `identity()`.
- On morphism objects (`FreeModuleMorphism`, `FGP_Morphism`), implement:
  - `to_matrix`, `to_dict`, `is_primitive`,
  - `base_change(S)`,
  - guaranteed `cokernel()` returning refined FGP module and `projection()` accessor.
- Add `End` / `Aut` constructors consistent with hom-category ownership:
  - `M.End() -> Hom(M, M)`,
  - `M.Aut()` built from `End` as invertible core, not a direct matrix group wrapper.

### Acceptance checks
- `[ ]` `M = ZZ^2`, `H = M.Hom(ZZ^2)`; `H.from_matrix(...)` constructs typed homs in `H`.
- `[ ]` `f.to_matrix()` and `f.to_dict()` are inverse round-trips under fixed generators.
- `[ ]` `f.is_injective()` / `f.is_surjective()` agree with `kernel()==zero` and
  `cokernel()==Modules(ZZ).zero()`.
- `[ ]` `g = H.from_images([2*h1, 3*h2])` returns a valid hom and
  `g.cokernel() == ZZ/2 + ZZ/3` in the intended refined codomain.
- `[ ]` `M.End() == M.Hom(M)` and `M.End().identity() in M.Aut()`.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/sage_patches/hom_enrichment.py`.

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

---
trackerStatus:
  type: task
title: Implement ModuleBaseRings category refinement and installation
status: to-do
priority: critical
created: '2026-05-03'
complexity: 65
progress: 0
planId: PLN-LAT-010
tags:
- category-specs
- implementation
- lattices
- phase-plan
- sage
- modules
- theme-modules-tensors
---

# Implement ModuleBaseRings category refinement and installation

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-010` is approved.

## Source Provenance

- `plans/PHASE_0_SAGE_PATCHES.md`
- Source section: ring_base_category.py -- ModuleBaseRings category and installation
- Parent plan: `PLN-LAT-010`
- Program plan: `PLN-CAT-000`

## Grounded Implementation Contract

### Canonical sources
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- `.agents/skills/lattice-redesign/references/lattice-redesign-corrections-spec.md`
- `category_specs/modules/docs/MAPPING.md`
- `theory/backends/software-capability-map.md`
- `theory/foundations/bilinear-forms-duals-morphisms.md` (for dual-notation and morphism discipline)
- `category_specs/rings.py` (contracted category surface)

### Public owner and target category
- Owner: `ModuleBaseRings` in `src/sage_patches/ring_base_category.py`.
- Integration boundary: ring parents are installed with
  `ring._refine_category_(ModuleBaseRings())` and dispatch through
  `ModuleBaseRings.ParentMethods`; no new ring classes.
- Downstream owners are `Modules(R)` and `Modules(R).WithForms()` for form-bearing
  modules built from those bases.

### Definitions and hypotheses
- `R` is a base ring in the enriched PID scope:
  `ZZ`, `Zp(p)`, `QQ`, `RR`, `CC`, `QQbar`, and `GF(p^n)`.
- `Modules(R)` methods are available on all parents reached by these overrides.
- `r * R` / `R * r` means principal ideal object with submodule semantics
  (`{r*x : x in R}`), not multiplication output.
- `R / I` means the corresponding finitely presented `R`-module quotient parent.
- `R / n` and `R.quotient(n*R)` are a single construction path through
  `quotient()`.
- Returned localizations/completions/fraction fields in scope stay in `ModuleBaseRings`
  so module expressions continue to route through redesigned semantics.

### Return objects / codomains
- `R / (n*R)` / `R / (n)` ⇒ module parent intended to satisfy `parent in Modules(R)`.
- `R^n` via `__pow__` ⇒ enriched free module parent in `Modules(R)`.
- `R.complete(...)`, `R.localize(...)`, `R.fraction_field()` outputs remain
  PID-family module-aware ring parents (when in scope).
- `ideal(...)` and `R * I` / `I * R` outputs remain ideal-submodule parents with
  module category membership.

### Concrete implementation work
- Implement `ModuleBaseRings = Rings().PrincipalIdealDomains().Commutative().Subcategory`
  and required `ParentMethods`.
- In `ParentMethods`, override:
  - `__pow__` to produce enriched `R^n`,
  - `ideal`, `__mul__`, `__rmul__` for ideal-submodule construction,
  - `quotient` and `__truediv__` dispatch to quotient construction,
  - `completion` / `localization` / `fraction_field` to refine returned parents.
- Make `_refine_category_` application idempotent in `install()`.
- Keep module-membership checks consistent with `Modules(R)` by refining ring
  quotient and ideal outputs after native construction.
- Wire install order via `_install.py` after module import path initialization.

### Acceptance checks
- `[ ]` `ZZ in Modules(ZZ)`, `ZZ/2 in Modules(ZZ)`, `ZZ/(2*ZZ) == ZZ/2`,
  `ZZ/4` is not field, `ZZ/2` is field.
- `[ ]` `QQ in Modules(QQ)` and `QQ / ZZ` routes through patched quotient path.
- `[ ]` `2 * ZZ`, `ZZ * 2`, and `ZZ.ideal(2)` land in module-compatible categories.
- `[ ]` `Zp(5)` and `GF(5)` produced by install still satisfy `Modules` membership
  expectations.
- `[ ]` `ZZ.complete(5)` and `ZZ.localize(5)` return refined ring parents that are
  accepted by the same `Modules` membership checks.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/sage_patches/ring_base_category.py`.

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

---
trackerStatus:
  type: task
title: Implement FormCodomain and quotient-valued codomain predicates
status: to-do
priority: critical
created: '2026-05-03'
complexity: 65
progress: 0
planId: PLN-LAT-020
tags:
- category-specs
- implementation
- lattices
- phase-plan
- theme-modules-tensors
---

# Implement FormCodomain and quotient-valued codomain predicates

## Summary

Leaf implementation card derived from the old phase plan. This card is executable only after `PLN-LAT-020` is approved.

## Source Provenance

- `plans/PHASE_2_CORE_OBJECTS.md`
- Source section: Step 2.2: FormCodomain
- Parent plan: `PLN-LAT-020`
- Program plan: `PLN-CAT-000`

## Grounded Implementation Contract

- Canonical codomain object: `FormCodomain` is a typed descriptor carrying
  `(base_ring: R, codomain: S)` where `S` is a genuine `R`-module parent accepting all
  form values.
- Required value targets:
  - `FormCodomain.integral(R) -> S = R` (`Bilinear`/`Quadratic` integral branch),
  - `FormCodomain.rational(R) -> S = Frac(R)`,
  - `FormCodomain.torsion_bilinear(R) -> S = Frac(R) / R`,
  - `FormCodomain.torsion_quadratic(R) -> S = Frac(R) / (2R)`.
- `R = ZZ` specializations are `QQ`, `QQ/ZZ`, and `QQ/2ZZ` in the working codomain stack.
- Method-level contract in `core/codomains.py`:
  - `integral`, `rational`, `torsion_bilinear`, `torsion_quadratic` constructors.
  - `coerce(value)`/call-style coercion into `S` for form evaluation.
  - `is_torsion_valued` predicate and `contains(value)` checks against the codomain parent.
- Ownership:
  - `Form` objects own no matrix/ambient conventions; codomain determines branch predicates.
  - No separate “fake codomain descriptor” is permitted beyond a validated parent holder.
- Acceptance checks:
  - `FormCodomain.integral(ZZ).codomain() is ZZ`.
  - `FormCodomain.rational(ZZ).codomain() is QQ`.
  - `FormCodomain.torsion_bilinear(ZZ).codomain() == QQ / ZZ`.
  - `FormCodomain.torsion_quadratic(ZZ).codomain() == QQ / (2*ZZ)`.

## Context

This card exists because the old phase document mixed high-level planning with executable substeps. The migration splits that material into a phase plan plus leaf cards so an implementation agent can work from one bounded contract.

Target boundary: `src/lattices/core/codomains.py`.

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

---
id: FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
- '[[FEATURE-COBLE-MODULI-COMPARISON]]'
plans: []
title: Coble cusp orbit classification
status: blocked
priority: high
description: Compute the isotropic vector and isotropic plane orbit data that control
  Baily-Borel cusp strata for the Coble period quotient.
---
# Feature: Coble cusp orbit classification

## Summary

Compute the isotropic vector, lifting, and isotropic plane orbit data for the Coble
period lattice. This feature owns the cusp-classification obligations that were
previously embedded as unverified status notes in theory background.

## Relationship to Geometry

The lattice T_Co is known abstractly from the literature as `I_{1,10}(2)` or
`⟨2⟩ ⊕ ⟨-2⟩^10` — a 2-elementary hyperbolic lattice with invariants
`(r, a, δ) = (11, 11, 1)` (or `(11, 11, 0)` depending on the even/odd
refinement). Its discriminant group `A_{T_Co} ≅ (ℤ/2ℤ)^11` and discriminant form
are determined by these invariants and can be studied as pure lattice theory
without the geometric Coble surface construction.

This means:
- The isotropic orbit enumeration in `A_{T_Co}` (Tasks 2.1-2.2) can proceed
  using the abstract isometry type of T_Co as input, without waiting for the
  full geometric pipeline to produce a concrete Gram matrix.
- The geometric construction (Coble surface → K3 cover → pullback lattice →
  T_Co embedding) is a logical prerequisite for establishing the Coble narrative
  from first principles and proving that the computed period quotient is the
  correct moduli space. It does not block the orbit classification, which
  depends only on having the correct spec vocabulary — the abstract lattice
  `I_{1,10}(2)` — and the backend capabilities to compute discriminant-form
  orbits.
- The orbit results are then available to verify against the geometric
  construction when the latter is completed.

## Source Provenance

- `theory/foundations/coble-task-background.md`, sections `Task 2.1`, `Task 2.2`, and
  `Task 3.2`.
- Nikulin (1979), Sterk (1991), AEGS (2023), and Dawes (2022), through
  `theory/references/index.md`.

## Scope

- Use the computed $T_{\mathrm{Co}}$ lattice and discriminant form from the Coble lattice
  pipeline.
- Enumerate isotropic classes in $A_{T_{\mathrm{Co}}}$ and compute their
  $O(q_T)$-orbits.
- Check Nikulin or backend hypotheses before lifting discriminant-form orbits to
  primitive isotropic vector orbits in $T_{\mathrm{Co}}$.
- Compute primitive isotropic plane orbits and the lattice $J^\perp/J$ for
  representatives.
- Verify the predicted uniqueness statements only after the orbit computations are
  exhaustive.

## Non-Goals

- Do not present a bounded search as orbit classification.
- Do not infer uniqueness from a handful of representatives with the expected quotient
  lattice.
- Do not assume notation such as $T_{\mathrm{Co}}$ already supplies the discriminant
  form, stable group, or arithmetic group action.

## Acceptance Criteria

- [ ] The input lattice and discriminant form are sourced from the constructed Coble/K3
  lattice pipeline.
- [ ] Isotropic discriminant classes are enumerated with exact quadratic-form checks.
- [ ] $O(q_T)$-orbits are computed with an exhaustive group action.
- [ ] Primitive isotropic vector orbit lifting states and verifies the theorem or backend
  hypotheses used.
- [ ] Primitive isotropic plane orbits are computed exhaustively.
- [ ] For each claimed plane orbit, $J^\perp/J$ is constructed and its isometry type is
  verified.

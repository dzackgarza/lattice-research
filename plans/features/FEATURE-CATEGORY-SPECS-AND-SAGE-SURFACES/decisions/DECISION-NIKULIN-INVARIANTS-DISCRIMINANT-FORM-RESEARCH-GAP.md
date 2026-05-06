---
id: DECISION-NIKULIN-INVARIANTS-DISCRIMINANT-FORM-RESEARCH-GAP
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Nikulin invariants discriminant-form research gap
status: unstarted
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decision: Nikulin invariants discriminant-form research gap

## Problem

The current lattice spec surface for `nikulin_invariants()` computes the triple
`(r, a, delta)` — rank, 2-rank of the discriminant group, and coparity. This is
sufficient for the Nikulin classification of 2-elementary lattices.

However, the downstream Coble orbit analysis (GOAL.md Tasks 2.1-2.2, isotropic
vector orbit enumeration under the stable orthogonal group) requires:

- The actual discriminant **form** `q_T: A_T -> Q/2Z`, not just its 2-elementary type.
- The orbit structure of isotropic vectors in `A_T` under `O(q_T)`.
- The lifting of those orbits back to vector orbits in `T_Co`.

The `nikulin_invariants()` surface as specified is too narrow for these needs.

## Required Research

Before any implementation card for the orbit analysis can be written, the following
research must be completed:

1. **Discriminant-form method surface**: What is the precise API for the discriminant
   form on a discriminant group object? This includes:
   - The quadratic form `q: A -> Q/2Z`
   - The bilinear form `b: A x A -> Q/Z`
   - The orthogonal group `O(A, q)` and its action on A
   - The stable orthogonal group kernel `O(L) -> O(A_L, q_L)`

2. **Isotropic orbit enumeration in A_T**: Given a discriminant group with form,
   what method surfaces are needed to compute the orbits of isotropic vectors
   under `O(q_T)`? This may involve:
   - Finite group action on a finite set
   - Burnside / Cauchy-Frobenius orbit counting
   - Explicit orbit representatives
   - GAP/Sage finite-group backend routing

3. **Lifting orbits**: What method surfaces connect orbits in `A_T` to vector
   orbits in `T_Co` under the stable orthogonal group `O^*(T_Co)`? This involves:
   - Eichler criterion / spinor norm conditions
   - The connecting homomorphism `O(L) -> O(A_L)`
   - Surjectivity criteria (Nikulin 1.5.2, condition on the spinor norm)

## Action

- Create new spec cards under `FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES` for the
  discriminant-form method surface (item 1 above), with source evidence from Sage's
  `TorsionQuadraticModule` and `QuadraticForm` classes, and the Oscar/Hecke
  discriminant-form API.
- Create a research card for the isotropic orbit enumeration in finite discriminant
  groups (item 2), surveying GAP, Sage, and Oscar capabilities.
- Create a research card for the lifting theorem application (item 3), verifying
  Nikulin 1.5.2 and the Eichler criterion against the specific lattice T_Co.
- Do not proceed to implementation of orbit analysis until these spec and research
  cards are resolved.

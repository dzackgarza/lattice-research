---
id: DECISION-TCO-DEFINITION-AND-SIGNATURE
trackerStatus:
  type: decision
parents:
- '[[FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION]]'
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
title: Clarify definition and signature of T_Co for Tasks 2-5
status: in-progress
tags:
- FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION
---
# Decision: Clarify definition of T_Co

## Problem

'T_Co' appears in the plans with at least two candidate definitions that yield
different signatures and therefore different mathematical frameworks:

## Requirement

Resolve which lattice is meant, document the relationship with T_En and S_En, and ensure
all downstream tasks (orbit classification, arithmetic group, Coxeter diagrams, folding
involution) agree on the same object.

### Candidate A: Complement of f*Pic(S) in Λ_K3

From GOAL.md: the K3 cover pullback f*Pic(S) ⊂ H²(X, ℤ) has Gram
diag(2, -2, ..., -2), rank 11, signature (1, 10). Its orthogonal complement in
Λ_K3 (signature (3, 19)) has signature (2, 9). This is Type IV (period domain
D(T_Co) exists). The orbit classification would use the Type IV Baily-Borel
framework with both isotropic lines (0-cusps) and isotropic planes (1-cusps).

### Candidate B: h_Co^⊥ in T_En

From the arithmetic group definition: Γ_Co is a subgroup of O(T_En) stabilizing
h_Co. If T_Co = h_Co^⊥ in T_En, where T_En has signature (2, 10) = U ⊕ E₁₀(2)
and h_Co satisfies h_Co² = 2, then T_Co has signature (1, 10). This is
hyperbolic, not Type IV, so D(T_Co) is not a Type IV period domain. The orbit
analysis here would concern hyperbolic-lattice isotropic vectors, not Baily-Borel
boundary components.

### Relationship with period domain

T_En (signature (2, 10)) is the period domain lattice. Its Type IV domain
D(T_En)/Γ is the Enriques moduli space. T_Co enters the picture through the
Coble polarization and the arithmetic group Γ_Co, but it is not itself the
period domain lattice.

## Resolution needed

- Which definition of T_Co do Tasks 2.1-2.3 (isotropic orbit classification) use? If
  Candidate A, the orbit analysis must handle a signature-(2, 9) lattice. If Candidate
  B, the orbit analysis is about hyperbolic isotropic vectors and is NOT about
  Baily-Borel cusps.

- How does T_Co embed into T_En? What is the relationship between the complement of
  f*Pic(S) in Λ_K3 and h_Co^⊥ in T_En? Are they isometric?

- The answer should be recorded in a theory note under `theory/foundations/` so
  downstream agents can rely on it.

## Acceptance Criteria

- A single definition of T_Co is chosen and documented.
- All references to T_Co in plans, specs, and task cards are reconciled to this
  definition or explicitly noted if they diverge.
- The signature and discriminant group invariants are recorded.
- The relationship with T_En (signature (2, 10)) and the period domain is stated.

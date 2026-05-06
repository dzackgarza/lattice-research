---
id: DECISION-TCO-DEFINITION-AND-SIGNATURE
trackerStatus:
  type: decision
parents:
- '[[FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION]]'
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
title: Decide Coble algebraic and transcendental lattice notation
status: decided
chosen: T_Co is the K3 orthogonal complement of S_Co
tags:
- FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION
---
# Decision: Coble algebraic and transcendental lattice notation

## Decision

Use three distinct lattice names, and do not conflate them:

| Symbol | Definition | Signature | Rank |
|--------|-----------|-----------|------|
| `Pic(S)` | Picard lattice of the blowup Coble surface before K3 pullback | (1, 10) | 11 |
| `S_Co` | Algebraic K3 pullback lattice `f^*Pic(S)` inside `Lambda_K3`; primary notation `I_{1,10}(2)` | (1, 10) | 11 |
| `T_Co` | Orthogonal complement `S_Co^perp` in `Lambda_K3`; Dolgachev-Kondo call this `N` | (2, 9) | 11 |
| `T_En` | Enriques period lattice `U + E_10(2)` in the Dolgachev-Kondo comparison | (2, 10) | 12 |

Concretely:

- `Pic(S)` is the unimodular odd lattice `I_{1,10}` with the geometric line and
  exceptional divisor basis.
- The K3 cover doubles intersections, so the algebraic pullback lattice is
  `S_Co = f^*Pic(S) = I_{1,10}(2)`. The diagonal spelling
  `<2> + <-2>^10` is a presentation of that family member, not the primary name.
- The period/transcendental lattice used for Coble cusp orbit work is
  `T_Co = S_Co^perp` in `Lambda_K3`. It has discriminant form `q_T = -q_S` and
  is the type-IV lattice `N = <2> + E_10(2)`. With the convention
  `E_10 = U + E_8(-1)`, this is `<2> + U(2) + E_8(-2)`.
- `T_Co` is not `I_{1,10}(2)`. That notation belongs to `S_Co`.

## Task Routing

- Tasks 2.1--2.2 use the discriminant form of `T_Co`.
- Task 3.2 uses primitive isotropic planes in `T_Co`.
- Task 4.1 uses the Coxeter/root data of the algebraic lattice `S_Co`.
- Arithmetic-group cards use `h_Co` as an algebraic polarization class in `S_Co`.
  When relating the Coble quotient to the Enriques period lattice, they must introduce
  the corresponding typed Heegner vector or embedding data explicitly.
  Dolgachev-Kondo identify `T_Co` with the orthogonal complement of a `(-2)` vector in
  `T_En = U + E_10(2)`.

## Sources

- `GOAL.md`: Picard lattice, K3 pullback lattice, orthogonal-complement lattice, and
  Task 2 input contract.
- `theory/references/literature/dolgachev_kondo_2013.md`: the K3 pullback lattice
  `M`, written here as `I_{1,10}(2)`, its complement `N`, and the identification
  `N=<2>+E_10(2)`.
- `theory/foundations/coble-task-background.md`: task-local operational summary,
  updated to use this notation.

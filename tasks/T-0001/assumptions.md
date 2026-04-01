# Mathematical Assumptions for Task T-0001

## Objects

- $S_{\mathrm{Co}}$: Coble lattice, rank 11
- $T_{\mathrm{Co}}$: Transcendental lattice, rank 11
- $\Lambda_{\mathrm{K3}}$: Standard K3 lattice $(22, 0, 0)_1$, unimodular

## Definitions

- $Q_{S_{\mathrm{Co}}} = \text{diag}(2, -2, \dots, -2)$ (diagonal Gram matrix)
- Basis: $\{e_0, e_1, \dots, e_{10}\}$ where $e_0 = \pi^* L$ (pullback of line bundle),
  $e_i = E_i$ (exceptional divisors)
- $T_{\mathrm{Co}} = S_{\mathrm{Co}}^{\perp \Lambda_{\mathrm{K3}}}$: orthogonal
  complement in K3 lattice

## Conventions

- All computations exact (rational/integer arithmetic)
- Nikulin's $(r, a, \delta)$ invariants follow standard definitions:
  - $r$ = rank
  - $a$ = length of discriminant group ($\ell(A_T)$)
  - $\delta$ = parity (0 or 1)
- Discriminant group $A_T = T^*/T$ where $T^*$ is dual lattice
- Quadratic form $q_T: A_T \to \mathbb{Q}/2\mathbb{Z}$

## References

- Nikulin, V. V. "Integral symmetric bilinear forms and their applications."
  Math. USSR-Izv. 14 (1980)
- Dolgachev, I., Keum, J. "Coble surfaces and related loci."
  (background)
- Task 1.2 in GOAL.md provides target values

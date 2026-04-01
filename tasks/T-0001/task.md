# Task T-0001: Foundation Verification (GOAL.md Task 1.2)

## Origin

GOAL.md Task 1.2: "Compute the Gram matrices for $S_{Co}$ and $T_{Co}$, and verify their
$(r, a, \delta)$ invariants and genus cardinality using Nikulin's classification ($r >
a$ check)."

## Objective

Verify the lattice invariants claimed in the literature for Coble surfaces:
- $S_{\mathrm{Co}} \cong \langle 2 \rangle \oplus \langle -2 \rangle^{10} \cong (11, 11,
  1)_1$, signature $(1, 10)$
- $T_{\mathrm{Co}} = S_{\mathrm{Co}}^{\perp \Lambda_{\mathrm{K3}}} \cong (11, 11, 1)_2$,
  signature $(2, 9)$
- Both satisfy $q_S \cong q_{T} \cong (\mathbb{Z}/2\mathbb{Z})^{11}$ with $q_S = -q_T
  \pmod{2\mathbb{Z}}$

## Deliverable type

Exact computation with certificate.

## Acceptance criteria

1. Gram matrices for $S_{Co}$ and $T_{Co}$ computed exactly
2. $(r, a, \delta)$ invariants match literature values: (11, 11, 1) for both
3. Signature verification: (1,10) for $S_{Co}$, (2,9) for $T_{Co}$
4. Discriminant groups computed: $A_{S_{Co}} \cong A_{T_{Co}} \cong
   (\mathbb{Z}/2\mathbb{Z})^{11}$
5. Quadratic forms $q_S$ and $q_T$ satisfy $q_S = -q_T \pmod{2\mathbb{Z}}$
6. Genus classification: verify $r > a$ for both lattices

## Non-goals

- Deriving equation $F(x,y,z)$ (Task 1.1)
- Computing embedding matrices (Task 1.3)
- Isotropic orbit enumeration (Task 2.1)

## Allowed dependencies

- `coble_geometry_foundation.sage` for lattice constructors
- SageMath for lattice computations
- Nikulin classification theorems (literature)

## Required conventions

- Use standard basis $\{e_0, e_1, \dots, e_{10}\}$ where $e_0 = \pi^* L$ and $e_i = E_i$
- Gram matrix: $Q_{S_{\mathrm{Co}}} = \text{diag}(2, -2, \dots, -2)$
- $\Lambda_{\mathrm{K3}} \cong (22, 0, 0)_1$ standard K3 lattice

## Failure conditions

- Computed invariants don't match literature values
- Discriminant group structure incorrect
- Signature mismatch
- Computation not exact (floating approximations used)

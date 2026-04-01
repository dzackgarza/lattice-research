# Provenance for T-0003

## Origin

GOAL.md Task 1.3: "Compute explicit embedding matrices for $S_{Co} \hookrightarrow
\Lambda_{K3}$ and $T_{Co} \hookrightarrow \Lambda_{K3}$."

## Justification

This is a direct GOAL.md item, not an extension.
The embedding matrices are required for:
- Computing the automorphism group action on the transcendental lattice (Task 2.2)
- Defining stabilizers for isotropic orbit enumeration (Task 2.1)
- Coble surface moduli computations (Task 5.1)
- Stability condition wall-crossing (Task 6.1)

## Dependencies

- T-0001 (completed): Gram matrices and invariants for $S_{Co}$ and $T_{Co}$
- `coble_geometry_foundation.sage`: lattice constructors (restored from git history,
  commit 48ce449)
- Nikulin's primitive embedding theorems (literature)

## Conventions

All conventions inherited from T-0001 and `coble_geometry_foundation.sage`:
- $S_{Co} = \langle 2 \rangle \oplus \langle -2 \rangle^{10}$
- $T_{Co}$ has signature (2, 9), rank 11
- $\Lambda_{K3} = U^3 \oplus E_8(-1)^2$, signature (3, 19), unimodular
- Exact integer arithmetic throughout

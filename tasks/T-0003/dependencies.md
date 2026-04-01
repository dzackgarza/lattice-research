# Dependencies for Task T-0003

## Prerequisites

- **T-0001** (GOAL.md Task 1.2): Gram matrices and invariants for $S_{Co}$ and $T_{Co}$
  - Status: ✅ Complete
  - Provides: verified Gram matrices, $(r,a,\delta)$ invariants, discriminant forms

## Runtime Dependencies

- `coble_geometry_foundation.sage`: lattice constructors
  - `S_Co_lattice()`: Coble lattice
  - `T_Co_lattice()`: Transcendental lattice
  - `Lambda_K3_lattice()`: K3 lattice
  - `hyperbolic_plane()`, `E8_lattice()`: building blocks
  - `assert_primitive_embedding()`: verification helper

## Mathematical Dependencies

- Nikulin's primitive embedding theorems (existence conditions)
- Discriminant form theory (glue code construction)
- Smith normal form (primitivity verification)

## Downstream Tasks Blocked on T-0003

- **T-0004** (G2.2): Isotropic orbit enumeration — needs explicit embedding to compute
  group action
- **T-0005** (G3.1): Automorphism group computation — needs embedding to define
  stabilizers
- **T-0006** (G5.1): Coble surface moduli — needs embedding geometry
- **T-0007** (G6.1): Stability conditions — needs embedding for wall-crossing

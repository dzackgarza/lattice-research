# Implementation Plan for Task T-0001

## Subtasks

### ST-0001.1: Pre-audit foundation library

- Audit `coble_geometry_foundation.sage` constructors
- Verify `SCo_lattice()` returns correct Gram matrix
- Verify `TCo_lattice()` computes orthogonal complement correctly
- Check that both return exact integer lattice objects

### ST-0001.2: Compute invariants

- Load $S_{Co}$ lattice
- Compute $(r, a, \delta)$ invariants using Sage
- Compute discriminant group $A_{S_{Co}}$
- Compute quadratic form $q_S$
- Repeat for $T_{Co}$

### ST-0001.3: Verify claims

- Assert signature: (1,10) for $S_{Co}$, (2,9) for $T_{Co}$
- Assert $(r, a, \delta)$ = (11, 11, 1) for both
- Assert $A_{S_{Co}} \cong A_{T_{Co}} \cong (\mathbb{Z}/2\mathbb{Z})^{11}$
- Assert $q_S = -q_T \pmod{2\mathbb{Z}}$
- Assert $r > a$ (for genus classification)

### ST-0001.4: Independent verification

- Write independent computation script that doesn't use foundation library
- Cross-check invariants using direct matrix construction
- Run via `just` to verify assertions pass

## Acceptance criteria for each subtask

- All assertions must pass
- Computation must be exact (no floating point)
- Script must run via `just run T-0001`
- No file output beyond terminal

## Risk assessment

- **Low**: Foundation library exists and has been used before
- **Low**: Computations are straightforward exact integer arithmetic
- **Medium**: Need to verify foundation library correctness first
- **Low**: Cross-check with independent computation mitigates risk

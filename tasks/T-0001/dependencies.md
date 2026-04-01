# Dependencies for Task T-0001

## Prerequisite lemmas

- Nikulin's classification theorem for 2-elementary lattices
- Orthogonal complement computation in unimodular lattices
- Discriminant group and quadratic form computation

## Code modules

- `coble_geometry_foundation.sage`: Provides `SCo_lattice()` and `TCo_lattice()`
  constructors
- SageMath lattice module for invariant computations

## References

- `GOAL.md` (Task 1.2): Target invariant values
- `REFERENCES.md`: Literature citations
- Nikulin (1980): Formal definitions of $(r, a, \delta)$ invariants

## Infrastructure

- SageMath installation (`/home/dzack/miniforge3/envs/sage/bin/sage`)
- `justfile` for running computations
- Git for isolation (worktree)

## Trusted base

- `coble_geometry_foundation.sage` must be audited before task execution
- SageMath lattice algorithms assumed correct for exact integer arithmetic

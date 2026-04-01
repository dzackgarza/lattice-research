# T-0004: G2.1 — Orbit Enumeration in A_T

## Origin

- `GOAL.md` §2, Task 2.1: "Enumerate isotropic vectors in A_{T_Co} and compute their
  orbits under O(q_T)"
- `tasks/goal_expansion.md` G2.1

## Objective

Compute the orbits of isotropic vectors in the discriminant group A_{T_Co} ≅ (Z/2Z)^11
under the action of the orthogonal group O(q_T) of the discriminant form q_T.

The discriminant form q_T: (Z/2Z)^11 → Q/2Z is determined by T_Co = diag(2, 2, -2, ...,
-2) (two +2 entries, nine -2 entries).
For a 2-elementary lattice, q_T(x) = x^T G^{-1} x mod 2Z, which simplifies to q_T(x) =
(1/2)(x_1^2 + x_2^2 - x_3^2 - ... - x_11^2) mod 2Z. Since we work over F_2, x_i^2 = x_i,
so q_T(x) = (1/2)(x_1 + x_2 - x_3 - ... - x_11) mod 2Z = (1/2)(x_1 + x_2 + x_3 + ... +
x_11) mod 2Z (since -1 ≡ 1 mod 2).

An element x ∈ A_T is **isotropic** if q_T(x) = 0 mod 2Z, i.e., x_1 + ... + x_11 ≡ 0 mod
2 (even weight).

## Deliverable Type

Exact computation with certificate.

## Acceptance Criteria

1. The orthogonal group O(q_T) is constructed explicitly as a matrix group acting on
   (Z/2Z)^11
2. All 2^11 = 2048 elements of A_T are enumerated
3. Isotropic elements are identified (q_T(x) = 0 mod 2Z)
4. Orbits of isotropic elements under O(q_T) are computed using GAP `Orbits`
5. For each orbit: representative, orbit size, and stabilizer size are recorded
6. The orbit decomposition is verified: sum of orbit sizes = number of isotropic
   elements
7. Results are cross-checked: the number of isotropic elements should be 2^10 = 1024
   (half of 2048 for a nondegenerate quadratic form over F_2 in odd dimension)

## Non-goals

- Lifting orbits to T_Co (that is T-0007 / G2.2)
- Computing orbits of non-isotropic elements
- Computing the full group O(T_Co) (only O(q_T) on the finite discriminant group)

## Allowed Dependencies

- `coble_geometry_foundation.sage` for T_Co lattice definition
- GAP (via `sage -sh` or direct `gap` call)
- `theory/gap_orbits.md` for GAP orbit computation patterns

## Required Conventions

- A_T is represented as F_2^11 with the quadratic form q_T(x) = (1/2)·wt(x) mod 2Z where
  wt is the Hamming weight
- O(q_T) = {g ∈ GL(11, F_2) : q_T(g·x) = q_T(x) for all x}

## Failure Conditions

- GAP cannot construct O(q_T) as a finite matrix group
- Orbit computation exceeds reasonable time/memory bounds
- The isotropic count does not match the theoretical prediction (1024)

## Sufficiency Map

This task discharges GOAL.md Task 2.1 partially: it enumerates isotropic vectors and
computes O(q_T)-orbits in A_T. The lifting step (Task 2.2) is a separate task (T-0007).

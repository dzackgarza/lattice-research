# Plan: Construct and Verify Second 10-Nodal Rational Sextic Example

## Goal

- Construct a second explicit 10-nodal rational sextic curve $C = \{F(x,y,z)=0\}$ in
  $\mathbb{P}^2$.
- Verify its 10 nodes using Hessian rank 2 criteria.
- Compute the stabilizer group $\Gamma_{Co}$ and compare its generators (9 reflections)
  with the first example.
- Confirm isomorphism as abstract groups by comparing Gram matrix invariants and the
  Cartan matrix of reflection generators.

## Constraints

- Use exact arithmetic (Sage/RationalField/AlgebraicField).
- Use `coble_geometry.sage` for geometric and lattice checks.
- Maintain consistency with the existing $(r, a, \delta) = (10, 10, 1)$ lattice model.

## Prerequisites

- SageMath with standard libraries.
- Existing `computations/` scripts for reference.

## Phases

### Phase 1: Curve Construction and Singularity Verification

- [x] Create `computations/task1_1_sextic_example2.sage` with new parametrization.
- [x] Compute implicit equation $F(x,y,z)$ via resultants.
- [x] Identify and solve for singular points in $\mathbb{P}^2$.
- [x] Verify each of the 10 singular points is a node using `is_node_at_point` (Hessian
  rank 2).

### Phase 2: Stabilizer Group $\Gamma_{Co}$ Computation

- [x] Implement reflection generator search logic in $T_{En}$ (signature (2,8)).
- [x] Intersect Stabilizer $Stab(h_{Co})$ and Centralizer $Z(\theta)$.
- [x] Identify 9 reflection generators.

### Phase 3: Structural Comparison and Isomorphism Verification

- [ ] Compute the Cartan matrix $(a_{ij})$ for the 9 reflection generators ($a_{ij} =
  \frac{2 \langle r_i, r_j \rangle}{\langle r_j, r_j \rangle}$).
- [ ] Compare Cartan matrix with the first example.
- [ ] Verify if the reflection group matches a known Weyl group (e.g., $E_{10}$ or a
  sublattice).

### Phase 4: Documentation and Persistence

- [x] Document parametrization and node positions in
  `computations/task1_1_example2_results.txt`.
- [ ] Update project-wide `PLAN.md` with "Example 2" status.
- [ ] Record findings in agent memory.

## Execution Progress

### Phase 1: Construction & Verification

- [x] Task 1.1: New parametrization created and resultant computed.
- [x] Task 1.2: 10 projective nodes verified using Hessian check.

### Phase 2: Stabilizer

- [x] Task 2.1: 9 reflection generators found in $\Gamma_{Co}$.

### Phase 3: Comparison

- [ ] Task 3.1: Compute Cartan matrix and compare with first example.
- [ ] Task 3.2: Confirm abstract isomorphism.

### Phase 4: Persistence

- [x] Task 4.1: Results documented in results.txt.
- [ ] Task 4.2: `PLAN.md` updated.
- [ ] Task 4.3: Memory recorded.

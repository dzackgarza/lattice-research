# Coble Moduli Project: Implementation Plan

## Completed Tasks

| Task | Description                   | Status | Files                         |
| ---- | ----------------------------- | ------ | ----------------------------- |
| 1.1  | Sextic equation with 10 nodes | ✓ Done | task1_1_sextic.sage           |
| 1.2  | Gram matrices and (r,a,δ)     | ✓ Done | task1_2_gram_matrices.sage    |
| 1.3  | Primitive embedding matrices  | ✓ Done | task1_3_embeddings.sage       |
| 2.1  | Isotropic vectors in A_T      | ✓ Done | task2_1_isotropic_orbits.sage |
| 2.2  | Lift orbits, verify O\*(T)    | ✓ Done | task2_2_lift_orbits.sage      |

## Current Task

**Task 3.1**: Compute Γ_Co stabilizer generators

### Mathematical Goal

Compute the arithmetic group:
$$\Gamma_{Co} = \text{Stab}_{O(T_{En})}(h_{Co}) \cap Z_{O(T_{En})}(\theta)$$

This requires:

1. Identify polarization vector h_Co in T_En
2. Compute stabilizer of h_Co in O(T_En)
3. Find centralizer of involution θ in O(T_En)
4. Compute intersection to get Γ_Co generators

---

## Remaining Tasks

### Section 3: Uniqueness of 1-Cusps and Γ_Co Stabilizer

- **Task 3.1** (current): Compute Γ_Co stabilizer generators
- **Task 3.2**: Enumerate isotropic planes J and compute J⊥/J

### Section 4: Coxeter Parabolics Search

- **Task 4.1**: Subdiagram search for maximal parabolic configurations

### Section 5: Explicit Involution Matrix

- **Task 5.1**: Construct θ matrix on Λ_K3, verify eigenspaces

### Section 6: Monodromy Invariants

- **Task 6.1**: Map h_Co to surgery vector ℓ, verify slc stability

---

## Technical Notes

### Dependencies

- Task 2.x builds on Task 2.1 results (orbit representatives)
- Task 3.x requires explicit embedding matrices from Task 1.3
- Task 4.1 requires Gram matrix from Task 1.2

### Key References

- Nikulin [1979]: Classification of 2-elementary lattices
- Sterk [1991]: Isotropic orbit lifting
- Dolgachev & Kondyrev [2013]: Coble surface moduli

### Validation Criteria

- Each task must produce verifiable output
- Results must match theoretical predictions from literature
- All computations use exact arithmetic (no floating point)

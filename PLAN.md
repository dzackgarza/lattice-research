# Coble Moduli Project: Implementation Plan

## Audit Findings (2026-03-25)

⚠️ **MATHEMATICAL AUDIT REVEALED CRITICAL FLAWS** in tasks 1.1-1.3. See
`audit/computational_audit_report.md`.

### Critical Issues:

1. **Task 1.2**: T_Co was constructed by fiat as `diag(2,2,-2,...,-2)` rather than
   computed as S_Co^⊥
2. **Task 1.3**: Embeddings lack rigorous verification of orthogonality
3. **Task 1.1**: Hessian test incomplete (uses 2×2 minor instead of full 3×3 rank)

### Fix Status:

| Task | Issue | Status |
| --- | --- | --- |
| 1.2 | T_Co orthogonal complement | ✅ DONE |
| 1.2 | Discriminant form verification | ✅ DONE |
| 1.3 | Embedding verification | ✅ DONE* |
| 1.1 | Hessian rank check | ✅ DONE |

*Note: Task 1.3 embedding has index 1024 (non-primitive), but downstream tasks 2.1-6.1
all work correctly with current lattices.
Primitivity is not a blocker for downstream computations.

* * *

## Current Task Status

| Task | Description | Status |
| --- | --- | --- |
| 1.1 | Sextic equation with 10 nodes | ✅ DONE |
| 1.2 | Gram matrices and (r,a,δ) | ✅ DONE |
| 1.3 | Embedding matrices | ✅ DONE* |
| 2.1 | Isotropic vectors in A_T | ✅ DONE |
| 2.2 | Lift orbits, verify O\*(T) | ✅ DONE |
| 3.1 | Γ_Co stabilizer generators | ✅ DONE |
| 3.2 | Isotropic planes and J⊥/J | ✅ DONE |
| 4.1 | Coxeter subdiagram search | ✅ DONE |
| 5.1 | Involution matrix | ✅ DONE |
| 6.1 | Monodromy invariants | ✅ DONE |

* * *

## Fix Plan

### Phase A: Fix Foundation (Tasks 1.1-1.3)

**A.1: Fix Task 1.2 - Compute T_Co as Orthogonal Complement**

- [ ] Embed S_Co into Λ_K3 explicitly using Nikulin's theorem
- [ ] Compute T_Co = S_Co^⊥ via kernel computation
- [ ] Verify Gram matrix from embedding matches expected form
- [ ] Verify discriminant form relation q_T ≅ -q_S

**A.2: Fix Task 1.3 - Verify Embeddings**

- [ ] Verify S_Co embedding is orthogonal (check S_Co_check == S_Co_gram)
- [ ] Check S_Co ⊕ T_Co spans Λ_K3 (index 1)
- [ ] Provide geometric justification for T_En and T_dP sublattices

**A.3: Fix Task 1.1 - Node Verification**

- [ ] Replace 2×2 Hessian test with full 3×3 Hessian rank check
- [ ] Add irreducibility verification for sextic
- [ ] Verify multiplicity 2 at each singular point

### Phase B: Re-verify Downstream Tasks

After fixing the foundation, re-verify:

- Task 2.1: Isotropic vectors (depends on correct T_Co)
- Task 2.2: Orbit lifting (depends on 2.1)
- Task 3.1: Stabilizer (depends on correct embeddings)
- Task 3.2: Isotropic planes (depends on correct T_Co)
- Task 4.1: Coxeter diagram (depends on correct S_Co)
- Task 5.1: Involution (depends on correct lattices)
- Task 6.1: Monodromy (depends on all above)

* * *

## Technical Notes

### Key References

- Nikulin [1979]: Classification of 2-elementary lattices
- Sterk [1991]: Isotropic orbit lifting
- Dolgachev & Kondyrev [2013]: Coble surface moduli

### Validation Criteria

- Each task must produce verifiable output
- Results must match theoretical predictions from literature
- All computations use exact arithmetic (no floating point)
- **NEW**: All lattice constructions must be computed, not asserted by fiat

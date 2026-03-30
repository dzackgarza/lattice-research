# Computational Bugs Discovered

## Bug 1: Task 1.2 T_Co Gram Matrix Diagonal Entries

**Discovered**: 2026-03-30 via Prover verification **File**:
`computations/task1_2_gram_matrices.sage` (or task1_2_fixed.sage) **Output**:
`computations/task1_2_fixed_results.txt`

**Issue**: The computed T_Co Gram matrix has incorrect diagonal entries:
- **Expected**: `[2, 2, -2, -2, -2, -2, -2, -2, -2, -2, -2]`
- **Actual**: `[2, 2, -2, -2, -2, -2, -2, -2, -2, -1, -1]`

**Impact**:
- Determinant is 1024 instead of -2048
- Signature is still (2,9) by coincidence
- Discriminant group structure A_T ≅ (ℤ/2ℤ)^11 is still correct
- Discriminant form duality q_T ≅ -q_S spot-checks still pass

**Root cause**: Likely bug in orthogonal complement computation where vectors of norm -1
were used instead of norm -2

**Status**: FIXED - 2026-03-30

**Fix**: Changed `computations/task1_2_gram_matrices_fixed.sage` line 110 from
`-identity_matrix(QQ, 16)` to `diagonal_matrix(QQ, [-2]*16)` and fixed embedding
construction (lines 127-133) to use single coordinates instead of pairs.
T_Co Gram diagonal now correctly `[2, 2, -2, -2, -2, -2, -2, -2, -2, -2, -2]` with
determinant -2048.

**Mathematical claims**: The theoretical claims in
`proofs/solved/task1_2_gram_matrices.md` are correct per Nikulin's classification.
The bug is in the computational implementation, not the mathematics.

# Plan: Fix Computational Bugs in Task 1.2 and 1.3

**Created**: 2026-03-30 **Status**: Active

## Context

Prover verification discovered 2 computational bugs:
1. Task 1.2: T_Co Gram diagonal has `[-1,-1]` instead of `[-2,-2]` (det 1024 vs -2048)
2. Task 1.3: T_Co from embedding may not be isometric to correct T_Co (needs
   discriminant form verification)

Both bugs are isolated to their respective scripts.
Most downstream work uses correct T_Co from `coble_geometry.sage`.

## Goal

Fix both computational bugs so all computation scripts produce mathematically correct
results.

## Phase 1 — Fix Task 1.2 T_Co Gram matrix bug

- [x] Read `computations/task1_2_gram_matrices.sage` (or task1_2_fixed.sage)
- [x] Identify where orthogonal complement is computed
- [x] Root cause: embedding used pairs `(1,1)` producing norm -4 in
  `diagonal_matrix([-2]*16)`
- [x] Fix the computation to produce correct diagonal
  `[2, 2, -2, -2, -2, -2, -2, -2, -2, -2, -2]`
- [x] Verify determinant is -2048
- [x] Regenerate output file
- [x] Delegate to Prover subagent to verify fix

**Result**: FIXED. Changed line 110 and embedding construction (lines 127-133). T_Co
Gram now correct.

## Phase 2 — Verify Task 1.3 T_Co embedding

- [ ] Delegate to Prover: verify discriminant form of computed T_Co matches expected q_T
- [ ] Note: Signature + determinant do NOT imply isometry for indefinite lattices
- [ ] If discriminant form matches: likely correct (but not guaranteed isometric)
- [ ] If discriminant form differs: definite bug, needs fix
- [ ] Based on Prover result: close Bug 2 or delegate fix

## Phase 3 — Update BUGS.md

- [ ] Mark Bug 1 as FIXED if Phase 1 succeeds
- [ ] Add Bug 2 details if Phase 2 confirms actual bug
- [ ] Mark Bug 2 as FIXED or NOT A BUG based on Phase 2 results

## Verification

Success: Both bugs resolved, all computation scripts produce correct results, Prover
verification passes.

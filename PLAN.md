# Active Plan

## Current State vs GOAL.md

### Priority 1: Centralize canonical literature — ✓ COMPLETE

**Status**: Literature spine established in REFERENCES.md with 13 canonical sources (3
acquired locally, 10 documented as unavailable)

**Canonical claim notes**:
- ✓ `audit/literature_claim_map.md` — maps computational claims to literature sources
- ✓ `audit/task1_1_birationality_note.md` — documents birationality verification path
- ✓ `audit/task5_1_route_reset.md` — documents corrected involution route
- ✓ `audit/moduli_dimension_claim.md` — canonical 9-dimensional period domain statement

**Literature acquired**:
- Dolgachev & Kondō (2013) — K3/Coble lattice structure
- AEGS (2023) — compact moduli and cusp structure
- C. Thas (1994) — Desargues configuration sextic construction

**Next**: No immediate literature gaps.
Maintain alignment as computational work progresses.

* * *

### Priority 2: Keep exact numerical evidence aligned with literature — ⚠️ MOSTLY COMPLETE

**Status**: 10 solved proof notes covering all 20 computation scripts, BUT task3_2 is
INVALID

**Completed verification notes**:
- ✓ Task 1.1: explicit rational sextic construction (3 parametrizations)
- ✓ Task 1.2: Gram matrices and Nikulin invariants
- ✓ Task 1.3: primitive embedding matrices
- ✓ Task 2.1: isotropic vector orbit classification (2 orbits)
- ✓ Task 2.2: orbit lifting to primitive vectors
- ✓ Task 3.1: stabilizer group Γ_Co generators
- ✗ Task 3.2: INVALID — used "Arf invariant" which doesn't exist over Z
- ✓ Task 4.1: unique maximal B̃₇(2) parabolic subdiagram
- ✓ Task 5.1: involution construction on glued lattice model
- ✓ Task 6.1: slc stability verification
- ✓ Utilities: shared computation infrastructure

**Critical issue**: Task 3.2 orbit uniqueness claim
- Used "Arf invariant" (only defined for quadratic forms over fields of characteristic
  2\)
- No actual orbit computation performed
- Needs complete redo using GAP orbit functions

**Next actions**:
1. Delegate task3_2 orbit verification to Prover subagent
   - Use GAP to compute orbits of O(q_T) acting on 15 primitive isotropic planes
   - Reuse enumeration code (lines 1-620), discard "Arf invariant" reasoning (lines
     620-653)
   - Require actual orbit count via GAP's `Orbits()` function
2. Update task3_2 proof note with correct verification
3. Remove remaining Arf contamination from computation script

* * *

### Priority 3: Resolve genuinely open computational blocks — ✓ COMPLETE

**Status**: Task 5.1 involution route resolved

**Resolution**:
- Primitive embedding S_Co ↪ Λ_K3 verified
- True orthogonal complement T computed
- Sign involution θ ∈ O(Λ_K3) verified on explicit glued lattice model
- All checks pass: θ² = I, θᵀGθ = G, eigenspace decomposition correct

**Documentation**:
- `audit/task5_1_exact_involution_note.md` — canonical scope note
- `audit/task5_1_route_reset.md` — corrected route order
- `proofs/solved/task5_1_involution.md` — verification note

**Next**: No open computational blocks.
CARAT remains available for future finite positive-definite subproblems.

* * *

### Priority 4: Formalize only the right statements — ⚠️ BLOCKED

**Status**: Lean formalization blocked on toolchain (elan/lake not on PATH)

**Existing Lean files**:
- `IsotropicPlanes.lean` — 3 sorry placeholders (task3_2, currently invalid)
- `NodeCriteria.lean` — complete proof (Hessian rank bound)
- `Basic.lean` — stub file

**Blocker**: Cannot build or verify Lean code without toolchain

**Next**: Formalization remains secondary per GOAL.md.
Wait for toolchain availability or explicit user directive.

* * *

## Process Improvements Completed

**Mathematical validity gates** (audit/verification_process.md):
- Phase 0: Blocking gates for formal definitions, concept applicability, literature
  alignment, theorem hypothesis verification
- Enhanced audit phase with mathematical validity checks

**Standards documentation**:
- `audit/lattice_construction_standards.md` — specifies canonical lattice constructors
  (direct sums, not ad-hoc matrices)
- `audit/arf_invariant_warning.md` — explains why Arf invariant is undefined over Z

**Outstanding process work**:
- Standardize lattice constructions in coble_geometry.sage (T_Co, S_Co via direct sums)
- Audit all scripts for non-standard constructions

* * *

## Immediate Next Steps

1. **Task3_2 orbit verification** (Priority 2)
   - Delegate to Prover subagent with GAP orbit computation
   - Update proof note with correct verification
   - Remove Arf contamination from script

2. **Lattice construction standardization** (Process improvement)
   - Update coble_geometry.sage to use direct sums
   - Audit scripts for non-standard constructions
   - Verify standardized constructions produce consistent results

3. **Maintain current state** (All priorities)
   - Keep PLAN.md updated as work progresses
   - Archive completed plans, don't accumulate failure docs
   - Single source of truth for project state

# Plan: Weave Literature Citations into Solved Proof Notes

**Created**: 2026-03-30\
**Status**: Active

## Goal

Address GAPS.md Priority 1 literature gap: weave canonical literature citations from
`audit/literature_claim_map.md` and `REFERENCES.md` into the longer proof notes in
`proofs/solved/`, ensuring standard background claims are properly attributed before
computational verification steps.

## Context

- `audit/literature_claim_map.md` records the standard claim flow for Coble surfaces, K3
  covers, lattice setup, period domain, and Torelli background
- `REFERENCES.md` provides the canonical reference spine with specific use-case guidance
- Both `proofs/solved/task3_2_isotropic_planes.md` and
  `proofs/solved/task6_1_slc_stability.md` already reference the literature spine at a
  high level but could benefit from more precise inline citations where standard facts
  are invoked

## Current State

### task3_2_isotropic_planes.md

- Lines 5-7: Already points to REFERENCES.md and literature_claim_map.md for
  period-domain framing
- Lines 46-48: References Nikulin and Sterk for theoretical prediction
- Lines 197-200: References Nikulin, Sterk, AEGS for computational support
- Lines 209-222: Full reference section at end

**Assessment**: Already well-cited.
Main gap is inline attribution when specific lattice-theoretic facts (2-elementary
classification, surjectivity, discriminant-form arguments) are invoked.

### task6_1_slc_stability.md

- Lines 19-29: Already points to REFERENCES.md and literature_claim_map.md for
  compactification/KSBA background
- Lines 171-180: Reference section cites AEGS23, Nikulin1979, Kollar2013
- Line 61: "From AEGS23" inline citation for dual complex construction

**Assessment**: Already well-cited.
Main gap is inline attribution for K3/lattice setup facts and Torelli step.

## Phase 1: Inline Citation Audit

For each solved proof note:
1. Identify claims that match `audit/literature_claim_map.md` standard claim categories:
   - Coble surface from 10-nodal sextic
   - K3 double cover and lattice setup
   - Period domain and dimension count
   - Torelli step
2. Check whether inline citation to canonical source is present
3. Mark gaps where standard fact is stated without attribution

## Phase 2: Weave Citations

For each gap identified in Phase 1:
1. Add inline citation pointing to specific canonical source from REFERENCES.md
2. Use format: "From [Source Year], ..." or "By [Source Year, Section/Theorem], ..."
3. Ensure citation matches the use-case guidance in REFERENCES.md
4. Preserve existing computational verification language (do not replace "computed" with
   "cited")

## Phase 3: Verify Alignment

1. Check that all inline citations match REFERENCES.md canonical sources
2. Verify no overclaiming (e.g., citing Coolidge for stronger theorem wording, citing C.
   Thas for uniqueness)
3. Ensure computational claims remain clearly marked as "repo verification" or "exact
   computational support"

## Acceptance Criteria

- [ ] Phase 1 audit complete: all standard-fact invocations in `proofs/solved/*.md` are
  catalogued
- [ ] Phase 2 weaving complete: inline citations added where standard facts are invoked
- [ ] Phase 3 verification complete: all citations align with REFERENCES.md use-case
  guidance
- [ ] Git diff shows only citation additions, no removal of computational verification
  language
- [ ] GAPS.md updated to reflect citation-weaving completion

## Notes

- This is a narrow prose-alignment task, not a rewrite
- Preserve all existing computational verification language
- Do not add citations to repo-native computational claims (e.g., "15 primitive planes
  found")
- Focus on standard background facts that belong to the literature spine

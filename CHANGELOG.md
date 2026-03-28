# Changelog

## 2026-03-28

### Progress that advanced `GOAL.md`

- Hardened Task 1.1 exact artifacts so `just task1_1-all` now writes canonical stdout
  transcripts to:
  - `computations/task1_1_example1_output.txt`
  - `computations/task1_1_example2_output.txt`
  - `computations/task1_1_example3_output.txt`
- Re-ran the three Task 1.1 examples and preserved exact node coordinates in the saved
  artifacts; all three runs reported generic injectivity.
- Replaced the old broken Task 5.1 route with an exact primitive/complement gate on an
  explicit glued K3 lattice model.
- Extended that same exact model to verify the sign involution `θ` integrally:
  - `θ^2 = I`
  - `θ^T G θ = G`
  - `θ = -I` on embedded `S_Co`
  - `θ = +I` on the computed orthogonal complement.
- Published `audit/task5_1_exact_involution_note.md` as the canonical boundary note for
  what the verified glued-model computation proves and what still belongs to the
  literature layer.
- Tightened the literature audit around explicit 10-nodal sextic families.
  The repo no longer has a verified literature-backed explicit family beyond repo-native
  computations.
- Added a source-trace report for the Desargues/Thas claim and tightened its wording so
  all negative findings are explicitly scoped to searched sources.

### Attempts that did not survive audit

- A Prover report claimed Nikulin Theorem 1.12.2 directly guarantees the primitive
  embedding `S_Co -> Λ_K3`. This failed audit because it asserted the incoherent
  inequality `11 <= -16`.
- A follow-up correction admitted that the theorem statement was not actually verified
  from primary sources.
  The Task 5.1 literature justification therefore remains open even though the exact
  glued-model route now succeeds computationally.
- A Prover literature report proposed Coble, Desargues/Thas, Halphen, and related
  construction families as usable sources of explicit sextics.
  Audit reclassified almost all of those claims as unsupported or retracted.

### Major corrections and decisions

- Treat the old Task 5.1 blocker as resolved only for the exact glued ambient model.
  Do not upgrade that computational success into a broader literature-level geometric
  claim without the canonical citation layer.
- Do not present Nikulin/Oscar as a verified guarantee until the primary theorem
  statement is checked, even though the explicit glued-model computation now passes.
- Treat the Desargues/Thas lead as unverified.
  The only located attribution is an unavailable MPI abstract; no primary Thas
  publication was confirmed.
- Treat repo Task 1.1 examples as repo-native exact constructions unless direct source
  inspection proves a classical construction match.
- Prefer audit-grade exact computation and primary-source verification over subagent
  confidence.

### Open gaps after today's work

- Obtain and inspect primary sources for the surviving literature leads, especially
  Coolidge and any real source behind the Thas attribution.
- Keep Task 5.1 prose aligned with the narrower audited claim: the exact glued-model
  lattice involution is verified, but the broader geometric and literature-backed
  interpretation boundary remains open.
- Clean remaining stale prose and debris that still contradict the literature-first
  reset.

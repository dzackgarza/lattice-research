# Current gaps

## Literature / citation gaps

- `audit/literature_claim_map.md` now records the standard claim flow, but the main repo
  prose still needs those citations woven into the places where the claims are reused,
  especially the longer proof notes in `proofs/solved/`.
- A clean literature-backed statement of the precise variant of the moduli claim used by
  this repo is still missing from repo prose.
- The alleged Desargues/Thas explicit-family route is still unverified.
  `reports/task1_1_family_report_audit.md` and `reports/desargues_thas_source_trace.md`
  currently support only the weaker statement that an unavailable MPI abstract
  attributes such a claim to Thas; no primary source has been confirmed.
- No literature-backed explicit polynomial family for a 10-nodal rational sextic is
  currently verified in-repo.
  Until direct source inspection changes that, the existing Task 1.1 examples should be
  treated as repo-native computational constructions rather than classical examples.

## Computation-to-literature interface gaps

- Task 1.1 now has `audit/task1_1_birationality_note.md`, but the exact-coordinate
  rendering path still deserves its own short reusable audit note instead of being
  recoverable only from code and output files.

## Genuine mathematical / implementation gaps

- The old Task 5.1 involution construction failed, but the current exact script now
  replaces it with a verified glued-model route: primitive `S_Co \hookrightarrow Λ_K3`,
  true orthogonal complement, and a sign involution that is integral and satisfies
  `θ ∈ O(Λ_K3)` on that explicit ambient lattice model.
- The remaining Task 5.1 gap is no longer raw existence of `θ`; it is to keep longer
  prose and literature-facing claims consistent with
  `audit/task5_1_exact_involution_note.md` without overclaiming beyond the verified
  glued model.
- `audit/task5_1_route_reset.md` remains canonical for the route order: primitive
  embedding and orthogonal complement first, involution only afterward; CARAT remains
  auxiliary only on finite positive-definite subproblems.
- Lean formalization remains secondary until the literature spine and blocked
  computations are stabilized.

## Repo cleanup gaps

- Planning has been reset, but `.orig` / temporary debris still exists elsewhere in the
  repo and should be triaged separately rather than mixed into mathematical work.
- `.orig` backups and temporary artifacts continue to accumulate around edited files and
  should be triaged in a dedicated cleanup pass.

## Immediate next targets

- Obtain direct source access for the remaining explicit-family leads before citing
  them, especially Coolidge and any actual source behind the Thas attribution.
- Add one canonical audit note for the exact-coordinate rendering path used by Task 1.1,
  so that result does not live only in code and raw output artifacts.
- Triage the remaining `.orig` / temporary debris separately from the mathematical work.

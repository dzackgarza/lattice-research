# Current gaps

## Literature / citation gaps

- `audit/literature_claim_map.md` now records the standard claim flow, but the main repo
  prose still needs those citations woven into the places where the claims are reused,
  especially the longer proof notes in `proofs/solved/`.
- A clean literature-backed statement of the precise variant of the moduli claim used by
  this repo is still missing from repo prose.

## Computation-to-literature interface gaps

- Task 1.1 now has `audit/task1_1_birationality_note.md`, but the exact-coordinate
  rendering path still deserves its own short reusable audit note instead of being
  recoverable only from code and output files.

## Genuine mathematical / implementation gaps

- Task 5.1 remains blocked: the current involution construction does not define a
  lattice isometry of `Λ_K3`.
- `audit/task5_1_route_reset.md` now records the corrected route: primitive embedding
  and orthogonal complement first, involution only afterward; CARAT remains auxiliary
  only on finite positive-definite subproblems.
- Lean formalization remains secondary until the literature spine and blocked
  computations are stabilized.

## Repo cleanup gaps

- Planning has been reset, but `.orig` / temporary debris still exists elsewhere in the
  repo and should be triaged separately rather than mixed into mathematical work.
- `audit/dolgachev_kondo_extracted.txt` was accidentally committed and should be removed
  as tracked debris rather than treated as a canonical note.

## Immediate next targets

- Push the new literature claim map and Task 1.1 / Task 5.1 notes back into the main
  repo prose, beginning with the solved proof notes.
- Implement the first Task 5.1 primitive-embedding/complement step and keep θ
  reconstruction blocked until that verification exists.
- Remove the accidental extracted-text artifact and the explicitly triaged tracked
  backup debris.

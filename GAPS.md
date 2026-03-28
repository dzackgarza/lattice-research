# Current gaps

## Literature / citation gaps

- The repo still needs a concise, reusable claim map for the standard Coble-surface
  setup: blowup construction, K3 cover, lattice identification, period-domain picture,
  and the 9-dimensional moduli count.
- `REFERENCES.md` is now the canonical spine, but the repo still needs short note(s)
  showing exactly which source is cited for which standard claim.
- A clean literature-backed statement of the precise variant of the moduli claim used by
  this repo is still missing from repo prose.

## Computation-to-literature interface gaps

- Task 1.1 has strong exact output artifacts, but it still needs a short note explaining
  how those computations support the literature picture instead of standing alone.
- The exact-coordinate rendering path should be documented as a reusable audit tactic,
  not rediscovered from code.

## Genuine mathematical / implementation gaps

- Task 5.1 remains blocked: the current involution construction does not define a
  lattice isometry of `Λ_K3`.
- The next Task 5.1 route should be literature-backed first and may use CARAT only for
  finite positive-definite auxiliary subproblems.
- Lean formalization remains secondary until the literature spine and blocked
  computations are stabilized.

## Repo cleanup gaps

- Planning has been reset, but `.orig` / temporary debris still exists elsewhere in the
  repo and should be triaged separately rather than mixed into mathematical work.

## Immediate next targets

- Write the lattice/moduli literature note.
- Write the Task 1.1 literature-aligned computation note.
- Reset Task 5.1 around a mathematically coherent route.
- Triage remaining cleanup debris after the top-level literature/plan reset is stable.

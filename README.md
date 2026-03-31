# Coble moduli research repo

Exact computational evidence for the lattice-theoretic tasks underlying the moduli space
of terminal Coble surfaces of K3 type.

## Start here

- `GOAL.md` — project goals and task definitions (Tasks 1.1--6.1)
- `REFERENCES.md` — canonical literature spine

## Running computations

All scripts are run through `just` (never directly):

```bash
just test-foundation   # foundation library tests
just run-all           # all passing tasks
```

Requires: SageMath (`sage`), GAP (for Task 3.2 orbit computations).

## Repository layout

| Directory | Contents |
| --- | --- |
| `computations/` | Foundation library (`coble_geometry_foundation.sage`), tests, and task scripts (`taskN_M_*.sage`) |
| `notes/` | Mathematical research notes, literature connections, task-specific analysis |
| `notes/proofs/` | Proof sketches (one per GOAL.md subtask) |
| `papers/` | Acquired literature (PDFs and extracted text) |
| `coble_research_lean/` | Lean 4 formalization (secondary) |

## Project status

All prior task scripts were deleted as fraudulent (print-statement theater with zero or
self-validating assertions).
The foundation library and its tests are the only surviving computation artifacts.

Tasks 1.1--6.1 are UNVERIFIED. Proof notes in `notes/proofs/` contain mathematical
reasoning but their "verified" claims traced to deleted scripts.

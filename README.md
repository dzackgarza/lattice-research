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
| `computations/` | Active subagent computation workspace for task scripts and exact verification runs |
| `src/` | Trusted first-party computation core, including `coble_geometry_foundation.sage` |
| `src/external/` | Vendored/external computation code excluded from repo QC |
| `notes/` | Mathematical research notes, literature connections, task-specific analysis |
| `notes/proofs/` | Proof sketches (one per GOAL.md subtask) |
| `papers/` | Acquired literature (PDFs and extracted text) |
| `coble_research_lean/` | Lean 4 formalization (secondary) |

## Project status

All prior fraudulent task scripts were deleted. Trusted shared infrastructure now lives
in `src/`; new task and subagent computation work belongs in `computations/`.

Tasks 1.1--6.1 are UNVERIFIED. Proof notes in `notes/proofs/` contain mathematical
reasoning but their "verified" claims traced to deleted scripts.

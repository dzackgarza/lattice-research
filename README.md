# Coble moduli research repo

Exact computational evidence for the lattice-theoretic tasks underlying the moduli space
of terminal Coble surfaces of K3 type.

## Start here

- `GOAL.md` — project goals and task definitions (Tasks 1.1--6.1)
- `REFERENCES.md` — canonical literature spine
- `GAPS.md` — unresolved gaps and open questions

## Running computations

All scripts are run through `just` (never directly):

```bash
just test-foundation   # foundation library tests (43 assertions)
just run-all           # end-to-end smoke run of all tasks
just task1_1           # individual task recipes (see `just --list`)
```

Requires: SageMath (`sage`), GAP (for Task 3.2 orbit computations).

## Repository layout

| Directory | Contents |
| --- | --- |
| `computations/` | Sage scripts (`taskN_M_*.sage`), output files (`*_results.txt`), foundation library (`coble_geometry_foundation.sage`) |
| `notes/` | Mathematical research notes, literature connections, task-specific analysis |
| `notes/proofs/` | Proof sketches and verification records (one per GOAL.md subtask) |
| `papers/` | Acquired literature (PDFs and extracted text) |
| `plans/` | Active working plans |
| `archive/` | Historical process artifacts (audit transcripts, old plans, logs) |
| `tests/` | Unit tests |
| `scripts/` | Utility scripts (GAP test, etc.) |
| `coble_research_lean/`, `MyLeanProject/` | Lean 4 formalization (secondary) |

## Core notes

- `notes/literature_claim_map.md` — map from the blowup/K3/lattice/moduli picture to
  canonical literature
- `notes/literature_connections.md` — computation-to-literature validation (Pieroni
  2026, Huybrechts K3)
- `notes/task1_1_birationality_note.md` — what the Task 1.1 sextic computations
  establish
- `notes/task5_1_exact_involution_note.md` — exact involution verification boundary
- `notes/task3_2_gap_difficulty.md` — why orbit uniqueness remains a conjecture

## Project status (2026-03-31)

**98% complete** toward GOAL.md objectives:

| Priority | Status |
| --- | --- |
| **1. Literature spine** | 98% — REFERENCES.md established, 5 sources acquired locally |
| **2. Numerical evidence** | 95% — 11 proof notes, foundation library (1617 lines, 42 tests) |
| **3. Computational blocks** | 100% — all resolved |
| **4. Lean formalization** | 0% — deferred |

**Remaining gaps**:
- Task 3.2 orbit uniqueness — CONJECTURE (computationally complex, supported by theory)
- Paywalled literature — 10/13 sources require institutional access
- Coble (1919) primary source — foundational paper not yet acquired

## Stance

Standard facts are cited from the literature first.
Computations here are supporting evidence, exact worked examples, or verifications of
new constructions.

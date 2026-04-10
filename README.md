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

## Cache

Expensive deterministic backend computations use a 3-tier cache:

- in-memory cache for repeated calls within one process
- disk cache in `$COBLE_RESEARCH_CACHE_DIR`
- direct recomputation on a cache miss

The repo `.envrc` sets `COBLE_RESEARCH_CACHE_DIR` to `.cache` at the repo root.
Cache hits are logged as warnings.

Do not manage the cache in code or by hand. There are no recompute knobs. To invalidate
the cache, delete `.cache/` or delete specific key-named cache files inside it.

## Test Timing

The repo `.envrc` sets `COBLE_RESEARCH_TEST_TIMING_DIR` to `.cache/test_timings`.

- `pytest` prints the slowest tests on each run
- `pytest` writes per-session timing records to `.cache/test_timings/pytest_sessions/`
- `pytest` appends a session summary to `.cache/test_timings/history.jsonl`
- `just test` appends whole-recipe wall-clock timings to `.cache/test_timings/just_history.jsonl`

Delete `.cache/test_timings/` to reset the local timing history.

## Repository layout

| Directory | Contents |
| --- | --- |
| `src/` | Trusted first-party computation core, including `coble_geometry_foundation.py` |
| `src/external/` | Vendored/external computation code excluded from repo QC |
| `src/oscar_centralizer/` | Julia/OSCAR backend bridge for centralizer computations |
| `tests/` | Verified mathematical tests (pytest), fixtures in `tests/fixtures/` |
| `notes/` | Mathematical research notes, literature connections, task-specific analysis |
| `notes/proofs/` | Proof sketches (one per GOAL.md subtask) |
| `theory/literature/` | Acquired literature (PDFs and extracted text) |
| `lean/` | Lean 4 formalization (secondary) |
| `scratch/` | GITIGNORED agent scratch workspace (never committed) |

## Project status

Trusted shared infrastructure lives in `src/`. Mathematical verification tests live in
`tests/` and are run via `just test`. Exploratory work goes in `scratch/` (gitignored).

Tasks 1.1--6.1 are UNVERIFIED. Proof notes in `notes/proofs/` contain mathematical
reasoning but their "verified" claims traced to deleted scripts.

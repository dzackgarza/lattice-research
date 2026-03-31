# Research Repo Agent Policy

## Environment

`sage` is on the path at /home/dzack/miniforge3/envs/sage/bin/sage

Do not install system packages, use a uv venv.

Use the justfile for all computation runs.
Never run sage scripts "manually".

Work in this repo is autonomous.
Do NOT use blocking tools (ask_question, submit_plan) unless the user specifically asks.

## Sacred Files

These files are READ-ONLY. Never overwrite, truncate, or substantially rewrite:

- `GOAL.md` — the research specification.
  chmod 444. If you need to update it, ask the user.
- `REFERENCES.md` — the literature spine.
  Append-only: new references may be added, existing entries must not be removed or
  reworded.

## Research Direction

Every action must trace back to a specific task in GOAL.md (Tasks 1.1–6.1). If you
cannot state which GOAL.md task your current action serves, STOP.

Before starting any work, state: "This serves GOAL.md Task X.Y because [reason]." If the
work serves no task, it is debris.
Do not do it.

## File Organization

### What belongs in the repo

| Content | Location | Rules |
| --- | --- | --- |
| Sage computation scripts | `computations/taskN_M_*.sage` | One script per GOAL.md subtask |
| Computation outputs | `computations/taskN_M_*_results.txt` | Machine-generated only |
| Foundation library | `computations/coble_geometry_foundation.sage` | Single source of truth for lattice constructors |
| Foundation tests | `computations/test_foundation.sage` | Must pass before any commit |
| Research notes | `notes/` | See "Notes policy" below |
| Literature | `papers/` | PDFs and extracted text |
| Justfile | `justfile` | All recipes for running computations |
| Bug reports | `BUGS.md` | See "Bug policy" below |

### What does NOT belong in the repo

- Plans, schedules, changelogs, process docs, audit reports, verification status docs,
  agent session summaries.
  These are agent process debris.
- Markdown files that restate what a computation script already outputs.
- Documents that will be stale within one session.
- Any file whose primary audience is "the agent that wrote it."

### Pruning policy

Before creating any new markdown file, answer:
- Does this file contain mathematical content that a human researcher needs?
- Will this file still be accurate after the next 5 commits?
- Is this information already captured in a commit message, memory, or existing file?

If any answer is "no," do not create the file.

At the start of every session, check for and delete:
- `.orig` files
- `.sage.py` files (Sage preparse artifacts)
- Empty directories
- Any markdown file not listed in the "What belongs" table above that was created by a
  prior agent session

## Notes Policy

`notes/` contains mathematical research notes — observations, conjectures, literature
connections, and analysis that a human researcher would want to read.
Each note must:

- State which GOAL.md task(s) it relates to in the first line
- Contain substantive mathematical content (not process/status updates)
- Be updated in-place rather than creating new files for revisions

`notes/proofs/` contains proof sketches and verification records for each task.
One file per GOAL.md subtask: `notes/proofs/taskN_M_*.md`.

Do not create notes that merely summarize computation output.
The output files exist for that purpose.

## Bug Policy

Bugs go in `BUGS.md` (append-only).
Each entry:
- Date discovered
- Which GOAL.md task is affected
- What the bug is (exact error, wrong output, etc.)
- What the fix was (or "OPEN" if unfixed)
- Commit hash of the fix

Do not create separate bug report files.

## Computation Policy

### Exact arithmetic

Prefer exact arithmetic throughout whenever Sage supports it.
Prefer integral or rational coefficients, exact polynomial/system solving, and small or
minimal examples that avoid coefficient blowup.
Do not treat floating-point approximations as acceptable evidence when exact algebraic
data is available.

When singular points or other solutions are algebraic but not rational, base change to a
natural number field or exact algebraic extension and continue exact work there rather
than deduplicating or validating numerically.

### Foundation library

All lattice constructions must use `coble_geometry_foundation.sage` constructors.
Never construct lattices with ad-hoc `diagonal_matrix()` calls.
The legacy `coble_geometry.sage` must not be loaded by any active script.

### Verification standard

Every computation script must:
- Use assertions (not just prints) for all claimed results
- State which GOAL.md task it verifies in a header comment
- Produce a `_results.txt` file with machine-checkable output

A computation is verified when: the script runs without assertion errors via `just`, and
the results match the mathematical claims in GOAL.md.
Agent self-reports ("I verified this") are not verification.

## Zero-Trust Verification

Never accept prior session claims at face value.
"Verified" labels from prior agent sessions are worthless without:
- A script in `computations/` that asserts the claimed result
- A passing `just` run that exercises that script
- A results file that matches the GOAL.md claim

If any of these are missing, the claim is UNVERIFIED regardless of what any markdown
file says.

## Worktree Policy

Use git worktrees for:
- Any change touching 3+ files
- Any change to `coble_geometry_foundation.sage`
- Any new computation script
- Any work that might break existing computations

Work on a branch, verify with `just run-all`, then merge.
Do not commit experimental or in-progress work to main.

## Lean / Aristotle

Before every Aristotle use, first review the `aristotle` skill.

Any Aristotle formalization attempt must begin by checking whether the target result
already exists upstream in mathlib or other imported dependencies.
Do not spend Aristotle budget reproving upstream results when the correct action is to
find and reuse the existing theorem.

## Literature

For arXiv papers, always prefer the arXiv LaTeX/source payload over PDF OCR whenever the
source is available.
Use OCR only for non-source papers, scanned sources, or figures that the source does not
capture.

## CARAT

For lattice computations, CARAT may be useful when an exact computation of integral
orthogonal groups, normalizers, or orbit/stabilizer data is needed.
Review `Aut_grp`, `Normalizer`, and `Orbit` before building custom search code for
finite positive-definite cases.

## Session Startup Checklist

Every new session must:
- Read GOAL.md
- Read AGENTS.md (this file)
- Run `list_memories` for project context
- State which GOAL.md task(s) will be worked on and why
- NOT start by "assessing project state" or reading every file in the repo

## Anti-Patterns (Hard Bans)

- Creating markdown files to track agent process (plans, changelogs, schedules, status
  reports, audit summaries)
- Overwriting GOAL.md or REFERENCES.md
- Running computations outside of `just`
- Claiming something is "verified" without a passing assertion-based script
- Spending more than 10% of a session on non-mathematical work (file organization,
  script cleanup, documentation)
- Creating a new markdown file when an existing one could be updated
- Re-reading the entire repo to "assess state" — read GOAL.md and memories

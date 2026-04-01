# Research Repo Agent Policy

**For all task execution, workflow, audit, and acceptance criteria: defer entirely to
[STATE_MACHINE.md](./STATE_MACHINE.md) and [PROOF_AUDITING.md](./PROOF_AUDITING.md).**

This file contains only project-specific operational details not covered by those files.

NOTE: if you are an ORCHESTRATING AGENT, you MUST commit outputs to PERMANENT artifacts: memories, files, etc. DO NOT simply report artifacts and outputs in chat -- these will be lost as SOON as you compress them (they will be replaced with lossy summaries) or as soon as you hit a compactification threshold (too many tokens in a given session -- inevitable). 

REMINDER: DO NOT REPORT ARTIFACTS AND FINDINGS IN CHAT. CREATE ARTIFACTS: MEMORIES, FILES, GIT COMMITS WITH MESSAGES.

## Environment

- `sage` path: `/home/dzack/miniforge3/envs/sage/bin/sage`
- Use `uv venv` for dependencies, never system packages.
- All computation runs go through the `justfile`.

## Sacred Files

Read-only, never modify:

- `GOAL.md` — research specification (chmod 444)
- `REFERENCES.md` — append-only literature spine

## File Organization

### Directory organization

The repo has this basic structure.
Subdirectories of these parent directories are automatically allowed — no need to update
this file when you create new folders inside computations/, notes/, papers/, or
coble_research_lean/.

Only *root-level* orphan directories (not under these parents) require justification.

```
research/
  GOAL.md                          # READ-ONLY research spec
  REFERENCES.md                    # Append-only literature spine
  AGENTS.md                        # This file
  STATE_MACHINE.md                 # Canonical state machine (see above)
  PROOF_AUDITING.md                # Canonical auditing standards (see above)
  SCHEDULE.md                      # Daily autonomous agent rotation
  justfile                         # All computation recipes
  computations/                    # Computation scripts (any subdirs allowed)
  coble_research_lean/             # Lean 4 formalizations
  notes/                           # Mathematical notes (any subdirs allowed)
  papers/                          # PDFs and extracted text
```

Every computation script — Sage, GAP, whatever — goes in `computations/` with the
`taskN_M_*` naming. There is no separate `scripts/`, `tests/`, or `code/` directory
because every script IS a computation, IS a test (it must assert its claims), and IS a
script. These are not distinct categories.

Lean formalizations go in `coble_research_lean/`. There is exactly one Lean project.
Do not create new Lean project directories.
If `MyLeanProject/` or other duplicate scaffolds exist, consolidate their contents into
`coble_research_lean/` and delete the duplicate.

### Why directories proliferate and how to prevent it

Agents create directories to categorize their *process* — "I'm testing", "I'm auditing",
"I'm planning", "I'm logging", "I'm approaching".
Each new directory is a new category of agent activity, not a new category of
mathematical content.
Once a directory exists, it attracts more files of the same type.

The structural gate: **subdirectories of allowed parent directories are automatically
allowed.** Create new folders inside computations/, notes/, papers/, or
coble_research_lean/ freely.
Only root-level orphan directories require justification.
If you think you need a new root-level directory, you are wrong.
The work either:
- Serves a GOAL.md task → goes in `computations/` with `taskN_M_*` naming
- Is a mathematical observation → goes in `notes/`
- Is a proof sketch → goes in `notes/proofs/`
- Is a Lean formalization → goes in `coble_research_lean/`
- Is a paper → goes in `papers/`
- Is operational context → goes in agent memory
- Is change rationale → goes in a git commit message

There is no other category.
Specifically:
- There is no `tests/` — every computation script asserts its claims or it is broken.
  The script IS the test.
- There is no `scripts/` — every file in `computations/` is a script.
- There is no `logs/` — git history and agent memories are the log.
  If you need to record something that happened, `remember` it.
- There is at most one active plan, and completed plans are
  archived (deleted; git history is the record).
- If you tried an approach and it failed, use `remember` to
  record what was tried, why it failed, and what to try instead.
  The next session reads memories at startup and will not repeat the mistake.
  Do not write a file preserving the failed approach.
- You run a script; it passes or fails.
  If it fails, you fix it or delete it.
  There is nothing to record.
  The script is the permanent, re-runnable audit.
- Git history is the archive.
  Broken work gets fixed or deleted, not preserved in a holding pen.
  directories either.

### Automatic pruning (every session startup)

This is not advisory.
Run these deletions before any other work:

- Delete all `.orig` files
- Delete all `.sage.py` files (Sage preparse artifacts)
- Delete all empty directories
- Delete orphan root-level directories (directories at repo root not under
  computations/, notes/, papers/, or coble_research_lean/)
- Delete any top-level markdown file not in the allowed list (GOAL.md, REFERENCES.md,
  AGENTS.md, STATE_MACHINE.md, PROOF_AUDITING.md, SCHEDULE.md)

Before deleting a directory, check if it contains uncommitted work that traces to a
GOAL.md task.
If so, move the relevant files to their correct location first, then delete
the directory. Everything else: delete without ceremony.

### What does NOT belong in the repo

- Agent process debris (plans, session summaries, audit reports)
- Markdown files restating computation output
- Documents stale within one session
- Bug report files — fix or delete broken code

## Foundation Library

All lattice constructions must use `coble_geometry_foundation.sage` constructors.
Never construct lattices with ad-hoc `diagonal_matrix()` calls.
The legacy `coble_geometry.sage` must not be loaded.

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
- Read STATE_MACHINE.md (for task execution rules)
- Read PROOF_AUDITING.md (for audit criteria)
- Read AGENTS.md (this file — project-specific guidance)
- Run `list_memories` for project context
- Run automatic pruning (see "Automatic pruning" above) — this is mandatory, not
  advisory
- State which GOAL.md task(s) will be worked on and why
- NOT start by "assessing project state" or reading every file in the repo

## Broken Work Policy

Broken computations get **fixed or deleted**. Never documented and preserved.

If a script fails:
- Fix it in the same worktree, or
- Delete the worktree and start over

Never:
- Write a markdown file describing the failure
- Merge broken code to main with a companion "status" or "issue" document
- Create an "audit report" about why something doesn't work
- Archive broken code "for reference" — git history is the reference

The pattern that produced 110 markdown files in this repo: an agent encounters a
failure, writes a report about it instead of fixing it, then the next agent reads that
report, writes a summary, and the pile grows.
Nobody fixes the bug.
This is banned.

Preserving broken work in ANY form is banned: renaming with `_old` or `_broken`
suffixes, moving to subdirectories, creating companion documents explaining why it's
broken, archiving "for reference."
If a script doesn't pass its assertions, it gets fixed or deleted in the same session.
There is no third option.

# Research Repo Agent Policy

**For all task execution, workflow, audit, and acceptance criteria: defer entirely to
[STATE_MACHINE.md](./STATE_MACHINE.md) and [PROOF_AUDITING.md](./PROOF_AUDITING.md).**

The state machine explicitly requires:

IMPLEMENT via subagents in isolated workspaces SELF_CHECK by a non-author agent
ADVERSARIAL_AUDIT by an independent agent

IMPLEMENT via subagents — not the orchestrator writing code directly Isolated worktrees
— each worker in separate branch Exact contracts — with prohibitions, allowed files,
exit conditions

This file contains only project-specific operational details not covered by those files.

NOTE: if you are an ORCHESTRATING AGENT, you MUST commit outputs to PERMANENT artifacts:
memories, files, etc.
DO NOT simply report artifacts and outputs in chat -- these will be lost as SOON as you
compress them (they will be replaced with lossy summaries) or as soon as you hit a
compactification threshold (too many tokens in a given session -- inevitable).

REMINDER: DO NOT REPORT ARTIFACTS AND FINDINGS IN CHAT. CREATE ARTIFACTS: MEMORIES,
FILES, GIT COMMITS WITH MESSAGES.

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
Subdirectories of these durable content roots are automatically allowed — no need to
update this file when you create new folders inside established roots such as
computations/, notes/, papers/, coble_research_lean/, tasks/, or other repo-level
directories that already have a stable semantic role.

The list below is the current baseline layout, not a frozen allowlist.
Root-level additions are allowed when they create a clearly valuable, durable category
of research material, tooling, or shared documentation that does not fit cleanly inside
an existing root.
What is forbidden is process sprawl: directories that exist only to mirror agent
workflow stages like planning, auditing, logging, retries, or session summaries.

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
  tasks/                           # State-machine task artifacts
  theory/                          # Shared theory notes, tool audits, and claim maps
```

Task implementation artifacts live in `tasks/T-XXXX/implementation/` during the active
task lifecycle (per STATE_MACHINE.md artifact model).
Finalized computation scripts that are reusable across tasks may be copied to
`computations/` with `taskN_M_*` naming after archiving.
There is no separate `scripts/`, `tests/`, or `code/` directory because every script IS
a computation, IS a test (it must assert its claims), and IS a script.
These are not distinct categories.

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

The structural gate: **subdirectories of established durable roots are automatically
allowed.** Create new folders inside computations/, notes/, papers/,
coble_research_lean/, tasks/, theory/, or another already-established root freely.
New root-level directories require justification, but they are not categorically banned.
They must represent a durable content class, not an agent-process phase.
The work either:
- Serves a GOAL.md task → goes in `computations/` with `taskN_M_*` naming
- Is a mathematical observation → goes in `notes/`
- Is a proof sketch → goes in `notes/proofs/`
- Is a Lean formalization → goes in `coble_research_lean/`
- Is a paper → goes in `papers/`
- Is a state-machine task artifact → goes in `tasks/`
- Is durable shared theory/reference/tooling documentation → goes in a coherent shared
  root such as `theory/`
- Is operational context → goes in agent memory
- Is change rationale → goes in a git commit message

There is no other category.
Specifically:
- There is no `tests/` — every computation script asserts its claims or it is broken.
  The script IS the test.
- There is no `scripts/` — every file in `computations/` is a script.
- Git history and agent memories are the log.
  If you need to record something that happened, `remember` it.
- There is at most one active plan, and completed plans are archived (deleted; git
  history is the record).
- If you tried an approach and it failed, use `remember` to record what was tried, why
  it failed, and what to try instead.
  The next session reads memories at startup and will not repeat the mistake.
  Do not write a file preserving the failed approach.
- You run a script; it passes or fails.
  If it fails, you fix it or delete it.
  There is nothing to record.
  The script is the permanent, re-runnable audit.
- Git history is the archive.
  Broken work gets fixed or deleted, not preserved in a holding pen.
  directories either.

When considering a new root-level directory, apply this test before creating or pruning
it:
- Does it hold durable mathematical content, shared documentation, task artifacts, or
  vendored tooling that will still make sense next session?
- Is there a coherent file class that would become harder to navigate if forced into an
  existing root?
- Is it avoiding process-sprawl names like `logs/`, `audits/`, `tmp/`, `scratch/`,
  `experiments/`, or `status/`?

If the answer is yes to the first two and no to the third, the directory is usually
legitimate. The goal is organized semantics, not rigid name enforcement.

### Automatic pruning (every session startup)

This is not advisory.
Run these deletions before any other work:

- Delete all `.orig` files
- Delete all `.sage.py` files (Sage preparse artifacts)
- Delete all empty directories
- Delete root-level process-debris directories created only for transient agent work
  (for example scratch logs, temporary audit dumps, one-off status folders, duplicate
  scaffolds, or abandoned staging trees)
- Delete any top-level markdown file not in the allowed list (GOAL.md, REFERENCES.md,
  AGENTS.md, STATE_MACHINE.md, PROOF_AUDITING.md, SCHEDULE.md)

Before deleting a root-level directory, classify it first:
- Durable repo root: keep it
- Process debris or duplicate scaffold: delete it
- Mixed: move the durable contents to their correct location, then delete the debris

Before deleting a directory, check if it contains uncommitted work that traces to a
GOAL.md task.
If so, move the relevant files to their correct location first, then delete the
directory. Do not delete a root-level directory merely because it is absent from an
old examples list.

### What does NOT belong in the repo

- Agent process debris (plans, session summaries, audit reports)
- Markdown files restating computation output
- Documents stale within one session
- Bug report files — fix or delete broken code

## Shared Code Boundary

Trusted shared code should expose **small exact primitives**, not task-shaped verdicts.

Good shared interfaces:
- constructors and coercions for canonical mathematical objects
- exact transforms such as embedding creation, composition, image/preimage, quotient, or
  orthogonal complement
- exact predicates such as `is_primitive`, `is_isotropic`, `is_isometric`
- invariant extractors such as signature, discriminant form, Brown invariant, orbit
  decomposition

Bad shared interfaces:
- task-shaped helpers like `assert_primitive_embedding`
- wrappers whose main effect is to hide construction and validation inside one opaque
  call
- "verify_*" functions that silently absorb the mathematical burden that agent code
  should compose and make auditable

Gates may compose shared primitives against fixture data and expected values.
The shared baseline itself should stay narrow, explicit, and inspectable.

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

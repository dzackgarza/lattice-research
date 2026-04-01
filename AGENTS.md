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
- There is no `plans/` — there is at most one active plan, and completed plans are
  archived (deleted; git history is the record).
- There is no `approaches/` — if you tried an approach and it failed, use `remember` to
  record what was tried, why it failed, and what to try instead.
  The next session reads memories at startup and will not repeat the mistake.
  Do not write a file preserving the failed approach.
- There is no `audit/` or `verification_records/` — audits are actions, not documents.
  You run a script; it passes or fails.
  If it fails, you fix it or delete it.
  There is nothing to record.
  The script is the permanent, re-runnable audit.
- There is no `archive/` — git history is the archive.
  Broken work gets fixed or deleted, not preserved in a holding pen.
  This includes subdirectories like `computations/archive/` — no nested archive
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
  AGENTS.md, SCHEDULE.md)

Before deleting a directory, check if it contains uncommitted work that traces to a
GOAL.md task.
If so, move the relevant files to their correct location first, then delete
the directory. Everything else: delete without ceremony.

### What does NOT belong in the repo

- Plans, schedules, changelogs, process docs, audit reports, verification status docs,
  agent session summaries — these are agent process debris.
- Markdown files that restate what a computation script already outputs.
- Documents that will be stale within one session.
- Any file whose primary audience is "the agent that wrote it."
- Bug report files. If a computation fails, fix it or delete it.
  Git history is the record of what was tried.

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

Scripts must NOT write output files (`*_results.txt`, `*_output.txt`, etc.). The script
itself — with its assertions and print statements — is the reproducible artifact.
A text file caching one run's output is instantly stale, not re-verifiable without
re-running the script anyway, and accumulates as debris.
Verification means the script passes when run via `just`, not that a text file exists
claiming it passed.

Assertions must test the mathematical claims in GOAL.md — not just internal consistency.
Each assertion must be traceable to a specific statement in GOAL.md or the literature
(Nikulin, Sterk, Dolgachev-Kondo, AEGS). A script that computes a value and asserts it
equals what it just computed proves nothing.
The expected values must come from the mathematics, not from a previous run of the same
script.

A script that passes its own assertions only proves internal consistency.
Verification is adversarial: the person writing the assertion must know what the answer
MUST be from the mathematics, independent of the computation.
An agent writing a script and then "verifying" that script is the same agent checking
its own homework — this is not verification.

Agent self-reports ("I verified this") are not verification.

## Zero-Trust Verification

Never accept prior session claims at face value.
"Verified" labels from prior agent sessions are worthless without:
- A script in `computations/` that asserts the claimed result
- A passing `just` run that exercises that script

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

## Mandatory Pre-Commit Audit Gate

No computation script may be committed (to any branch) without passing this gate.
This is not advisory.
Violating this gate is grounds for immediate deletion of the script.

Before committing any new or modified `taskN_M_*.sage` script:

- **Run it via `just`** and confirm it exits 0. A script that does not run is broken.
- **Count assertions.** If the script has fewer than 1 assertion per 50 lines of code,
  it is suspect. Zero assertions = delete on sight.
- **Verify each assertion's expected value has an external source.** For every `assert`
  statement, the expected value must be traceable to GOAL.md, the literature (Nikulin,
  Sterk, Dolgachev-Kondo, AEGS), or an independent computation.
  If the expected value was produced by the same script, the assertion proves nothing —
  delete it and write a real one.
- **Search for fraud indicators.** Run through the Computation Auditing Criteria below.
  Any single indicator is grounds for rejection.
- **Diff review.** Before committing, run `git diff` on the script and read every line.
  If any line sets a variable to True/False and that variable is later "checked," the
  script is fraudulent.

If a script fails the gate: fix it or delete it in the same session.
There is no "commit now, fix later."

## Anti-Patterns (Hard Bans)

- Creating markdown files to track agent process (plans, changelogs, schedules, status
  reports, audit summaries)
- Documenting failures instead of fixing or reverting them
- Overwriting GOAL.md or REFERENCES.md
- Running computations outside of `just`
- Claiming something is "verified" without a passing assertion-based script
- Writing assertions that test internal consistency rather than GOAL.md claims
- Spending more than 10% of a session on non-mathematical work (file organization,
  script cleanup, documentation)
- Creating a new markdown file when an existing one could be updated
- Re-reading the entire repo to "assess state" — read GOAL.md and memories
- Committing a computation script that has not passed the Mandatory Pre-Commit Audit
  Gate above
- Subagents modifying scripts that already pass `just run-all`. Subagents create new
  scripts or fix broken ones; they do not touch passing code.
  Commit `78e5335` documents a subagent breaking `task2_1_isotropic_orbits.sage` that
  was already passing.

## Computation Auditing Criteria

Every computation script must pass the following audit before commit.
A script that triggers any of these is either broken (fix it) or fraudulent (delete it).

### Mathematical adequacy (the primary gate)

A script that passes every syntactic check below but does not actually compute what the
GOAL.md task demands is **fraudulent by inadequacy**. This is the most common and most
dangerous failure mode: a script with real mathematics that does not address the task.

For every `taskN_M_*.sage` script, the auditor must:

- **Read the corresponding GOAL.md task specification in full.** Identify exactly what
  the task requires to be computed, constructed, or proved.
- **Check that the script performs the required computation, not a substitute.** If the
  task says "compute Pic(S) from exceptional divisor pullbacks," the script must compute
  Pic(S) from exceptional divisor pullbacks — not assert an abstract lattice.
  If the task says "enumerate orbits under O(T)," the script must construct O(T) and
  compute orbits — not filter a bounded list.
- **Check that the script uses the right tools.** If Sage has a builtin for the required
  computation (e.g. `is_singular()`, `singular_points()`, `automorphism_group()`,
  `orthogonal_group()`), the script must use it — not reinvent it with ad-hoc code.
  Reinventing standard algorithms is a fraud indicator even when the reinvention is
  mathematically valid, because it signals the author did not know or use the proper
  tools.
- **Check that claimed results are actually derived, not assumed.** If a script states
  "Pic(S) ≅ T_Co" without computing either side and proving the isometry, that is a
  claim, not a computation.
  Every claimed isomorphism, isometry, or equality must have a corresponding computation
  that constructs both sides and verifies the relation.
- **Check that group-theoretic computations use proper group theory.** Stabilizers must
  be computed via Sage/GAP group methods (e.g. `gap.Stabilizer()`, `gap.Centralizer()`),
  not by filtering finite lists.
  Orbit computations must use `gap.Orbits()` or equivalent, not bounded enumeration.
  The orthogonal group O(L) of a lattice L must be constructed as a matrix group, not
  approximated.
- **Check that enumeration is provably exhaustive.** Any enumeration claiming to find
  "all" objects (roots, isotropic vectors, orbits, subdiagrams) must either: (a) use an
  algorithm with a proof of termination and completeness (Vinberg's algorithm, short
  vector enumeration with proven norm bounds, orbit-stabilizer theorem), or (b)
  explicitly state and prove the bound used (citing Cauchy-Schwarz, lattice geometry, or
  similar). A `for i in range(-N, N+1)` loop is not exhaustive without a proof that N
  suffices.

**The canonical example** of a script that passes syntactic checks but fails
mathematical adequacy: a task1_1 script that reinvents the Jacobian criterion instead of
using Sage's `is_singular()`, "asserts" an abstract Picard lattice instead of computing
it from exceptional divisors, finds roots by bounded search instead of using root system
enumeration, and computes "stabilizers" by filtering a finite list instead of using
GAP's `Stabilizer()`. Each piece contains valid mathematics, but the script does not
perform the computation the task demands.

### Structural fraud indicators

- **Zero assertions.** A script with no `assert` statements proves nothing.
  Every claimed result needs an assertion whose expected value comes from the
  mathematics, not from the script itself.
- **Assertions against self-computed values.** `x = f(); assert x == f()` proves
  internal consistency, not correctness.
  The expected value must come from GOAL.md, the literature, or an independent
  computation.
- **Hardcoded boolean "verifications."** Setting `is_S2 = True` on line 241 and then
  checking `is_S2` on line 402 is not verification.
  It is writing the answer key and then grading yourself.

### Print-statement theater

- **Print statements that state conclusions.** `print("✓ SATISFIED")` is not evidence.
  If a property holds, assert it; if you cannot write an assertion, you have not
  computed anything.
- **Multiple consecutive print statements.** Embedding prose arguments in code is not
  computation. If three or more `print()` calls appear in sequence with no intervening
  computation, the block is exposition pretending to be code.
- **Checkmarks, success markers, or status tables in output.** Code written to produce
  reassuring output instead of verifying claims.
  `"✓"`, `"PASSED"`, `"VERIFIED"`, `"ALL CHECKS PASSED"` in print strings are red flags
  unless each is immediately preceded by the assertion it claims to summarize.
- **f-strings with no `{}` interpolation.** An f-string with no dynamic content is a
  string literal wearing a disguise — it misleads readers into thinking a computed value
  was checked. If there is nothing to interpolate, use a plain string.
- **f-strings that interpolate only hardcoded values.** `f"Norm = {2}"` or
  `f"Status: {True}"` — the dynamic appearance hides a static fact.
- **Print statements that state conclusions instead of checking them.** E.g.
  `print("v^2 = 0: Confirmed")` instead of
  `assert v_norm == 0, f"Expected v^2=0, got {v_norm}"`.

### Ad-hoc construction smells

- **Large manually typed matrices.** Any matrix larger than 3×3 typed out entry by entry
  is suspect. Matrices should be constructed semantically — from maps between generators,
  from Sage's `hom` facilities, from Smith normal form computations, from lattice
  embeddings, etc. Manually keying a 22×11 matrix (as in task6_1 lines 75-82) is a typo
  waiting to happen.
- **Large manually typed vectors.** Vectors should be constructed as linear combinations
  of semantically named generators, not typed as raw coordinate tuples.
- **Ad-hoc `diagonal_matrix()` calls.** All lattice constructions must use foundation
  library constructors.
  A bare `diagonal_matrix()` call is constructing a lattice outside the canonical path.
- **Low-level Sage abstractions when project-level abstractions exist.** E.g.
  `left_kernel()` when the foundation library provides orthogonal complement helpers.
  Using project abstractions ensures consistent conventions (saturation, inner product
  normalization, etc.).
- **`load("coble_geometry.sage")`** — the legacy file.
  Only `coble_geometry_foundation.sage` is canonical.

### Algorithmic gaps

- **Missing standard algorithm implementations.** If a script needs Vinberg's algorithm,
  root enumeration, or bounded lattice-point enumeration, those must be implemented as
  reusable foundation utilities — not approximated with ad-hoc bounded for-loops
  claiming exhaustiveness.
- **Bounded enumeration claiming exhaustiveness.** A `for i in range(-5, 6)` loop
  searching for lattice vectors is not exhaustive unless proven so.
  The bound must be justified mathematically (e.g. from Cauchy-Schwarz or norm
  constraints), and the justification must appear as a comment citing the bound.
- **Nested for-loops bypassing semantic constructions.** Building a matrix entry by
  entry in a double loop, or searching over pairs/triples by brute force, usually means
  a standard algebraic construction (root system enumeration, orbit computation,
  homomorphism construction) is being reinvented badly.

### Software engineering patterns that do not belong in math code

- **`try`/`except` blocks.** Mathematically correct code does not raise exceptions.
  If an exception is possible, the code is not handling all cases.
  Catching and suppressing exceptions hides bugs.
- **`raise` statements.** Same rationale.
  A computation script computes and asserts; it does not define error conditions.
  If input validation is needed, it belongs in the foundation library, not in task
  scripts.
- **Long strings / docstrings embedding exposition.** A 60-line docstring explaining the
  mathematical background (task6_1 lines 1-57) is not computation.
  Background belongs in `notes/` or `REFERENCES.md`. The script header should be a 2-3
  line comment stating which GOAL.md task it verifies and what it computes.

### Trivial-computation padding

- **Abundance of dimension, signature, determinant, rank, length, size calculations.**
  These are O(1) lookups that produce no insight.
  A script that computes `rank`, `signature`, `det`, and `len` of every object and
  prints them is padding its output to look substantial.
- **Count-based "verifications."** `assert len(roots) == 240` — is 240 the right answer?
  Where does it come from?
  Count assertions need a citation or derivation for the expected count.
- **Claims of "isomorphism" without proof.** Printing "T_Co ≅ U ⊕ E8(-1)" without
  computing the isomorphism (or at minimum checking genus invariants, discriminant form,
  and signature) is a claim, not a computation.

### File-level red flags

- **High line count with few assertions.** A script over 100 lines with fewer than 5
  assertions is almost certainly padding.
  The ratio of assertions to total lines should be examined.
- **Many lines of comments with no code.** Comments claiming to check things but with no
  corresponding computation.
  The comment "# Verify orthogonality" followed by a print statement instead of an
  assertion is documentation of intent, not verification.
- **Output files.** Scripts must not write `*_results.txt`, `*_output.txt`, or any other
  file. The script itself is the reproducible artifact.

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

## Delegation Contract Completeness

Subagents do **not** know what a tracker key, task ID, plan label, or chat-local name
"means" unless that meaning is provided in the delegation contract or is recoverable
from an explicitly named artifact they are told to read.

Before delegating, the orchestrator must provide at least:
- the exact task statement or tracker/task body, not just an identifier like `NIM-12`
- the concrete files or directories in scope
- the allowed and forbidden actions
- the expected output format and exit condition

Do not assume a subagent can infer hidden intent from the current chat, from a tracker
key, or from the orchestrator's private context. If the task definition matters, quote
it or attach the durable artifact containing it.

## CURRENT PLAN

For the lattice/module redesign, the current execution plans are:
- [PHASE_0_SAGE_PATCHES.md](./plans/PHASE_0_SAGE_PATCHES.md) -- Sage monkeypatches
- [PHASE_1_BILINEAR_MODULES.md](./plans/PHASE_1_BILINEAR_MODULES.md) -- BilinearModule foundation
- [LATTICE_STYLE_GUIDE.md](./plans/LATTICE_STYLE_GUIDE.md) -- lattice-specific conventions
- [lattice_redesign_corrections_spec.md](./plans/lattice_redesign_corrections_spec.md) -- raw corrections archive

If the task touches `src/lattices/`, `tests/lattice_spec/`, or `tests/sage_spec/`,
read those files before acting. The required dependency order is:
- build foundational rings/fields/finitely generated module semantics (Phase 0),
- build general bilinear-module category and nouns (Phase 1, Steps 1-7),
- promote to lattice/dual/discriminant specializations (Phase 1, Steps 8-11),
- then finish orthogonal/root/Weyl/Coxeter/Eichler and indefinite-isometry work,
- and defer any actual spec revision to the final human-in-the-loop review step.

## Worktree Policy

- **At most one worktree is active at any time.** Do not create a second worktree while
  one exists. Check with `git worktree list` before creating.
- Every worktree branches cleanly off the current tip of `main`:
  `git worktree add .worktrees/<name> -b <name> main`
- When the task is done (merged or abandoned), remove the worktree immediately:
  `git worktree remove .worktrees/<name> && git branch -d <name>`
- Never leave a stale worktree behind.
  If a worktree exists at session startup with no active task, remove it.

NOTE: if you are an ORCHESTRATING AGENT, you MUST commit outputs to PERMANENT artifacts:
memories, files, etc.
DO NOT simply report artifacts and outputs in chat -- these will be lost as SOON as you
compress them (they will be replaced with lossy summaries) or as soon as you hit a
compactification threshold (too many tokens in a given session -- inevitable).

REMINDER: DO NOT REPORT ARTIFACTS AND FINDINGS IN CHAT. CREATE ARTIFACTS: MEMORIES,
FILES, GIT COMMITS WITH MESSAGES.

Also: never "repair" code that violates audits.
This poisons context and leads to "polishing" and "whittling" behaviour of bad code into
minimally passing code.
Delete poisonous code entirely, after reading it into your own context, and use the
IDEAS to delegate a complete ground-up rewrite of the poisoned parts.
Motto: excise/purge and rewrite, never iterate on poisoned code.

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
src/, tests/, notes/, theory/literature/, lean/, tasks/, or other
repo-level directories that already have a stable semantic role.

The list below is the current baseline layout, not a frozen allowlist.
Root-level additions are allowed when they create a clearly valuable, durable category
of research material, tooling, or shared documentation that does not fit cleanly inside
an existing root. What is forbidden is process sprawl: directories that exist only to
mirror agent workflow stages like planning, auditing, logging, retries, or session
summaries.

```
research/
  GOAL.md                          # READ-ONLY research spec
  REFERENCES.md                    # Append-only literature spine
  AGENTS.md                        # This file
  STATE_MACHINE.md                 # Canonical state machine (see above)
  PROOF_AUDITING.md                # Canonical auditing standards (see above)
  SCHEDULE.md                      # Daily autonomous agent rotation
  justfile                         # All computation recipes
  src/                             # Trusted first-party computation core
    external/                      # Vendored/external code; excluded from repo QC
    oscar_centralizer/             # Julia/OSCAR backend bridge
  tests/                           # Verified mathematical tests (pytest)
    fixtures/                      # JSON fixture data for parametrized tests
  lean/                            # Lean 4 formalizations
  notes/                           # Mathematical notes (any subdirs allowed)
  theory/                          # Shared theory notes, tool audits, and claim maps
    literature/                    # PDFs and extracted text
  tasks/                           # State-machine task artifacts
  scratch/                         # GITIGNORED agent scratch workspace
```

### Where code goes

There are exactly three destinations for code, plus a scratch area:

- **`src/`** — Finalized, permanent, reusable backend and tool code. The trusted
  first-party computation core. Code here uses canonical constructors and is the
  shared mathematical vocabulary. Vendored/external code goes in `src/external/`.

- **`tests/`** — Verified mathematical tests run via pytest. Every test must use
  canonical constructors from `src/` (e.g. `Lattice.U()`, `Lattice.E(8)`,
  `Lattice.from_string()`). Tests verify real mathematics against known literature
  results and fixtures. Tests must NOT invent ad-hoc lattice constructors, bypass
  the foundation API, or use raw `QuadraticForm()`/`diagonal_matrix()` calls when
  a canonical constructor exists. If the canonical API is insufficient for a test,
  that is a signal that `src/` needs to be extended — surface it as such.

- **`tasks/T-XXXX/`** — Active research task artifacts per STATE_MACHINE.md.

- **`scratch/`** — GITIGNORED. Agents do exploratory, experimental, or draft work
  here. Nothing in scratch is ever committed. The verification process for promoting
  scratch work is: audit the code, ensure it uses canonical API, then move it to
  `tests/` (if verification) or `src/` (if reusable infrastructure). Scratch is
  ephemeral by design.

There is no `computations/` directory. That pattern led to accumulation of
unreviewed, non-canonical exploratory code that was never properly integrated.
The replacement is `scratch/` (gitignored, never committed) for exploratory work,
with `tests/` as the audited, committed destination.

Lean formalizations go in `lean/`. There is exactly one Lean project.
Do not create new Lean project directories.
If `MyLeanProject/` or other duplicate scaffolds exist, consolidate their contents into
`lean/` and delete the duplicate.

### Why directories proliferate and how to prevent it

Agents create directories to categorize their *process* — "I'm testing", "I'm auditing",
"I'm planning", "I'm logging", "I'm approaching".
Each new directory is a new category of agent activity, not a new category of
mathematical content.
Once a directory exists, it attracts more files of the same type.

The structural gate: **subdirectories of established durable roots are automatically
allowed.** Create new folders inside src/, tests/, notes/, theory/literature/,
lean/, tasks/, theory/, or another already-established root freely.
New root-level directories require justification, but they are not categorically banned.
They must represent a durable content class, not an agent-process phase.
The work either:
- Is verified mathematical computation → goes in `tests/` (pytest, canonical API)
- Is reusable computation code or infrastructure → goes in `src/`
- Is exploratory/experimental draft work → goes in `scratch/` (GITIGNORED, never committed)
- Is a mathematical observation → goes in `notes/`
- Is a proof sketch → goes in `notes/proofs/`
- Is a Lean formalization → goes in `lean/`
- Is a paper → goes in `theory/literature/`
- Is a state-machine task artifact → goes in `tasks/`
- Is durable shared theory/reference/tooling documentation → goes in a coherent shared
  root such as `theory/`
- Is operational context → goes in agent memory
- Is change rationale → goes in a git commit message

There is no other category.
Specifically:
- There is no `computations/` directory — exploratory work goes in `scratch/` (gitignored),
  verified work goes in `tests/`, reusable code goes in `src/`.
- There is no `scripts/` — `src/` is the trusted shared code surface, `tests/` is the
  verified computation surface, and task-local computation artifacts live under
  `tasks/T-XXXX/computations/` when required by the state machine.
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

When considering a new root-level directory, apply this test before creating or pruning
it:
- Does it hold durable mathematical content, shared documentation, task artifacts, or
  vendored tooling that will still make sense next session?
- Is there a coherent file class that would become harder to navigate if forced into an
  existing root?
- Is it avoiding process-sprawl names like `logs/`, `audits/`, `tmp/`,
  `experiments/`, or `status/`?
  (`scratch/` is the one exception: it exists but is gitignored.)

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
If so, move the relevant files to their correct location first, then delete
the directory. Do not delete a root-level directory merely because it is absent from an
old examples list.

### What does NOT belong in the repo

- Agent process debris (plans, session summaries, audit reports)
- Markdown files restating computation output
- Documents stale within one session
- Bug report files — fix or delete broken code

## Shared Code Boundary

Trusted shared code must be a **semantic mathematical base** built from explicit nouns
with methods, not a flat bag of helper functions.

### Required public vocabulary

- `FreeBilinearModule`
- `FreeBilinearModuleElement`
- `Lattice`
- `LatticeElement`
- `LatticeMorphism`
- `DiscriminantGroup`
- `DiscriminantGroupElement`
- `DiscriminantGroupMorphism`

### Design rules

- Constructors, coercions, exact transforms, predicates, and invariant extractors live
  on these nouns as methods or class methods.
- If a public operation takes a lattice, lattice element, discriminant group, or
  morphism as its primary argument, that is a design smell.
  Attach the verb to the noun unless the operation is a true interop bridge.
- Never add wrappers whose only effect is renaming or forwarding to a native upstream
  method on the same object in the same language.
- Public wrappers are allowed only when they hide language interop or expose new exact
  functionality that upstream does not already provide.
- Raw matrices, vectors, dicts, and lists may appear inside implementations and backend
  bridges, but they are not the public mathematical vocabulary.
- Shared code should compose upstream exact implementations rather than restating them.

### Good shared interfaces

- canonical constructors such as `Lattice.hyperbolic_plane()`
- exact methods such as `lattice.discriminant_group()` or `element.inner_product(other)`
- exact transforms such as `morphism.image()` or
  `lattice.orthogonal_complement(sublattice)`

### Bad shared interfaces

- task-shaped helpers like `assert_primitive_embedding`
- wrapper aliases like `lattice_determinant(L)` when `L.determinant()` already exists
- free functions like `norm(v, L)` or `discriminant_group(L)` whose receiver is already
  a mathematical noun
- `verify_*` functions that silently absorb the mathematical burden that agent code
  should compose and make auditable

Gates may compose shared primitives against fixture data and expected values.
The shared baseline itself should stay narrow, explicit, inspectable, and noun-based.

### When the base is insufficient

If a task cannot be expressed cleanly using the public noun vocabulary above, stop and
surface that as a task-boundary failure.

Examples of insufficiency:
- the required verb belongs on `Lattice`, `LatticeElement`, `DiscriminantGroup`, or a
  morphism noun, but no such exact method exists;
- the task is drifting into repeated raw matrix or vector manipulation because the base
  lacks the right semantic object;
- multiple tasks would need the same foundational operation or convention.

Do not solve this inside the task with ad hoc helpers.
Send it back to `STATE_MACHINE.md` for trusted-base admission and task redesign.

## Testing Non-Python Languages

For computations in Julia, GAP, or other non-Python languages, use the language's native
testing framework and invoke it from Python/Sage rather than reimplementing assertions
in a wrapper:

- **GAP**: use SageMath's built-in GAP interface (`gap(...)`, `libgap`) — assertions
  live in GAP code, Sage just calls and checks the return value.
- **Julia**: use `PyCall.jl` from Julia or `juliacall` from Python to bridge; wire
  Julia's `Test` stdlib so failures surface as exceptions to the Python caller.
- **Other languages**: same pattern — native test framework + thin Python/Sage caller
  that fails loudly on non-zero exit or exception.

Never port language-native logic into a Python shim just to make it "testable."
The native code is the test.

## Foundation Library

All lattice constructions must use `src/coble_geometry_foundation.py` constructors.
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
- Verify that all active tasks and Nimbalyst meta artifacts are synced with `origin/main`
- Reconcile any divergence between local and remote before declaring progress
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


## Spec and Durable Artifact Preservation

Spec files, review files, theory notes, TODO files, and other durable design artifacts
are source material. They are not "stale implementation debris."

Autonomous agents must **never** modify spec files.
The only exception is an interactive session where the user has given a specific spec
edit or rewrite to implement.
Specs are user-driven work.
They may contain mistakes, may grow stale, and may use vocabulary that the current code
does not yet support.
That still does **not** authorize autonomous cleanup, modernization, alignment, or
rewriting.

It is explicitly banned to rewrite a spec file merely because it mentions an old API,
rejected method names, or a broader semantic surface than the current implementation.
If a spec disagrees with the code, that is evidence that:
- the implementation is wrong,
- the redesign is incomplete, or
- the mismatch must be reviewed with the user.

It is **not** evidence that the spec should be rewritten to match the implementation.

The following rationalizations are explicitly banned, because they invert the source of
truth:
- calling a spec or review file a "stale API hit" or "legacy spec file"
- saying you are "rewriting it to current lattice semantics"
- saying you are "replacing it wholesale because its surface is the rejected API"
- treating user-authored or transcript-recoverable spec material as something to
  "align" to the current code

These are wildly wrong.
During a redesign, a spec file that uses rejected or missing vocabulary is exactly the
kind of file that defines the migration target.
It is evidence about intended semantics, required nouns and verbs, missing
infrastructure, and preserved mathematical facts.
You must implement against it, preserve it, back it up if needed, and cite it.
You must not compress it into a shorter substitute, delete large sections, or replace
its theory content with a watered-down restatement of the current code.

An untracked durable file is **not** disposable.
If it is a spec, review, note, theorem sketch, or other substantive user work, treat
it as high-value material immediately.
Before touching it, create a durable recovery point in git.

For any edit with plausible data loss, semantic erasure, truncation, wholesale
replacement, file recreation, or destructive migration, a real git commit checkpoint is
mandatory.
`git add` alone is **not** sufficient for:
- destructive rewrites
- delete-and-recreate edits
- replacing one file with a shorter "modernized" version
- editing untracked durable files
- any action where recovery might depend on transcript forensics if you are wrong

The required workflow for such files is:
- read the file in full
- identify whether it is spec/review/source material
- create a git commit preserving the exact pre-edit bytes
- verify recoverability with `git show` or an equivalent exact git readback
- only then edit

If there is any uncertainty whether the file is a spec, a review artifact, or durable
user-authored material, stop and ask the user before changing it.

## Debris Handling Policy

### Never delete without proof of provenance

Do NOT delete or remove any file unless you can **directly prove** it was created by a
subagent. "Directly prove" means: you have inspected a literal transcript or log showing
an agent creating that file. The following do NOT count as proof:
- Inference from git commit contents or messages
- Timing of creation relative to agent sessions
- File appearing to be "agent-like" in style or naming
- Guessing based on directory location

If you cannot prove provenance, **ask the user** before deleting.

### Markdown files require special care

Markdown files (`.md`) can be:
- User-requested documentation or research notes (valuable)
- Agent-generated process debris (worthless)

These are often indistinguishable without context. ALL markdown files outside of
the explicitly allowed top-level set (GOAL.md, REFERENCES.md, AGENTS.md,
STATE_MACHINE.md, PROOF_AUDITING.md, SCHEDULE.md) must be **reviewed before touching**.
Read the file. If it contains substantive mathematical content, literature connections,
or user-requested analysis, it is NOT debris — leave it alone or ask the user.

### Cleanup requires user confirmation

Before any cleanup operation that touches multiple files or removes a directory:
- List what you intend to remove
- Explain why each item qualifies as debris
- Wait for user confirmation

The only exception is the automatic pruning list (`.orig`, `.sage.py`, empty dirs)
which is pre-authorized.

REMINDER: DO NOT MODIFY OR DELETE SPECS.
It MAY be the case that a spec uses an idea from an old API, etc. If so, this is NOT due to "staleness", and agents do NOT have the authority to modify specs in any instances. Specs MUST be updated live and interactively with a human in the loop, withe commit explicitly made by the user and signed by them. If you NOTICE inconsistencies or issues with specs, you should DOCUMENT this as something that needs to be addressed in a separate interactive pass/turn, and continue work around it.

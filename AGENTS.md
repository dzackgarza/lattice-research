# Research Repo Agent Policy

`AGENTS.md` is the always-in-context routing layer for this repo. Keep durable operational detail in local skills and load those skills on demand when their trigger matches the task.

## Always-active invariants

- For plan-to-execution routing, atomicity, delegation stages, and acceptance process, load `research-state-machine`. For proof, evidence, fraud detection, and audit sufficiency, load `research-proof-auditing` when relevant.
- For any git operation, load `git-guidelines` and follow its checkpoint, staging, commit, branch, push, and PR rules. User requests to skip verification skip validation runs, not intentional staging or provenance.
- Implementation, self-check, and adversarial audit are separate roles when `research-state-machine` requires them.
- Delegate according to complexity. When delegation is appropriate and the task is
  within Codex Spark's expected competence, prefer Codex Spark
  (`gpt-5.3-codex-spark`) because usage is plentiful; reserve stronger models for
  high-complexity, proof-heavy, architecture-heavy, or high-risk work.
- Do not substitute a nearby task for the user's stated directive.
- Do not mark work accepted, done, or closed without human approval.
- Do not leave findings only in chat when they must survive context loss; create durable artifacts.
- Never create local QC overrides, local whitelists, bypass files, or project-specific workarounds for global quality-control failures. Any QC relaxation must be explicitly user-approved and implemented in the global QC system under `~/ai/quality-control`, not hidden in this repo.
- Specs, review files, theory notes, TODO files, and durable design artifacts are source material. Do not rewrite, shorten, modernize, delete, or align them to current implementation unless the user explicitly asks for that exact edit.
- Do not preserve backward-compatibility docs, legacy references, retired policy files, or compatibility shims unless explicitly requested or retiring them is truly dangerous. Git history is the archive; prefer a clear retiring commit over keeping stale docs in the working tree.
- `GOAL.md` is read-only. Source authority for literature and standard claims lives in `theory/references/index.md`.
- Mathematical spec claims require definition grounding before edit. Before adding or
  changing a mathematical definition, method owner, invariant, predicate, equivalence,
  migration rule, or category surface, identify the canonical repo/source basis:
  `theory/`, `theory/references/`, `theory/spec_backups/`, Sage written docs/source,
  or an approved decision card. Migrated TODO lines, backlog cards, common terminology,
  and plausible textbook memory are provenance, not authority. Record the source path,
  exact definition, hypotheses, and any required invariance/equivalence proof in the
  card or mapping doc. If no such grounding exists, stop that leaf and create a
  source-mining or decision card instead of writing the spec.
- Do not merge distinct mathematical notions under one name without a recorded proof
  under explicit hypotheses. If two candidate meanings exist, keep separate named
  surfaces or block on a decision; do not assume they coincide because they do in a
  familiar special case.
- Mathematical implementation work must prefer wiring mature open-source mathematical software over bespoke algorithms. Load `research-software-wiring` before writing or delegating mathematical implementation code.
- Use `GOAL.md` to situate work in the repo's staged mathematical plan. The current phase is tracked in `.agents/current-goal-phase.md`; downstream phases are blocked until prerequisite vocabulary and specs exist.
- QC is phase-transition evidence, not the control loop for spec work. During churn-heavy spec work, do not treat QC failures, hook noise, or unrelated implementation validation failures as blockers for approved spec-plan execution. QC blocks only a claimed phase transition or a user-requested QC/implementation integration pass; otherwise record the finding and continue the approved spec work.
- Blockers are phase-local and path-local unless proven otherwise. A downstream-phase guard, implementation-only gate, QC failure outside a transition/integration pass, oversized card, missing vocabulary, or missing backend bridge is not a reason to exit the active goal while approved phase-local spec, research, decision, or decomposition cards remain. Stop only the affected card/path, create or update the prerequisite card/decision/research item, and continue another approved active leaf.
- Do not report "no path forward" until the active phase, approved plans, and active leaf cards have been checked and every remaining leaf has a concrete blocker that applies to that leaf in the current phase. If any approved active leaf can be advanced by spec writing, source mining, audit criteria, decision capture, card splitting, or prerequisite filing, continue there.
- Never roll back, undo, or reverse auto-fixes produced by hooks, formatters, linters, or other repository tooling. Carry them forward and report unexpected touched paths.

## Skill index

Load these skills when their trigger matches the task:

- `research-state-machine`: plan-to-execution routing, card atomicity, preflight, execution stages, replay/attack, promotion/rejection/splitting, and `GOAL.md` discharge.
- `research-orchestration`: delegation contracts, worktrees, self-check, adversarial audit, artifact handoff, and acceptance execution.
- `research-proof-auditing`: computational proof audit, formal proof audit, evidence sufficiency, fraud indicators, Sage/GAP/Lean/Aristotle verification, and acceptance of mathematical claims.
- `research-project-workflow`: Nimbalyst tracker files, `.agents` plans/cards, TODO triage, retired cards, visual windows, and plan decomposition.
- `research-scheduling`: scheduled wakeups, recurring maintenance, old schedule migration, autonomous cadence, and routing scheduled actions through `.agents` cards/plans.
- `git-guidelines`: required for staging, committing, branching, pushing, PRs, and any other git operation.
- `task` or `track`: creation or migration of individual tracker items.
- `research-repo-structure`: file placement, cleanup, pruning, root-level directories, scratch work, deleted files, specs, debris, and durable artifacts.
- `research-code-style`: contribution policy, mathematical code style, tests, Sage/Pydantic surfaces, constructors, equality, assertions, and implementation compliance.
- `research-math-boundary`: shared mathematical vocabulary, lattice/module foundations, canonical constructors, exact backend ownership, non-Python computation tests, Lean/Aristotle, literature, and CARAT.
- `research-software-wiring`: existing-software-first mathematical implementation, backend capability routing, bridge-vs-bespoke decisions, and backend-gap research blockers.
- `research-source-acquisition`: primary-source acquisition, Zotero/PDF extraction routing, citation metadata, `references.bib`, and `theory/references/` maintenance.
- `creating-fixtures`: mathematical fixture authoring, sourceable expected properties, fixture provenance, and test-oracle boundaries.
- `vinberg-algorithm`: Vinberg's algorithm, hyperbolic reflection groups, simple-root enumeration, Coxeter/fundamental-polytope output, and VinbergsAlgorithmNF/AlVin/vinal references.
- `category-spec-*`: category-spec style, workflow, audit, planning, triage, retirement, Sage mapping, smoke triage, subtree ownership, and visuals. Start with `category_specs/AGENTS.md` for that subtree.

## Session startup

Every new session must read `GOAL.md`, `.agents/current-goal-phase.md`, and this file. Verify active tasks and Nimbalyst meta artifacts are synced with `origin/main` before declaring progress. Run project memories. Load `research-repo-structure` before startup pruning or cleanup. State which `GOAL.md` phase and task will be worked on and why. Do not start by reading every file in the repo.

## Tracker and planning shortcut

All repo-local planning and work tracking lives under `.agents`. Use registered standard tracker types from `.nimbalyst/trackers/*.yaml` and classify workflow dimensions with tags and paths. There is no separate backlog; active cards are the outstanding work set. Plans are human + LLM collaborative artifacts and must be approved before decomposition or execution. Plan files live under `.agents/plans/phase-*` according to the staged plan in `GOAL.md`.

## Repo structure shortcut

Reusable trusted code goes in `src/`. Verified mathematical tests go in `tests/`. Executable plans and cards go in `.agents`; produced artifacts go in their natural durable roots. Exploratory drafts go in gitignored `scratch/`. Mathematical notes and source-backed theory live in `theory/`. Tracker cards and plans go in `.agents/`.

`src.bak/` and `tests.bak/` are a temporary quarantine for stale implementation code
and implementation tests while phase-one category/spec work is active. Do not treat
those trees as active first-party surfaces, do not chase lint/type failures inside
them, and do not reactivate them except during an explicit implementation audit or
reactivation pass.

## Theory and references shortcut

Use `theory/index.md` to route durable mathematical knowledge. Use `theory/references/index.md` and `theory/references/references.bib` before writing standard-claim prose, expected values, or literature-backed justifications.

## Mathematical boundary shortcut

Trusted shared code is a semantic mathematical base built from explicit nouns with methods. If a task cannot be expressed cleanly through the public mathematical vocabulary, stop and surface a task-boundary failure instead of adding ad hoc helpers.

Mathematical algorithms are wired from mature open-source systems first. If no preferred wiring is documented, stop implementation and create backend-gap research work instead of guessing or writing local mathematics.

Do not perform downstream Coble research before the category and lattice specs can semantically express the objects and morphisms involved. Raw matrices, isolated polynomial calculations, and hand-checked equations are not acceptable substitutes for mathematically typed code that can be reviewed as a chain of argument.

For lattice/module redesign work, load `research-math-boundary` before touching `src/lattices/`, `tests/lattice_spec/`, `tests/sage_spec/`, or lattice/module plan files.

## Deletion and cleanup shortcut

Do not delete markdown, specs, review artifacts, theory notes, or directories without provenance and user confirmation unless the deletion is explicitly pre-authorized by `research-repo-structure`. Broken computations are fixed or deleted; they are not preserved with status reports, archives, `_old` names, or companion explanations.

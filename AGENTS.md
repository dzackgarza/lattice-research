# Research Repo Agent Policy

`AGENTS.md` is the always-in-context routing layer for this repo. Keep durable operational detail in local skills and load those skills on demand when their trigger matches the task.

## Always-active invariants

- For plan-to-execution routing, atomicity, delegation stages, and acceptance process, load `research-state-machine`. For proof, evidence, fraud detection, and audit sufficiency, load `research-proof-auditing` when relevant.
- For any git operation, load `git-guidelines` and follow its checkpoint, staging, commit, branch, push, and PR rules. User requests to skip verification skip validation runs, not intentional staging or provenance.
- Implementation, self-check, and adversarial audit are separate roles when `research-state-machine` requires them.
- When reviewing or starting a task, assess it for delegation, including
  parallel delegation, against `opencode-one-shot-workers`. As a first
  approximation, prefer cheap Opencode one-shot workers for bounded atomic
  leaves. If that route fails or is clearly mismatched, promote to stronger
  Codex delegation: prefer Codex Spark (`gpt-5.3-codex-spark`) when usage is
  available, otherwise `gpt-5.4` with low or medium reasoning is usually the
  next bet. Escalate to `gpt-5.5` only when delegation is still a net token
  savings over doing the work directly.
- Do not substitute a nearby task for the user's stated directive.
- Do not mark work accepted, done, or closed without human approval.
- Do not leave findings only in chat when they must survive context loss; create durable artifacts.
- Never create local QC overrides, local whitelists, bypass files, or project-specific workarounds for global quality-control failures. Any QC relaxation must be explicitly user-approved and implemented in the global QC system under `~/ai/quality-control`, not hidden in this repo.
- Resist the urge to silence QC or treat it as an obstacle to work around in phase transitions. QC findings are signals that something is underspecified, unreferenced, or broken -- fix the code, don't expand the whitelist to hide the signal. If a whitelist entry is truly the last resort after code fixes are exhausted, it must be raised as an explicit human-gated request with justification.
- Periodically reflect: review the last 3-5 git commits and self-assess for meta-process churn -- fiddling with card statuses, commenting on task bodies, rearranging bookkeeping, or producing planning artifacts without contributing real work toward the project's mathematical goals. This kind of managerial work is sometimes needed, especially during interactive user sessions where the human is shaping policy, but in autonomous or goal-driven sessions it is often a sign of drift.
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
- Human-facing reports, Plannotator plans, and status briefs are forward-facing artifacts. Do not back-explain prior agent failures, include proof-of-work dumps, or tell the user how to answer; state the current source-grounded classification, the consequence, and the next action.
- QC is phase-transition evidence, not the control loop for spec work. During churn-heavy spec work, do not treat QC failures, hook noise, or unrelated implementation validation failures as blockers for approved spec-plan execution. QC blocks only a claimed phase transition or a user-requested QC/implementation integration pass; otherwise record the finding and continue the approved spec work.
- Blockers are phase-local and path-local unless proven otherwise. A downstream-phase guard, implementation-only gate, QC failure outside a transition/integration pass, oversized card, missing vocabulary, or missing backend bridge is not a reason to exit the active goal while approved phase-local spec, research, decision, or decomposition cards remain. Stop only the affected card/path, create or update the prerequisite card/decision/research item, and continue another approved active leaf.
- Follow the planning DAG literally. Do not even attempt a task whose declared
  dependencies are incomplete. A task with unmet `dependsOn` edges is `unstarted`, not
  `blocked`. Reserve `blocked` for a ready current-phase leaf that cannot proceed
  because it needs an external decision, source, credential, missing theory, or other
  prerequisite that is not currently satisfiable through the DAG.
- Reserve `needs-human-input` for genuine human judgment that remains after source review, mathematical grounding, repo policy, and `dependsOn` have been checked. Source-forced facts, routine plan/card cleanup, and planned downstream dependency order are agent work, not user decisions.
- Constructor placement reports must separate mathematical owner, human naming convention, and code-maintenance owner. Constructors are Sage-backed entry points for building objects in categories; a specific object can carry many structures, while aggregate surfaces such as `Cat().Constructors()` can provide the canonical user entry point independent of the implementation owner.
- Do not report "no path forward" until the active phase, approved plans, and active leaf cards have been checked and every remaining leaf has a concrete blocker that applies to that leaf in the current phase. If any approved active leaf can be advanced by spec writing, source mining, audit criteria, decision capture, card splitting, or prerequisite filing, continue there.
- Never roll back, undo, or reverse auto-fixes produced by hooks, formatters, linters, or other repository tooling. Carry them forward and report unexpected touched paths.

## Skill index

Load these skills when their trigger matches the task:

- `research-state-machine`: plan-to-execution routing, card atomicity, preflight, execution stages, replay/attack, promotion/rejection/splitting, and `GOAL.md` discharge.
- `research-orchestration`: delegation contracts, worktrees, self-check, adversarial audit, artifact handoff, and acceptance execution.
- `opencode-one-shot-workers`: cheap parallel `command opencode` one-shot workers, PTY-watched progress, atomic-task suitability, git/worktree hygiene, and retry/escalation guidance.
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

Every new session must read `GOAL.md`, `.agents/current-goal-phase.md`, and this file. Verify active tasks and Nimbalyst meta artifacts are synced with `origin/main` before declaring progress. Use `iwe` as the repo markdown query and resume layer before broad file scanning: from `.agents/memories`, retrieve or search `current-goal-handoff`, relevant memories, and the current cards named there; from the repo root, use IWE to discover plans, cards, specs, and policy files. Load `research-repo-structure` before startup pruning or cleanup. State which `GOAL.md` phase and task will be worked on and why. Do not start by reading every file in the repo.

## IWE and memory practice

Use `iwe` as the central markdown management, query, and resume interface for this repo. The managed memory library is `.agents/memories` through `.iwe/config.toml`; run IWE from that directory for memory keys such as `current-goal-handoff` and `hermes/MEMORY`. Run IWE from the repo root to discover non-hidden repo markdown such as plans, cards, specs, and policy files. Search with IWE before manually scanning broad subtrees, especially when starting a new task, resuming related work, receiving a compaction/summary, or taking over after context loss or session handoff. Do not rely on chat summaries alone when durable repo markdown or memory may already exist. Add or update notes there when durable context would otherwise be lost.

Hermes memory is part of the same corpus: `/home/dzack/.hermes/memories` is a symlink to `.agents/memories/hermes`, so Hermes, Ralph loops, and IWE-backed agents share one operational memory namespace instead of copying notes between systems.

The rolling handoff note is `.agents/memories/current-goal-handoff.md`. Update it by replacement only when the resumption path changes: current phase, recent decision delta, next pickup cards, non-goals, and validation state. It is a routing aid, not an authoritative tracker. Cards and plans remain authoritative for statuses, dependencies, source grounding, and acceptance.

Store short, opinionated, durable notes:

- important decisions that were too small for a decision card but would still
  affect future agent choices;
- constraints, rulings, and inputs that came out of interactive user discussion
  and should survive chat history loss;
- current state or status notes that help a future agent restart work correctly,
  provided they can be kept accurate without heavy bookkeeping;
- non-obvious environment findings, research results, and workflow rules that
  took effort to discover.

Review memories periodically with `iwe` and prune by replacement rather than
letting stale guidance accumulate silently. If a memory is superseded, update the
IWE note that owns that topic instead of scattering a new contradictory note.

Do not turn memories into a second tracker or metadata database. Avoid complex
manual state, exhaustive status matrices, cross-linked bookkeeping layers, or
anything else that creates combinatorial sync work across plans, decisions,
commits, and memories. If the information wants structured workflow state, it
probably belongs in `plans/`, a decision card, or git history rather than memory.

## Tracker and planning shortcut

All active repo-local planning and work tracking lives under root `plans/`. Use
`plans/AGENTS.md` and registered standard tracker types from
`.nimbalyst/trackers/*.yaml`. There is no separate backlog; active cards under
`plans/features/` are the outstanding work set, while completed feature trees should be
moved under `plans/features/completed/`. Plans are human + LLM collaborative
artifacts and must be approved before decomposition or execution. `GOAL.md` remains the
staged-program source; do not recreate staged phases as active tracker features.

## Repo structure shortcut

Reusable trusted code goes in `src/`. Verified mathematical tests go in `tests/`.
Executable plans and cards go in `plans/`; produced artifacts go in their natural
durable roots. Exploratory drafts go in gitignored `scratch/`. Mathematical notes and
source-backed theory live in `theory/`. Agent skills, TODO scratchpad, retirement
holding, and phase marker files remain under `.agents/`.

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

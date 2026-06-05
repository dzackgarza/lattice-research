# Research Repo Agent Policy

`AGENTS.md` is the always-in-context routing layer for this repo.
Keep durable operational detail in memories (`mem:skills/...`) and load the remaining
local skills on demand when their always-in-context description triggers matching.

## HARD GATE: ONBOARDING

**Before reading any other file, running any tool, scanning any plan, or making any
edit:**

```
iwe retrieve -k onboarding
```

Run this command from `.agents/memories/`. Read the full output.
This is not optional and not skippable.
The onboarding memory is the single source of truth for what this project is, what phase
we are in, what the most common agent failure modes are, and what concrete work to do
next.

If you have not read the onboarding output in full, you are not allowed to:
- Run mypy, structural reports, or ledgers
- Read plan files or cards
- Scan the codebase
- Make any edit

No exception for "I've been here before," "I remember the project," or "the handoff is
enough." Read onboarding first.
Every time.

## Always-active invariants

- For substantial mathematical research directions, onboarding, workstream coordination,
  living-paper maintenance, uncertainty surfacing, and failed-path preservation, load
  `research-co-mathematician-workflow`. For plan-to-execution routing, atomicity,
  delegation stages, and acceptance process, load `research-state-machine`. For proof,
  evidence, fraud detection, and audit sufficiency, load `research-proof-auditing` when
  relevant.
- For any git operation, load `git-guidelines` and follow its checkpoint, staging,
  commit, branch, push, and PR rules.
  User requests to skip verification skip validation runs, not intentional staging or
  provenance.
- Before any nontrivial edit, load every skill whose trigger matches the file, domain,
  and operation, then read the canonical reference files named by those skills before
  checkpointing or editing.
  "Nontrivial" includes changes to method ownership, mathematical definitions, type
  surfaces, inheritance, decorators, constructors, category/Hom/End/Aut structure,
  tests, smokes, specs, mapping docs, tracker state, or agent-facing policy.
  If the relevant skill or reference is not in context, stop and load it; do not patch
  from memory.
- Implementation, self-check, and adversarial audit are separate roles when
  `research-state-machine` requires them.
- After any nontrivial category-spec implementation or mapping edit, the card moves to
  `needs-agent-review`. The coordinator must dispatch a fresh-context review subagent
  under the review kernel before claiming completion.
  A review that does not inspect the card, sources, artifacts, and diff is not a review.
  Synthesis is required; a review that could be produced by a schema validator, grep, or
  diff-presence script is insufficient.
  A status-only card update without substantive findings in the card body is fraudulent.
  Completion means moving the card past `needs-agent-review`, not merely updating
  handoff or chat.
- If an approved repo workflow, task card, review kernel, plan, or user-provided
  objective explicitly requires subagent review or delegation, that requirement is
  already the user's explicit request for the scoped subagent use.
  Do not demand a second live-chat authorization, do not mark the card `blocked` or
  `needs-human-input` for permission to spawn the required review/delegation subagent,
  and do not repeat a permission blocker.
  Execute the documented subagent step under the workflow's isolation and evidence
  rules.
- When reviewing or starting a task, assess it for delegation, including parallel
  delegation, against `opencode-one-shot-workers`. As a first approximation, prefer
  cheap Opencode one-shot workers for bounded atomic leaves.
  If that route fails or is clearly mismatched, promote to stronger Codex delegation:
  prefer Codex Spark (`gpt-5.3-codex-spark`) when usage is available, otherwise
  `gpt-5.4` with low or medium reasoning is usually the next bet.
  Escalate to `gpt-5.5` only when delegation is still a net token savings over doing the
  work directly.
- Do not substitute a nearby task for the user's stated directive.
- Before accepting, activating, delegating, or resuming a Goalcraft-generated `/goal`,
  apply the Goalcraft acceptance gate below.
  Goalcraft form is not enough; a goal with a Sage-surface or process witness is
  invalid for mathematical/spec work.
- Do not mark parent plans, features, native items, sprint plans, or `GOAL.md` discharge
  accepted, done, or closed without human approval.
  This is not a license to park ordinary reviewed task cards in `needs-human-input`: if
  the remaining action is source-forced, policy-forced, DAG-forced, or agent-reviewable,
  keep executing the state machine.
- Do not leave findings only in chat when they must survive context loss; create durable
  artifacts.
- Every new card, memory, report, or handoff edit must state what mathematical or
  epistemic object it preserves against context loss.
  The memory-management discipline (`mem:memory-management-discipline`) requires this of
  memories; the same rule applies to cards, reports, and handoff edits.
  If the artifact cannot name the object-level claim it preserves, it is suspect.
- Never create local QC overrides, local whitelists, bypass files, or project-specific
  workarounds for global quality-control failures.
  QC fixes go to the global QC system under `~/ai/quality-control`; local relaxation is
  not an option.
- Tracker schemas, QC validation, and plan-validate authority are global, not
  repo-local. The schemas under `.nimbalyst/trackers/` are symlinks to
  `~/ai/planning/schemas/`. Schema edits go to that repo with a git commit; local schema
  forks are never correct — if a schema is too restrictive, add the field to the
  canonical schema. `just plan-validate` delegates to the centralized validator.
  Never write repo-local relaxed validators, warning-only schema checks, skip-gate
  justfile recipes, or inline Python validators that bypass the global validator.
- QC findings are mandatory within their scope.
  The applicable scope depends on whether the code is being actively edited, claimed
  complete, or inherited from outside the current leaf.
  **Priority rule:** (1) Touched-scope failures (code modified by the current leaf) are
  defects and must be fixed or globally configured away; (2) Claimed-completion failures
  (code in a card/transition that is declared done) are defects and the claim is void
  until resolved; (3) Unrelated inherited failures (code outside the current leaf or
  phase scope) are routed to a tracking TODO/decision but do not control the active
  leaf. Phase transitions and integration passes require QC-zero or a global config fix;
  during active spec drafting, only touched-scope or claimed-completion failures block
  the leaf. A static analysis error — mypy, ruff, semgrep, vulture, etc.
  — is a defect in the repo, not a defect in the tool.
  The correct response to a QC finding is to fix the code or fix the tool configuration
  at the global level.
  Never dismiss findings as "expected for this phase," "just spec work," "just stubs,"
  "mypy can't handle metaclasses," or any other rationalization that ends with the
  finding unaddressed.
  If the tool is misconfigured, fix the global config.
  If the code has missing types, add the types.
  The only acceptable outcomes for a touched-scope or claimed-completion surface are
  zero findings or a global config change committed to the tool repo.
- Resist the urge to silence QC or treat it as an obstacle to work around in phase
  transitions. QC findings are signals that something is underspecified, unreferenced, or
  broken -- fix the code, don't expand the whitelist to hide the signal.
  If a whitelist entry is truly the last resort after code fixes are exhausted, it must
  be raised as an explicit human-gated request with justification.
- Periodically reflect: review the last 3-5 git commits and self-assess for meta-process
  churn -- fiddling with card statuses, commenting on task bodies, rearranging
  bookkeeping, or producing planning artifacts without contributing real work toward the
  project's mathematical goals.
  This kind of managerial work is sometimes needed, especially during interactive user
  sessions where the human is shaping policy, but in autonomous or goal-driven sessions
  it is often a sign of drift.
- Specs, review files, theory notes, TODO files, and durable design artifacts are source
  material. Do not rewrite, shorten, modernize, delete, or align them to current
  implementation unless the user explicitly asks for that exact edit.
- Do not preserve backward-compatibility docs, legacy references, retired policy files,
  or compatibility shims unless explicitly requested or retiring them is truly
  dangerous. Git history is the archive; prefer a clear retiring commit over keeping
  stale docs in the working tree.
- `GOAL.md` is read-only.
  Source authority for literature and standard claims lives in
  `theory/references/index.md`.
- Mathematical spec claims require definition grounding before edit.
  Before adding or changing a mathematical definition, method owner, invariant,
  predicate, equivalence, migration rule, or category surface, identify the canonical
  repo/source basis: `theory/`, `theory/references/`, `theory/spec_backups/`, Sage
  written docs/source, or an approved decision card.
  Migrated TODO lines, backlog cards, common terminology, and plausible textbook memory
  are provenance, not authority.
  Record the source path, exact definition, hypotheses, and any required
  invariance/equivalence proof in the card or mapping doc.
  If no such grounding exists, stop that leaf and create a source-mining or decision
  card instead of writing the spec.
- No nontrivial category-spec edit may be committed unless it is attached to a tracked
  card or mapping doc that contains the visible object/operation/owner,
  recovery/missing-obligation, or representation-split statement required by
  `mem:category-spec-epistemic-foundation`. "Nontrivial" here means any change to method
  ownership, category surface, type signature, constructor placement, Hom/End/Aut
  structure, smoke spec, mapping row, or category graph edge.
  The epistemic statement must be visible in the card body, mapping row, or commit
  message — hidden reasoning in the agent session is not sufficient.
- Do not merge distinct mathematical notions under one name without a recorded proof
  under explicit hypotheses.
  If two candidate meanings exist, keep separate named surfaces or block on a decision;
  do not assume they coincide because they do in a familiar special case.
- Mathematical implementation work must prefer wiring mature open-source mathematical
  software over bespoke algorithms.
  Load `research-software-wiring` before writing or delegating mathematical
  implementation code.
- In `category_specs`, resolve circular imports by separating type surfaces from runtime
  wiring. Mathematical type names and aliases belong in `category_specs/types.py` as the
  single source of truth; annotation-only imports use `TYPE_CHECKING` and import those
  names from `types.py`. Runtime category, subcategory, Hom/End/Aut, and constructor
  wiring must avoid importing from a package `__init__` while that package is
  initializing; use local imports or Sage `LazyImport` for real runtime dependencies
  instead of moving the cycle to `types.py`.
- Use `GOAL.md` to situate work in the repo's staged mathematical plan.
  The current phase is tracked in `.agents/current-goal-phase.md`; downstream phases are
  blocked until prerequisite vocabulary and specs exist.
- Human-facing reports, Plannotator plans, and status briefs are forward-facing
  artifacts. Do not back-explain prior agent failures, include proof-of-work dumps, or
  tell the user how to answer; state the current source-grounded classification, the
  consequence, and the next action.
- QC is phase-transition evidence, not the control loop for spec work.
  During churn-heavy spec work, do not treat QC failures, hook noise, or unrelated
  implementation validation failures as blockers for approved spec-plan execution.
  QC blocks only a claimed phase transition or a user-requested QC/implementation
  integration pass; otherwise record the finding and continue the approved spec work.
  See the QC priority rule above for touched-scope vs.
  inherited-failure routing.
- Blockers are phase-local and path-local unless proven otherwise.
  A downstream-phase guard, implementation-only gate, QC failure outside a
  transition/integration pass, oversized card, missing vocabulary, or missing backend
  bridge is not a reason to exit the active goal while approved phase-local spec,
  research, decision, or decomposition cards remain.
  Stop only the affected card/path, create or update the prerequisite
  card/decision/research item, and continue another approved active leaf.
- Follow the planning DAG literally.
  Do not even attempt a task whose declared dependencies are incomplete.
  A task with unmet `dependsOn` edges is `unstarted`, not `blocked`. Reserve `blocked`
  for a ready current-phase leaf that cannot proceed because it needs an external
  decision, source, credential, missing theory, or other prerequisite that is not
  currently satisfiable through the DAG.
- Priority reports must cut the graph at the earliest incomplete dependency frontier.
  If `B dependsOn A` and `A` is incomplete, then `B`'s status, partial progress, child
  cards, review state, and apparent readiness are irrelevant for priority.
  Do not rank, discuss, or select work inside `B` until every prerequisite on every
  incoming dependency path is complete; mention it only as DAG-gated by the incomplete
  root.
- Reserve `needs-human-input` for genuine human judgment that remains after source
  review, mathematical grounding, repo policy, and `dependsOn` have been checked.
  Source-forced facts, routine plan/card cleanup, and planned downstream dependency
  order are agent work, not user decisions.
- Never use `needs-human-input` as a reward-hacking stop condition.
  A clean review awaiting bookkeeping, an approval-shaped yes/no on already
  policy-determined routing, or an agent's desire to stop early is not human input.
  To classify a card as `needs-human-input`, record the exact non-agent-resolvable
  question; if the question is merely "approve this reviewed work as complete," continue
  with agent-executable closure or another active leaf instead of reporting a blocker.
- Constructor placement reports must separate mathematical owner, human naming
  convention, and code-maintenance owner.
  Constructors are Sage-backed entry points for building objects in categories; a
  specific object can carry many structures, while aggregate surfaces such as
  `Cat().Constructors()` can provide the canonical user entry point independent of the
  implementation owner.
- Do not report "no path forward" until the active phase, approved plans, and active
  leaf cards have been checked and every remaining leaf has a concrete blocker that
  applies to that leaf in the current phase.
  If any approved active leaf can be advanced by spec writing, source mining, audit
  criteria, decision capture, card splitting, or prerequisite filing, continue there.
- Never roll back, undo, or reverse auto-fixes produced by hooks, formatters, linters,
  or other repository tooling.
  Carry them forward and report unexpected touched paths.

## Goalcraft acceptance gate

Apply this gate before accepting, activating, delegating, or resuming a
Goalcraft-generated `/goal` for long-running work in this repo.
This is a quality gate on the generated objective, not another worker-progress rule.
A generated goal is invalid unless its completion witness is a
mathematical/research-state witness.

For mathematical/spec work, the generated goal must write down the Goalcraft consequence
comparison before activation:

- Request witness: the mathematical object or research state whose truth-state changes.
- Draft witness: the facts that would be true if the generated goal were marked
  complete.
- Acceptance test: the draft witness must entail the request witness without replacing
  it by a Sage-surface inventory, process state, review state, status note, plan, or
  compatibility audit.

For category-spec work, the completion object is not "all Sage surfaces touching the
subtree." A valid object is shaped like:

```text
The category-spec foundation for <subtree> has a source-backed mapping from
Sage methods/constructors to the minimal mathematical structures and hypotheses
they require.
```

Reject unbounded scope words unless the generated goal immediately gives a finite
universe generator. Invalid scope words include `full`, `every`, `all relevant`,
`adjacent`, and especially `touches`. A valid generated goal must define:

```text
Universe U is generated by:
  source roots:
  exported constructors/functions:
  class/provider methods:
  excluded nonmathematical families:
  queue artifact:
  residue/subtraction rule:
```

Every mathematical/spec goal must require semantic extraction before classification:

```text
Sage method body/examples
-> mathematical behavior implemented
-> required vocabulary/hypotheses
-> weakest mathematical owner
-> Sage evidence
-> mapping/spec row
```

Reject any generated goal whose unit of progress is only `row patched`, `surface
classified`, `source location found`, `mapping updated`, or `review passed` without a
mathematical operation statement in ordinary mathematical language.

Split queues before activation. A generated goal may include several queues, but it
must state which queue is active and which queues are subordinate:

- Mathematical vocabulary/foundation controls research progress.
- Sage source inventory supports the mathematical queue.
- Implementation/runtime/display/backend compatibility is a separate residue audit.
- Testing/review/proof evidence verifies the artifact; it does not substitute for the
  prior act of establishing the mathematical inventory.

Large repetitive goals must define a unit loop:

```text
Unit:
Method:
Acceptance evidence for one unit:
Queue state:
How one unit is removed from Remaining:
```

For category-spec work, a valid unit is one Sage method cluster with a shared
mathematical behavior, classified by minimal structure/hypotheses and source evidence.
A file, row cluster, package export set, or handoff frontier is invalid unless it is
also a mathematically coherent operation family.

Completion may be claimed only when the queue artifact shows:

```text
U = C ⊔ R ⊔ Q
```

where `C` has mathematical operation statements and weakest owners, `R` is explicitly
nonmathematical/runtime/display/backend residue, and `Q` contains only genuine
unresolved mathematical/spec decisions. Wrapper compliance, onboarding, handoffs,
memories, plans, status labels, review state, and proof gates cannot satisfy this
witness.

Example rejection:

```text
Invalid:
Complete full Sage-sourced inventory of every provider, method, constructor,
factory, Hom/End/Aut surface, and interop/display/backend surface touching
category_specs/lattices.

Reason:
The unit is a Sage surface, the scope word "touching" has no finite generator,
and mathematical vocabulary is not the controlling object.
```

Example acceptance:

```text
Valid:
Build the source-backed mathematical operation map for category_specs/lattices:
generate the finite Sage method/constructor queue from named source roots,
read each method cluster, state the mathematical operation and weakest required
structure, classify implementation/runtime/display residue separately, and mark
complete only when the queue artifact has no unclassified mathematical operations.
```

Reject Goalcraft-generated goals for this repo if they:

- use Sage source surfaces as the primary completion object;
- use `all`, `every`, `full`, `relevant`, `adjacent`, or `touches` without a finite
  generated queue and residue rule;
- omit the semantic extraction step from Sage behavior to mathematical vocabulary;
- combine mathematical foundations with runtime/display/backend audits as one queue;
- define progress by plans, mappings, status, handoff, or review state rather than
  reduction of a concrete mathematical frontier;
- make proof/review gates substitute for establishing the inventory.

Accept Goalcraft-generated goals for this repo only if they:

- state the mathematical/research consequence that becomes true;
- define the finite work universe and residue subtraction rule;
- require method semantics to determine vocabulary;
- separate mathematical operations from implementation residue;
- define one-unit acceptance evidence;
- preserve completion as artifact truth, not process compliance.

## Skill index

Load these skills when their description triggers matching.
For behavioral content previously in skills that are now memories, read the
corresponding `mem:skills/...` entry.

**Remaining skills (always-in-context dynamic triggers):**

- `research-state-machine`: plan-to-execution routing, card atomicity, preflight,
  execution stages, replay/attack, promotion/rejection/splitting, and `GOAL.md`
  discharge.
- `research-orchestration`: delegation contracts, worktrees, self-check, adversarial
  audit, artifact handoff, and acceptance execution.
- `research-code-style`: contribution policy, mathematical code style, tests,
  Sage/Pydantic surfaces, constructors, equality, assertions, and implementation
  compliance.
- `research-software-wiring`: existing-software-first mathematical implementation,
  backend capability routing, bridge-vs-bespoke decisions, and backend-gap research
  blockers. **Forced preflight: load before any mathematical implementation work.**
- `research-relevance-check`: detects artifact-heavy drift.
  Load when work becomes artifact-heavy, engineering-heavy, or unclear in relation to
  mathematical research.
- `category-spec-style`: mathematical and code/spec compliance for category specs, type
  surfaces, Sage wrappers, constructors, method ownership, smoke files.
- `handling-corrections`: required protocol when the user corrects a mathematical,
  repo-architecture, or task-framing claim.
- `task`: creation of tracker items under `.agents/plans/`.
- `track`: creation of tracking items from `/track` commands.
- `git-guidelines`: required for staging, committing, branching, pushing, PRs, and any
  other git operation.

**Migrated to memories — read these via `iwe retrieve -k skills/<name>`:**

| Former skill | Memory key |
| --- | --- |
| `category-framework-design` | `skills/category-framework-design` |
| `category-spec-audit` | `skills/category-spec-audit` |
| `category-spec-complexity-rubric` | `skills/category-spec-complexity-rubric` |
| `category-spec-planning` | `skills/category-spec-planning` |
| `category-spec-priority-rubric` | `skills/category-spec-priority-rubric` |
| `category-spec-retirement` | `skills/category-spec-retirement` |
| `category-spec-sage-mapping` | `skills/category-spec-sage-mapping` |
| `category-spec-smoke-triage` | `skills/category-spec-smoke-triage` |
| `category-spec-subtrees` | `skills/category-spec-subtrees` |
| `category-spec-triage` | `skills/category-spec-triage` |
| `category-spec-visuals` | `skills/category-spec-visuals` |
| `category-spec-workflow` | `skills/category-spec-workflow` |
| `creating-fixtures` | `skills/creating-fixtures` |
| `lattice-redesign` | `skills/lattice-redesign` |
| `opencode-one-shot-workers` | `skills/opencode-one-shot-workers` |
| `request-triager` | `skills/request-triager` |
| `research-co-mathematician-workflow` | `skills/research-co-mathematician-workflow` |
| `research-math-boundary` | `skills/research-math-boundary` |
| `research-planning-cleanup` | `skills/research-planning-cleanup` |
| `research-project-workflow` | `skills/research-project-workflow` |
| `research-proof-auditing` | `skills/research-proof-auditing` |
| `research-repo-structure` | `skills/research-repo-structure` |
| `research-scheduling` | `skills/research-scheduling` |
| `research-source-acquisition` | `skills/research-source-acquisition` |
| `sage-category-source-maps` | `skills/sage-category-source-maps` |
| `vinberg-algorithm` | `skills/vinberg-algorithm` |
| `plannotator-workflow` | `plannotator-workflow` |

Many of these memories have sub-memories for their reference files (e.g.,
`skills/category-framework-design/category-refinement-phases`). Use `iwe find skills/`
to discover the full tree.

Start with `category_specs/AGENTS.md` for that subtree.

## Session startup

Every new session must:
1. Run `iwe retrieve -k onboarding` from `.agents/memories/` and read the full output.
   This is the HARD GATE (see above).
   No file reads, tool runs, plan scans, or edits are permitted before onboarding.
2. Run `iwe retrieve -k current-goal-handoff` and read the named files.
3. Read `GOAL.md`, `.agents/current-goal-phase.md`, and this file.
   Verify active tasks and Nimbalyst meta artifacts are synced with `origin/main` before
   declaring progress. Use `iwe` as the repo markdown query and resume layer before broad
   file scanning: from `.agents/memories`, retrieve or search relevant memories and the
   current cards named by the handoff; from the repo root, use IWE to discover plans,
   cards, specs, and policy files.
   Load `research-repo-structure` before startup pruning or cleanup.
   State which `GOAL.md` phase and task will be worked on and why.
   Do not start by reading every file in the repo.
4. Before category-spec work, review, or source repair, use IWE to surface normal
   governing memories by topic, not by historical session.
   Start from the handoff's named memories, then use `iwe find` for the actual work
   shape: `purpose`, `category specs`, `red flags`, `sanity`, `grounded analysis`,
   `paperwork`, `corrections`, `refinement`, `provider`, `hooks`, or the concrete
   method/category names involved.
   The goal is that repo-purpose, review, artifact-drift, correction, and refinement
   rules surface during ordinary work; do not rely on remembering any past transcript.

## IWE and memory practice

Use `iwe` as the central markdown management, query, and resume interface for this repo.
The managed memory library is `.agents/memories` through `.iwe/config.toml`; run IWE
from that directory for memory keys such as `current-goal-handoff` and `hermes/MEMORY`.
Run IWE from the repo root to discover non-hidden repo markdown such as plans, cards,
specs, and policy files.
Search with IWE before manually scanning broad subtrees, especially when starting a new
task, resuming related work, receiving a compaction/summary, or taking over after
context loss or session handoff.
Do not rely on chat summaries alone when durable repo markdown or memory may already
exist. Add or update notes there when durable context would otherwise be lost.

Hermes memory is part of the same corpus: `/home/dzack/.hermes/memories` is a symlink to
`.agents/memories/hermes`, so Hermes, Ralph loops, and IWE-backed agents share one
operational memory namespace instead of copying notes between systems.

The rolling handoff note is `.agents/memories/current-goal-handoff.md`. Update it by
replacement whenever the resumption path changes: current phase, recent decision delta,
next pickup cards, non-goals, and validation state.
**It is a routing aid, nothing more.** It exists for exactly one purpose: to tell the
next session where to start and what to avoid.
It is NOT a status report, NOT a changelog, NOT a tracker, and NOT an audit log.
Cards, plans, and git history are the sole authorities for status, dependencies, source
grounding, acceptance, and completed work.
If the information describes what was done rather than what to do next, it does not
belong here.

**This is not optional.** After any of the following, update the handoff note
immediately — before reporting the result in chat:
- Creating, promoting, or splitting task cards
- Completing a review pass (cards moving to complete/revision-required)
- Resolving a blocker or discovering a new one
- Decomposing a plan into tasks
- Any state change that alters what the next session should pick up

Chat is the delivery channel; the handoff note is the durable checkpoint.
If the handoff is stale, the process has failed.

Store short, opinionated, forward-facing notes only.
**Never store:**
- summaries of completed work (belongs in commit messages)
- changelogs, diff histories, or "what happened" narratives (git history is the sole
  record)
- descriptions of past agent actions, decisions already captured in cards, or lengthy
  retrospective writeups
- anything that describes what was done instead of what to do next

The handoff is meant to be read in 30 seconds by a cold-start agent.
If it takes longer, it contains something that should be in a card, plan, decision, or
git history instead.

Appropriate handoff content:

- important decisions that were too small for a decision card but would still affect
  future agent choices;
- constraints, rulings, and inputs that came out of interactive user discussion and
  should survive chat history loss;
- current state or status notes that help a future agent restart work correctly,
  provided they can be kept accurate without heavy bookkeeping;
- non-obvious environment findings, research results, and workflow rules that took
  effort to discover.

Review memories periodically with `iwe` and prune by replacement rather than letting
stale guidance accumulate silently.
If a memory is superseded, update the IWE note that owns that topic instead of
scattering a new contradictory note.

### IWE command reference

Documents live in `.agents/memories/`; the key for a file is its path relative to that
directory without the `.md` extension (e.g. `theory/backends/vinberg-algorithm`). Run
`iwe` from the repo root for non-memory repo markdown; run it from `.agents/memories/`
for memory keys.

**Discover**

```
iwe find                          # all docs sorted by incoming references
iwe find "keyword"                # fuzzy match on title and key
iwe find -f keys                  # bare key list (for scripting)
iwe find -f json                  # full graph metadata
iwe tree                          # document hierarchy
iwe stats                         # graph overview (doc count, top docs, etc.)
```

**Filter**

```
iwe find --filter 'status: draft'          # frontmatter predicate
iwe find --referenced-by KEY              # docs that link to KEY
iwe find --references KEY                 # docs that KEY links to
iwe find --included-by KEY               # docs block-included by KEY
iwe find --includes KEY                  # docs that KEY block-includes
```

**Retrieve**

```
iwe retrieve -k KEY               # document content with default context
iwe retrieve -k KEY -d 2          # follow inclusion edges 2 levels deep
iwe retrieve -k KEY -c 2          # include 2 levels of parent context
iwe retrieve -k KEY -l            # also follow inline markdown links
iwe retrieve -k KEY -b            # also show backlinks (incoming references)
```

**Navigation patterns**

Never dump the full tree into a session.
Start broad, then drill.

```
# Top-level structure; expand one more level when you know which area
iwe tree --depth 1
iwe tree --depth 2

# Retrieve a doc plus its children (depth controls how many inclusion levels)
iwe retrieve -k <key> -d 1
iwe retrieve -k <key> -d 2

# Retrieve a doc plus its parent context
iwe retrieve -k <key> -c 1
```

```
# Fuzzy search to locate a doc before reading it
iwe find "keyword"

# Find which docs include a given doc (its parents) or it includes (its children)
iwe find --included-by <key>
iwe find --includes <key>

# Fast key lookup by path fragment
iwe find -f keys | grep <pattern>
```

Do not turn memories into a second tracker or metadata database.
Avoid complex manual state, exhaustive status matrices, cross-linked bookkeeping layers,
or anything else that creates combinatorial sync work across plans, decisions, commits,
and memories. If the information wants structured workflow state, it probably belongs in
`.agents/plans/`, a decision card, or git history rather than memory.

## Tracker and planning shortcut

All active repo-local planning and work tracking lives under `.agents/plans/`. Use
`.agents/plans/AGENTS.md` and registered standard tracker types from
`.nimbalyst/trackers/*.yaml` (symlinks to `~/ai/planning/schemas/`; schema edits go to
that repo). There is no separate backlog; active cards under `.agents/plans/features/`
are the outstanding work set, while completed feature trees should be moved under
`.agents/plans/features/completed/`. Plans are human + LLM collaborative artifacts and
must be approved before decomposition or execution.
`GOAL.md` remains the staged-program source; do not recreate staged phases as active
tracker features.

Validate planning edits with `just plan-validate`, which delegates to the centralized
planning validator.
Do not add repo-local relaxed validators, warning-only schema checks,
or bypass recipes.

## Repo structure shortcut

Reusable trusted code goes in `src/`. Verified mathematical tests go in `tests/`.
Executable plans and cards go in `.agents/plans/`; produced artifacts go in their
natural durable roots.
Exploratory drafts go in gitignored `scratch/`. Mathematical notes and source-backed
theory live in `theory/`. The living LaTeX working paper lives in `paper/`, reviewed
workstream reports live in `reports/workstreams/`, and repo-local delegation role
prompts live in `.agents/agent-roles/`. Agent skills, TODO scratchpad, retirement
holding, and phase marker files remain under `.agents/`.

`src.bak/` and `tests.bak/` are a temporary quarantine for stale implementation code and
implementation tests while phase-one category/spec work is active.
Do not treat those trees as active first-party surfaces, do not chase lint/type failures
inside them, and do not reactivate them except during an explicit implementation audit
or reactivation pass.

## Theory and references shortcut

Use `theory/index.md` to route durable mathematical knowledge.
Use `theory/references/index.md` and `theory/references/references.bib` before writing
standard-claim prose, expected values, or literature-backed justifications.

## Mathematical boundary shortcut

Trusted shared code is a semantic mathematical base built from explicit nouns with
methods. If a task cannot be expressed cleanly through the public mathematical
vocabulary, stop and surface a task-boundary failure instead of adding ad hoc helpers.

Mathematical algorithms are wired from mature open-source systems first.
If no preferred wiring is documented, stop implementation and create backend-gap
research work instead of guessing or writing local mathematics.

Do not perform downstream Coble research before the category and lattice specs can
semantically express the objects and morphisms involved.
Raw matrices, isolated polynomial calculations, and hand-checked equations are not
acceptable substitutes for mathematically typed code that can be reviewed as a chain of
argument.

For lattice/module redesign work, load `research-math-boundary` before touching
`src/lattices/`, `tests/lattice_spec/`, `tests/sage_spec/`, or lattice/module plan
files.

## Deletion and cleanup shortcut

Do not delete markdown, specs, review artifacts, theory notes, or directories without
provenance and user confirmation unless the deletion is explicitly pre-authorized by
`research-repo-structure`. Broken computations are fixed or deleted; they are not
preserved with status reports, archives, `_old` names, or companion explanations.

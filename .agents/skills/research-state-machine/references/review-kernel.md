# Research Review Kernel

This is the canonical review protocol for the research repo. It formalizes the Replay/Attack and Promote/Reject stages from the execution kernel into a structured gate-based procedure that gates every card moving from `needs-review` or `needs-human-input` toward `complete`/`done`.

## Operational directive

When you encounter a card with `status: needs-review`, it is your work. But it is
NOT work you can do inline in your own session.

**You must delegate review to a fresh-context subagent.** This is mandatory. The
subagent must never have been exposed to the implementation session, implementing
agent's chat history, or the implementing agent's rationalizations. Its only inputs
are: the card body, the work artifacts (at known paths), the baseline artifacts (at
known paths), and this review kernel.

What the subagent does: read the card, read the artifacts, apply the ordered gates
below, and produce a review log with concrete findings. Concrete means: for every
gate that passes, the subagent names the exact file, line, command, or source it
checked. "Looks good" is a gate failure.

What you (the coordinator) do afterward: verify the subagent's review for
box-checking behavior. See the coordinator verification step at the end of the
Review procedure section. If the review is substantively wrong or shallow, reject it
and re-dispatch.

When you encounter a card with `status: needs-human-input`, it specifically requires
human attention. Do not delegate it to a review subagent. Record it as a blocker and
surface the question or decision needed.

## Core invariant

A card is not complete because it passed review. It is complete only when every gate in the ordered protocol was checked, every finding was resolved, and the human gate has approved the result.

## Status extension

Two statuses are added to the standard Nimbalyst status set:

- `revision-required` is added to `task`, `spec`, `feature`, and `phase` schemas to represent a card that passed preliminary review but needs rework.
- `needs-human-input` is added to `feature`, `spec`, `phase`, `task`, and `plan` schemas to represent a card that specifically requires human review (as distinct from `needs-review`, which indicates agent-executable gate-based review).

```yaml
- value: revision-required
  label: Revision Required
  icon: replay
  color: '#f59e0b'
```

```yaml
- value: needs-human-input
  label: Needs Human Input
  icon: person
  color: '#8b5cf6'
```

A `blocked_reason` text field is added to the same schemas, placed immediately after the `status` field. When a card is `blocked`, this field records the specific gap and the prerequisite card.

Semantics:

| Status | Meaning |
|---|---|---|
| `unstarted` | No work has been done. May have planned dependencies in `dependsOn`; read the DAG to determine start-readiness. |
| `in-progress` | Work actively underway |
| `needs-review` | Work completed; awaiting gate-based review (agent-executable protocol) |
| `needs-human-input` | Work completed; specifically requires human input or review |
| `revision-required` | Review found defects; rework required within this card's scope |
| `complete`/`done` | All gates passed; accepted |
| `blocked` | Work was attempted (or preflighted); a specific blocker was discovered that requires a different card to be resolved first. The blocker is recorded in `blocked_reason`. |

`needs-review` and `needs-human-input` are sibling states reached from `in-progress`. The distinction is the kind of review required:
- `needs-review`: the card is ready for the ordered gate-based protocol (Gates 1-6), which an independent agent can execute.
- `needs-human-input`: the card specifically requires human attention -- a design decision, policy choice, or evaluation that cannot be delegated to an agent. Human input may be requested directly or may arise when an agent's gate-based review determines that human judgment is needed.

`revision-required` is distinct from `unstarted` (no work was ever done) and `blocked` (discovered blocker requiring external resolution). A card cycling through `needs-review → revision-required → in-progress → needs-review` is normal. Repetitive cycles indicate a deeper design problem, which should be escalated to a plan review or decision card rather than reworked in isolation.

### Blocked vs. unstarted vs. dependsOn

The `dependsOn` DAG already encodes the dependency graph. An intelligent agent reads it and infers that a card with unsatisfied upstream dependencies should not be started. This does not require `status: blocked`.

| Situation | Status | Mechanically captured by |
|---|---|---|
| Card was never attempted; its upstream dependencies in `dependsOn` are unsatisfied | `unstarted` | `dependsOn` → read upstream `status` |
| Card was attempted; review or preflight discovered a concrete blocker requiring another card | `blocked` | `blocked_reason` + the blocker card (linked in `dependsOn`) |
| Card was attempted; review found defects fixable within this card's scope | `revision-required` | Review log findings in card body |
| Card should logically follow X (narrative ordering), but only needs X's abstract output, not X's completion | `unstarted` or `in-progress` | Phase containment + priority; no `dependsOn` edge |

Cards that are currently `blocked` solely because a planned upstream dependency is unfinished should be audited and moved to `unstarted` (if work was never attempted) or `revision-required` (if work was attempted and found to require upstream resolution). The `dependsOn` field suffices to prevent premature execution; the `blocked` status is reserved for discovered blockers found during execution or review.

## Review state slice

```
unstarted → in-progress → needs-review → [review gates applied]
                        → needs-human-input → [human input/review]
                                                │
                                ┌───────────────┼───────────────┐
                                ▼               ▼               ▼
                            complete        revision-        blocked
                            / done          required       (discovered
                                           (rework           blocker:
                                            needed)       blocked_reason
                                                           set)
                                │
                                └──→ in-progress (rework) → needs-review → ...
```

An `unstarted` card with unsatisfied `dependsOn` entries stays `unstarted` -- this is a planned dependency, not a blocker. The DAG encodes it. Do not set `blocked` for planned upstream dependencies.

Cards route to `needs-review` or `needs-human-input` based on the kind of review required:
- Route to `needs-review` when the review can follow the ordered gate protocol (agent-executable).
- Route to `needs-human-input` when a human decision, policy choice, or evaluation is required.
- A card in `needs-review` may be transitioned to `needs-human-input` if the gate-based review determines that human input is needed.

## Review execution requirements

### Subagent isolation (mandatory)

Every review must be executed by a **fresh-context subagent** dispatched by the
coordinator. The subagent has never seen the implementation session. It receives:

- The card body (the task/spec/phase/plan file)
- Paths to work artifacts (files changed, branches, PRs, commits)
- Paths to baseline artifacts (decision cards, prior specs, smoke baselines — see
  Gate 4 for the full list)
- This review kernel

The subagent must not receive: the implementing agent's chat transcript, the
implementing agent's rationalizations, the coordinator's opinions about the work,
or any prior review logs (unless the card is cycling through a revision cycle, in
which case the subagent sees previous review logs as evidence).

The coordinator must not perform review inline in its own session. The
coordinator's context already contains the implementing state. Even if the
coordinator did not personally implement the work, its session may contain
delegation records, summaries, or ambient discussion that contaminates independent
judgment.

### Anti-boxchecking rules (applied by the review subagent)

Every gate pass must produce concrete, falsifiable evidence. Forbidden review
language:

- "Appears correct" / "looks good" / "seems fine" → re-do the check
- "I assume" / "probably" / "should be" → the gate is not checked yet
- "The test passes" without citing which test and showing its output → not checked
- "The spec is consistent" without naming the specific parts verified → not checked
- "No issues found" without describing what was specifically examined → not checked

For each gate that passes, the review log must include at least one concrete
artifact:

- Gate 1: the exact source path that grounds each definition
- Gate 2: each acceptance criterion listed with the artifact that satisfies it
- Gate 3: the git diff command run and the specific surfaces inspected
- Gate 4: the baseline artifact consulted and the comparison produced
- Gate 5: the test command run or the proof step verified
- Gate 6: the specific rule checked and the evidence that it is satisfied

### Role boundaries

Gates 1-2 may be self-checked by the implementer before submitting to review, but
the review subagent must independently verify both gates from scratch.

Gates 3-6 require the review subagent. The implementer must not pre-check these
gates; the subagent approaches them with fresh context and no prior exposure to the
implementer's working assumptions.

The review subagent is not the adversarial auditor (that is a separate
state-machine stage governed by `research-proof-auditing`). The review subagent
applies the gates with rigor; it does not run a full attack.

## Ordered gates

Apply gates in order. Stop at the first failing gate (fail-fast). A failure at gate N invalidates any work that would be checked at gates N+1 through 6, so documenting those downstream gates after an upstream failure is wasted effort.

### Gate 1: Definition Grounding

Every mathematical definition, type, predicate, constructor, and method-owner claim must trace to a canonical source.

**Check:**
- For each definition the work introduces or depends on, the card body (or a linked card) records: source path or reference, exact definition, owner category, hypotheses, codomain/return object, and proof obligations for choice-independence or equivalence.
- For implementation code: public types correspond to grounded mathematical categories. Raw `Parent`/`Element` surface leaks are absent.

**Sources to consult:** `category_specs/*/docs/MAPPING.md`, `category_specs/*/docs/SAGE_INVENTORY.md`, Sage written docs/source, `theory/references/index.md`, and any linked decision cards.

**Failure modes:**
- **Ungrounded definition** (definition present but not sourced) → `revision-required`. Record the missing source.
- **Missing definition** (speculative spec writing, no definition recorded) → `revision-required`. Split a source-mining or decision leaf.
- **Ambiguous term** (multiple plausible meanings, no decision recorded) → `revision-required`. Split a decision card. Parent blocked until decided.
- **Raw Sage type leak** (`Parent`/`Element` on public API without mathematical alias) → `revision-required`.

### Gate 2: Acceptance Criteria

The work must satisfy its own acceptance criteria and every applicable parent criterion.

**Check:**
- Card's `successCriteria` or `acceptanceCriteria` -- verify each item against the artifacts.
- Parent card's `successCriteria` -- verify each item that applies to this child.
- If this card claims to discharge a parent-plan obligation: is the claim explicit and backed by evidence?

**Failure modes:**
- **Own criteria unmet** → `revision-required`. List each unmet item.
- **Parent criteria violated** → `revision-required`. This is a backsliding offense; see also Gate 4. List the parent criteria and how they are violated.
- **Discharge claim unbacked** → `revision-required`. Card claims to discharge a parent obligation but evidence is missing.

### Gate 3: Spec-Weakening (category-spec cards)

No spec obligation may be deleted, weakened, narrowed, or relocated without a source-grounded replacement owner.

**Check (patch-level):**
```
git diff --cached
git diff
# and any commits created during the work, via git show <commit>
```
Inspect with a patch view. Flag:
- Deleted abstract methods or `@abstract_method` decorators
- Removed constructor/category obligations from `Constructors()` namespaces
- Narrowed smoke assertions (fewer checks, weaker predicates, shallower probes)
- Weakened acceptance criteria in any touched card body
- Moved obligations to a card/phase/plan without a source-grounded replacement owner
- Sage-gap-driven interface shrinkage (the smoke got quieter but the spec got smaller)

**Failure modes:**
- **Any of the above** → `revision-required`. Document the exact deletion/weakening and the missing replacement owner. The rework must either restore the obligation verbatim or provide a grounded replacement card.
- **Smoke improvement paired with interface shrinkage** → `revision-required`. This is a spec-regression task failure regardless of command output.

### Gate 4: Gradient (Backsliding Detection)

The work must not reverse, weaken, or contradict any previously established truth.

**Baseline artifacts (in priority order):**

1. **Decided decision cards** -- Scan `plans/features/*/decisions/` for cards with `status: decided` or `status: implemented`. Does the work reverse the chosen outcome? Does it reintroduce a rejected alternative?
2. **Previously approved specs** -- Are `specs/*.md` files modified? Does `git diff` show removal of accepted requirements?
3. **Previously passing smokes** -- Does `just smoke` produce new failures on assertions that previously passed? Compute against the last known-good smoke baseline.
4. **Previously resolved TODO entries** -- Has a resolved observation from `.agents/TODO.md` history been reintroduced?
5. **Git history of committed work** -- Does `git log` show previous commits that established invariants, tests, or properties the current work implicitly reverts?
6. **Approved plans and phase cards** -- Do modified `PHASE-*.md` or `PLAN-*.md` files show removed or weakened phase gates?

**Gradient computation:**
```
gradient(dimension) = post_state(dimension) - baseline_state(dimension)
```
A negative gradient on any dimension is a finding. The review records which dimension, the baseline value, and the post-work value.

**Decision-card gradient check (explicit procedure):**
1. List all decided decision cards in the owning feature tree.
2. For each decision, extract the `chosen` value and the implications described in the card body.
3. Check the work artifacts for any action, definition, naming, or structure that contradicts a chosen outcome or adopts a rejected alternative.
4. If a contradiction is found AND no superseding decision card exists → `revision-required`.
5. If a contradiction is found and a superseding decision card exists → the gradient is intentional. Note it in the review log but do not block.

**Smoke gradient check:**
```bash
# Record baseline (from last known-good commit or a cached snapshot)
just smoke 2>&1 | tee /tmp/smoke-baseline.txt

# Post-work
just smoke 2>&1 | tee /tmp/smoke-post.txt

# Compute gradient
diff /tmp/smoke-baseline.txt /tmp/smoke-post.txt
```
- New failures → negative gradient → flag.
- New passes → positive gradient.
- Disappeared assertions (the smoke file itself changed) → Gate 3 violation, not a gradient finding.

**Failure modes:**
- **Decision reversal without superseding card** → `revision-required`. Design-level defect.
- **Previously passing smoke now fails** → `revision-required` or `blocked` (if the failure reveals a genuine prerequisite gap).
- **Previously resolved TODO reappears** → `revision-required`.
- **Previously approved spec surface removed** → `revision-required`. May overlap with Gate 3.
- **Implicit decision contradicting repo policy** → `revision-required`. Examples: creating a local workaround when `research-software-wiring` requires backend-first routing; introducing variadic option-bag constructors after `PHASE-VARIADIC-SIGNATURE-CLOSURE-AUDIT` was approved.

### Gate 5: Mathematical Correctness

The mathematical content must be correct and the evidence must match the claim's escalation tier.

**Check by card type:**
- **Spec cards:** Are claims well-typed? Do they form a coherent interface (no missing required methods, no contradictory obligations)? Are hypotheses explicit?
- **Implementation tasks:** Do tests pass? Does the implementation actually implement what the spec requires? Is the algorithm correct for the claimed generality?
- **Research tasks:** Does the evidence support the claim at the appropriate escalation tier (exploratory, local-promotion, GOAL-discharge)?

Use `research-proof-auditing` for evidence sufficiency. The argument-shape gate applies: reject notes that replace construction with naming, cite authority without stating hypotheses, or inflate immediate consequences into claims. The standardness calibration memory applies: do not flag trivial derivations as gaps, and do not accept niche claims without precise citations and hypothesis checks.

**Failure modes:**
- **Tests fail** → `revision-required`.
- **Mathematical error in spec** (contradictory axioms, ill-typed method signatures) → `revision-required`.
- **Cheaper proxy evidence** (proves a weaker claim, uses numerics where exactness is required) → `revision-required`.
- **Escalation tier mismatch** (GOAL-discharge language on exploratory evidence) → `revision-required` or `blocked` (if additional evidence infrastructure is needed).

### Gate 6: Style and Compliance

The work must follow repo style and compliance rules.

**Check:** Load `category-spec-style`, `clean-code`, and `anti-slop`. Verify:
- No raw `ConditionSet` on public API surfaces (must be wrapped in project aut/subobject objects)
- No broad variadic option-bag constructors as public surface
- Import hygiene (no unused imports, no lazy-import bloat)
- Type annotations present and correct
- No AI-slop patterns (boilerplate docstrings, placeholder prose, fake tests)
- Task-local agent-authored commit messages follow Conventional Commit format

**Failure modes:**
- **Style violations** → `revision-required`. Minor fixes; document which rule is violated.
- **Anti-slop patterns** → `revision-required`. May require rewriting generated prose.
- **Multiple style violations** → aggregate into a single checklist in the revision-required card.

**Commit-history scope:**
- Gate 6 commit-message compliance applies to the commits created to discharge the
  card under review, especially agent-authored implementation, spec, migration, or
  review commits.
- Historical human checkpoint commits that are already ancestors of `origin/main`
  are provenance, not per-card style failures. Do not convert every card touched by
  such a checkpoint into `blocked` or `revision-required`.
- If a historical checkpoint introduced a substantive defect, fail the gate that
  covers the defect itself: Gate 1 for ungrounded definitions, Gate 3 for spec
  weakening, Gate 4 for backsliding, Gate 5 for mathematical error, or Gate 6 for
  current style/content defects. The commit message alone is not the blocker.
- Published commits that used forbidden git operations such as `--no-verify` may
  still be recorded as process findings, but do not treat them as global blockers
  for unrelated ready leaves. Scope the finding to the card whose reviewed work
  actually depends on that commit and continue other DAG-ready work.

## Review procedure

This is the procedure executed by the **review subagent** (a fresh-context agent
dispatched by the coordinator):

```
1. Receive the card body, work artifact paths, and baseline artifact paths from
   the coordinator.
2. Verify the card is not oversized. If it hides major theorem, algorithm,
   convention, or trusted-base work, report this to the coordinator and do not
   proceed with gates.
3. Read the card body.
4. Read the work artifacts and baseline artifacts.
5. Apply Gates 1-6 in order:
   a. Run the checks for the current gate.
   b. If the gate passes, record the concrete evidence and proceed.
   c. If the gate fails, stop. Record findings. Set outcome. Do not continue to
      later gates.
6. If all gates pass → outcome is complete/done.
7. If any gate fails → outcome is revision-required or blocked:
   - revision-required: the work can be fixed within this card's scope.
   - blocked: a new prerequisite card (decision, source-mining, backend-gap) must
     be created and resolved before this card can proceed.
8. Write the review log into the card body under ## Review Log and return it to
   the coordinator.
```

This is the procedure executed by the **coordinator** after the review subagent
completes:

```
1. Receive the review log from the subagent.
2. Verify the review for box-checking:
   a. Every gate pass has an associated concrete artifact (file path, command run,
      diff inspected, source consulted).
   b. The review contains no forbidden language: "looks good", "appears correct",
      "seems fine", "no issues found" without specific examination.
   c. Failures cite specific code, line numbers, source paths, or test output.
   d. The outcome is supported by the findings (a list of passed gates with no
      failures should not produce revision-required; a gate failure should not
      produce complete/done).
3. If the review is substantive → apply the status change (or prepare it for human
   approval if the final gate requires it).
4. If the review is a box-checking exercise → reject it. Document the specific
   deficiencies. Re-dispatch to a review subagent with a tightened prompt that
   quotes the anti-boxchecking rules and demands concrete evidence for every gate.
```

## Review Log format

Each review produces a dated entry in the card body:

```markdown
## Review Log

### Review YYYY-MM-DD (Reviewer)

**Gates passed:** Gate 1 Definition Grounding, Gate 2 Acceptance Criteria, ...
**Gates failed:** Gate 3 Spec-Weakening, ...
**Outcome:** revision-required

#### Gate 3 Findings: Spec-Weakening

- `category_specs/rings/subcategories/fields.py:42` -- Deleted `KroneckerSymbolField`
  from `Constructors()` without a replacement card. This surface must be restored or a
  grounded replacement card must be created before re-review.

- `category_specs/rings/subcategories/fields.py:78` -- Smoke assertion narrowed from
  `check_method_surface(R, expected_methods=15)` to `check_method_surface(R,
  expected_methods=12)`. The deleted methods (`torsion_subgroup`, `class_group`,
  `class_number`) were category-spec obligations. Missing grounded replacement card.

**Required fixes:**
1. Either restore `KroneckerSymbolField` to `Constructors()` or create a source-grounded
   card that replaces it.
2. Restore the smoke assertion to 15 expected methods or document where each of the 3
   removed methods was moved with a grounded replacement owner.

**Re-review criteria:**
- `git diff` from the rework must show no net deletion of `Constructors()` entries
  without grounded replacement cards.
- Smoke method count must match or exceed the previous baseline of 15, OR the 3 removed
  methods must have explicit grounded replacement cards.

---
```

## Escalation during review

If a review reveals findings that cannot be resolved within the current card:

- **Human input needed** (the review determines that a human decision, policy choice, or evaluation is required that an agent cannot provide) → Set `status: needs-human-input`, record the specific question or decision needed in the card body, and optionally link a decision card. The card remains `needs-human-input` until a human provides input.
- **Discovered blocker** (a prerequisite decision, source-mining result, or backend gap is needed to proceed) → Set `status: blocked`, set `blocked_reason` to a one-line description of the gap and the prerequisite card ID, create the prerequisite card, and link it in `dependsOn`.
- **Design-level defect** (the card's fundamental approach is wrong, not the implementation) → Set `status: revision-required`, but note that the rework may require plan-level redesign. Create a decision card or plan-review task.
- **Pattern repeated across multiple cards** (same gate failure on N cards) → Create a phase-level corrective card. Do not rework N cards independently for the same systemic issue.

Do not set `status: blocked` for planned upstream dependencies already expressed in `dependsOn`. Those cards remain `unstarted` until their dependencies resolve.

Do not set `status: blocked` for planned upstream dependencies already expressed in `dependsOn`. Those cards remain `unstarted` until their dependencies resolve.

## What this kernel does not govern

- **Plan approval** -- Plans are human-gated before decomposition; the review kernel applies to their child cards after execution.
- **Feature approval** -- Features are always human-gated.
- **GOAL.md discharge** -- Requires the full composed-goal audit described in the execution kernel; the review kernel handles card-level review, not program-level discharge.
- **QC transition gate** -- QC is phase-transition evidence, not a per-card review step. QC failures during review should be recorded but do not by themselves block a spec card during spec-phase work.
- **Adversarial audit** -- The review kernel's reviewer is independent but focused on gate compliance. Full adversarial attack (trying to break the strongest claim by any means) is a separate state-machine stage following card-level review, governed by `research-proof-auditing`.

## Load with

- Load `research-proof-auditing` for proof, evidence, and fraud checks within Gate 5.
- Load `category-spec-style` for style and compliance checks within Gate 6.
- Load `category-spec-audit` for mathematical ownership, spec surface, and downstream-poisoning checks across Gates 3-5.
- Load `research-orchestration` for delegation of review to independent agent sessions.

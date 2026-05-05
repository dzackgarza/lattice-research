# Research Execution Kernel

This is the canonical simplified state machine for the research repo. It replaces the old ad hoc task-directory machine with a Nimbalyst-integrated workflow.

## Core invariant

No process label creates mathematical trust. Trust comes only from the artifacts that justify the claim: exact statement, sourced proof, replayable computation, formal proof, certificate, counterexample, PR diff, review decision, and linked plan/card history.

## Canonical objects

Use five objects only:

- `GOAL.md`: the read-only research objective spine.
- `plans/features/**`: active feature, spec, plan, phase, task, and decision cards.
- `.agents/current-goal-phase.md`, `.agents/TODO.md`, and `.agents/retired/**`: phase marker, scratchpad inbox, and short-term retired legacy cards.
- Git branches, PRs, commits, and worktrees: provenance, review, and merge gates.
- Produced artifacts in their natural durable roots: `src/`, `tests/`, `notes/`, `theory/`, `lean/`, and linked proof/computation outputs.

Do not create a parallel `tasks/T-XXXX` planning universe for new work. A tracked Nimbalyst card is the task spec. Its frontmatter and body must contain enough context for another agent to execute without chat recovery.

## Live stages

### Plan

Use planning only when work is complex, architectural, mathematically foundational, or multi-card. Plans are human + LLM collaborative artifacts. They require explicit human approval before decomposition or execution.

A plan records goal links, phases, dependencies, risks, acceptance strategy, and high-level task inventory. It does not replace task cards.

### Specify card

Each executable unit becomes a tracked `task` card under `plans/features/FEATURE-ID/plans/PLAN-ID/PHASE-ID/tasks/`. The card must define the exact claim or work target, source provenance, plan or `GOAL.md` link, accepted scope, owner/role if known, complexity, dependencies, acceptance criteria, verification plan, and branch/PR policy when relevant.

For mathematical claims, the card must state whether it is exploratory, preparatory, local-claim promotion, or `GOAL.md` discharge.

### Preflight

Before execution, reject or split any card that hides major work. Hidden major work includes choosing or inventing the core algorithm, building reusable exact infrastructure, proving a new reduction theorem, fixing a convention that changes downstream meaning, or solving a classification/search problem comparable to the nominal task.

For mathematical spec work, preflight must also reject cards whose definitions are not
source-grounded. A card is not ready for spec editing until it records the canonical
source path or reference, exact definition, hypotheses, codomain/return object, and any
proof obligation for choice-independence or equivalence with another notion. Old TODO
lines, migrated cards, common terminology, and plausible special-case intuition do not
meet this bar.

If a term has multiple plausible meanings, or if a familiar special case suggests an
equivalence that has not been proved under explicit hypotheses, split to a decision or
source-mining card. Keep the affected spec leaf blocked until the distinction is
resolved. Do not normalize bespoke project terminology to the most common textbook or
Sage interpretation by default.

If the shared mathematical base lacks the noun, method, morphism, coercion, constructor, or backend bridge needed to express the task cleanly, stop and create the base task. Do not patch around the gap locally.

This stop is path-local. It blocks the current implementation or claim path, not the
active phase. After creating or updating the prerequisite task, continue another
approved active leaf if one exists.

### Continuation and blocker test

An agent may report that there is no path forward only after checking the current
phase marker, approved plans, and active leaf cards. Every remaining active leaf must
have a concrete current-phase blocker.

The following are not global blockers during approved spec-phase work:

- QC failures outside a user-requested QC pass, commit integration pass, or phase
  transition.
- Downstream-phase guards against Coble, lattice implementation, raw matrix, orbit,
  or geometry computations.
- Overscoped cards that can be split, promoted to an approved plan, or decomposed.
- Missing vocabulary or backend bridges when a prerequisite spec, decision, research,
  or implementation-gap card can be filed.
- Human approval gates for acceptance, closure, or phase transition when ordinary
  approved leaf execution remains.

If a spec leaf can advance through source mining, writing/refining a spec, centralizing
terminology, drafting audit criteria, capturing a decision, splitting work, or filing a
prerequisite, continue there.

### Execute

Run nontrivial implementation in the required branch/worktree and within the card's allowed scope. The implementing agent updates the card with files touched, branch, PR, validation notes, blockers, and follow-up findings. The implementing agent does not mark accepted/done/closed.

Small administrative metadata edits can be direct when the repo workflow allows them. Production code, canonical docs, mathematical infrastructure, and agent-guiding docs require branch/PR routing according to the project workflow.

### Replay and attack

Replay/attack is required when a card claims mathematical correctness, proof evidence, code correctness, state-machine acceptance, or parent-plan discharge. Use `research-proof-auditing` for proof and evidence sufficiency. Use independent review where failure modes must be separated from the implementation context.

Attack the strongest claim made anywhere: title, card body, plan, PR, filenames, summary, comments, and downstream references.

### Promote, reject, split, or retire

Promotion means the linked artifacts support the exact claim and the human gate has approved the result. Otherwise reject, split, or send back to planning.

Resolved cards leave active paths and move to `.agents/retired/` only while short-term reference is useful. Durable history belongs in git commits, PR bodies, plan history, canonical decisions, and durable docs.

## Escalation tiers

### Exploratory or preparatory

Requires a tracked card, scoped work, source provenance, and replayable artifacts if any. No theorem-discharge language is allowed.

### Local claim promotion

Requires proof/evidence audit, exact claim-surface alignment, checked dependencies, and a clear parent-sufficiency edge explaining what burden is discharged.

### `GOAL.md` discharge

Requires final composed-goal audit, assumption unification, exact theorem or counterexample statement, provenance for all imported artifacts, and human approval.

## Tangential findings

During work, discoveries route through the lightest safe mechanism:

- File a real tracked card immediately when the finding is concrete enough to execute.
- Add a short entry to `.agents/TODO.md` when it needs investigation before carding.
- Delegate a cheap branching investigator when important but tangential.
- Create a decision card for naming, ownership, mathematical, or organizational choices.

Do not bury follow-up obligations in chat, implementation comments, or PR summaries as the only durable record.

## Replan rule

Replanning is valid only when it reduces the real burden: clarified claim, exposed hidden major work, separated base admission, discharged prerequisite, or removed ambiguity. Replan churn that only adds paperwork is failure.

## Acceptance rule

A sprint item, task card, theorem claim, or `GOAL.md` item is not complete because an agent says it is complete. It is complete only when the Nimbalyst card, linked plan, artifacts, git/PR evidence, proof-audit evidence when applicable, reviewer decision, and current canonical docs all agree.

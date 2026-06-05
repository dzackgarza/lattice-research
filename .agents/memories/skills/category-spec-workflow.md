---
title: Category Spec Workflow
status: active
date: 2026-05-29
---
# Category Spec Workflow

This skill is the canonical agent-facing workflow authority for category-spec project
management.

## Canonical source

The source of truth is this skill plus `references/workflow.md`.

Read `references/workflow.md` before changing workflow state.

## Use this skill for

- Creating, moving, normalizing, or retiring cards.
- Setting status, priority, complexity, progress, tags, or plan links.
- Creating or decomposing approved plans.
- Recording decisions or tangential findings.
- Updating `.agents/TODO.md`.
- Preparing visual windows into the work.
- Coordinating branch, PR, validation, and review metadata.

## Hard reminders

- There is no separate backlog; active cards are the outstanding work set.
- Plans require human + LLM planning and approval before execution.
- Approved plans plus active cards define the concrete continuation surface.
  Do not substitute abstract blocker analysis for selecting and advancing an approved
  active spec leaf.
- Sage constructor/method inventory and mapping progress is controlled by
  `[[SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER]]`, not by surrounding process artifacts.
  The required object is the finite set difference
  `Remaining = U - C - R - Q`. A progress claim must name rows moved from `Remaining`
  into classified, rejected, or decision-needed states; row counts, file counts, review
  prose, handoff edits, and broad checkpoints are not completion evidence.
- Plans, phases, and tasks that touch category specs must put the ideal-interface
  invariant at the local decision point: specs extend Sage's category/object universe,
  current Sage coverage is not the adequacy standard, Sage interop remains a design
  constraint where mathematically appropriate, smokes expose current implementation
  gaps, and spec obligations are preserved unless a grounded replacement owner carries
  them.
- Plans, phases, and tasks that touch type checking, implementation inheritance, or
  category constructors must also ask whether each "fix" directionally aligns with the
  framework design. Mathematical subcategories may refine operations beyond ordinary
  software method-subtype rules, and dynamic provider inheritance is intentional.
  Do not accept local casts, trivial wrappers, explicit subclassing, or
  provider-splicing when the real issue is that QC tooling lacks the Sage/category
  static model. Create or route a dedicated QC-tooling task that teaches the checker to
  enforce the convention; do not mark the finding as ignorable or silence it in the
  local code. QC-zero must not be achieved by contorting the mathematical surface into
  warning-free but conceptually worse code.
- Casting in category-spec work is a review trigger.
  Non-isolated casts or cast patterns must not be accepted as ordinary hygiene; route a
  decision about whether the spec is doing too much implementation work, whether the
  type obligation belongs at a downstream implementation boundary, or whether QC tooling
  must learn the inherited category-promotion convention.
- Plans, phases, and tasks that touch category specs must also include a spec-weakening
  review gate before advancement: inspect staged changes, unstaged changes, and any
  task-local commits for deleted obligations, narrowed smokes, or moved spec surfaces
  without source-grounded replacement owners.
- A spec leaf is executable only after definition grounding: it must identify canonical
  mathematical sources, exact definitions, hypotheses, and proof/decision obligations.
  Vague migrated backlog text must be refined before spec editing.
- A blocker must be tied to the current phase and current leaf.
  Downstream guards, non-transition QC failures, implementation-only gates, oversized
  cards that can be split, and missing prerequisites that can be carded do not justify
  exiting while approved spec leaves remain.
- `needs-human-input` is not a parking status for agent uncertainty.
  Use it only after source review, math grounding, repo policy, and `dependsOn` show
  that a real human convention or scope decision remains.
- `needs-human-input` is also not a completion shortcut.
  A clean review awaiting closure, ordinary parent approval, or an approval-shaped
  yes/no on policy-forced routing is not a human decision.
  Route agent-executable work through `needs-agent-review`, `revision-required`, or
  ordinary completion instead.
- If an obvious mathematical fact or source-forced category edge is surfaced as a human
  decision, fix the process artifact that let it escalate: missing owner row, missing
  subcategory relationship, stale status, incomplete dependency, or weak review rubric.
- Constructor cards must separate mathematical owner, human-facing named-constructor
  convention, and code-maintenance owner.
  Aggregate constructor surfaces can expose canonical entry points even when
  implementation lives on a more specific owner.
- Priority and complexity are metadata, not tags.
- Load `category-spec-priority-rubric` and `category-spec-complexity-rubric` before
  scoring cards.
- Theme tags group workstreams; they do not order work.
- Durable history belongs in git, PRs, plan history, and canonical decisions/docs.
- Completed or resolved cards move to `.agents/retired/` only as temporary working
  residue.

## Tangential-work routing

When work reveals a bug, inconsistency, smell, missing decision, stale source, or
possible downstream-poisoning risk, choose the lightest safe route:

- File a real tracked card immediately when the finding is concrete enough to execute.
- Add a short entry to `.agents/TODO.md` when the finding needs investigation before it
  can become a card.
- Delegate a cheap branching investigator when the finding is important but tangential
  to the current task.
- Create a decision card when the blocker is a naming, ownership, mathematical, or
  organizational choice.
- Treat blockers as path-local by default: stop the affected card, make the finding
  durable, set the affected leaf card to `status: blocked` when the tracker schema
  supports it, and continue another approved active leaf unless every remaining leaf is
  concretely blocked in the current phase.

Do not bury follow-up work in chat, commit messages, or inline comments as the only
record.

## Referenced documents

[Category Spec Workflow Reference](category-spec-workflow/workflow)

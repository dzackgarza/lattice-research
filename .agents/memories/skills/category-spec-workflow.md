---
title: Category Spec Workflow
status: active
date: 2026-05-29
---
# Category Spec Workflow

This skill is the canonical agent-facing workflow authority for category-spec project
management.

## Canonical source

The source of truth is this memory plus `mem:skills/category-spec-workflow/workflow`.

Read `mem:skills/category-spec-workflow/workflow` before changing workflow state.

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
- Spec obligations are preserved unless a grounded replacement owner carries them.
- Casting in category-spec work is a review trigger.
- A spec leaf is executable only after definition grounding.
- `needs-human-input` is not a parking status for agent uncertainty.
- Priority and complexity are metadata, not tags.
- Load rubric skills before scoring cards.
- Durable history belongs in git, PRs, plan history, and canonical decisions/docs.

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
- Treat blockers as path-local by default.

Do not bury follow-up work in chat, commit messages, or inline comments as the only
record.

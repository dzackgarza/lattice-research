---
name: category-spec-workflow
description: 'Use when handling category-spec workflow state: cards, plans, decisions,
  TODO triage, retired cards, visual windows, branch/PR routing, validation handoff,
  or status updates.'
---

# Category Spec Workflow

This skill is the canonical agent-facing workflow authority for category-spec project management.

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
- Priority is metadata, not a tag.
- Theme tags group workstreams; they do not order work.
- Durable history belongs in git, PRs, plan history, and canonical decisions/docs.
- Completed or resolved cards move to `.agents/retired/` only as temporary working residue.

## Tangential-work routing

When work reveals a bug, inconsistency, smell, missing decision, stale source, or possible downstream-poisoning risk, choose the lightest safe route:

- File a real tracked card immediately when the finding is concrete enough to execute.
- Add a short entry to `.agents/TODO.md` when the finding needs investigation before it can become a card.
- Delegate a cheap branching investigator when the finding is important but tangential to the current task.
- Create a decision card when the blocker is a naming, ownership, mathematical, or organizational choice.

Do not bury follow-up work in chat, commit messages, or inline comments as the only record.

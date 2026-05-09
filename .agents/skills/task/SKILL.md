---
description: Track planning work items as markdown files under root `plans/`.
---

# Tracking Work Items

Create tracking items as markdown files under `plans/features/` using registered
standard types and tags.

## Registered Types

Read `.nimbalyst/trackers/*.yaml` before creating an item. Use one of the registered
planning types: `feature`, `spec`, `plan`, `phase`, `decision`, or `task`.

Use tags and containment for workflow dimensions such as category-specs, implementation,
research, sprint, smoke, validation, docs-migration, and theme groups. Do not create or
use derivative tracker types such as `spec-work`, `implementation-work`,
`research-work`, `sprint-work`, `task-work`, or `agent-work`.

## Destination Rules

- `plans/features/FEATURE-ID/FEATURE-ID.md`: feature cards.
- `plans/features/FEATURE-ID/specs/SPEC-ID.md`: spec cards owned by a feature.
- `plans/features/FEATURE-ID/decisions/DECISION-ID.md`: decision cards owned by a feature.
- `plans/features/FEATURE-ID/plans/PLAN-ID/PLAN-ID.md`: plan cards.
- `plans/features/FEATURE-ID/plans/PLAN-ID/PHASE-ID/PHASE-ID.md`: phase cards.
- `plans/features/FEATURE-ID/plans/PLAN-ID/PHASE-ID/tasks/TASK-ID.md`: executable task cards.

Do not create aggregate tracker indexes. The GUI is the index. There is no separate
backlog; active tracked cards under `plans/features/` are the outstanding work set.

## Frontmatter

Use `trackerStatus`, not `trackingStatus`. Card IDs must match filename stems.

```markdown
---
id: TASK-EXAMPLE
trackerStatus:
  type: task
parents:
- '[[PHASE-EXAMPLE]]'
dependsOn: []
title: Brief executable description
status: unstarted
priority: medium
description: Brief executable description.
successCriteria:
- Observable acceptance criterion.
complexity: 40
---
```

The `trackerStatus.type` value must match a registered schema. Keep metadata compact;
put detailed grounding, acceptance criteria, examples, audit notes, and work logs in
the body.

For category-spec cards, load `category-spec-priority-rubric` before setting `priority`
and `category-spec-complexity-rubric` before setting `complexity`. Do not encode
priority or complexity as tags.

## Body Requirements

Full-document bodies must include enough context for another agent to act without chat
recovery. Use at least:

- `Summary`
- `Source Provenance`
- `Context`
- `Acceptance Criteria`
- `Dependencies And Boundaries`
- `Work Log`

Inline tracker syntax is only for temporary discovery placeholders. Convert anything
ready for assignment or execution into a full markdown file under `plans/features/`.

## Execution Steps

1. Read `.nimbalyst/trackers/*.yaml`.
2. Select a registered standard type.
3. Convert workflow words such as spec, implementation, research, or sprint into tags
   and destination path.
4. Generate the item file under `plans/features/` with `trackerStatus` frontmatter.
5. Preserve source provenance and enough execution context in the body.
6. Confirm the destination file.

## Hard Constraint

Never call `tracker_create` or `create_task`. The markdown file is the source of truth;
calling a tracker tool creates duplicates.

## Sizing

A task is atomic when a subagent with zero repo context, given only the card
body and artifact paths, can complete it in one pass without discovering scope,
making classification decisions, or synthesizing cross-subtree findings.

Before creating a task, ask: can the subagent start work immediately after
reading the card? Or does it first need to figure out what to do?

**Not atomic:** "Audit all super_categories() in category_specs/" — the
subagent must discover which files exist, understand the category hierarchy,
decide what counts as "documented," and synthesize a cross-subtree report.
That's a research project.

**Atomic:** "Grep category_specs/rings/ for super_categories(, extract each
returned list, write a table into the plan body" — the subagent reads the card,
runs the grep, writes the table. No discovery, no classification, no synthesis.

**Concrete test:** if the card body contains the word "all" followed by a
directory path spanning multiple subtrees, it's a survey. Split by subtree.
If the card asks the subagent to "determine," "classify," "decide whether,"
or "cross-reference," those are coordinator-level judgments — the coordinator
does that work, the subagent executes the mechanical step.

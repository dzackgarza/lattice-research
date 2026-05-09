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

A task is one mechanical operation a subagent completes in a single pass without
timing out. Concrete bounds:

- **Files touched:** at most ~10 files read, at most ~3 files edited.
- **Scope:** one subtree (e.g., `category_specs/rings/`), not "all of category_specs/."
- **Operation:** grep-and-extract, write-one-section, fix-one-contradiction — not
  "audit everything" or "fill the entire table."

If a task description starts with "audit all ... across" or "fill the ... with all
results," it's a survey — split by subtree. Three 5-minute greps are better than
one 20-minute file-reading marathon that times out.

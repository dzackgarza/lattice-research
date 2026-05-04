---
description: Track bugs, tasks, ideas, decisions, and related work items as markdown files under `.agents`.
---

# Tracking Work Items

Create tracking items as markdown files under `.agents` using registered standard types
and tags.

## Registered Types

Read `.nimbalyst/trackers/*.yaml` before creating an item. Use one of the registered
standard types: `automation`, `bug`, `decision`, `feature`, `idea`, `plan`, or `task`.

Use tags and `.agents` placement for workflow dimensions such as `spec`,
`implementation`, `research`, `sprint`, and `category-specs`. Do not create or use
`spec-work`, `implementation-work`, `research-work`, `sprint-work`, `task-work`, or
`agent-work` types.

## Destination Rules

- `.agents/plans/`: plan and sprint-plan documents using `trackerStatus.type: plan`.
- `.agents/decisions/`: decisions using `trackerStatus.type: decision`.
- `.agents/tasks/spec/`: spec-surface work using `task`, `bug`, `feature`, or `idea`.
- `.agents/tasks/implementation/`: implementation work using `task`, `bug`, `feature`,
  or `idea`.
- `.agents/tasks/research/`: research work using `task`, `bug`, `feature`, or `idea`.

Do not create aggregate tracker indexes. The GUI is the index.

There is no separate backlog. Active tracked cards under `.agents` are the outstanding
work set. Resolved, rejected, implemented, or superseded cards should leave active paths
and move to `.agents/retired/` only while short-term reference is useful.

## Frontmatter

Use `trackerStatus`, not `trackingStatus`.

```markdown
---
trackerStatus:
  type: task
title: Brief executable description
status: to-do
priority: medium
tags:
  - category-specs
  - implementation
created: YYYY-MM-DD
complexity: 40
progress: 0
---
```

The `trackerStatus.type` value must match a registered schema. Put `title`, `status`,
`priority`, `tags`, `complexity`, `progress`, and other fields at the top level of the
frontmatter.

For category-spec cards, load `category-spec-priority-rubric` before setting
`priority` and `category-spec-complexity-rubric` before setting `complexity`.
Do not encode priority or complexity as tags.

## Body Requirements

Full-document bodies must include enough context for another agent to act without chat
recovery. Use at least:

- `Summary`
- `Source Provenance`
- `Context`
- `Complexity And Ownership`
- `Acceptance Criteria`
- `Dependencies And Boundaries`
- `Validation Requirements`
- `Work Log`

Inline tracker syntax is only for temporary discovery placeholders. Convert anything
ready for assignment or execution into a full markdown file under `.agents/tasks/...`.

## Execution Steps

1. Read `.nimbalyst/trackers/*.yaml`.
2. Select a registered standard type.
3. Convert workflow words such as `spec`, `implementation`, `research`, or `sprint` into
   tags and destination path.
4. Generate the item file under `.agents` with `trackerStatus` frontmatter.
5. Preserve source provenance and enough execution context in the body.
6. Confirm the destination file.

## Hard Constraint

Never call `tracker_create` or `create_task`. The markdown file is the source of truth;
calling a tracker tool creates duplicates.

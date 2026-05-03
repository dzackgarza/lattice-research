---
name: track
description: Use when creating tracking items from `/track` commands. Map requests to registered standard tracker types, write markdown under `.agents`, and use tags/path placement for workflow class.
---

# /track Command

Create a tracking item in the correct `.agents` location.

## Usage

```text
/track [type] [description]
```

Examples:

- `/track bug Ring constructor returns the wrong refined type`
- `/track task Remove raw ConditionSet from public Aut surface`
- `/track idea Add a constructor smoke example for compact real intervals`
- `/track decision Decide where Hom/End/Aut ownership belongs`

## Registered Types

Read `.nimbalyst/trackers/*.yaml` before creating an item. Use one of the registered
standard types: `automation`, `bug`, `decision`, `feature`, `idea`, `plan`, or `task`.

Use tags and `.agents` placement for workflow dimensions such as `spec`,
`implementation`, `research`, `sprint`, and `category-specs`. Do not create or use
`spec-work`, `implementation-work`, `research-work`, `sprint-work`, `task-work`, or
`agent-work` types.

## Destination Rules

- Plans and sprint plans go under `.agents/plans/` with `trackerStatus.type: plan`.
- Decisions go under `.agents/decisions/` with `trackerStatus.type: decision`.
- Tasks, bugs, features, and ideas go under `.agents/tasks/spec/`,
  `.agents/tasks/implementation/`, or `.agents/tasks/research/` according to the work
  class.
- Automation records are non-creatable unless project tooling owns them.

Do not create aggregate index files. The GUI is the index.

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
  - spec
created: YYYY-MM-DD
complexity: 40
progress: 0
---
```

The `trackerStatus.type` value must match a registered schema. Put `title`, `status`,
`priority`, `tags`, `complexity`, `progress`, and other fields at the top level of the
frontmatter.

Set `priority` from the category-spec rubric by loading `category-spec-workflow` when
the work is category-spec related. Do not encode priority as a tag.

## Body Requirements

Full-document task bodies must include enough context for another agent to act without
chat recovery. Use at least these sections:

- `Summary`
- `Source Provenance`
- `Context`
- `Acceptance Criteria`
- `Dependencies And Boundaries`
- `Work Log`

Inline tracker syntax is only for temporary discovery placeholders. Convert anything
ready for assignment or execution into a full markdown file under `.agents/tasks/...`.

## Execution Steps

1. Read `.nimbalyst/trackers/*.yaml`.
2. Map the requested type to a registered standard type.
3. Convert workflow words such as `spec`, `implementation`, `research`, or `sprint` into
   tags and destination path, not tracker types.
4. Generate the item file under `.agents` with `trackerStatus` frontmatter.
5. Preserve source provenance and enough execution context in the body.
6. Confirm the destination file.

## Migration Requirements

When migrating existing docs, preserve substantive context in the full-document body:
source paths, original heading or line, acceptance criteria, and known boundaries. Never
collapse real work into a one-line tracker row.

## Hard Constraint

Do not call `tracker_create` or `create_task`. The markdown file is the source of truth;
calling a tracker tool creates duplicates.

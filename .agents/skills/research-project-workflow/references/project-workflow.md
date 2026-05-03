# Research Project Workflow Reference

## Nimbalyst tracker workspace

All planning, organization, task, bug, feature, idea, automation, and decision documents for this repo live under `.agents` and are organized by broad category.

Use `.agents/plans/` for plan and sprint-plan documents. Organize plans by staged
phase under `.agents/plans/phase-*`; use `.agents/current-goal-phase.md` to identify
which phase is active. Use `.agents/decisions/` for documented decisions. Use
`.agents/tasks/implementation`, `.agents/tasks/spec`, and `.agents/tasks/research` for
task, bug, feature, and idea work items. Use `.agents/retired/` for completed or
retired cards kept temporarily before deletion.

Do not create `nimbalyst-local/tracker` indexes or parallel task inventories. The GUI is the index. Use GUI filtering/search for agent-facing work, and use CLI/YAML parsing against `.agents` only when scripting is needed.

There is no separate backlog. The active tracked cards are the outstanding work set. When work is implemented, resolved, rejected, or superseded, move the card out of active paths and retire or delete it according to the retired-card policy.

A plan is not a task container. A plan defines high-level phases and milestones. Each execution item must exist as its own dedicated tracked file.

## Standard tracker types and tags

Accepted `trackerStatus.type` values are the registered schemas in `.nimbalyst/trackers/*.yaml`: `automation`, `bug`, `decision`, `feature`, `idea`, `plan`, and `task`.

Use tags such as `spec`, `implementation`, `research`, `sprint`, `category-specs`, `bug`, `smoke`, `validation`, and `docs-migration`. Use `.agents/tasks/spec`, `.agents/tasks/implementation`, and `.agents/tasks/research` to organize task files by work class. Use `.agents/plans` plus tags such as `sprint` for sprint planning.

Do not create or use derivative custom types such as `spec-work`, `implementation-work`, `research-work`, `sprint-work`, `task-work`, or `agent-work`.

## Tracker frontmatter

Use YAML frontmatter and keep metadata in `trackerStatus`, not `trackingStatus`.

```markdown
---
trackerStatus:
  type: task
title: Remove raw ConditionSet from Aut category surface
status: to-do
priority: medium
tags: [category-specs, spec]
created: '2026-05-03'
complexity: 40
progress: 10
---
```

The `trackerStatus.type` value must match a registered schema. All other metadata fields such as `title`, `status`, `priority`, `tags`, `complexity`, and `progress` go at the top level of the frontmatter, not nested inside `trackerStatus`.

Do not use `create_task` or `tracker_create` for these items. Create or update the markdown file directly under `.agents` so the file is the source of truth and is reloaded by the GUI indexer.

Keep active `.agents` paths forward-facing. After human approval, merge, rejection, or supersession, move completed or retired cards out of active task paths and into `.agents/retired/` only while they remain useful for short-term reference. Durable history belongs in git commits, PRs, plan history, and canonical decisions/docs, not in permanent piles of completed cards.

## Inline items

Avoid inline items in general. Use inline entries only as temporary placeholders while a broader task is being discovered and a full tracker file is being prepared.

Inline items define a task but provide little context by construction. Any inline item that is ready to be solved, assigned, or actively worked on must be converted into a full markdown file under `.agents/tasks/...` before execution.

Do not call `create_task` or `tracker_create` for inline items. That creates a database-only entry with no backing file and produces a duplicate.

## Planning and progressive disclosure

Use `.agents/plans/` for Nimbalyst-backed plan and sprint-plan documents. Plans are
strictly human + LLM collaborative artifacts. To create or materially revise a plan,
switch to planning mode, use the planning tools, iterate with the user until approval,
then decompose the approved plan into tracked task files. Do not enact a chat-only,
harness-local, scratch, or unapproved plan.

Plan placement is semantic. Put plan files under the phase directory they advance:
`.agents/plans/phase-00-overall-program/`,
`.agents/plans/phase-01-category-specs/`,
`.agents/plans/phase-02-sage-refinement-gap-discovery/`,
`.agents/plans/phase-03-owned-categorical-implementation/`,
`.agents/plans/phase-04-universal-categorical-algorithms/`,
`.agents/plans/phase-05-lattice-theory/`,
`.agents/plans/phase-06-geometry-coble-interfaces/`, or
`.agents/plans/phase-07-confined-experimental-research/`.

Existing active plans are currently in phase 01 unless a human explicitly moves them to
a later phase as part of phase-transition planning.

Use the built-in plan card fields (`planId`, `planType`, `progress`, status, owner, priority, and tags) on the plan file itself. Trackable plan files are the planning documents.

Break every approved plan into phases and concrete tracked files. Phases belong in the plan narrative. Executable work belongs in dedicated `task`, `bug`, `feature`, `idea`, or `decision` files under `.agents`.

Avoid inline task markers. Use `.agents/TODO.md` only as a scratchpad inbox for tangential discoveries that need investigation before they can become real cards. Convert anything executable into a full tracked file with context, source provenance, complexity, ownership, boundaries, and acceptance criteria before assignment.

Subtree `AGENTS.md` files may stay small by delegating detailed policy to local skills and skill-local references. Agents must load those skills when their task matches the documented trigger.

## Visual windows

Use `.agents/visuals/` for optional human-facing windows into complex systems. Visuals crystallize structure that is too hard to understand from code, cards, or kanban alone: category inheritance, constructor routing, subcategory-spec organization, dependency digraphs, audit flow, sprint structure, and plan-to-task breakdowns.

Visuals help humans give high-level organizational and directional input when implementation details are too in-the-weeds. Visuals are supporting material only; the operative state remains in tracked plan, task, bug, feature, idea, and decision files.

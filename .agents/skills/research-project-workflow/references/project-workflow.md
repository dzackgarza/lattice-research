# Research Project Workflow Reference

## Nimbalyst tracker workspace

All active planning, spec, task, and decision documents for this repo live under root
`plans/` and follow the central planning hierarchy:

```text
plans/features/FEATURE-ID/
├── FEATURE-ID.md
├── specs/SPEC-ID.md
├── decisions/DECISION-ID.md
└── plans/PLAN-ID/
    ├── PLAN-ID.md
    └── PHASE-ID/
        ├── PHASE-ID.md
        └── tasks/TASK-ID.md
```

Use `.agents/current-goal-phase.md` to identify the active staged-program phase. Use
`.agents/retired/` only for short-lived retired legacy cards. Do not create
`nimbalyst-local/tracker` indexes or parallel task inventories. The GUI is the index.

There is no separate backlog. The active tracked cards under `plans/features/` are the
outstanding work set. When work is implemented, resolved, rejected, or superseded, move
the card out of active paths and retire or delete it according to the retired-card
policy.

A plan is not a task container. A plan defines high-level phases and milestones. Each
execution item must exist as its own dedicated tracked file under a phase directory.

## Standard tracker types

Accepted planning `trackerStatus.type` values are the registered central schemas in
`.nimbalyst/trackers/*.yaml`: `feature`, `spec`, `plan`, `phase`, `task`, and
`decision`.

Use containment and `dependsOn` as the primary workflow axes. Generated tags come from
feature, plan, and phase ancestry; do not manually maintain status rollups in card
bodies.

## Tracker frontmatter

Use YAML frontmatter and keep metadata in `trackerStatus`, not `trackingStatus`.

```markdown
---
id: TASK-REMOVE-RAW-CONDITIONSET-FROM-AUT-CATEGORY-SURFACE
trackerStatus:
  type: task
parents:
- '[[PHASE-EXAMPLE]]'
dependsOn: []
title: Remove raw ConditionSet from Aut category surface
status: unstarted
priority: medium
description: Replace the public ConditionSet surface with an explicit typed object.
successCriteria:
- Public Aut-category APIs no longer expose raw ConditionSet values.
complexity: 40
---
```

The `trackerStatus.type` value must match a registered schema. Card IDs must match
filename stems. Use `parents` for containment and `dependsOn` for blocking relations.

Metadata fields should stay compact. Put complex explanations, full acceptance
criteria, gates, tables, diagrams, examples, and other structured markdown in the body.

When an active card cannot proceed, set `status: blocked` if its tracker schema
supports that value, record the exact blocker in the body, and link or create the
prerequisite task, research item, or decision. A blocked card remains active until it is
accepted, rejected, or superseded.

## Inline items

Avoid inline items in general. Use inline entries only as temporary placeholders while
a broader task is being discovered and a full tracker file is being prepared.

Inline items define a task but provide little context by construction. Any inline item
that is ready to be solved, assigned, or actively worked on must be converted into a
full markdown file under `plans/features/.../tasks/` before execution.

Do not call `create_task` or `tracker_create` for inline items. That creates a
database-only entry with no backing file and produces a duplicate.

## Planning and progressive disclosure

Use root `plans/` for Nimbalyst-backed planning documents. Plans are strictly human +
LLM collaborative artifacts. To create or materially revise a plan, switch to planning
mode, use the planning tools, iterate with the user until approval, then decompose the
approved plan into tracked phase and task files. Do not enact a chat-only,
harness-local, scratch, or unapproved plan.

Plan placement follows the hierarchy in `plans/AGENTS.md`. Root features own sibling
plans. Plans own phases. Phases own tasks. Specs live under the owning feature's
`specs/` directory, and decisions live under the owning feature's `decisions/`
directory.

The staged program remains explicit in `GOAL.md` and `.agents/current-goal-phase.md`,
while the active planning corpus lives under `plans/features/`.

Avoid inline task markers. Use `.agents/TODO.md` only as a scratchpad inbox for
tangential discoveries that need investigation before they can become real cards.
Convert anything executable into a full tracked file with context, source provenance,
boundaries, and acceptance criteria before assignment.

Subtree `AGENTS.md` files may stay small by delegating detailed policy to local skills
and skill-local references. Agents must load those skills when their task matches the
documented trigger.

## Visual windows

Use `.agents/visuals/` for optional human-facing windows into complex systems. Visuals
are supporting material only; the operative state remains in tracked feature, spec,
plan, phase, task, and decision files under `plans/features/`.

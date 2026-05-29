---
title: Research Project Workflow Reference
status: active
date: 2026-05-29
---
# Research Project Workflow Reference

## Nimbalyst tracker workspace

All active planning, spec, task, and decision documents live under root `.agents/plans/`
following the central planning hierarchy:

```
.agents/plans/features/FEATURE-ID/
├── FEATURE-ID.md
├── specs/SPEC-ID.md
├── decisions/DECISION-ID.md
└── plans/PLAN-ID/
    └── PHASE-ID/
        ├── PHASE-ID.md
        └── tasks/TASK-ID.md
```

There is no separate backlog.
Completed feature trees move under `.agents/plans/features/completed/`. The path
`.agents/plans/features/FEATURE-ID/plans/PLAN-ID/tasks/TASK-ID.md` is forbidden — a
plan-level `tasks/` directory is evidence that the phase gate was skipped.

## Source order

1. `/home/dzack/ai/planning/AGENTS.md` — reusable card framework
2. `.agents/plans/AGENTS.md` — repo-local feature buckets
3. `.nimbalyst/trackers/*.yaml` — installed schema fields
4. `GOAL.md` and `.agents/current-goal-phase.md` — staged mathematical phase gate

## Standard tracker types

Accepted types: `feature`, `spec`, `plan`, `phase`, `task`, `decision`. Use `parents`
for containment and `dependsOn` for blocking relations.

## Tracker frontmatter

Use `trackerStatus`, not `trackingStatus`. Card IDs must match filename stems.

```markdown
---
id: TASK-EXAMPLE
trackerStatus:
  type: task
parents:
- '[[PHASE-EXAMPLE]]'
dependsOn: []
title: ...
status: unstarted
priority: medium
description: ...
successCriteria: [...]
complexity: 40
---
```

For substantial research plans, treat intake, workstream, paper, agent-organization, and
uncertainty metadata as part of the contract.

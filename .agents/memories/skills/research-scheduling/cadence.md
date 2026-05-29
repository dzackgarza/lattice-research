---
title: Research Scheduling Cadence
status: active
date: 2026-05-29
---
# Research Scheduling Cadence

Scheduling is not a parallel planning system.
It is a way to wake agents, run periodic checks, or rotate attention across active
`.agents` work without losing the Nimbalyst source of truth.

## Source of truth

Use `.agents` plans, cards, decisions, TODO scratchpad entries, and current git/PR state
to decide what should run.

## Cadence model

### Startup steering

At session startup, read `AGENTS.md`, `GOAL.md`, current Nimbalyst state, and the
relevant skill index.
Load only the skills needed for the chosen work.

### Card-driven work blocks

Select work from active `.agents` cards by dependency, priority-rubric, current plan,
and human direction.

### Scheduled wakeups

Use one-shot wakeups for delayed continuation.
Use recurring schedules only for persistent maintenance that has a card or approved
automation policy.

### Maintenance passes

Run maintenance because evidence calls for it, not because a wall-clock slot says so.
Valid triggers include repeated agent failure patterns, stale active cards, unresolved
TODO entries, PR/check transitions, suspected drift from `GOAL.md`.

### Audit passes

Audit passes must load `research-proof-auditing` and target claims, scripts, PRs, or
cards that are trying to promote evidence.

## What replaced the old fixed rotation

The old schedule categories are now work classes routed through appropriate skills or
`mem:skills/*` memories.

## Scheduling hygiene

Do not create orphaned wakeups.
Remove recurring schedules when their linked card, PR, or process is resolved.
Do not schedule broad destructive cleanup, unsupervised proof acceptance, or autonomous
policy rewrites.

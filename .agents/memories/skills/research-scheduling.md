---
title: Research Scheduling
status: active
date: 2026-05-29
---
# Research Scheduling

Canonical scheduling and cadence policy for the research repo.

## Canonical source

Read `mem:skills/research-scheduling/cadence` before creating recurring schedules,
replacing daily rotations, planning autonomous maintenance, waking an agent for
follow-up, or deciding whether a scheduled action should exist.

## Core policy

- Scheduling serves `.agents` plans/cards, git/PR state, and user-approved maintenance.
  It is not a separate authority.
- Fixed wall-clock rotations do not decide priority.
  Active cards, approved plans, dependency structure, proof risk, and human direction
  do.
- One-shot wakeups are acceptable for delayed continuation or external-process polling.
- Recurring schedules require a linked card, plan, PR/check transition, maintenance
  policy, or explicit user-approved automation.
- Every scheduled action needs an owner, purpose, removal condition, and expected next
  action.
- Do not schedule destructive cleanup, proof acceptance, or policy rewrites without
  current authorization.

## Load with

- Load `scheduling-tasks-and-subagents` for concrete `at` or `task-sched` command
  mechanics.
- Read `mem:skills/research-project-workflow` to create or update linked cards/plans.
- Load `research-state-machine` when scheduled work will move a card through execution.
- Read `mem:skills/research-proof-auditing` when the scheduled work audits proof or
  computation evidence.
- Read `mem:skills/research-repo-structure` before scheduled cleanup or pruning.

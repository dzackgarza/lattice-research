---
title: Research Project Workflow
status: active
date: 2026-05-29
---
# Research Project Workflow

Canonical repo-level workflow authority for Nimbalyst-backed features, specs, plans,
phases, tasks, decisions, and project-management state.

## Canonical source

Read `mem:skills/research-project-workflow/project-workflow`, interpreted against the
reusable framework in `/home/dzack/ai/planning/AGENTS.md` and installed local schemas in
`.nimbalyst/trackers/`.

## Core policy

- Root `.agents/plans/` is the active repo-local tracker workspace.
- Substantial research coordination follows
  `mem:skills/research-co-mathematician-workflow`.
- The GUI is the index; do not create aggregate tracker indexes.
- Use only registered standard tracker types from `.nimbalyst/trackers/*.yaml`.
- There is no separate backlog; active cards are the outstanding work set.
- Completed feature trees should be moved under `.agents/plans/features/completed/`.
- Execute according to the DAG. Unmet declared dependencies mean a card remains
  `unstarted`.
- Plans are human + LLM collaborative artifacts and must be approved before
  decomposition.
- Task creation has a hard phase-owner preflight.
- Validate planning edits with `just plan-validate`.

## Load with

- Load `task` or `track` before creating individual tracker items.
- Read `mem:skills/category-spec-workflow` for category-spec-specific planning.
- Load `research-state-machine` when planned work moves into execution.
- Load `research-orchestration` for delegation, worktrees, self-check, adversarial
  audit.
- Read `mem:skills/research-scheduling` when a plan or card needs scheduling.
- Read `mem:skills/research-planning-cleanup` for post-hoc meta-review of completed
  cards.

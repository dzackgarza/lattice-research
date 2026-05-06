---
name: research-project-workflow
description: Use when handling research repo planning, root `plans/` Nimbalyst
  tracker files, layer-gated plan decomposition, TODO triage, retired cards,
  visual windows, or card metadata.
---

# Research Project Workflow

This skill is the canonical repo-level workflow authority for Nimbalyst-backed features, specs, plans, phases, tasks, decisions, and project-management state.

## Canonical source

The source of truth is this skill plus `references/project-workflow.md`, interpreted
against the reusable framework in `/home/dzack/ai/planning/AGENTS.md` and the
installed local schemas in `.nimbalyst/trackers/`.

Read `references/project-workflow.md` before creating, migrating, normalizing,
retiring, or interpreting root `plans/` tracker files.

## Core policy

- Root `plans/` is the active repo-local tracker workspace.
- The GUI is the index; do not create aggregate tracker indexes.
- Use only registered standard tracker types from `.nimbalyst/trackers/*.yaml`.
- Use the root feature/plan/phase/task hierarchy for workflow dimensions. Tags are secondary grouping aids.
- There is no separate backlog; active cards are the outstanding work set.
- Work top-down through feature/spec, plan, phase, and task gates. Do not create
  lower-layer cards before the owning layer is approved.
- Plans are human + LLM collaborative artifacts and must be approved before
  decomposition or execution.
- Executable work belongs in dedicated tracked files, not chat-only plans or inline markers.
- Decision cards are feature-level blockers only; do not leave unresolved decision
  language inside feature, spec, plan, phase, or task bodies.
- Validate planning edits with the repo-local recipe and stage generated tag or DAG
  changes deliberately.

## Load with

- Load `task` or `track` before creating individual tracker items.
- Load `category-spec-workflow` for category-spec-specific planning, triage, priority, visuals, or retirement.
- Load `research-state-machine` when planned work moves into execution, preflight, replay/attack, promotion, rejection, splitting, or `GOAL.md` discharge. Load `research-orchestration` for delegation, worktrees, self-check, adversarial audit, and artifact handoff.
- Load `research-scheduling` when a plan or card needs a delayed wakeup, recurring maintenance, autonomous cadence, or migration from fixed schedule thinking.

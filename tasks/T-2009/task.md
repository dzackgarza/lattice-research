# Task T-2009: Reduction-Ledger Gate

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: Gate for theorem-support promotion in T-3002, T-3003, and T-3011

## Objective

Require a reduction ledger for every T-3 task that promotes exact computation toward a stronger GOAL.md statement.

## Parent Sufficiency Map

Prevents proof-burden laundering across activated mathematical tasks.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: none
- Local sources:
- STATE_MACHINE.md
- GOAL.md

## Acceptance Scaffold

- The task must stay within the objective and sufficiency map above.
- Tier semantics from [STATE_MACHINE.md](/home/dzack/research/STATE_MACHINE.md) are binding.
- Detailed acceptance criteria, non-goals, and failure conditions remain to be pinned in
  TASK_SPECIFICATION.

## Tier Constraints

- Must remain a thin gate over T-0 primitives and T-1 fixtures.
- Must not replace object-level primitives with task-shaped black boxes.
- Must define what happens when a downstream T-3 task fails the gate.

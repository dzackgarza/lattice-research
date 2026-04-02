# Task T-2002: Gate Discriminant-Form And Invariant Primitives

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: Gate for T-3002, T-3005, and T-3006

## Objective

Gate the discriminant-form and invariant primitives by replaying them on T-1002 and T-1003, then matching Brown invariants, divisibilities, and isotropic counts exactly.

## Parent Sufficiency Map

Blocks downstream discriminant-group and lifting results until the finite quadratic data is exact.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: T-0002, T-1002, T-1003
- Local sources:
- tasks/goal_expansion.md
- STATE_MACHINE.md
- PROOF_AUDITING.md

## Acceptance Scaffold

- The task must stay within the objective and sufficiency map above.
- Tier semantics from [STATE_MACHINE.md](/home/dzack/research/STATE_MACHINE.md) are binding.
- Detailed acceptance criteria, non-goals, and failure conditions remain to be pinned in
  TASK_SPECIFICATION.

## Tier Constraints

- Must remain a thin gate over T-0 primitives and T-1 fixtures.
- Must not replace object-level primitives with task-shaped black boxes.
- Must define what happens when a downstream T-3 task fails the gate.

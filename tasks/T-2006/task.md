# Task T-2006: Gate Sextic Primitives

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: Gate for T-3001

## Objective

Gate the sextic primitives by checking exact nodal multiplicities, rationality or birationality criteria, and K3-cover singularity profiles against T-1007.

## Parent Sufficiency Map

Blocks the explicit sextic example until the chosen construction really matches the literature-backed geometry.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: T-0007, T-1007
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

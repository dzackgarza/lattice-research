# Task T-2008: Gate Involution Primitives

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 2.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: Gate for T-3011 and later G3.1/G6.1 work

## Objective

Gate the involution primitives by checking order, isometry, eigensublattice invariants, transported vectors, and discriminant-image consistency against the standard fixtures.

## Parent Sufficiency Map

Blocks involution-dependent claims until the activated involution primitives are exact.

## Deliverable Type

assertion gate

## Current Dependencies

- Prerequisite tasks: T-0008, T-1001, T-1002, T-1004
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

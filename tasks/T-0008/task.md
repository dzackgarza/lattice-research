# Task T-0008: Involution And Polarization Primitives

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 0.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: Prerequisite for G5.1, G3.1, and G6.1

## Objective

Expose involution and polarization primitives: sign involution construction, invariant and coinvariant lattices, distinguished vector transport, and discriminant-image extraction.

## Parent Sufficiency Map

Supplies the exact infrastructure for involution, arithmetic-group, and surgery-vector tasks; discharges no GOAL.md burden by itself.

## Deliverable Type

shared tool

## Current Dependencies

- Prerequisite tasks: T-0003
- Local sources:
- theory/oscar_lattices.md
- theory/library_integration.md

## Acceptance Scaffold

- The task must stay within the objective and sufficiency map above.
- Tier semantics from [STATE_MACHINE.md](/home/dzack/research/STATE_MACHINE.md) are binding.
- Detailed acceptance criteria, non-goals, and failure conditions remain to be pinned in
  TASK_SPECIFICATION.

## Tier Constraints

- Must expose object-level exact primitives with explicit contracts.
- Must not make or imply theorem-level claims.
- Must remain reusable and not absorb task-specific mathematical burden.

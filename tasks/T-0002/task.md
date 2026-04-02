# Task T-0002: Invariant And Predicate Primitives For 2-Elementary Lattices

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 0.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: Prerequisite for G1.2, G2.*, and G5.1

## Objective

Expose invariant and predicate primitives for rank, signature, determinant, (r,a,delta), discriminant forms, Brown invariants, divisibility, and isotropicity in 2-elementary lattices.

## Parent Sufficiency Map

Supplies the invariant layer needed for downstream lattice, discriminant, and lifting tasks; discharges no GOAL.md burden by itself.

## Deliverable Type

shared tool

## Current Dependencies

- Prerequisite tasks: T-0001
- Local sources:
- theory/mathematical_background.md
- theory/oscar_lattices.md

## Acceptance Scaffold

- The task must stay within the objective and sufficiency map above.
- Tier semantics from [STATE_MACHINE.md](/home/dzack/research/STATE_MACHINE.md) are binding.
- Detailed acceptance criteria, non-goals, and failure conditions remain to be pinned in
  TASK_SPECIFICATION.

## Tier Constraints

- Must expose object-level exact primitives with explicit contracts.
- Must not make or imply theorem-level claims.
- Must remain reusable and not absorb task-specific mathematical burden.

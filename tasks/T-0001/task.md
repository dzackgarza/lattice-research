# Task T-0001: Canonical Lattice Constructors And Coercions

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 0.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: Prerequisite for G1.2, G1.3, and G5.1

## Objective

Build canonical lattice constructors and coercions for S_Co, T_Co, T_En, T_dP, Lambda_K3, and the standard U, A_1, E_8 factors, with exact conversion between the foundation library and Oscar objects.

## Parent Sufficiency Map

Supplies the canonical lattice objects for downstream lattice-theoretic tasks; discharges no GOAL.md burden by itself.

## Deliverable Type

shared tool

## Current Dependencies

- Prerequisite tasks: none
- Local sources:
- computations/coble_geometry_foundation.sage
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

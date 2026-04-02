# Task T-1001: Standard Lattice Fixtures

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 1.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: Fixture support for T-0001, T-0002, T-0003, and T-0008

## Objective

Assemble standard lattice fixtures for U, A_1, E_8, and Lambda_K3 with published rank, signature, determinant, and isometry data.

## Parent Sufficiency Map

Provides known-good fixture data for the activated lattice primitives; does not verify correctness by itself.

## Deliverable Type

fixture data

## Current Dependencies

- Prerequisite tasks: none
- Local sources:
- REFERENCES.md
- theory/oscar_lattices.md

## Acceptance Scaffold

- The task must stay within the objective and sufficiency map above.
- Tier semantics from [STATE_MACHINE.md](/home/dzack/research/STATE_MACHINE.md) are binding.
- Detailed acceptance criteria, non-goals, and failure conditions remain to be pinned in
  TASK_SPECIFICATION.

## Tier Constraints

- Must collect fixture data only; no verification or theorem promotion.
- Every expected value must be tied to a local source or directly inspected reference.

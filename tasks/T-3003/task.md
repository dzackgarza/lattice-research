# Task T-3003: Direct Primitive Embedding T_Co Into Lambda_K3

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 3.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: GOAL.md Task 1.3 (direct embedding portion)

## Objective

Construct an explicit primitive embedding T_Co -> Lambda_K3 with matrix data, complement certificate, and exact provenance.

## Parent Sufficiency Map

Discharges only the direct Lambda_K3 portion of G1.3; the intermediate factorization remains separate.

## Deliverable Type

exact computation

## Current Dependencies

- Prerequisite tasks: T-0003, T-1002, T-1004, T-2003, T-2009
- Local sources:
- GOAL.md
- REFERENCES.md
- theory/oscar_lattices.md
- theory/mathematical_background.md

## Acceptance Scaffold

- The task must stay within the objective and sufficiency map above.
- Tier semantics from [STATE_MACHINE.md](/home/dzack/research/STATE_MACHINE.md) are binding.
- Detailed acceptance criteria, non-goals, and failure conditions remain to be pinned in
  TASK_SPECIFICATION.

## Tier Constraints

- May apply existing tools, but may not invent missing algorithms.
- Must not broaden the mathematical claim beyond the parent sufficiency map.
- Must be ready to downgrade to REPLAN_REQUIRED or conjectural status if prerequisites fail.

# Task T-3011: Construct Involution Theta On Lambda_K3

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 3.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: GOAL.md Task 5.1

## Objective

Construct an explicit involution theta on Lambda_K3 and verify that its +1 and -1 eigensublattices match T_Co and S_Co with the required primitivity data.

## Parent Sufficiency Map

Discharges G5.1 if the lattice and embedding certificates all pass.

## Deliverable Type

exact computation

## Current Dependencies

- Prerequisite tasks: T-0003, T-0008, T-1001, T-1002, T-1004, T-2003, T-2008, T-2009
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

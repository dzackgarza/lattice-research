# Task T-3001: Explicit 10-Nodal Sextic And K3 Cover

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 3.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: GOAL.md Task 1.1

## Objective

Fix a literature-backed special 10-point configuration and derive one exact rational sextic F(x,y,z)=0 with ten nodes together with the K3-cover equation w^2 = F.

## Parent Sufficiency Map

Discharges the explicit-example burden of G1.1 only; it does not prove uniqueness or classify all such sextics.

## Deliverable Type

exact computation

## Current Dependencies

- Prerequisite tasks: T-0007, T-1007, T-2006
- Local sources:
- GOAL.md
- REFERENCES.md
- theory/literature_claim_map.md
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

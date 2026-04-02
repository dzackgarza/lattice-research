# Task T-1003: Finite Quadratic-Form Fixtures

## Status

Selected in Wave A. This is scaffolded for TASK_SPECIFICATION; detailed acceptance and
failure criteria must be finalized before PRE_AUDIT.

## Tier

Tier 1.

## Origin

- Canonical backlog source: [tasks/goal_expansion.md](/home/dzack/research/tasks/goal_expansion.md)
- GOAL linkage: Fixture support for T-0002 and T-2002

## Objective

Assemble finite quadratic-form fixtures for 2-elementary forms, including known isotropic counts and small-orbit examples that exercise the discriminant-group machinery.

## Parent Sufficiency Map

Provides exact expected values for discriminant-form and isotropic-count gates; does not verify them by itself.

## Deliverable Type

fixture data

## Current Dependencies

- Prerequisite tasks: none
- Local sources:
- theory/mathematical_background.md
- theory/gap_orbits.md
- REFERENCES.md

## Acceptance Scaffold

- The task must stay within the objective and sufficiency map above.
- Tier semantics from [STATE_MACHINE.md](/home/dzack/research/STATE_MACHINE.md) are binding.
- Detailed acceptance criteria, non-goals, and failure conditions remain to be pinned in
  TASK_SPECIFICATION.

## Tier Constraints

- Must collect fixture data only; no verification or theorem promotion.
- Every expected value must be tied to a local source or directly inspected reference.

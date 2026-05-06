---
id: SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT]]'
- '[[SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE]]'
title: Recover Vinberg algorithm input and enumeration contract
status: unstarted
priority: medium
requirement: Vinberg algorithm recovery must specify exact typed inputs, root enumeration
  semantics, backend ownership, integrality checks, and termination evidence.
acceptanceCriteria:
- Inputs are a hyperbolic lattice, control vector or chamber seed, root predicate,
  and exact backend route.
- Root candidates are lattice elements satisfying sourced norm, angle, integrality,
  and chamber constraints.
- Enumeration states whether it is complete for the reported distance shell or chamber
  and records the backend/theorem that proves completeness.
- Number-field and rational/integral coordinate systems are explicit when a backend
  diagonalizes over a fraction field.
complexity: 90
tags:
- FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY
---
# Recover Vinberg algorithm input and enumeration contract

## Source Provenance

- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/README.md`
  and docs: Julia/Hecke implementation, number-field support, root iteration.
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/README.md`: Sage
  implementation route and examples.
- IWE `theory/backends/vinberg-algorithm`: integrality checks, diagonal-coordinate
  versus original-coordinate enumeration, and positive-definite subproblem notes.
- `.agents/skills/vinberg-algorithm/SKILL.md`: local workflow trigger.

## Contract

The recovered Vinberg surface accepts typed mathematical inputs: a hyperbolic lattice,
a chosen control vector or chamber seed, and root constraints. It returns a typed
result recording roots as lattice elements, the control vector, search state, and a
termination or continuation status.

If a backend diagonalizes over a field of fractions or number field, the bridge must
record how candidates are converted back to the original lattice and how integrality is
checked. Completeness claims must be tied to the backend algorithm or theorem branch,
not to a finite window selected by code.

## Non-Preservation Boundaries

- Do not hand-roll root enumeration before checking Oscar, VinbergsAlgorithmNF, AlVin,
  VinAl, Sage, Normaliz, and polyhedral backends.
- Do not hide the coordinate system used by the backend.
- Do not return raw vectors without parent lattice and root predicate evidence.
- Do not call a finite prefix of roots a fundamental domain unless the termination
  criterion is satisfied.

## Acceptance Criteria

- [ ] Inputs and root predicates are typed and source-grounded.
- [ ] Candidate enumeration records integrality and completeness evidence.
- [ ] Backend routes are documented with exact domains and limitations.
- [ ] The result object distinguishes partial search state from complete chamber data.

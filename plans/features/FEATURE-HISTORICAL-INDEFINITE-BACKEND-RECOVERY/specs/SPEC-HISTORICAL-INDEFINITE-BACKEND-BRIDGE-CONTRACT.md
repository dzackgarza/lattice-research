---
id: SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY]]'
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
title: Recover exact indefinite form backend bridge contract
status: unstarted
priority: high
requirement: Historical Indefinite and polyhedral_common wrappers must be recovered
  as exact backend bridges with normalized matrix conventions and witness verification.
acceptanceCriteria:
- Indefinite isometry, automorphism group, orbit representative, isotropic subspace
  orbit, and stabilizer calls have documented mathematical domains.
- Backend row-action or right-action matrices are converted to the repo public action
  convention exactly once at the bridge boundary.
- Witnesses and generators are checked as lattice isometries or group elements before
  public methods return them.
- Missing binaries, unsupported signatures, and environment failures stop the backend
  call rather than silently substituting weaker evidence.
complexity: 85
tags:
- FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY
---
# Recover exact indefinite form backend bridge contract

## Source Provenance

- `src.bak/backends/external/README.md`: built binary list and limits.
- `src.bak/backends/external/py_polyhedral/binaries.py`:
  `INDEF_FORM_TestEquivalence`, `INDEF_FORM_AutomorphismGroup`,
  `INDEF_FORM_GetOrbitRepresentative`, `INDEF_FORM_GetOrbit_IsotropicKplane`,
  `INDEF_FORM_StabilizerVector`, and `INDEF_FORM_StabilizerIsotropicPlane`.
- `src.bak/backends/isometry_backend.py`: exact obstruction sequence and general
  indefinite witness branch.
- IWE `theory/backends/indefinite-isometry`: verified upstream Indefinite.jl/GAP/C++
  routes and limitations.

## Contract

The recovered bridge accepts exact presented form data from a public lattice or
formed-module object and calls a documented exact backend. Outputs are raw until the
public layer verifies them: an isometry witness must preserve the form and have the
claimed source/target behavior; group generators must be elements of the appropriate
Aut object; orbit representatives must be typed and verified.

The bridge owns backend conventions. If an upstream binary returns row-action matrices
or uses a right-action convention, the bridge converts them before they enter public
group semantics.

## Non-Preservation Boundaries

- Do not expose `run_and_check`, temporary files, or Python-literal parser details as
  part of the public contract.
- Do not make `M G M^T = G` and `G^T M G = M` both appear at call sites; normalize the
  convention at the bridge.
- Do not replace exact witness calls with finite-window enumeration.
- Do not mark an operation supported merely because a wrapper name exists; the binary
  or upstream package must be available and verified.

## Acceptance Criteria

- [ ] Each backend operation records its domain, output, and completeness claim.
- [ ] Raw output conversion is centralized and tested against the public convention.
- [ ] Public methods assert or otherwise verify the returned witness/generator data.
- [ ] Unsupported or unavailable backend states fail loudly at the bridge boundary.

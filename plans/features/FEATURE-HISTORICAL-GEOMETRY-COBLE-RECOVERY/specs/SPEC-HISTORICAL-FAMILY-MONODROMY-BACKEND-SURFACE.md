---
id: SPEC-HISTORICAL-FAMILY-MONODROMY-BACKEND-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE]]'
title: Recover family, Picard-Fuchs, and monodromy backend surface
status: unstarted
priority: medium
requirement: Historical family and foliation backend code must be recovered as a source-admitted
  monodromy interface for one-parameter hypersurface families.
acceptanceCriteria:
- A family object exposes fibers, specialization, and a unique hypersurface equation
  only under explicit hypotheses.
- Picard-Fuchs, indicial polynomial, Milnor number, semisimple and nilpotent monodromy,
  and Jordan data have typed result objects.
- Singular/Ore algebra backend calls are isolated behind a backend contract with exact
  input and output validation.
- Monodromy outputs are not used as Coble evidence until connected to the relevant
  family and source theorem.
complexity: 75
tags:
- FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY
---
# Recover family, Picard-Fuchs, and monodromy backend surface

## Source Provenance

- `src.bak/varieties/varieties.py`: `FamilyOfVarieties`,
  `hypersurface_family_equation`, `hodge_theoretic_monodromy`,
  `picard_fuchs_operator`, `indicial_polynomial`, `monodromy_matrix`, and
  nilpotent monodromy methods.
- `src.bak/backends/foliation_backend.py`: `HodgeTheoreticMonodromy`,
  Picard-Fuchs operator construction, indicial polynomial, Jordan blocks, and monodromy
  matrices.
- IWE `theory-graph-monodromy-hodge-methods` and `theory-backend-routing`.

## Contract

The recovered family surface applies to a family with explicit base, total space, and
fiber operation. A one-parameter hypersurface helper is valid only when the base is a
curve and the total space has exactly one defining equation.

Monodromy output must be a typed result object containing the Picard-Fuchs operator,
indicial polynomial, Milnor number, logarithmic Jordan data, semisimple part,
nilpotent part, and monodromy matrices. Backend calls to Singular, Ore algebra, or
related exact systems are implementation details behind this object.

## Non-Preservation Boundaries

- Do not cache monodromy data as mutable hidden state without a reproducible backend
  contract.
- Do not use symbolic complex exponentials as exact proof without a stated coefficient
  field and normalization.
- Do not apply the hypersurface-family shortcut to non-hypersurface or multi-parameter
  families.
- Do not use monodromy data as a substitute for the geometric construction that
  defines the family.

## Acceptance Criteria

- [ ] Family hypotheses are explicit before monodromy methods apply.
- [ ] Picard-Fuchs and monodromy outputs are typed and reproducible.
- [ ] Backend calls are isolated and validated.
- [ ] Downstream geometry or Coble use records the map from the family to the claim.

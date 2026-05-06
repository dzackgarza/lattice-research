---
id: SPEC-HISTORICAL-GEOMETRY-NOUN-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY]]'
dependsOn:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
title: Recover geometry nouns, morphisms, divisors, and Picard group surface
status: unstarted
priority: medium
requirement: Historical geometry nouns must be recovered as source-admitted category
  interfaces with backend ownership for schemes, varieties, morphisms, divisors, and
  Picard groups.
acceptanceCriteria:
- Variety, subvariety, morphism, curve, surface, divisor, line bundle, Picard group,
  blowup, and cover nouns have explicit owners and source grounding.
- Divisor pullback, pushforward, intersection, linear equivalence, Cartier/Q-Cartier/Weil
  predicates, and Picard group intersection matrices have backend routes.
- Blowups record centers, exceptional divisors, and induced Picard-group changes as
  maps and generators.
- Geometry specs do not assume Coble-specific outputs before the construction supplies
  them.
complexity: 80
tags:
- FEATURE-HISTORICAL-GEOMETRY-COBLE-RECOVERY
---
# Recover geometry nouns, morphisms, divisors, and Picard group surface

## Source Provenance

- `src.bak/varieties/varieties.py`: `Variety`, `Subvariety`, `VarietyMorphism`,
  `Curve`, `Surface`, `Divisor`, `LineBundle`, `PicardGroup`, `Blowup`, and
  `BranchedCover` abstract surfaces.
- IWE `theory-backend-routing`: Macaulay2, Singular, Sage, Oscar, and
  commutative-algebra backend ownership for geometry methods.
- `plans/features/FEATURE-GEOMETRY-CATEGORY-INTERFACES/FEATURE-GEOMETRY-CATEGORY-INTERFACES.md`

## Contract

The recovered geometry layer must provide nouns and morphisms that make algebraic
geometry computations readable as geometry. Pullbacks, pushforwards, exceptional
divisors, Picard groups, intersection forms, canonical classes, Hilbert polynomials,
Hodge numbers, and singularity operations are methods on the relevant objects or maps,
with backend ownership recorded before implementation.

Blowups must expose the center, exceptional divisor data, induced divisor/Picard maps,
and any changes in intersection pairing as typed constructions. These are prerequisites
for later Coble work but are not themselves Coble claims.

## Non-Preservation Boundaries

- Do not preserve abstract methods as if they define accepted behavior without source
  and backend admission.
- Do not express Picard groups only as raw lattices; the divisor generators and maps
  that produce the lattice must be recoverable.
- Do not collapse Weil, Cartier, and `Q`-Cartier predicates.
- Do not assume a single backend owns all geometry operations.

## Acceptance Criteria

- [ ] Each recovered noun has owner, definition source, and backend route.
- [ ] Divisor and Picard operations are maps and objects, not detached matrices.
- [ ] Blowup-induced Picard behavior is specified in a reusable form.
- [ ] Coble-specific specs can depend on this surface without restating it.

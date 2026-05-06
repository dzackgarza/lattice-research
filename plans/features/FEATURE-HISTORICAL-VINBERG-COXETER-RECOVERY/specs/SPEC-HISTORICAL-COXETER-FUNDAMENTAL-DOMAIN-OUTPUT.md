---
id: SPEC-HISTORICAL-COXETER-FUNDAMENTAL-DOMAIN-OUTPUT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT]]'
title: Recover Coxeter diagram and fundamental chamber output contracts
status: unstarted
priority: medium
requirement: Vinberg/Coxeter recovery must specify exact output objects for reflection
  groups, Coxeter diagrams, chamber inequalities, and finite-volume evidence.
acceptanceCriteria:
- Simple roots, reflection morphisms, Coxeter matrix or diagram, Gram data, and chamber
  inequalities are separate typed outputs with shared provenance.
- Fundamental chamber claims include verification that the reported inequalities define
  the chamber for the generated reflection group under stated hypotheses.
- Finite-volume or parabolic-subdiagram claims are exact combinatorial or polyhedral
  checks, not diagram eyeballing.
- Outputs are reusable by downstream Coble Coxeter and cusp-classification features.
complexity: 80
tags:
- FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY
---
# Recover Coxeter diagram and fundamental chamber output contracts

## Source Provenance

- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/docs/src/roots.md`
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/README.md`
- `src.bak/backends/external/vinbergs_algorithm/references/sterk-peters_symmetric-quadratic-forms.md`
- `plans/features/FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION/FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION.md`

## Contract

The recovered output surface must separate the mathematical objects involved:
simple roots are lattice elements, reflections are automorphisms of the lattice,
the Coxeter diagram records pairwise reflection data, and the chamber is a polyhedral
object or inequality system in the appropriate hyperbolic cone.

Downstream code must be able to ask for parabolic subdiagrams, finite-volume status,
incidence data, or chamber faces without reconstructing the meaning of a raw root list.

## Non-Preservation Boundaries

- Do not store Coxeter data only as a drawn graph or list of labels.
- Do not treat a Gram matrix of roots as the whole chamber object.
- Do not conflate a root enumeration prefix with a verified fundamental domain.
- Do not make Coble-specific parabolic classification depend on unsourced diagram
  conventions.

## Acceptance Criteria

- [ ] Simple roots, reflections, diagrams, and chambers are distinct linked outputs.
- [ ] Finite-volume and parabolic claims have exact checks.
- [ ] The output can feed downstream Coble Coxeter/parabolic feature specs.
- [ ] Known reference examples can be represented as fixtures with sourced expected
  structure.

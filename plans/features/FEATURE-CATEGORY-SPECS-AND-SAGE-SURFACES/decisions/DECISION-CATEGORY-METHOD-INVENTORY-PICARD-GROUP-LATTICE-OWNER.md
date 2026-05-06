---
id: DECISION-CATEGORY-METHOD-INVENTORY-PICARD-GROUP-LATTICE-OWNER
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[TASK-INTEGRATE-VARIETIES-CATEGORY]]'
- '[[TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY]]'
title: Decide Picard group and Picard lattice method ownership
status: unstarted
options:
- name: Picard group is primary and Picard lattice is a refinement
  pros:
  - Matches the general Picard group meaning as line bundles or divisor classes.
  - Avoids treating every variety Picard object as a lattice.
  cons:
  - Requires an explicit bridge surface for surfaces with an admitted intersection pairing.
- name: Picard lattice is primary for surface workflows
  pros:
  - Matches the dominant Coble, K3, and reflection-group source material.
  cons:
  - Conflates a surface-specific lattice with the general Picard group of a variety.
- name: Separate PicardGroup and PicardLattice owners with explicit bridge methods
  pros:
  - Preserves the distinct mathematical objects and prevents downstream conflation.
  - Lets `picard_group()` and lattice intersection methods cite different hypotheses.
  cons:
  - Requires both geometry and lattice vocabulary before implementation cards can use the bridge.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide Picard group and Picard lattice method ownership

## Summary

Decide how the method inventory should route `picard_group()`, `intersection_matrix()`,
and `underlying_picard_group()` without collapsing the general Picard group into a
surface-specific Picard lattice.

## Source Provenance

- `theory/backends/abstract-to-external-mapping.md`: source rows for
  `Variety.picard_group()`, `PicardGroup.intersection_matrix()`, and malformed
  `PicardeLattice.underlying_picard_group()`.
- `theory/foundations/reflective-two-elementary-lattices.md`: local definition section
  `Picard lattice`.
- `theory/foundations/coble-task-background.md`: Coble blowup Picard lattice source
  material.
- `theory/references/literature/pieroni_2026_coble_surfaces.md`: Picard group, divisor,
  canonical class, and surface intersection context.
- `theory/references/literature/huybrechts_k3_lectures.md`: K3 Picard group and
  Neron-Severi/Picard lattice context.
- Geometry source-admission cards
  `TASK-INTEGRATE-VARIETIES-CATEGORY` and
  `TASK-INTEGRATE-COMPLEX-ALGEBRAIC-SURFACES-CATEGORY`.

## Context

The assembled method inventory has two nearby but distinct source surfaces:

- `picard_group()` on varieties or surfaces, whose general meaning is a Picard group
  of line bundles or divisor classes.
- Picard-lattice methods such as `intersection_matrix()` and
  `underlying_picard_group()`, whose meaning requires a surface, an intersection
  pairing, and a lattice realization.

The backend map also contains the malformed spelling `PicardeLattice`, already blocked
by `DECISION-CATEGORY-METHOD-INVENTORY-MALFORMED-BACKEND-SURFACES`. This decision is
about the mathematical owner split, not merely the typo.

## Acceptance Criteria

- [ ] State whether `picard_group()` returns a `PicardGroup` object for general
  varieties, a surface-specific lattice object, or another named object.
- [ ] State the minimal owner and hypotheses for `intersection_matrix()` on Picard data.
- [ ] State whether `underlying_picard_group()` is an admitted public bridge method,
  and if so on which Picard-lattice owner.
- [ ] Cite the exact geometry source-admission card or source section that justifies
  the chosen owner.
- [ ] Update the literal method ownership inventory before any implementation card uses
  these surfaces.

## Dependencies And Boundaries

- Do not implement Picard group or Picard lattice methods until this decision is made.
- Do not use the malformed `PicardeLattice` spelling as a public API.
- Do not assume the Picard group and Picard lattice coincide outside the hypotheses
  recorded by this decision.

## Work Log

- 2026-05-06: Created by the literal method inventory gap audit as the one remaining
  mathematical owner split not covered by existing source-admission cards.

---
id: SPEC-CURVE-JACOBIAN-PERIOD-LATTICE-OWNERSHIP
trackerStatus:
  type: spec
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING]]'
title: Specify curve Jacobian homology and period-lattice ownership
status: unstarted
priority: medium
requirement: Define the geometry category owners for analytic curve refinements,
  homology, holomorphic differentials, Jacobians, period lattices, Abel-Jacobi
  maps, and projection monodromy before any Sage RiemannSurface wrapper work.
acceptanceCriteria:
- The spec names the caller category, required curve/model/projection data,
  hypotheses, codomain, and source evidence for each admitted surface.
- Sage `RiemannSurface` constructor and curve entry points are mapped as backend
  evidence, not as public raw wrapper owners.
- Numerical, certified-homotopy, rigorous-integration, and exact-evidence
  boundaries are explicit for period matrices, Jacobian morphisms, Abel-Jacobi
  values, and monodromy permutations.
- The spec separates branch-cover monodromy, curve-family monodromy, and
  curve-complement fundamental groups.
complexity: 65
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Specify curve Jacobian homology and period-lattice ownership

## Summary

Define the geometry-category ownership vocabulary needed before Sage
`RiemannSurface` functionality can be wired into project code. The output is a
source-grounded spec for public mathematical nouns and method owners, not an
implementation card.

## Source Provenance

- `[[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]`
- `[[SPEC-SAGE-RIEMANN-SURFACE-BACKEND-MAPPING]]`
- Sage Riemann surface documentation:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/riemann_surfaces/riemann_surface.html>
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/riemann_surfaces/riemann_surface.py`
- Installed Sage curve entry points:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/affine_curve.py`
  and
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/projective_curve.py`

## Context

The Riemann-surface research card found a concrete next spec need: curve,
Jacobian, homology, period-lattice, Abel-Jacobi, and projection-monodromy owners
must exist before a public wrapper or backend bridge can be admitted.

Sage's backend is useful source evidence, but the project interface must be
owned by mathematical objects such as complex curves, analytic Riemann-surface
refinements, homology objects, holomorphic differential spaces, Jacobians, and
period lattices.

## Required Surface Questions

- Which curve category first owns an analytic Riemann-surface refinement, and
  what plane model/projection/complex-embedding data is required?
- Which object owns `homology_basis()`, and what is the codomain: cycles, a
  homology module, or backend graph-path data?
- Which object owns holomorphic differential bases and how are Singular-backed
  differential computations distinguished from user-supplied differential data?
- Which object owns `period_matrix()`, `riemann_matrix()`, period-lattice
  reduction, Jacobian homomorphism/endomorphism searches, and symplectic
  automorphism searches?
- Which object owns `abel_jacobi(...)`, and what divisor, base-point, and
  period-lattice quotient data are required?
- Which object owns `monodromy_group()` for a fixed projection, and how is this
  kept distinct from complement fundamental groups and family monodromy?

## Acceptance Criteria

- [ ] Each admitted method row names the literal surface, object level, minimal
      owner, hypotheses, codomain, source paths, and decision status.
- [ ] Raw Sage graph, Voronoi, edge-permutation, and constructor helper data is
      either rejected as public API or assigned only as backend interop evidence.
- [ ] Numerical outputs have explicit proof/audit status and cannot be used as
      exact mathematical evidence without a stated certificate policy.
- [ ] Any unresolved naming, ownership, or exactness question is split to a
      decision card rather than left as prose.
- [ ] The resulting spec links back to the Riemann-surface backend mapping and
      states whether implementation work is admitted, deferred, or blocked on
      additional geometry specs.

## Dependencies And Boundaries

- Do not implement a Sage `RiemannSurface` wrapper in this card.
- Do not admit raw Sage helper names as public project vocabulary without a
  mathematical owner and codomain.
- Do not conflate branch-cover monodromy for a projection, curve-complement
  fundamental groups, and family monodromy on cohomology.

## Work Log

- 2026-05-06: Created from Gate 2 review of
  `[[TASK-RESEARCH-SAGE-RIEMANN-SURFACE-INTERFACE]]`, which found that the
  Riemann-surface mapping spec named this concrete next work as inline prose
  rather than a tracked successor.

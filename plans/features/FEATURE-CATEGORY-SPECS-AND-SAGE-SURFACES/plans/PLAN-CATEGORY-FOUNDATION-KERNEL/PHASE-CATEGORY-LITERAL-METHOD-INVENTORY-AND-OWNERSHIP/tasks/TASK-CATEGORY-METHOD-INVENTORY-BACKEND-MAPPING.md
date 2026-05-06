---
id: TASK-CATEGORY-METHOD-INVENTORY-BACKEND-MAPPING
trackerStatus:
  type: task
parents:
- '[[PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP]]'
dependsOn:
- '[[TASK-CATEGORY-METHOD-INVENTORY-SOURCE-CORPUS]]'
title: Translate external software mappings into method ownership rows
status: unstarted
priority: critical
owner: Zack
description: Convert theory backend and external software maps into method/backend
  ownership rows covering Julia/Oscar, GAP, Singular, Macaulay2, CARAT, Indefinite.jl,
  Sage bridges, and related exact systems.
successCriteria:
- The target method-inventory spec contains backend-routing rows for every method
  in `theory/backends/abstract-to-external-mapping.md`.
- Backend rows use the routing labels from `software-capability-map.md` and name the
  mature system before any implementation card exists.
- Variety, curve, surface, divisor, sheaf, family, Picard/lattice, group-action, isometry,
  orbit, and embedding methods are attached to mathematical owners and backend codomains.
- Missing or uncertain backend support becomes backend-gap research or decision cards
  instead of bespoke implementation permission.
complexity: 68
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-FOUNDATION-KERNEL
- PHASE-CATEGORY-LITERAL-METHOD-INVENTORY-AND-OWNERSHIP
---
# Translate external software mappings into method ownership rows

## Summary

Translate backend and external software mapping notes into method-owner and
backend-routing rows. The output should make visible which mathematical object owns a
method and which mature system should implement it.

## Source Provenance

- `theory/backends/software-capability-map.md`
- `theory/backends/abstract-to-external-mapping.md`
- `theory/backends/library-integration.md`
- `theory/backends/comprehensive-tool-docs.md`
- `theory/backends/oscar-lattices.md`
- `theory/backends/gap-orbits.md`
- `theory/backends/indefinite-jl.md`
- `theory/backends/carat.md`
- `theory/backends/vinberg-algorithm.md`
- Backend notes for Singular, Macaulay2, Sage, GAP, Oscar/Julia, CARAT, and
  Indefinite.jl as linked from those files.

## Context

The seed rows include:

- varieties and surfaces: `blowup`, `resolve_singularities`, `picard_group`,
  `kodaira_dimension`, `hilbert_polynomial`, `hodge_number`,
  `holomorphic_euler_characteristic`, `canonical_class`, `birational_involution`;
- curves and plane curves: `genus`, `arithmetic_genus`, `normalization`,
  `equation`, `dual_curve`, node and singularity methods;
- divisors and sheaves: Riemann-Roch space dimension, ampleness, nefness,
  intersections, sheaf cohomology, Euler characteristic, rank;
- families: `specialization`, `monodromy`;
- Picard and lattice objects: intersection matrices, discriminant groups,
  primitive embeddings, automorphism groups, isometry tests, orbit representatives,
  Vinberg-related surfaces;
- group actions and finite groups: orbit, stabilizer, centralizer, finite group
  action methods;
- backend statuses: `preferred-backend`, `bridge-needed`, `candidate-backend`,
  `true-gap`, `out-of-scope`.

## Complexity And Ownership

- Owner/role: backend-routing source miner.
- Complexity: `68` (high).
- Rationale: the task is mostly source translation, but mistakes can cause local
  bespoke algorithms where mature systems should be wired.
- Split/promote note: split only if a backend note needs its own research card because
  current source coverage is insufficient.

## Acceptance Criteria

- [ ] The target method-inventory spec contains backend-routing rows for every method in `theory/backends/abstract-to-external-mapping.md`.
- [ ] Backend rows use the routing labels from `software-capability-map.md` and name the mature system before any implementation card exists.
- [ ] Variety, curve, surface, divisor, sheaf, family, Picard/lattice, group-action, isometry, orbit, and embedding methods are attached to mathematical owners and backend codomains.
- [ ] Missing or uncertain backend support becomes backend-gap research or decision cards instead of bespoke implementation permission.

## Dependencies And Boundaries

- This task does not approve bespoke algorithms.
- Do not route implementation to proprietary systems unless the repo's backend map
  explicitly authorizes them for comparison only.
- Do not confuse backend method availability with category ownership. The owner row
  names the project object; the backend row names the bridge target.
- If external source support is stale or uncertain, create a research card rather than
  declaring the method unsupported.

## Work Log

- 2026-05-05: Created as the backend/external-software leaf for the literal method ownership inventory phase.

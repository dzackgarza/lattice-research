---
id: FEATURE-COBLE-K3-FOLDING-INVOLUTION
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
- '[[FEATURE-COBLE-MODULI-COMPARISON]]'
plans: []
title: Coble K3 folding involution
status: blocked
priority: high
description: Construct the horizontal folding involution on the K3 lattice and verify
  its eigenspace lattices from primitive embedding and gluing data.
---
# Feature: Coble K3 folding involution

## Summary

Construct the horizontal folding involution $\theta$ on $\Lambda_{\mathrm{K3}}$ and
verify its eigenspace lattices. The feature replaces the old unverified glued-lattice
script obligation with a source-backed lattice construction.

## Source Provenance

- `theory/foundations/coble-task-background.md`, section `Task 5.1: Involution theta on
  Lambda_K3`.
- Nikulin (1979), Dolgachev-Kondo (2013), Sterk (1991), and Pieroni (2026), through
  `theory/references/index.md`.

## Scope

- Construct the primitive sublattice and orthogonal complement inside
  $\Lambda_{\mathrm{K3}}$.
- Construct the sign involution acting by $+1$ and $-1$ on the appropriate summands,
  including gluing constraints.
- Express $\theta$ as a K3-lattice isometry.
- Verify $\theta^2=I$ and $\theta^T G\theta=G$ in the chosen presentation.
- Compute and verify the $+1$ and $-1$ eigenspace lattices, signatures, primitive
  embeddings, and isometry types.

## Non-Goals

- Do not accept a hand-assembled 22-by-22 matrix without deriving the sublattices and
  gluing data.
- Do not infer eigenspaces from desired signatures alone.
- Do not use a matrix equality as the whole proof if the lattice construction is absent.

## Acceptance Criteria

- [ ] The input primitive embedding and complement are source-grounded.
- [ ] The involution is constructed as a lattice isometry, not postulated as a matrix.
- [ ] The matrix realization satisfies the involution and isometry equations.
- [ ] The eigenspace lattices are computed from $\theta$.
- [ ] The claimed identifications with $T_{\mathrm{Co}}$ and $S_{\mathrm{Co}}$ are
  verified by explicit isometries under stated hypotheses.

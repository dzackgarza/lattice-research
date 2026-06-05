---
id: FEATURE-COBLE-ARITHMETIC-GROUP-GENERATORS
trackerStatus:
  type: feature
parents: []
dependsOn:
- '[[FEATURE-QC-WARNINGS-ZERO]]'
- '[[FEATURE-COBLE-GEOMETRIC-LATTICE-FOUNDATION]]'
- '[[FEATURE-COBLE-K3-FOLDING-INVOLUTION]]'
plans: []
title: Coble arithmetic group generators
status: unstarted
priority: high
description: Construct Gamma_Co as a stabilizer-centralizer arithmetic subgroup and
  compute explicit generators with exact lattice-group verification.
---
# Feature: Coble arithmetic group generators

## Summary

Define and construct the Coble arithmetic group intended by the notation
$\Gamma_{\mathrm{Co}}$.  The sourced Dolgachev-Kondo quotient is the full
$\mathcal D(N)/O(N)$ quotient for $N=T_{\mathrm{Co}}$ and the birational quotient of the
$(-2)$ Heegner divisor in the Enriques period domain by
$O(T_{\mathrm{En}})$.  A smaller group written schematically as

```text
Stab(h_Co or tilde h_Co) ∩ Z(theta)
```

is a mathematical object only after the ambient lattice, stabilized class, involution,
restriction to $T_{\mathrm{Co}}$, and discriminant-form image are specified.

## Source Provenance

- `theory/foundations/coble-task-background.md`, section `Task 3.1: Arithmetic Group
  Gamma_Co`.
- Dolgachev-Kondo (2013), through `theory/references/index.md`, for the full
  orthogonal quotient and the Enriques Heegner-divisor quotient.
- Sterk (1991), through `theory/references/index.md`, remains a source target for the
  Enriques period-space and cusp framework; the local Sterk extracted note must be
  restored before Sterk-specific subgroup-orbit claims can be sourced from repo-local
  text.

## Scope

- Represent $T_{\mathrm{En}}$, $h_{\mathrm{Co}}$, and $\theta$ through the repo's lattice
  and morphism vocabulary.
- Specify whether the stabilized class is downstairs $h_{\mathrm{Co}}$, the K3-side
  pullback $\tilde h_{\mathrm{Co}}$, or a transported Enriques-side class.
- Specify the Heegner vector whose orthogonal complement is $T_{\mathrm{Co}}$.
- Construct the stabilizer of $h_{\mathrm{Co}}$ in $O(T_{\mathrm{En}})$.
- Construct the centralizer of $\theta$ in $O(T_{\mathrm{En}})$.
- Compute the intersection defining $\Gamma_{\mathrm{Co}}$ only after the preceding
  objects are typed in one ambient lattice.
- Construct the restriction of the subgroup to $T_{\mathrm{Co}}$, if it is meant to act
  on Coble cusp data.
- Produce a generator set and verify that the generated group has the intended
  stabilizer-centralizer property.

## Non-Goals

- Do not infer generators from notation or from a period-domain quotient statement.
- Do not accept sampled or bounded group elements as a generator computation.
- Do not use raw matrices as the public proof language; matrices are internal
  realizations of lattice isometries and subgroup operations.

## Acceptance Criteria

- [ ] $T_{\mathrm{En}}$, $h_{\mathrm{Co}}$, and $\theta$ are constructed from sourced
  lattice data.
- [ ] The ambient lattice, Heegner vector, stabilized class, and involution are all
  stated as objects in the same lattice category.
- [ ] The restriction of the subgroup to $T_{\mathrm{Co}}$ and its image in
  $O(A_{T_{\mathrm{Co}}},q_T)$ are constructed when the group is used for cusp orbits.
- [ ] The stabilizer and centralizer are computed by exact group methods or a
  source-backed backend.
- [ ] The intersection subgroup is computed as $\Gamma_{\mathrm{Co}}$ with explicit
  membership checks.
- [ ] The claimed generators are verified to generate the same subgroup, not merely to
  satisfy necessary conditions.
- [ ] The result states the theorem or backend guarantee that makes the group computation
  exhaustive.

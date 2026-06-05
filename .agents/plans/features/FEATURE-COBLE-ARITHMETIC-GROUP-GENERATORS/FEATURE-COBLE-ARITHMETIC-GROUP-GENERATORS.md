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

A source-backed Enriques-side candidate is now available.  For a $(-2)$ Heegner vector
$\delta\in T_{\mathrm{En}}$ with $\delta^\perp\simeq T_{\mathrm{Co}}$, AEGS define the
degree-2 Enriques arithmetic group
$\Gamma_{\mathrm{En},2}\subset O(T_{\mathrm{En}})$ from K3-lattice isometries
commuting with $I_{\mathrm{En}}$ and fixing $h=e+f$.  The Heegner component attached to
the line $\mathbf Z\delta$ gives the subgroup

```text
Gamma_Co^En(delta)
  := im(Stab_{Gamma_En,2}(Z delta) -> O(delta^perp)).
```

This subgroup has the right Enriques degree-2 source data.  It becomes the project
$\Gamma_{\mathrm{Co}}$ only after a theorem identifies it with the Coble-side
stabilizer-centralizer subgroup involving the folding involution $\theta$ and the
transported polarization class.

## Source Provenance

- `theory/foundations/coble-task-background.md`, section `Task 3.1: Arithmetic Group
  Gamma_Co`.
- AEGS (2023), through `theory/references/literature/aegs_2023.md:122-172`, for
  $L=II_{3,19}$, $I_{\mathrm{En}}$, $I_{\mathrm{dP}}$, $T_{\mathrm{En}}$, the
  polarization vector $h=e+f$, and $\Gamma_{\mathrm{En},2}$.
- AEGS (2023), through `theory/references/literature/aegs_2023.md:174-186`, for the
  $(-2)$ discriminant divisor in $T_{\mathrm{En}}$ and its Coble-surface
  interpretation.
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
- Define the Enriques-side subgroup
  $\Gamma_{\mathrm{Co}}^{\mathrm{En}}(\delta)$ from
  $\operatorname{Stab}_{\Gamma_{\mathrm{En},2}}(\mathbf Z\delta)$ and the restriction to
  $\delta^\perp$.
- Determine the $\Gamma_{\mathrm{En},2}$-orbits of admissible $(-2)$ Heegner lines;
  AEGS source uniqueness only modulo the full group
  $\Gamma_{\mathrm{En}}=O(T_{\mathrm{En}})$.
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
- [ ] The source-backed subgroup
  $\Gamma_{\mathrm{Co}}^{\mathrm{En}}(\delta)
  =\operatorname{im}(\operatorname{Stab}_{\Gamma_{\mathrm{En},2}}(\mathbf Z\delta)\to
  O(\delta^\perp))$ is constructed for a chosen Heegner line with
  $\delta^\perp\simeq T_{\mathrm{Co}}$.
- [ ] The $\Gamma_{\mathrm{En},2}$-orbit of the chosen Heegner line is sourced or
  computed; the full $\Gamma_{\mathrm{En}}$-orbit statement is not used as a substitute.
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

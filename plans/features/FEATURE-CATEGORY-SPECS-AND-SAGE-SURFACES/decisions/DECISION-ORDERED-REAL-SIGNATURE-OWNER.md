---
id: DECISION-ORDERED-REAL-SIGNATURE-OWNER
trackerStatus:
  type: decision
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Decide ordered real realization owner for signature and definiteness methods
status: unstarted
chosen: ''
options:
- name: Add ordered-real-realization refinement to formed modules
  pros:
  - Captures the real mathematical hypothesis needed for signature and definiteness.
  - Lets integral lattices inherit signature through the standard embedding into real
    scalars.
  cons:
  - Requires naming and wiring a new base-scalar refinement before implementation.
- name: Keep signature only on explicit integer and real-field lattice endpoints
  pros:
  - Matches currently visible Sage implementation evidence more closely.
  - Avoids adding a broad refinement before source review.
  cons:
  - Leaves number-field or other ordered-domain cases without a general owner.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Decide ordered real realization owner for signature and definiteness methods

## Summary

The mathematical-correctness audit found that the Lattices mapping spec placed
`signature_pair()`, `signature()`, `is_positive_definite()`, and
`is_negative_definite()` at `Free + Symmetric + OverIntegralDomain`. That is too broad:
an arbitrary integral domain does not provide signs, eigenvalue ordering, or a chosen
real realization.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`
- Sage source `sage/modules/free_quadratic_module_integer_symmetric.py`, where the
  visible implementation evidence is `ZZ`-specific.

## Context

Signature data is meaningful for finite free symmetric bilinear data after extension to
a signed scalar context, for example `ZZ -> QQ -> RR`. The current category vocabulary
has `OverIntegralDomain`, but that only supplies a fraction field; it does not supply
an ordered field, a real embedding, or a rule for comparing signs.

## Acceptance Criteria

- Choose the category/refinement owner for signature and definiteness methods.
- Record whether the owner is a new formed-module/lattice refinement or only selected
  endpoint methods such as `OverZZ` and real-field formed modules.
- Update Lattices and Forms mapping specs so method rows state caller category,
  hypotheses, codomain/return object, and source evidence.
- Block implementation of general signature/definiteness surfaces until this decision
  is made.

## Dependencies And Boundaries

This decision does not block ordinary `ZZ` lattice signature interop, but it blocks any
claim that signature or definiteness is owned by all free symmetric bilinear modules
over integral domains.

## Work Log

- 2026-05-06: Created from the mapping mathematical-correctness audit after detecting
  the over-broad `OverIntegralDomain` owner.

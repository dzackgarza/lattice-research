---
id: TASK-SOURCE-GROUND-POSETS-FINITE-AUTOMORPHISM-GROUP-HOMSET-ENUMERATION
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[TASK-AUDIT-POSETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES]]'
- '[[SPEC-MAPPING-POSETS]]'
title: Source-ground finite poset automorphism group enumeration before AutCategory admission
status: unstarted
priority: medium
description: Determine whether Sage Hasse-diagram automorphism machinery can ground
  an executable finite Posets AutCategory enumeration surface, or whether it must
  remain graph-backend interop only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- Sage finite poset and Hasse-diagram automorphism sources are audited for mathematical ownership and return-object semantics.
- The project owner is identified as Posets AutCategory, finite-poset parent validation, graph-backend interop, or rejected from public API.
- Any admitted API states domain, codomain, hypotheses, and how graph automorphisms become poset automorphisms without confusing graph and order owners.
complexity: 24
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Source-ground finite poset automorphism group enumeration before AutCategory admission

## Summary

Source-ground the Hasse-diagram automorphism evidence found during the Posets homset
mirroring audit before any executable finite Posets AutCategory enumeration surface is
admitted.

## Source Provenance

- `[[SPEC-MAPPING-POSETS]]`
- `category_specs/posets/homsets.py`
- Sage `sage/combinat/posets/hasse_diagram.py`
- Sage `sage/combinat/posets/posets.py`
- Sage generic homset and automorphism machinery as needed

## Context

The current Posets audit treats Hasse-diagram automorphism-group calls as backend
graph evidence only. Admitting finite poset automorphism enumeration requires a
separate proof that the graph automorphisms are exposed as order automorphisms with
the correct project owner and return object.

## Acceptance Criteria

- [ ] The Sage source path from finite posets to Hasse-diagram automorphism groups is documented with line-level evidence.
- [ ] The mathematical owner and return object for finite poset automorphism enumeration are specified or the surface is rejected from public API.
- [ ] The result is reflected in the Posets mapping spec or in a follow-up decision card.

## Dependencies And Boundaries

- Do not admit graph automorphism APIs directly as Posets AutCategory methods.
- Do not implement enumeration until the source-grounded owner and codomain are settled.

## Work Log

- 2026-05-17: Created from the Posets homset mirroring audit to track finite
  automorphism-group enumeration separately from generic order-preserving map
  vocabulary.

---
id: TASK-AUDIT-SETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-SETS]]'
title: Audit Sets hom mapping for mirrored Sage homset surfaces
status: unstarted
priority: high
description: Audit `category_specs/sets/homsets.py` and the Sets mapping/spec surface so
  retained Sage homset/container methods such as identity, zero-like constructors,
  and image-list construction paths are explicitly mirrored or rejected.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Sets hom mapping records the retained Sage homset/container methods relevant to set maps.
- Each retained method is assigned to a Sets hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 38
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Sets hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Sets hom mapping to ensure the project explicitly mirrors any retained
Sage homset/container methods instead of assuming generic Sage homset inheritance.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-SETS.md`
- `category_specs/sets/homsets.py`
- `category_specs/sets/docs/MAPPING.md`
- `category_specs/sets/docs/SAGE_INVENTORY.md`
- Sage docs/source for set homsets and finite-set-map behavior as needed

## Context

Sets is the first subtree where generic hom containers meet actual concrete map
behavior. This audit decides which Sage homset/container methods belong on the
project Sets hom/end/aut surfaces and which are interop-only.

## Acceptance Criteria

- [ ] The Sets mapping/spec identifies Sage homset/container methods relevant to set
      hom objects and set-map construction.
- [ ] Each method is mirrored onto a project owner, routed elsewhere, or rejected as
      interop-only with source grounding.
- [ ] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not use this audit to weaken set-map obligations already admitted in the Sets
  mapping.
- Keep this card on `sets/homsets.py` and the Sets mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.

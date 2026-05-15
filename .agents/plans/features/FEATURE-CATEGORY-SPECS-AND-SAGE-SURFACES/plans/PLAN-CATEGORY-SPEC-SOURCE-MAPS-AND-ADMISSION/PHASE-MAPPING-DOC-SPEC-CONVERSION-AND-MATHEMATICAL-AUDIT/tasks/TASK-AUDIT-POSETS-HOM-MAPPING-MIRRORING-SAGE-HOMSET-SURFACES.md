---
id: TASK-AUDIT-POSETS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-POSETS]]'
title: Audit Posets hom mapping for mirrored Sage homset surfaces
status: unstarted
priority: high
description: Audit `category_specs/posets/homsets.py` and the Posets mapping/spec
  surface so retained Sage order-map container methods are explicitly mirrored,
  rerouted, or rejected as interop-only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Posets hom mapping records the retained Sage homset/container methods relevant to order-preserving maps and endomorphisms.
- Each retained method is assigned to a Posets hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 38
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Posets hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Posets hom mapping under the project-owned HomCategory semantic base so
retained Sage homset/container methods are mirrored explicitly rather than
silently inherited.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-POSETS.md`
- `category_specs/posets/homsets.py`
- `category_specs/posets/docs/MAPPING.md`
- `category_specs/posets/docs/SAGE_INVENTORY.md`
- Sage docs/source for poset/order-map homsets as needed

## Context

Posets has a specialized hom surface for order-preserving maps. This audit makes
the retained Sage container methods explicit in the project mapping.

## Acceptance Criteria

- [ ] The Posets mapping/spec identifies Sage homset/container methods relevant to poset hom objects and their constructors.
- [ ] Each method is mirrored onto a project owner, routed elsewhere, or rejected as interop-only with source grounding.
- [ ] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not weaken poset-map obligations to avoid mirroring work.
- Keep this card on `posets/homsets.py` and the Posets mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.

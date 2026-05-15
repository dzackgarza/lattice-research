---
id: TASK-AUDIT-RINGS-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-RINGS]]'
title: Audit Rings hom mapping for mirrored Sage homset surfaces
status: unstarted
priority: high
description: Audit `category_specs/rings/homsets.py` and the Rings mapping/spec surface so
  retained Sage ring-hom container methods are explicitly mirrored, rerouted, or
  rejected as interop-only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Rings hom mapping records the retained Sage homset/container methods relevant to ring homs and endomorphisms.
- Each retained method is assigned to a Rings hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 38
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Rings hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Rings hom mapping under the project-owned HomCategory semantic base so
retained Sage homset/container methods are mirrored explicitly rather than
silently inherited.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-RINGS.md`
- `category_specs/rings/homsets.py`
- `category_specs/rings/docs/MAPPING.md`
- `category_specs/rings/docs/SAGE_INVENTORY.md`
- Sage docs/source for ring homsets and ring endomorphism containers as needed

## Context

Rings is a major homset-bearing subtree with constructor/coercion conventions that
should not be carried into the project by assumption. This audit makes those
choices explicit in the mapping surface.

## Acceptance Criteria

- [ ] The Rings mapping/spec identifies Sage homset/container methods relevant to ring hom objects and their constructors.
- [ ] Each method is mirrored onto a project owner, routed elsewhere, or rejected as interop-only with source grounding.
- [ ] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not weaken ring-hom obligations or overload signatures to match current Sage
  convenience behavior.
- Keep this card on `rings/homsets.py` and the Rings mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.

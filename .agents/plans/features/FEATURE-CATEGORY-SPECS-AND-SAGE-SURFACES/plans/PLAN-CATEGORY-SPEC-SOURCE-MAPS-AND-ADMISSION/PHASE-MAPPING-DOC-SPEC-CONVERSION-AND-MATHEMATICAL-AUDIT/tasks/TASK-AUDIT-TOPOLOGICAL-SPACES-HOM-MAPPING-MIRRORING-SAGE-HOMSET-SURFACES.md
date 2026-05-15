---
id: TASK-AUDIT-TOPOLOGICAL-SPACES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-TOPOLOGICAL-SPACES]]'
title: Audit TopologicalSpaces hom mapping for mirrored Sage homset surfaces
status: unstarted
priority: high
description: Audit `category_specs/topological_spaces/homsets.py` and the TopologicalSpaces
  mapping/spec surface so retained Sage continuous-map container methods are
  explicitly mirrored, rerouted, or rejected as interop-only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The TopologicalSpaces hom mapping records the retained Sage homset/container methods relevant to continuous maps and homeomorphisms.
- Each retained method is assigned to a TopologicalSpaces hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 38
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit TopologicalSpaces hom mapping for mirrored Sage homset surfaces

## Summary

Audit the TopologicalSpaces hom mapping under the project-owned HomCategory
semantic base so retained Sage homset/container methods are mirrored explicitly
rather than silently inherited.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-TOPOLOGICAL-SPACES.md`
- `category_specs/topological_spaces/homsets.py`
- `category_specs/topological_spaces/docs/MAPPING.md`
- `category_specs/topological_spaces/docs/SAGE_INVENTORY.md`
- Sage docs/source for continuous-map/homeomorphism containers as needed

## Context

TopologicalSpaces carries hom surfaces for continuous maps and homeomorphisms. This
audit makes the retained Sage container methods explicit in the project mapping.

## Acceptance Criteria

- [ ] The TopologicalSpaces mapping/spec identifies Sage homset/container methods relevant to topological hom objects and their constructors.
- [ ] Each method is mirrored onto a project owner, routed elsewhere, or rejected as interop-only with source grounding.
- [ ] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not weaken continuous-map or homeomorphism obligations to avoid mirroring work.
- Keep this card on `topological_spaces/homsets.py` and the TopologicalSpaces mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.

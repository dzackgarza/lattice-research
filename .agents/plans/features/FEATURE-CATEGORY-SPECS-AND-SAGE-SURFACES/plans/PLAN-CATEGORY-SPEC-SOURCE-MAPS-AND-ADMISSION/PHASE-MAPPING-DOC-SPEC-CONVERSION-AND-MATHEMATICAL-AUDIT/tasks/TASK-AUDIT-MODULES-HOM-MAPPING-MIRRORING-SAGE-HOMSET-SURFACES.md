---
id: TASK-AUDIT-MODULES-HOM-MAPPING-MIRRORING-SAGE-HOMSET-SURFACES
trackerStatus:
  type: task
parents:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
dependsOn:
- '[[DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION]]'
- '[[SPEC-MAPPING-MODULES]]'
title: Audit Modules hom mapping for mirrored Sage homset surfaces
status: unstarted
priority: critical
description: Audit `category_specs/modules/homsets.py` and the Modules mapping/spec
  surface so retained Sage module-hom container methods such as `zero()`,
  identity/coercion constructors, and homspace operations are explicitly mirrored,
  rerouted, or rejected as interop-only.
activityType: source-mining
workstreamRole: review
claimStatus: source-backed
uncertaintyState: ordinary-open
successCriteria:
- The Modules hom mapping records the retained Sage homset/container methods relevant to module homs, endomorphisms, and automorphisms.
- Each retained method is assigned to a Modules hom/end/aut owner or rejected as interop-only with source evidence.
- Follow-up gaps become tracked cards instead of inline TODOs or chat-only notes.
complexity: 44
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
- PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION
- PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT
---
# Audit Modules hom mapping for mirrored Sage homset surfaces

## Summary

Audit the Modules hom mapping under the project-owned HomCategory semantic base so
retained Sage homset/container methods are mirrored explicitly rather than
silently inherited.

## Source Provenance

- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/decisions/DECISION-GENERIC-HOMSET-PARENT-OWNERSHIP-AND-SAGE-INTEGRATION.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-MODULES.md`
- `category_specs/modules/homsets.py`
- `category_specs/modules/docs/MAPPING.md`
- `category_specs/modules/docs/SAGE_INVENTORY.md`
- Sage docs/source for `sage.categories.modules.Homsets`, `Endset`, and concrete module homspace containers

## Context

Modules is the richest current homset-bearing subtree in repo specs. It already
declares project-owned `zero()` and related surfaces, so this audit must decide
which Sage homset/container methods remain part of the project contract and which
are merely backend convenience.

## Acceptance Criteria

- [ ] The Modules mapping/spec identifies Sage homset/container methods relevant to module hom objects, constructors, and endomorphism structure.
- [ ] Each method is mirrored onto a project owner, routed elsewhere, or rejected as interop-only with source grounding.
- [ ] Any missing owner or constructor consequence becomes a tracked follow-up card.

## Dependencies And Boundaries

- Do not treat Sage coercive convenience as automatic mathematical admission.
- Keep this card on `modules/homsets.py` and the Modules mapping/spec surface.

## Work Log

- 2026-05-10: Created after the homset semantic-base decision shifted from generic
  inheritance repair to explicit subtree mirroring audits.

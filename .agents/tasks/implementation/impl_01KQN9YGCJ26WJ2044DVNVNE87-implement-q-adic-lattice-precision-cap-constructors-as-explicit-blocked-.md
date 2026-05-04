---
trackerStatus:
  type: feature
title: Implement q-adic lattice precision-cap constructors as explicit blocked Sage-gap surfaces rather than broken pass-throughs
status: to-do
priority: high
planId: SPR-RINGS-PADIC-01KQN9
tags:
- category-specs
- implementation
- feature
- constructors
- sage
- rings
- precision
- lattices
- theme-constructor-routing
---

# Implement q-adic lattice precision-cap constructors as explicit blocked Sage-gap surfaces rather than broken pass-throughs
## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
lattice-precision gaps.

## Source Provenance

- `category_specs/rings/docs/MAPPING.md`
- Original migrated line: `Implement q-adic lattice precision-cap constructors as explicit blocked Sage-gap surfaces rather than broken pass-throughs from category_specs/rings/docs/MAPPING.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- ZqWithPrecisionCaps and QqWithPrecisionCaps are retained admitted split names but remain deferred frontiers because installed Sage lacks a working unramified q-adic extension path with split lattice caps.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Acceptance Criteria

- [ ] The implementation changes only the scoped category-spec surface and does not weaken smokes or mapping decisions to make failures disappear.
- [ ] Relevant smoke output is updated in this task body or a linked tracker item, with exact failing surfaces preserved when work remains.
- [ ] The change uses project category vocabulary rather than Sage fallback helper names or wrapper-only categories.
- [ ] For q-adic precision items, preserve the five-field negative finding format when updating evidence.
- [ ] For topological ring work, check both ring and topological-space category membership.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


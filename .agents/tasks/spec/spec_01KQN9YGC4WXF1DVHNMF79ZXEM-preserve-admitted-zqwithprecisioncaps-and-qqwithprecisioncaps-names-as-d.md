---
trackerStatus:
  type: feature
title: Preserve admitted ZqWithPrecisionCaps and QqWithPrecisionCaps names as deferred Sage-gap frontiers with exact gap assertions
status: in-review
priority: critical
planId: SPR-RINGS-PADIC-01KQN9
tags:
- category-specs
- spec
- feature
- sage
- precision
- theme-local-cleanup
progress: 90
updated: '2026-05-05'
---

# Preserve admitted ZqWithPrecisionCaps and QqWithPrecisionCaps names as deferred Sage-gap frontiers with exact gap assertions
## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
lattice-precision gaps.

## Source Provenance

- `category_specs/rings/docs/MAPPING.md`
- Original migrated line: `Preserve admitted ZqWithPrecisionCaps and QqWithPrecisionCaps names as deferred Sage-gap frontiers with exact gap assertions from category_specs/rings/docs/MAPPING.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- ZqWithPrecisionCaps and QqWithPrecisionCaps are retained admitted split names but remain deferred frontiers because installed Sage lacks a working unramified q-adic extension path with split lattice caps.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Grounded Review Outcome

Sources: `category_specs/rings/docs/MAPPING.md`,
`category_specs/rings/docs/SAGE_INVENTORY.md`, and the migrated source line named in
`Source Provenance`.

The naming decision is already grounded and should be preserved: `ZqWithPrecisionCaps`
and `QqWithPrecisionCaps` remain admitted split constructor names under
`Rings().Constructors()` as deferred Sage-gap frontiers, parallel to the concrete
`ZpWithPrecisionCaps` and `QpWithPrecisionCaps` routes.

Grounded owner and hypothesis rule:

- the owner category remains the rings constructor namespace, not a valuation-only
  side API;
- the intended hypotheses are unramified q-adic extension construction with lattice
  relative/absolute precision caps, matching the mathematically meaningful split
  already used for p-adic base constructors;
- the intended codomain is the corresponding q-adic ring or field parent refined into
  the local valued/complete ring surface once Sage exposes a working constructor path.

Deferred review outcome:

- no new public mathematical meaning is needed on this card;
- the exact five-field negative finding already recorded in `rings/docs/MAPPING.md`
  is the source of truth for why these names stay deferred;
- future work on this leaf is limited to replacing the deferred-gap assertion with a
  source-backed working Sage route or upstream fix, not renaming or deleting the split
  names.
- `category_specs/rings/__init__.py` already preserves the admitted public names and
  asserts the installed Sage gap in both `ZqWithPrecisionCaps(...)` and
  `QqWithPrecisionCaps(...)`; this card does not replace those assertions with a fake
  implementation path.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [x] The implementation blocker is the preserved Sage-gap frontier recorded in `rings/docs/MAPPING.md`; no new implementation card was created because this leaf exists to keep the admitted names deferred until a real Sage route exists.
- [x] For q-adic precision items, preserve the five-field negative finding format when updating evidence.
- [x] This is not topological-ring work; the owner remains the ring constructor namespace.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- 2026-05-05: Confirmed the existing spec state: `rings/docs/MAPPING.md` owns the
  five-field negative finding, `rings/__init__.py` preserves both deferred constructor
  names with explicit gap assertions, and the card is ready for review without
  introducing a fake q-adic lattice-precision implementation path.

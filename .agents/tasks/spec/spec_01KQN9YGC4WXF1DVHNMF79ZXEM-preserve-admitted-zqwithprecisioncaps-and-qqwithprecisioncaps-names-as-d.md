---
trackerStatus:
  type: feature
title: Preserve admitted ZqWithPrecisionCaps and QqWithPrecisionCaps names as deferred Sage-gap frontiers with exact gap assertions
status: to-do
priority: critical
planId: SPR-RINGS-PADIC-01KQN9
tags:
- category-specs
- spec
- feature
- sage
- precision
- theme-local-cleanup
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

## Definition Grounding Required Before Spec Edit

This migrated card is executable for source mining and decision capture, but it does not by itself authorize a mathematical spec edit. Before moving, deleting, admitting, or generalizing any public category, method, constructor, predicate, invariant, Hom/End/Aut surface, or return type, record the canonical source path, exact definition, owner category, hypotheses, codomain/return object, and any invariance or equivalence proof obligation.

Use the subtree `MAPPING.md` and `SAGE_INVENTORY.md` files, Sage written docs/source, `theory/references/index.md` for literature-backed claims, and relevant repo `theory/` or skill-local sources. If the term is ambiguous or only supported by migrated backlog text, split to source-mining or decision work before editing specs.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] For q-adic precision items, preserve the five-field negative finding format when updating evidence.
- [ ] For topological ring work, check both ring and topological-space category membership.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


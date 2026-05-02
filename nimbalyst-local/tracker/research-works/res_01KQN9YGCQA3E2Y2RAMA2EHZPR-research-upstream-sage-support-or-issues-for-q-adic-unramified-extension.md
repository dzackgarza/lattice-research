---
trackingStatus:
  itemId: res_01KQN9YGCQA3E2Y2RAMA2EHZPR
  title: Research upstream Sage support or issues for q-adic unramified extensions
    with split lattice precision caps
  type: research-work
  status: to-do
  priority: medium
  assignee: null
  tags:
  - cat
  - category-specs
  - research-work
  - rings
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Research upstream Sage support or issues for q-adic unramified extensions with split lattice precision caps

## Summary

Rings mapping records constructor namespace decisions, split p-adic and q-adic precision
routes, matrix-ring ownership, topological ring inheritance, and deferred q-adic
lattice-precision gaps.

## Source Provenance

- `plans/category_specs/rings/docs/MAPPING.md`
- Original migrated line: `Research upstream Sage support or issues for q-adic unramified extensions with split lattice precision caps from plans/category_specs/rings/docs/MAPPING.md`

## Context

- ZpWithPrecisionCaps and QpWithPrecisionCaps are concrete because Sage base constructors canonicalize lattice precision pairs.
- ZqWithPrecisionCaps and QqWithPrecisionCaps are retained admitted split names but remain deferred frontiers because installed Sage lacks a working unramified q-adic extension path with split lattice caps.
- Topological ring structure must inherit topological-space methods rather than duplicate them in ring-only files.
- Matrix rings are rings, algebras over their base ring, and free finite-rank modules; method ownership follows that split.

## Acceptance Criteria

- [ ] The research result cites the exact sources searched and separates source evidence from inference.
- [ ] Negative findings use the repository five-field format: Searched, Found, Conclusion, Confidence, Gaps.
- [ ] Any admitted design consequence is linked to a spec-work or design-decision item rather than buried in prose.
- [ ] For q-adic precision items, preserve the five-field negative finding format when updating evidence.
- [ ] For topological ring work, check both ring and topological-space category membership.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


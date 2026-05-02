---
trackerStatus:
  itemId: spec_01KQN9YGCCQ9EDZWW6H98WDY3X
  title: Audit the variadic signature scoping result and open owner-specific follow-ups
    for any public surface still using placeholder collapsed Sage casework
  type: spec-work
  status: to-do
  priority: high
  assignee: null
  tags:
  - cat
  - category-specs
  - spec-work
  - variadic
  created: '2026-05-02'
  updated: '2026-05-02T00:00:00.000Z'
---

# Audit the variadic signature scoping result and open owner-specific follow-ups for any public surface still using placeholder collapsed Sage casework

## Summary

The deleted variadic inventory records the scoping pass for public surfaces that had
collapsed Sage casework or raw coordinate interop into broad signatures.

## Source Provenance

- `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`.
- Original migrated line: `Audit the variadic signature scoping result and open owner-specific follow-ups for any public surface still using placeholder collapsed Sage casework from plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`

## Context

- Module constructors and quotient inputs were split and mapped in modules docs/code.
- Ring constructors, p-adic precision tuples, series factories, matrix element construction, and number-field optional arguments were split and mapped in rings docs/code.
- Tensor component catch-all data was removed from public surface in favor of named constructors.
- Algebra subalgebra and ideal option bags were split into named methods.
- Lattice short_vectors kwargs were split into short_vectors(bound) and short_vectors_up_to_sign(bound).
- Poset, set iterator, element-class forwarding, and RealSet variadics were mapped or excluded from public specs.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Audit public signatures for remaining *args, **kwargs, option bags, and placeholder union data shapes.
- [ ] Open owner-specific tasks for any remaining collapsed Sage casework rather than restoring the inventory doc.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


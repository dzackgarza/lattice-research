---
trackerStatus:
  type: feature
title: Audit the variadic signature scoping result and open owner-specific follow-ups for any public surface still using placeholder collapsed Sage casework
status: to-do
priority: critical
planId: SPR-VARIADIC-AUDIT-01KQN9
tags:
- category-specs
- spec
- feature
- sage
- rings
- precision
- signatures
- audit
- theme-audit-uniformity
---

# Audit the variadic signature scoping result and open owner-specific follow-ups for any public surface still using placeholder collapsed Sage casework
## Summary

The deleted variadic inventory records the scoping pass for public surfaces that had
collapsed Sage casework or raw coordinate interop into broad signatures.

## Source Provenance

- `category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`.
- Original migrated line: `Audit the variadic signature scoping result and open owner-specific follow-ups for any public surface still using placeholder collapsed Sage casework from category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`

## Context

- Module constructors and quotient inputs were split and mapped in modules docs/code.
- Ring constructors, p-adic precision tuples, series factories, matrix element construction, and number-field optional arguments were split and mapped in rings docs/code.
- Tensor component catch-all data was removed from public surface in favor of named constructors.
- Algebra subalgebra and ideal option bags were split into named methods.
- Lattice short_vectors kwargs were split into short_vectors(bound) and short_vectors_up_to_sign(bound).
- Poset, set iterator, element-class forwarding, and RealSet variadics were mapped or excluded from public specs.

## Source-Mining Contract

This card is an audit card. Its job is to identify public surfaces that still collapse
finite Sage casework into placeholder signatures and to pin each one to its real owner.

- Primary source anchors:
  - `.agents/skills/category-spec-style/references/style.md`, especially the no-variadic
    and overload rules;
  - `category_specs/modules/docs/MAPPING.md`;
  - `category_specs/forms/docs/MAPPING.md`;
  - `category_specs/lattices/docs/MAPPING.md`;
  - `category_specs/cat/docs/MAPPING.md`;
  - `category_specs/homsets/docs/MAPPING.md`;
  - Sage written docs/source for the exact public surface under audit.
- For each audited surface, record the closed set of mathematical input patterns Sage
  actually supports, the owner category or constructor namespace, the codomain/return
  object, and any compatibility obligation to preserve already-mapped call routes.
- Placeholder unions, `*args`, `**kwargs`, and option bags stay out of the public spec
  unless the source material proves a genuinely open-ended mathematical family. Finite
  Sage casework must be restated as named constructors or explicit overload families.
- When an audited surface crosses module, forms, lattice, or hom/end/aut boundaries,
  use the existing mapping docs to pin the owner instead of re-opening the owner
  question in this card.
- If audit work hits a surface whose owner or definition is still unresolved, record
  that concrete blocker here rather than papering it over with another generic grounding
  gate.

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

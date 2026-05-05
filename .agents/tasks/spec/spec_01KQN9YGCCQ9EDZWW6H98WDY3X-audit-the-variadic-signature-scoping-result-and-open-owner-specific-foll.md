---
trackerStatus:
  type: feature
title: Audit the variadic signature scoping result and open owner-specific follow-ups for any public surface still using placeholder collapsed Sage casework
status: in-review
priority: critical
progress: 90
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

- The migrated source path in the original card text is stale. The deleted file
  actually lived at `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`
  and was removed in commit `8d1c21c`; recover exact prior content with
  `git show 8d1c21c^:plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`.
- Original migrated line: `Audit the variadic signature scoping result and open owner-specific follow-ups for any public surface still using placeholder collapsed Sage casework from category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`
- Recovery check: the recovered inventory records the scoping result as already split
  across modules, rings, tensor algebra components, algebras, lattices, posets, sets,
  and topological spaces.

Stale-path check:

- Searched: `git show 8d1c21c^:category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`,
  then broadened with `git ls-tree -r --name-only 8d1c21c^ | rg 'VARIADIC_SIGNATURE_INVENTORY|category_specs/docs|plans/category_specs/docs'`.
- Found: the `category_specs/...` path is absent at `8d1c21c^`; the recoverable file
  is `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md`.
- Conclusion: inference - the card's migrated source path was stale, but the exact
  source inventory is recoverable from the deleted `plans/` tree.
- Confidence: High.
- Gaps: none for the existence and location of this deleted source file.

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

## Audit Result

The current public category-spec surfaces match the recovered scoping result:

| Surface family | Current owner and result |
| --- | --- |
| Module constructors and quotient inputs | `category_specs/modules/docs/MAPPING.md` records named constructors for rank, basis-key, inner-product, FPModule, integer-lattice, torsion-quadratic, ring-as-module, and quotient input shapes. Current module code uses named methods such as `FreeModuleWithBasisKeys`, `FPModuleFromCokernelMap`, `quotient_by_relation_matrix`, and series/ring bridge methods instead of the recovered collapsed signatures. |
| Ring constructors, p-adic precision, series factories, matrix element construction, and number-field optional arguments | `category_specs/rings/docs/MAPPING.md` records the closed constructor split. Current ring code has named number-field tower, p-adic cap/relaxed/prime-power/factorization, polynomial, series, matrix-element, discriminant, integral-basis, and order/maximal-order surfaces rather than the recovered collapsed inputs. |
| Tensor component data | `category_specs/tensor_algebra_components/docs/MAPPING.md` rejects the catch-all component constructor and admits only named tensor constructors plus explicit `trace(...)` and `contract(...)`. |
| Algebra subalgebra and ideal option bags | `category_specs/algebras/docs/MAPPING.md` maps Sage option bags to `subalgebra(generators)`, left/right/two-sided ideal methods, and principal left/right/two-sided ideal methods. |
| Lattice `short_vectors(..., **kwargs)` | `category_specs/lattices/docs/MAPPING.md` splits the only sourced keyword case into `short_vectors(bound)` and `short_vectors_up_to_sign(bound)`. |
| Poset, set, and RealSet variadics | `category_specs/posets/docs/MAPPING.md`, `category_specs/sets/docs/MAPPING.md`, and `category_specs/topological_spaces/docs/MAPPING.md` keep raw variadic constructors private or rejected and expose named constructor families. |
| Cat constructor aggregation | `category_specs/cat/docs/MAPPING.md` now records that generated `Cat().Constructors()` forwarding hooks are private Python/Sage dispatch glue, not public variadic mathematical surfaces. |

Remaining public-variadic check:

- Searched: recovered variadic inventory; `.agents/skills/category-spec-style/references/style.md`;
  current module, ring, tensor, algebra, lattice, poset, set, topological-space, and
  Cat mapping files; `rg -n "def .*\\*args|def .*\\*\\*kw|def .*\\*\\*kwargs|def .*kwds|args:|kwargs:" category_specs -g '*.py'`; and targeted reads of the current files named in the recovered inventory.
- Found: no remaining public constructor or method from the recovered inventory still
  exposes raw `*args`, `**kwargs`, `kwds`, or an unresolved placeholder union. The only
  live code hits are Cat internal generated forwarding/subclass-registration hooks,
  now mapped as private aggregation plumbing in `category_specs/cat/docs/MAPPING.md`.
- Conclusion: inference - this audit leaf has no owner-specific follow-up tasks to
  open for remaining collapsed Sage casework.
- Confidence: Medium.
- Gaps: this audit covers the recovered inventory plus current textual signature
  searches; it is not a fresh exhaustive semantic review of every finite union in every
  typed collection signature.

## Acceptance Criteria

- [x] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [x] No new subtree-local TRIAGE or process document is created.
- [x] No implementation blocker was discovered in this audit pass.
- [x] Public signatures were audited for remaining `*args`, `**kwargs`, option bags, and placeholder union data shapes from the recovered inventory.
- [x] No owner-specific tasks were opened because the only remaining `*args`/`**kwargs` hits are private Cat aggregation hooks, now mapped as nonpublic infrastructure.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.
- Recovered the deleted variadic inventory from `plans/category_specs/docs/VARIADIC_SIGNATURE_INVENTORY.md` after the migrated `category_specs/...` provenance path proved stale.
- Audited the recovered inventory against current module, ring, tensor, algebra, lattice, poset, set, topological-space, and Cat mapping/code surfaces.
- Added Cat mapping for generated constructor aggregation forwarders so future audits do not mistake private dispatch glue for a public variadic constructor.
- Skipped subtree smokes and global QC intentionally; this was a documentation/source-map audit, not implementation integration or phase transition.

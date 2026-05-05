---
trackerStatus:
  type: feature
title: Map poset deferred graph polytope order-complex algebra polynomial Coxeter display and raw-interop surfaces to final owners
status: to-do
priority: critical
planId: SPR-POSETS-PART-01KQN9
tags:
- category-specs
- spec
- feature
- sets
- algebras
- posets
- mapping
- theme-posets-partitions
---

# Map poset deferred graph polytope order-complex algebra polynomial Coxeter display and raw-interop surfaces to final owners
## Summary

Posets mapping owns constructor names, finite surface methods, certificate method split,
deferred non-core surface ownership, and slice/coslice structure methods.

## Source Provenance

- `category_specs/posets/docs/MAPPING.md`
- Original migrated line: `Map poset deferred graph polytope order-complex algebra polynomial Coxeter display and raw-interop surfaces to final owners from category_specs/posets/docs/MAPPING.md`

## Context

- Graph, plotting, TikZ, polytope, order-complex, algebra, polynomial, and Coxeter surfaces are deferred mapping work, not open design decisions.
- Boolean predicates remain boolean; certificate variants become separately named certificate methods.
- Slice and coslice posets use structure_poset and structure_map, with domain/codomain inherited through Cat-owned structure_morphism.

## Source-Mining Contract

This leaf remains source-mining because the posets mapping defers several non-core
method groups to their final owners without yet assigning each owner explicitly.

Exact source anchors to mine:

- `category_specs/posets/docs/MAPPING.md:232-253`, which inventories the deferred
  non-core surfaces and states that ownership follows the target mathematical object or
  display/interop status rather than open-ended redesign.
- `category_specs/posets/docs/SAGE_INVENTORY.md:112-123`, which enumerates the same
  graph, polytope, order-complex, algebra, polynomial, Coxeter, display, and raw-interop
  Sage surfaces that need final placement.
- `.agents/skills/category-spec-style/references/style.md:1139-1149`, which makes
  `SAGE_INVENTORY.md` and `MAPPING.md` the canonical inputs for the mapping decision.
- `.agents/skills/category-spec-style/references/style.md:1229-1242`, which requires
  each surface to be placed at the highest category that actually owns the mathematics.

Decision this source-mining pass must produce:

- Graph/display group: assign final owner or explicit non-owner status for
  `comparability_graph`, `incomparability_graph`, `frank_network`, `graphviz_string`,
  `plot`, `show`, `tikz`, and `order_ideal_plot`, including which are display-only and
  therefore not category methods.
- Polytope/order-complex group: assign the owner categories and codomains for
  `order_polytope`, `chain_polytope`, and `order_complex`, including whether they land
  in polytope or simplicial-complex objects owned outside `Posets()`.
- Algebra group: assign owner and codomain for `incidence_algebra`,
  `p_partition_enumerator`, `moebius_algebra`, `quantum_moebius_algebra`, and
  `feichtner_yuzvinsky_ring`.
- Polynomial/Coxeter/invariant group: decide which of `zeta_polynomial`,
  `apozeta_polynomial`, `chain_polynomial`, `characteristic_polynomial`,
  `f_polynomial`, `flag_f_polynomial`, `flag_h_polynomial`, `h_polynomial`,
  `M_triangle`, `degree_polynomial`, `coxeter_polynomial`,
  `coxeter_transformation`, `coxeter_smith_form`, `kazhdan_lusztig_polynomial`,
  `moebius_function`, `moebius_function_matrix`, `magnitude`, `spectrum`, and
  `atkinson` stay as poset methods and which belong to separate target-object owners.
- Raw interop group: decide whether `unwrap` is retained only as Sage compatibility
  access with no category-level mathematical owner.

Hypotheses to record in the outcome:

- whether each surface is defined for all finite posets, only for finite lattices, or
  for stricter subclasses already named in the posets mapping;
- the exact return object/codomain for each admitted method group;
- the migration consequence when a surface is classed as display-only or raw interop.

Retire this card only when every deferred method listed in the cited mapping block has a
named owner or a documented display/interop exclusion. Reject individual surfaces from
category admission when the sources show they are presentation helpers rather than
mathematical category methods.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] When closing deferred surface mapping, place each method by target mathematical object or display/interop status.
- [ ] Keep order-theoretic lattice vocabulary separate from module/quadratic lattice vocabulary.

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.

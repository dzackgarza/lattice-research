---
trackerStatus:
  type: feature
title: Finish algebra constructor admission and explicit names for additive and table algebra construction routes
status: to-do
priority: critical
planId: SPR-ALG-TENSOR-01KQN9
tags:
- category-specs
- spec
- feature
- constructors
- algebras
- theme-constructor-routing
---

# Finish algebra constructor admission and explicit names for additive and table algebra construction routes
## Summary

The deleted Algebras triage recorded an initialization blocker for Algebras(ZZ), a
module hom-category/forms blocker for DualObjects, and constructor admission gaps.

## Source Provenance

- `category_specs/algebras/docs/TRIAGE.md` was removed in commit `8d1c21c`; recover exact prior content with `git show 8d1c21c^:category_specs/algebras/docs/TRIAGE.md`.
- Original migrated line: `Finish algebra constructor admission and explicit names for additive and table algebra construction routes from category_specs/algebras/docs/TRIAGE.md`

## Context

- Algebras(ZZ) raises _SageObject__custom_name while Sage resolves subcategory_class during category initialization.
- Algebras(ZZ).DualObjects() fails while Sage/project axiom inference builds modules.homsets._Forms; this is not an algebra constructor issue.
- Free-construction names may appear as abstract spec targets, but callable implementations require Sage-backed routing and refinement.
- Algebra construction is canonicalized to from_multiplication_tensor(multiplication=mu), where mu is a Tensor in T_R(M)[1,2].
- Basis-returning helpers such as center_basis, radical_basis, and derivations_basis should become object-returning methods such as center, radical, and derivations.

## Definition Grounding Required Before Spec Edit

This migrated card is executable for source mining and decision capture, but it does not by itself authorize a mathematical spec edit. Before moving, deleting, admitting, or generalizing any public category, method, constructor, predicate, invariant, Hom/End/Aut surface, or return type, record the canonical source path, exact definition, owner category, hypotheses, codomain/return object, and any invariance or equivalence proof obligation.

Use the subtree `MAPPING.md` and `SAGE_INVENTORY.md` files, Sage written docs/source, `theory/references/index.md` for literature-backed claims, and relevant repo `theory/` or skill-local sources. If the term is ambiguous or only supported by migrated backlog text, split to source-mining or decision work before editing specs.

## Acceptance Criteria

- [ ] The mathematical owner, public surface, and migration consequence are recorded in the relevant MAPPING.md or category spec file.
- [ ] No new subtree-local TRIAGE or process document is created; follow-up work is represented as tracker items.
- [ ] Any implementation blocker discovered during spec work is split into an implementation-work item with source provenance.
- [ ] Run just smoke-file algebras/smoketest.sage after algebra category initialization or constructor changes.
- [ ] Do not route plain-set S.algebra(R) into Algebras(R); it belongs to free_module over Modules(R).

## Dependencies And Boundaries

- Keep `SAGE_INVENTORY.md` and `MAPPING.md` as the source and mapping provenance; do not recreate subtree-local `TRIAGE.md` files.
- If execution reveals a missing mathematical owner, constructor, or category graph edge, split that as a new tracker item instead of patching around it.
- Preserve the original source path in updates so future agents can trace why this item exists.

## Work Log

- Created by migration repair from inline tracker item to full-document Nimbalyst task.


---
id: PLAN-STATIC-CATEGORY-REFINEMENT-ORDER
trackerStatus:
  type: plan
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn: []
title: Static category refinement order and constructor-interception sequence
status: needs-review
priority: critical
owner: Zack
description: 'Define and enforce the static category refinement order (which categories
  sit above which in the hierarchy) and the constructor-interception order (which
  constructors fire before which). Prevents downstream work from depending on
  unstable category graph edges or incorrect interception chains.'
successCriteria:
- Every `super_categories()` return in `category_specs/` is documented in the
  admitted-edges table or has an approved decision card.
- No constructor refines into a category whose status is `unstarted`.
- New categories added to the refinement order require an update to this plan
  and a decision card.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Static category refinement order and constructor-interception sequence

## Objective

Encode the project's category refinement order as a static constraint: every
`super_categories()` return is a documented, justified edge in the category
graph. Constructor interception order is similarly constrained: constructor
routing must not depend on unstable or downstream categories.

## Core principles

### Category refinement order

- Every subcategory's `super_categories()` must be justified by a mathematical
  specialization relationship (e.g. Fields → IntegralDomains → Rings) or a
  structural construction relationship (e.g. Subobjects → Sets).
- No subcategory may list a supercategory that is still under active spec review
  unless the edge is already settled by an approved decision or accepted spec.
- The refinement order is static: it should not change during execution based on
  Sage runtime state, constructor parameters, or coercion outcomes.

### Constructor-interception order

- Constructor routing must call Sage once, refine the returned parent into the
  appropriate project categories, and return the refined object.
- The refinement target categories must be a subset of the categories that the
  constructed parent actually satisfies. Do not refine into a category whose
  supercategory is not yet settled.
- Do not refine into a downstream category whose vocabulary depends on method
  ownership decisions still in review.

### Enforcement

- Before a subcategory is added or changed, verify that its supercategory chain
  does not include categories with unstarted or in-review status for their
  foundational specs.
- Before a constructor refines into a target category, verify that the target
  category's method surface is settled (status is at least needs-review with
  checked acceptance criteria).

## Admitted category refinement edges

The following edges are admitted as settled. Future work may add edges but must
not remove or reorder existing edges without a decision card.

| Subcategory | Supercategories | Justification |
|---|---|---|
| `Algebras(R)` | `Rings(R)`, `Modules(R)` | Algebras are rings with an R-module structure; Sage confirms. Source: category_specs/algebras/docs/MAPPING.md |
| `Algebras(R).WithBasis()` | `Algebras(R)`, `Modules(R).WithBasis()` | Basis-bearing algebras inherit both structures. Source: same. |
| `Modules(R).Free()` | `Modules(R)` | Free modules are modules. |
| `Modules(R).Free().FiniteRank()` | `Modules(R).Free()` | Finite-rank free modules refine free modules. |
| `Posets().Finite()` | `Posets()`, `SageFinitePosets()` | Finite posets refine posets and use Sage's finite poset implementation. |
| `Posets().JoinSemilattice().Finite()` | `Posets().JoinSemilattice()`, `Posets().Finite()` | Finite join-semilattices refine both. |
| `Sets().Partitioned()` | `Sets().Countable()`, `Sets().Subobjects()` | Partition sets are countable subobjects of the powerset. |
| `Sets().Partitioned().FiniteTotallyOrderedBase()` | `Sets().Partitioned()`, `Sets().Countable().Finite()` | Finite totally-ordered base partitions refine both. |
| `TensorAlgebraComponents(R)` | `Modules(R).TensorProducts()`, `Modules(R).Free().FiniteRank()` | Tensor components are tensor products of finite-rank free modules. |
| `_MatrixAlgebras(R, n, n)` | `Algebras(R)`, `Modules(R).Free().FiniteRank()` | Square matrix rings are algebras and finite-rank free modules. |
| `_ImageSets` | `Sets().Subobjects()`, `Sets().Subquotients()` | Image subobjects are both subobjects and subquotients. |

## Constructor interception order

Constructors must refine into target categories in this order of stability:

1. `Sets()` — always stable, always available.
2. `Modules(R)` — stable for PID base rings.
3. `Modules(R).Free()` — stable.
4. `Modules(R).Free().FiniteRank()` — stable.
5. `Algebras(R)` — stable.
6. `Posets()` / `Posets().Finite()` — stable.
7. `Sets().Countable()` / `Sets().Finite()` — stable.
8. `Sets().Subobjects()` / `Sets().Subquotients()` — stable.
9. `Rings()` subcategories — stable for settled rings (ZZ, QQ, finite fields, p-adics).
10. `TensorAlgebraComponents(R)` — stable.
11. `_MatrixAlgebras(R, n, n)` — stable.

Categories that should NOT be used as constructor refinement targets yet
(because their method ownership or supercategory edges are still under review):

- `Modules(R).Graded()` — Sage/project base-category mismatch not resolved.
- `Modules(R).WithForms()` — forms-owned categories pending Phase 02.
- Lattice/discriminant categories — pending FEATURE-MODULES-WITH-FORMS-AND-LATTICES.

## Acceptance Criteria

- [ ] Every `super_categories()` return in `category_specs/` is documented in the admitted-edges table or has an approved decision card.
- [ ] No constructor refines into a category whose status is `unstarted`.
- [ ] New categories added to the refinement order require an update to this plan and a decision card.

## Source corpus

- `.agents/skills/lattice-redesign/references/category-abc-spec.md`
- `category_specs/*/docs/MAPPING.md`
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-FOUNDATION-KERNEL/PLAN-CATEGORY-FOUNDATION-KERNEL.md`

## Work Log

- 2026-05-07: Created as missing skeleton plan referenced in current-goal-phase.md.
  Sources category refinement edges from existing super_categories() returns in
  the implementation files under category_specs/.

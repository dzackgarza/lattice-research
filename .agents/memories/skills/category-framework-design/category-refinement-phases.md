---
title: Category Refinement Phases
status: active
date: 2026-05-29
---
# Category Refinement Phases

Build the Sage category refinement surface as a static mathematical spec before
installing behavior.
The category hierarchy is the source of truth.
Runtime inspection may be used once to learn Sage's existing method names on examples,
but the resulting method lists are recorded explicitly in the spec.

## Constraints

- `Rings` is only a staging namespace so the spec does not clobber Sage's `Rings`
  category during development.
- Subcategories are mathematical categories, not software categories.
- Predicates are mathematical names such as `is_field`, `is_number_field`,
  `is_complete_ring`, and `is_pid`.
- No runtime method discovery, generic routing tables, or exception-driven type checks
  belong in the spec.
- Constructor interception is deferred until the category hierarchy and method surfaces
  are explicit.

## Phase 1: Static Hierarchy And Method Surface

Define the full ring and module subcategory hierarchy first.
For each subcategory, statically enumerate the relevant existing Sage method names on
`ParentMethods`, `ElementMethods`, or Hom-category `ElementMethods`. Methods remain
abstract unless the category itself owns a trivial predicate.

## Phase 2: Constructor Interception

Wire named Sage constructors such as `ZZ`, `QQ`, `PolynomialRing(R, n)`, and
`MatrixRing(R, n)` into the project category system via category refinement
(`_refine_category_`). Wrappers are thin and exist only to connect non-project objects
to project categories.

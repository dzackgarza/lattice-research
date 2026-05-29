---
title: Category Spec Subtrees — Subtree Ownership Reference
status: active
date: 2026-05-29
---
# Category Spec Subtree Ownership

This reference replaces the deleted nested `category_specs/**/AGENTS.md` files.
It records durable local ownership rules without forcing every agent to load every
subtree note.

## Global category-spec entry

Agents working under `category_specs/` must obey the root repo `AGENTS.md` and
`category_specs/AGENTS.md`. Load `category-spec-style` before touching specs, method
surfaces, constructors, morphisms, Hom/End/Aut surfaces, Sage wrappers, type
annotations, test files, smoke files, implementations, Sage inventory, or mapping
documents. Read `mem:skills/category-spec-workflow` before changing tracking, status,
plans, delegation, PR metadata, validation handoff, smoke triage, or stale-document
migration.

## Cat

`cat/` owns the category of categories, written `Cat()`.

Rules:

- `Cat()` is intentionally barebones.
  Do not build a deep subcategory hierarchy here.
- `Cat()` is the ambient category of 1-categories at this spec level.
  It is not an object of itself.
- Every project category and subcategory below this root is an object of `Cat()`.
- Every project category class must inherit from registered re-exported bases in
  `category_specs.cat`, not directly from `sage.categories.*`.
- `base_category_types.py` is the only Sage category-base touch point.
- Prefer the smallest wrapper that lets Sage do its usual work.
- Extensive class manipulation is a design smell.
- `Cat` uniformizes category-object constructions below the root.
- Category-level construction methods on `Cat()` itself belong in
  `Cat.SubcategoryMethods`.
- `Cat().join(...)` and `Cat().meet(...)` are thin category-order entry points over
  Sage's `Category.join` and `Category.meet`.
- Standard construction selectors are defined once in
  `universal_subcategory_methods.py`.
- `Constructors` classes are plain opt-in constructor collectors, not category objects
  or construction categories.
- Nontrivial algorithms belong under `implementations/`; trivial Sage wiring stays on
  the category surface.

## Homsets, endsets, and autsets

`homsets/` owns the generic hom, end, and aut category specs.

- Extend Sage's `HomsetsCategory`, `Homsets`, and `Homsets.Endset` through registered
  re-exports.
- Domain, codomain, call, identity, composition, inverse, and invertibility are
  universal morphism/hom-category concerns.
- Subtree hom-category specs own only structure that first appears there.
- Keep root spec categories separate: `homsets.py`, `endsets.py`, `autsets.py`.
- Use `C.HomCategory().Of(A, B)`, `C.EndCategory().Of(A)`, and `C.AutCategory().Of(A)`.
- Generic method surfaces are public universal classes.
- A hom object has a domain and codomain.
  `End_C(A)` is `Hom_C(A, A)`. `Aut_C(A)` is the invertible part of `End_C(A)`.

## Sets

`sets/` maps Sage set methods into mathematical category specs on specific
subcategories.

- Expose named Sage set constructors through `Sets().Constructors()`.
- Ring-theoretic methods do not go here.
- Set tests must use `Sets().Constructors()`.

## Topological spaces

`topological_spaces/` owns topological-space and metric-space method surfaces.

- A topological space is a set equipped with a topology.
  `Sets().Topological()` is the category of topological spaces.
- `Sets().Metric()` is the metric-space subcategory.

## Rings

`rings/` records Sage ring methods as ABC specs on specific subcategories.

- Expose named Sage ring constructors through `Rings().Constructors()`.
- Ring tests must use `Rings().Constructors()`.

## Modules

`modules/` records Sage module methods as ABC specs on specific subcategories.

- Ensure all named module constructors appear as methods on `Modules(R).Constructors()`.
- Module tests must use `Modules(R).Constructors()`.

## Forms and lattices

`forms/` owns categories for modules equipped with forms.
`lattices/` specifies module lattices (unrelated to order-theoretic lattices in
`posets/`).

- Preserve mathematical nouns in public names: `Lattice`, `LatticeMorphism`,
  `DiscriminantGroup`, `Overlattice`, `DualLattice`.

## Algebras

`algebras/` records algebra-specific method surfaces as ABC specs on subcategories of
`Algebras(R)`.

## Tensor algebra components

`tensor_algebra_components/` owns tensor-algebra component modules and tensor elements.
Use standard Sage tensor type order: `(p,q)` means `p` contravariant and `q` covariant
slots.

## Posets

`posets/` specifies order-theoretic categories.
A lattice here is a poset with meets and joins — unrelated to module lattices.

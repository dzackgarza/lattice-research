---
title: Category Creation Notes
status: active
date: 2026-05-29
---
# Category Creation: Base Rings and Module Categories

Three interlocking mechanisms:

## 1. `_refine_category_` — enrolling existing objects

`_refine_category_` is the proper non-monkey-patching way to add `ZZ`, `QQ`, `Zp`, etc.
to a new category. It computes the join of the object's current category with the new
one, and for Python-based parents also updates the dynamic class.
After this, `ZZ in ModuleBaseRings()` is `True`, and methods from `ParentMethods` become
accessible.

Important caveat for Cython types: `ZZ` is a Cython extension type
(`IntegerRing_class`), so `can_assign_class(ZZ)` is `False` — `_refine_category_`
updates `ZZ._category` but does NOT replace `ZZ.__class__` with a dynamic subclass.
Methods from `ParentMethods` are still reachable via `__getattr__` →
`getattr_from_category`.

## 2. Defining `ModuleBaseRings` as a `Category_singleton`

Uses `Category_singleton` since there is exactly one category of base rings globally.
No `Category_over_base_ring` needed.

## 3. `Category_over_base_ring` — parameterized categories

For categories that depend on a base ring (Modules(R), Algebras(R)), use
`Category_over_base_ring`. Sage caches these and `_with_axiom` dispatch works correctly
when the parameterized category is registered in `all_super_categories`.

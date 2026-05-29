---
title: Autset Categories Path
status: active
date: 2026-05-29
---
# How Endset and Autset Categories Are Constructed

The endset machinery is built on three interlocking pieces:

1. **Axiom registration.** `"Endset"` listed in `all_axioms` in
   `src/sage/categories/category_with_axiom.py`.
2. **Homsets as singleton.** `Homsets().Endset()` via `self._with_axiom("Endset")`.
   `extra_super_categories` encodes that every endset is a monoid.
3. **Per-category specialization.** Individual categories override
   `extra_super_categories` inside their own `Homsets.Endset`:
   - `Modules(R).Homsets().Endset()` → endomorphism ring is a `MagmaticAlgebra`
   - `AbelianVarieties(k).Homsets().Endset()` → endomorphism ring is a `Ring`
4. **Automatic dispatch.** When `X is Y`, the homset is placed in `category.Endsets()`
   automatically.

## Autset construction path

Follows the same pattern: `"Autset"` registered in `all_axioms`, nested as
`Endset.Autset`, with per-category `extra_super_categories`. An autset is a group
(invertible endomorphisms under composition).
The `Aut()` method dispatches through `_Hom_`.

The `SubcategoryMethods.Endset()` and `SubcategoryMethods.Autset()` methods make
`SomeCategory().Homsets().Endset()` and `SomeCategory().Homsets().Autset()` work
uniformly.

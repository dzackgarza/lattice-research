# Homsets Sage Inventory

This inventory records the Sage homset category surfaces that the project-level
`homsets` subtree extends.

## Sage Category Surfaces

| Sage surface | Source anchor | Method surface to represent |
| --- | --- | --- |
| `sage.categories.homsets.HomsetsCategory` | `sage/categories/homsets.py` | Functorial construction for `C.Homsets()`, default supercategory computation, `_test_homsets_category`, `base`, and named-class key routing through the base category. |
| `sage.categories.homsets.HomsetsOf` | `sage/categories/homsets.py` | Stub homset category for categories that have structure but no specialized homset category. |
| `sage.categories.homsets.Homsets` | `sage/categories/homsets.py` | Category of all homsets, supercategory `Sets()`, and generic homset parent method `is_endomorphism_set`. |
| `Homsets().Endset()` | `sage/categories/homsets.py`, nested `Homsets.Endset` | Endomorphism-set axiom; Sage adds `Monoids()` as an extra supercategory and provides parent method `is_endomorphism_set() -> True`. |

## Project Extension Surface

| Project surface | Mathematical meaning | Method surface to represent |
| --- | --- | --- |
| `Homsets().Autset()` | Automorphism sets, i.e. the invertible part of an endomorphism set. | Parent: `endset`, `domain`, `codomain`, `identity`, `Aut`; element: `is_invertible`, `is_injective`, `is_surjective`, `is_bijective`, `is_isomorphism`, `inverse`, `order`. |
| `homsets.utils.refine_automorphism_set_from_endset` | Generic construction of `Aut(X)` from `End(X)`. | Builds a Sage `ConditionSet` over the endset using the shared automorphism predicate, then refines through the requested autset category. |

Subtree-specific homset files must extend this surface by adding the laws of the
ambient category: set maps, ring homomorphisms, module homomorphisms, algebra
homomorphisms, and so on.

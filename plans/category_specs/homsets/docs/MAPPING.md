# Homsets Mapping

This file records the forward mapping from Sage's generic homset construction to the
project hom/end/aut hierarchy.

## Sage To Project Mapping

| Sage surface | Project surface | Consequence |
| --- | --- | --- |
| `HomsetsCategory` | `HomsetsCategory` | The project extends Sage's functorial construction through the registered re-export in `category_specs.cat`. |
| `Homsets()` | `Homsets()` | The project root homset category remains a subcategory of sets and supplies generic parent/element method surfaces. |
| `HomsetsCategory.category_of(C)` | `Homsets().Of(C)` | The project makes the base category explicit, so `C.Homsets()`, `C.Homsets().Endset()`, and `C.Homsets().Autset()` share one generic hierarchy before subtree-specific structure is added. |
| `Homsets().Endset()` | `Homsets().Endset()` | Sage's root endset category is valid and remains the root supercategory for generic endsets. |
| Sage has no independent `EndsetsCategory` functorial construction | `EndsetsCategory` and `Endsets().Of(C)` | The project adds this construction layer so `C.Endsets()` has the same uniform shape as `C.Homsets()`. |
| Sage has no generic `Autset` axiom in the audited file | `Homsets().Autset()` | The project adds the missing automorphism-set construction once, as the invertible part of an endset. |

## Subtree Contract

Subtree homset files use `Homsets().Of(C)`, `Endsets().Of(C)`, and `Autsets().Of(C)`
for generic supercategories instead of constructing their own `ConditionSet` over an endset. The
generic `End(X).Aut()` method dispatches through the actual category of `End(X)`, so
`End_R(M).Aut()` lands in `Modules(R).Homsets().Autset()` rather than the root
`Homsets().Autset()`. The allowed split is:

| Responsibility | Owner |
| --- | --- |
| Generic `Aut(X)` construction from `End(X)` | `homsets/utils.py` |
| Generic homset object and morphism specs | `homsets/homsets.py` |
| Generic endset specs | `homsets/endsets.py` |
| Generic autset specs | `homsets/autsets.py` |
| Public re-export surface | `homsets/__init__.py` |
| Set-specific function laws | `sets/homsets.py` |
| Ring-homomorphism laws | `rings/homsets.py` |
| Module-homomorphism laws and the extra `R`-module / `R`-algebra structure on `Hom_R(M, N)` and `End_R(M)` | `modules/homsets.py` |
| Algebra-homomorphism laws | `algebras/homsets.py` |
| Order-preserving-map laws | `posets/homsets.py` |
| Continuous-map and homeomorphism laws | `topological_spaces/homsets.py` |

Subtrees may refine `extra_super_categories()` and add category-specific methods, but
they must not duplicate the generic autset construction or generic autset element
predicates. Construction categories do not define method surfaces; root categories and
subtree categories do.

## Extra Structure Pattern

`modules/homsets.py` is the model for this pattern. `Modules(R).Homsets()` declares
both the generic `Homsets().Of(Modules(R))` supercategory and the additional module
structure on `Hom_R(M, N)`. Its endset subcategory declares the generic
`Endsets().Of(Modules(R))` supercategory and the additional `Algebras(R)` structure
on `End_R(M)`, while also retaining Sage's `MagmaticAlgebras(R)` surface.

Other subtrees follow the same rule. A subtree homset file must always declare its
homset, endset, and autset categories, even when they currently add only mathematical
names and future method locations. It adds a supercategory only when the hom/end/aut
set genuinely carries that structure.

## Source Note: Generic Sage Autsets

- Searched: Sage develop `src/sage/categories/homsets.py`, installed local
  `sage/categories/homsets.py`, and local subtree homset files.
- Found: Sage exposes `HomsetsCategory`, `Homsets`, and `Homsets.Endset`; the audited
  Sage file does not define a generic `Autset` category.
- Conclusion: inference -- the project `Homsets().Autset()` is a deliberate extension
  of Sage's generic homset construction, not a remapping of an existing Sage class.
- Confidence: High.
- Gaps: Sage git history and third-party Sage extensions were not searched.

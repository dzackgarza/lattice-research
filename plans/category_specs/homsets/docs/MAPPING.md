# Homsets Mapping

This file records the forward mapping from Sage's generic homset construction to the
project hom/end/aut hierarchy.

## Sage To Project Mapping

| Sage surface | Project surface | Consequence |
| --- | --- | --- |
| `HomsetsCategory` | `homsets.Homsets` as the project generic base | The project extends Sage's functorial construction instead of inventing a parallel category. |
| `Homsets()` | `Homsets()` | The project root homset category remains a subcategory of sets and supplies generic parent/element method surfaces. |
| `Homsets().Endset()` | `Homsets().Endset()` | Endsets are homsets `Hom(X, X)`. Subtrees may add algebraic structure, but the endset axiom and shared endomorphism surface live here. |
| Sage has no generic `Autset` axiom in the audited file | `Homsets().Autset()` | The project adds the missing automorphism-set construction once, as the invertible part of an endset. |

## Subtree Contract

Subtree homset files must import the generic autset helper instead of constructing
their own `ConditionSet` over an endset. The allowed split is:

| Responsibility | Owner |
| --- | --- |
| Generic `Aut(X)` construction from `End(X)` | `homsets/utils.py` |
| Generic homset/endset/autset object and element methods | `homsets/__init__.py` |
| Set-specific function laws | `sets/homsets.py` |
| Ring-homomorphism laws | `rings/homsets.py` |
| Module-homomorphism laws | `modules/homsets.py` |

Subtrees may refine `extra_super_categories()` and add category-specific methods, but
they must not duplicate the generic autset construction.

## Source Note: Generic Sage Autsets

- Searched: Sage develop `src/sage/categories/homsets.py`, installed local
  `sage/categories/homsets.py`, and local subtree homset files.
- Found: Sage exposes `HomsetsCategory`, `Homsets`, and `Homsets.Endset`; the audited
  Sage file does not define a generic `Autset` category.
- Conclusion: inference -- the project `Homsets().Autset()` is a deliberate extension
  of Sage's generic homset construction, not a remapping of an existing Sage class.
- Confidence: High.
- Gaps: Sage git history and third-party Sage extensions were not searched.

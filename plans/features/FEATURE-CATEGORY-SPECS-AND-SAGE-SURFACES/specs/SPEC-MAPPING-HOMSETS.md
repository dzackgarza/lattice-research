---
id: SPEC-MAPPING-HOMSETS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track homsets mapping spec
status: needs-review
priority: critical
requirement: Convert category_specs/homsets/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  Hom, End, Aut, image, kernel, and morphism signatures.
acceptanceCriteria:
- Source paths category_specs/homsets/docs/MAPPING.md and category_specs/homsets/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 80
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Hom Category Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/homsets/docs/MAPPING.md`.

Source inventory: `category_specs/homsets/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/homsets/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/homsets.py`
  - `sage/categories/homset.py`
  - `sage/categories/objects.py`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the generic
  homset reconciliation is recorded below, with remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Completeness Reconciliation: Generic Homset Surface

This pass checked the Sage generic homset construction and parent-method surface:

- `sage.categories.objects.Objects.SubcategoryMethods.Homsets()` calls
  `HomsetsCategory.category_of(self)`, and `Endsets()` is implemented as the
  `Endset` axiom on that homset category;
- `sage.categories.homsets.HomsetsCategory`, `HomsetsOf`, `Homsets`, and
  `Homsets.Endset` are represented by `C.HomCategory()`, `C.EndCategory()`, and the
  project extension of `C.AutCategory()` as the invertible part of `End_C(A)`;
- `sage.categories.homset.Homset` supplies parent-level `domain()`, `codomain()`,
  `identity()`, call/coercion behavior, reverse homsets, and
  `is_endomorphism_set()`;
- `identity()` is mathematically an endomorphism identity and is admitted on generic
  hom objects only under the endomorphism hypothesis; non-end homsets keep the Sage
  error behavior as interop evidence, not as a separate project method;
- the deprecated Sage helper `is_Endset(x)` remains compatibility evidence only; the
  project surface is categorical containment in the end-category owner.

Negative missing-surface finding for the generic homset pass:

- Searched: `category_specs/homsets/docs/SAGE_INVENTORY.md`, installed Sage
  `sage/categories/homsets.py`, `sage/categories/homset.py`,
  `sage/categories/objects.py`, and the converted generic homset mapping rows above.
- Found: the checked Sage generic surface consists of Homsets category construction,
  the Endset axiom, concrete Homset parent accessors and identity/coercion behavior,
  and a deprecated `is_Endset` compatibility helper. The converted spec represents
  these as generic Hom/End/Aut category surfaces, Hom-object methods, end-category
  identity behavior, or interop-only evidence.
- Conclusion: inference -- this pass found no additional generic Sage homset surface
  requiring a new public project owner outside the existing generic Hom/End/Aut
  mapping.
- Confidence: Medium.
- Gaps: subtree-specific homsets for sets, rings, modules, algebras, posets, and
  topological spaces remain owned by their corresponding mapping specs and are not
  closed by this generic homsets reconciliation.

## Converted Mapping Content

This file records the forward mapping from Sage's generic homset construction to the
project hom/end/aut category hierarchy.

## Sage To Project Mapping

| Sage surface | Project surface | Consequence |
| --- | --- | --- |
| `HomsetsCategory` | `HomCategoryConstruction` | Sage identifies the homsets construction, but project `HomCategoryConstruction` owns the mathematical method surface; Sage `HomsetsCategory` is inventory/interop, not a semantic superclass. |
| `Homsets()` | `HomCategory()` | The project root hom category supplies generic parent and element method surfaces. |
| `HomsetsCategory.category_of(C)` | `C.HomCategory()` | The project makes the base category explicit, so `C.HomCategory()`, `C.EndCategory()`, and `C.AutCategory()` share one generic hierarchy before subtree-specific structure is added. |
| `Homsets().Endset()` | `HomCategory().EndCategory()` | Sage's root endset category remains an interop supercategory for generic ends. |
| Sage has no independent `EndsetsCategory` functorial construction | `EndCategoryConstruction` and `C.EndCategory()` | The project adds this construction layer so `C.EndCategory()` has the same uniform shape as `C.HomCategory()`. |
| Sage has no generic `Autset` axiom in the audited file | `AutCategoryConstruction` and `C.AutCategory()` | The project adds the missing automorphism construction once, as the invertible part of an end category. |

## Project Extension Surface

| Project surface | Mathematical meaning | Method surface to represent |
| --- | --- | --- |
| `C.HomCategory().Of(A, B)` | `Hom_C(A, B)` for objects `A, B in C`. | Parent: `domain`, `codomain`, `identity`, `__call__`; element: morphism predicates and composition. |
| `C.EndCategory().Of(A)` | `End_C(A) = Hom_C(A, A)`. | Parent: endomorphism identity; element: endomorphism predicates. |
| `C.AutCategory().Of(A)` | `Aut_C(A)`, the invertible part of `End_C(A)`. | Parent: `end_category`, `domain`, `codomain`, `identity`; element: `is_invertible`, `is_isomorphism`, `inverse`, `order`. |
| `AutCategory.from_end_category` | Generic construction of `Aut_C(A)` from `End_C(A)`. | Calls a private condition-subset bridge over the end object using the aut predicate, with the requested aut category installed as the public project surface. |

Because `End_C(A)` is `Hom_C(A, A)`, the object `A` is already represented by the
generic hom-object methods `domain()` and `codomain()`. Subtree aliases such as
`base_set()` or `base_space()` are redundant and map to `domain()` for migration.

The raw Sage `ConditionSet` is an implementation detail of the generic aut
construction. Public aut objects expose `end_category()`, `domain()`,
`codomain()`, and `identity()`; they do not expose a `condition_set()` method.

## Subtree Contract

Subtree hom-category files use `HomCategoryOf(C)`, `GenericEndCategory`, and
`GenericAutCategory` for generic supercategories instead of constructing their own
`ConditionSet` over an end object. The allowed split is:

| Responsibility | Owner |
| --- | --- |
| Generic `Aut_C(A)` construction from `End_C(A)` | `homsets/autsets.py` |
| Generic hom object and morphism specs | `homsets/homsets.py` |
| Generic end specs | `homsets/endsets.py` |
| Generic aut specs | `homsets/autsets.py` |
| Public re-export surface | `homsets/__init__.py` |
| Set-specific function laws | `sets/homsets.py` |
| Ring-homomorphism laws | `rings/homsets.py` |
| Module-homomorphism laws and the extra `R`-module / `R`-algebra structure on `Hom_R(M, N)` and `End_R(M)` | `modules/homsets.py` |
| Algebra-homomorphism laws | `algebras/homsets.py` |
| Order-preserving-map laws | `posets/homsets.py` |
| Continuous-map and homeomorphism laws | `topological_spaces/homsets.py` |

Subtrees may refine `extra_super_categories()` and add category-specific methods, but
they must not duplicate the generic aut construction or generic aut element predicates.
Construction categories do not define method surfaces; root categories and subtree
categories do. Concrete hom categories attach an `Endset` axiom hook; concrete end
categories attach an `Autset` axiom hook. Those hook names exist for Sage interop only.

Selector ownership:

| Old local surface | Project surface | Rationale |
| --- | --- | --- |
| `HomCategory.SubcategoryMethods.EndCategory()` | inherited `Cat` universal `EndCategory()` selector | The universal selector already detects hom-category objects and applies the `Endset` axiom hook. The local method duplicated that selector. |
| `HomCategory.SubcategoryMethods.AutCategory()` | inherited `Cat` universal `AutCategory()` selector | Automorphism selection factors through the universal end selector and the `Autset` axiom hook. |
| `HomCategoryConstruction.SubcategoryMethods.EndCategory()` | inherited `Cat` universal `EndCategory()` selector | Construction categories are still category objects; the universal selector produces the same `Endset` refinement. |
| `HomCategoryConstruction.SubcategoryMethods.AutCategory()` | inherited `Cat` universal `AutCategory()` selector | The construction-level aut selector is inherited, not locally owned. |
| `EndCategory.SubcategoryMethods.AutCategory()` | inherited `Cat` universal `AutCategory()` selector | The universal selector already detects end-category objects and applies `Autset`. |
| `EndCategoryOf.SubcategoryMethods.AutCategory()` | inherited `Cat` universal `AutCategory()` selector | The generic end-category construction has no separate aut-navigation law beyond the universal selector. |

## Extra Structure Pattern

`modules/homsets.py` is the model for this pattern. `Modules(R).HomCategory()`
declares both the generic `HomCategoryOf(Modules(R))` supercategory and the additional
module structure on `Hom_R(M, N)`. Its end subcategory declares the additional
`Algebras(R)` structure on `End_R(M)`, while also retaining Sage's
`MagmaticAlgebras(R)` surface. Its aut subcategory is based on the end subcategory, so
it inherits endomorphism methods instead of re-declaring them.

Other subtrees follow the same rule. A subtree homset file must always declare its hom,
end, and aut categories, even when they currently add only mathematical names and
future method locations. It adds a supercategory only when the hom/end/aut object
genuinely carries that structure.

## Source Note: Generic Sage Autsets

- Searched: Sage develop `src/sage/categories/homsets.py`, installed local
  `sage/categories/homsets.py`, and local subtree hom-category files.
- Found: Sage exposes `HomsetsCategory`, `Homsets`, and `Homsets.Endset`; the audited
  Sage file does not define a generic `Autset` category.
- Conclusion: inference -- the project `AutCategory` layer is a deliberate extension of
  Sage's generic homset construction, not a remapping of an existing Sage class.
- Confidence: High.
- Gaps: Sage git history and third-party Sage extensions were not searched.

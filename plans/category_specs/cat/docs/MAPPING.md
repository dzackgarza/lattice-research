# Cat Mapping

This file maps Sage's category and functor machinery to the project `Cat()` subtree.

## Category Objects

Sage `sage.categories.category.Category` instances are the objects of `Cat()`.
For `C = Cat()`, the membership check `X in C` means exactly that `X` is a category
object. A functor is not an object of `Cat()`; it is an element of a functor homset
`A.Hom(B)`.

Consequences:

- Every project top-level category and subcategory should satisfy `C in Cat()`.
- Every category object should get shared category-object operations from
  `Cat.ParentMethods`.
- A homset category is itself a category object, so no separate object-membership
  rule is needed for functor categories.

## Category Order

Sage `Category.is_subcategory(self, c)` is the canonical subcategory relation.

Mapping:

- `C.leq(D)` means `C.is_subcategory(D)`.
- `C.geq(D)` means `D.is_subcategory(C)`.
- `C <= D` and `C >= D` are shorthands for the same relation.

This follows Sage's own meaning: `C.is_subcategory(D)` asserts that there is a
natural forgetful functor from `C` to `D`.

## Uniform Category-Object Surface

`Cat.ParentMethods` is the single source of truth for operations every category
object should expose:

- `Hom(D)`, `End()`, and `Aut()` for functor homsets in `Cat`;
- `leq`, `geq`, `<=`, and `>=` for the Sage category order;
- containment hooks for categories that need object and morphism membership:
  `_sage_super_categories`, `_sage_object_classes`, and `_sage_morphism_classes`.

Sage category instances receive ordinary category-object methods through generated
subcategory classes, so `Cat.register_category` copies the canonical `Cat.ParentMethods`
implementations into the registered `SubcategoryMethods` adapter. The copy is an
implementation bridge, not a second definition.

If a subtree already defines the same operation directly on its category class, that
local method takes precedence at runtime and should be treated as a later refactor
target. The Cat-level method remains the canonical specification for category objects.

## Containment

For an arbitrary category object `C`, `X in C` may mean either:

- `X` is an object of `C`; or
- `X` is a morphism in `C`.

For `C = Cat()`, this specializes to category-object membership only. Functor
membership is expressed by the relevant homset:

- `F in A.Hom(B)` for functors `A -> B`;
- `F in A.End()` for endofunctors of `A`;
- `F in A.Aut()` for autofunctors of `A`.

## Functors

Sage `Functor` instances are morphisms between category objects.

The project surface records Sage's functor call model:

- `_coerce_into_domain(x)`;
- `_apply_functor(x)`;
- `_apply_functor_to_morphism(f)`;
- `__call__(x)` dispatching through those hooks;
- `domain()` and `codomain()`.

Construction functors are still functors, but their extra Sage surface is recorded
separately: `pushout`, `merge`, `commutes`, `expand`, `common_base`, and
`coercion_reversed`.

## Standard Constructions

Sage functorial construction categories map directly to category-object methods:

| Sage class | Project method | Local file |
| --- | --- | --- |
| `SubobjectsCategory` | `C.Subobjects()` | `subcategories/constructions/subobjects.py` |
| `QuotientsCategory` | `C.Quotients()` | `subcategories/constructions/quotients.py` |
| `SubquotientsCategory` | `C.Subquotients()` | `subcategories/constructions/subquotients.py` |
| `CartesianProductsCategory` | `C.CartesianProducts()` | `subcategories/constructions/cartesian_products.py` |
| `HomsetsCategory` | `Cat().Homsets()` | `homsets.py` |

For `Cat()`, `Subobjects` means subcategories, `Quotients` means quotient
categories, `Subquotients` means category-level subquotients, and
`CartesianProducts` means product categories.

## Slice and Coslice Categories

Sage does not provide a dedicated installed class for categories over or under a
fixed category in the same way it provides `SubobjectsCategory` and
`QuotientsCategory`. The local mapping is:

- `C.ObjectsOver(T)` means categories `D` equipped with a structure functor
  `D -> T`;
- `C.ObjectsUnder(T)` means categories `D` equipped with a structure functor
  `T -> D`;
- `Slice = ObjectsOver`;
- `Coslice = ObjectsUnder`.

These classes use Sage's `RegressiveCovariantConstructionCategory` plus
`Category_over_base`, so they follow the same `category_of(...)` entry point as
Sage's built-in regressive constructions.

## Homsets, Endsets, and Autsets

`CatHomsets` is the category of functor homsets internal to `Cat()`.

Mapping:

- `A.Hom(B)` returns Sage's `Hom(A, B, category=Cat())` parent;
- `A.End()` returns Sage's `End(A, category=Cat())` parent;
- `A.Aut()` refines `A.End()` through the repository-level generic `Autset`
  construction;
- `A.Hom(B).category()` is `Cat().Homsets()`;
- `A.End().category()` is `Cat().Endsets()`;
- homset elements are Sage `Functor` instances;
- construction functors are a specialized functor method surface, not category
  objects.

The repository-level `homsets/` subtree owns generic homset/endset/autset
vocabulary such as `domain`, `codomain`, `Endset`, and `Autset`. The Cat subtree
adds only the functor-specific element surface and the `CatHomsets` category
refinement, following the same `HomsetsOf`/`GenericEndsets`/`GenericAutsets`
pattern used by the other subtrees.

## Constructors

`Cat().Constructors()` exists as an empty namespace to satisfy the subtree
structure and make the absence of direct constructors explicit. Category objects are
registered by being Sage/project `Category` instances. Functors are registered by
being Sage `Functor` or `ConstructionFunctor` instances and by lying in the relevant
functor homset.

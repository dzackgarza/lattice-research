# Cat Mapping

This file records how Sage's category and functor implementation maps to the
project's `Cat()` subtree.

## Category Objects

Sage `sage.categories.category.Category` instances are the objects of `Cat()`.

Consequences:

- Every project top-level category and subcategory should satisfy `C in Cat()`.
- `Cat()` itself accepts Sage/project categories through `_sage_object_classes()`.
- Existing set, ring, module, algebra, poset, homset, and topological-space
  categories should eventually reuse the same containment hooks instead of each
  writing a local membership test.

## Category Order

Sage `Category.is_subcategory(self, c)` is the canonical subcategory relation.

Mapping:

- `C.leq(D)` means `C.is_subcategory(D)`.
- `C.geq(D)` means `D.is_subcategory(C)`.
- `C <= D` and `C >= D` are shorthands for the same relation.

This follows Sage's own meaning: `C.is_subcategory(D)` asserts that there is a
natural forgetful functor from `C` to `D`.

## Uniform Containment

For any category object `C`, containment of an input `D` is checked uniformly:

- subcategory: `D` is a category and `D.is_subcategory(C)`;
- object: `D` is an instance of one of `C._sage_object_classes()` or lies in one
  of `C._sage_super_categories()`;
- morphism: `D` is an instance of one of `C._sage_morphism_classes()`.

The refinement hooks are:

- `_sage_super_categories() -> tuple[Category, ...]`;
- `_sage_object_classes() -> tuple[type, ...]`;
- `_sage_morphism_classes() -> tuple[type, ...]`.

For `Cat()`, `_sage_object_classes()` is `(Category,)` and
`_sage_morphism_classes()` is `(Functor, ConstructionFunctor)`.

## Required-Method Boilerplate

Sage builds parent, element, and morphism method classes from nested
`ParentMethods`, `ElementMethods`, and `MorphismMethods`. Its
`required_methods()` surface reports abstract parent and element requirements
after that dynamic class construction.

Mapping:

- shared category-object containment belongs in `Cat.ParentMethods`;
- category-element methods stay empty until a real category-element notion is
  introduced;
- category-morphism methods mirror Sage functor hooks;
- standard construction navigation belongs in `Cat.SubcategoryMethods` and is
  copied onto `Cat.ParentMethods` so concrete category objects can share it.

## Functors

Sage `Functor` instances are morphisms in `Cat()`.

The project surface records Sage's three-part functor call model:

- `_coerce_into_domain(x)`;
- `_apply_functor(x)`;
- `_apply_functor_to_morphism(f)`;
- `__call__(x)` dispatching through those hooks;
- `domain()` and `codomain()`.

Construction functors are still functors, but their extra Sage surface is
recorded separately: `pushout`, `merge`, `commutes`, `expand`, `common_base`,
and `coercion_reversed`.

## Standard Constructions

Sage functorial construction categories map directly to category-object methods:

| Sage class | Project method | Local file |
| --- | --- | --- |
| `SubobjectsCategory` | `C.Subobjects()` | `subcategories/constructions/subobjects.py` |
| `QuotientsCategory` | `C.Quotients()` | `subcategories/constructions/quotients.py` |
| `SubquotientsCategory` | `C.Subquotients()` | `subcategories/constructions/subquotients.py` |
| `CartesianProductsCategory` | `C.CartesianProducts()` | `subcategories/constructions/cartesian_products.py` |
| `HomsetsCategory` | `C.Homsets()` | `homsets.py` |

For `Cat()`, `Subobjects` means subcategories, `Quotients` means quotient
categories, `Subquotients` means category-level subquotients, and
`CartesianProducts` means product categories.

## Slice and Coslice Categories

Sage does not provide a dedicated installed class for "categories over a fixed
category" in the same way it provides `SubobjectsCategory` and
`QuotientsCategory`. The local mapping is:

- `C.ObjectsOver(T)` means categories `D` equipped with a structure functor
  `D -> T`;
- `C.ObjectsUnder(T)` means categories `D` equipped with a structure functor
  `T -> D`;
- `Slice = ObjectsOver`;
- `Coslice = ObjectsUnder`.

These classes use Sage's `RegressiveCovariantConstructionCategory` plus
`Category_over_base`, so they follow the same construction-category entry point
as Sage's built-in regressive constructions.

## Homsets, Endsets, and Autsets

`CatHomsets` is the category of functor homsets internal to `Cat()`.

Mapping:

- homset elements are functors;
- endset elements are endofunctors;
- autset elements are autofunctors;
- construction functors are documented as a specialized functor method surface,
  not as ordinary category objects.

The repository's top-level `homsets/` subtree owns generic homset/endset/autset
vocabulary. `cat/homsets.py` is deliberately local because functor homsets have a
different element surface than ordinary object morphism sets.

## Constructors

`Cat().Constructors()` exists as an empty namespace to satisfy the subtree
structure and make the absence of direct constructors explicit. Category objects
are registered by being Sage/project `Category` instances; functors are registered
by being Sage `Functor` or `ConstructionFunctor` instances.

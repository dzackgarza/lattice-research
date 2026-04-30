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
- `Cat().join([C, D, ...])` delegates to Sage `Category.join`.
- `Cat().meet([C, D, ...])` delegates to Sage `Category.meet`, except that the empty
  meet returns `Cat().Constructors().EmptyCategory()`.

This follows Sage's own meaning: `C.is_subcategory(D)` asserts that there is a
natural forgetful functor from `C` to `D`. The comparison shorthands are specified
for ordinary category objects only; `Cat()` itself is the root ambient category in
this spec and does not re-export `leq`, `geq`, `<=`, or `>=`.

## Uniform Category-Object Surface

`Cat.ParentMethods` is the single source of truth for operations every category
object should expose:

- `Hom()` / `End()` / `Aut()` for category-level homset, endset, and autset
  constructions;
- `Hom(D)` for the object-level functor homspace in `Cat`;
- `leq`, `geq`, `<=`, and `>=` for the Sage category order between ordinary
  category objects;
- containment hooks for categories that need object and morphism membership:
  `_sage_super_categories`, `_sage_object_classes`, and `_sage_morphism_classes`.

Wrapped category instances receive ordinary category-object methods through Sage's
generated classes. The wrapper base layer in `base_category_types.py` is the only
place that flattens `UniversalSubcategoryMethods` into Sage's `SubcategoryMethods`
provider path.

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
- `F in A.Hom(A)` for endofunctors of `A`;
- autofunctors are the invertible elements of `A.Hom(A)`.

## Functors

Sage `Functor` instances are morphisms between category objects.

The project surface records Sage's functor call model:

- `_coerce_into_domain(x)`;
- `_apply_functor(x)`;
- `_apply_functor_to_morphism(f)`;
- `__call__(x)` dispatching through those hooks;
- `domain()` and `codomain()`.

Sage construction functors from `sage.categories.pushout` are still actual functors,
but their extra Sage surface is recorded separately: `pushout`, `merge`, `commutes`,
`expand`, `common_base`, and `coercion_reversed`.

This is distinct from Sage `FunctorialConstructionCategory` classes such as
`SubobjectsCategory` or `QuotientsCategory`. Those are category objects produced by
methods like `C.Subobjects()`, not functors with domains, codomains, and object/morphism
actions.

## Standard Constructions

Sage functorial construction categories map directly to category-object methods:

| Sage class | Project method | Local file |
| --- | --- | --- |
| `SubobjectsCategory` | `C.Subobjects()` | `subcategories/constructions/subobjects.py` |
| `QuotientsCategory` | `C.Quotients()` | `subcategories/constructions/quotients.py` |
| `SubquotientsCategory` | `C.Subquotients()` | `subcategories/constructions/subquotients.py` |
| `CartesianProductsCategory` | `C.CartesianProducts()` | `subcategories/constructions/cartesian_products.py` |
| `HomsetsCategory` | `C.Homsets()` / `C.Hom()` | `homsets.py` |
| `HomsetsCategory.Endset()` | `C.Endsets()` / `C.End()` | `endsets.py` |
| `HomsetsCategory.Autset()` | `C.Autsets()` / `C.Aut()` | `autsets.py` |
| `JoinCategory` | `Cat().JoinCategories()` containment | `join_categories.py` |

The universal selectors for the standard construction rows live in
`universal_subcategory_methods.py`. Individual category classes still declare their
construction classes, and Sage's `category_of(...)` machinery resolves the specific
construction for the receiver.

For wrapped ordinary category objects, `Hom` has a closed two-case arity split in
`base_category_types._CatObjectMixin`: `C.Hom()` is the category-level construction,
and `C.Hom(D)` delegates to Sage's parent homspace for functors `C -> D`. `End()` and
`Aut()` are the category-level construction aliases; the object-level endomorphism
functor space is `C.Hom(C)`.

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

- `C.Hom()` is the category-level functorial construction whose objects are
  `Hom_C(A, B)` for objects `A, B` of `C`;
- `Cat().Hom()` is therefore the category of functor homsets;
- `A.Hom(B)` returns Sage's `Hom(A, B, category=Cat())` parent when `A` and `B`
  are category objects;
- `A.Hom(B).category()` is `Cat().Homsets()`;
- `A.Hom(A)` is the object-level endofunctor parent; `A.End()` is the category-level
  endset construction selector;
- homset elements are Sage `Functor` instances;
- construction functors are a specialized functor method surface, not category
  objects.

The repository-level `homsets/` subtree owns generic homset/endset/autset
vocabulary such as `domain`, `codomain`, `Endset`, and `Autset`. The Cat subtree
adds only the functor-specific element surface and the `CatHomsets`, `CatEndsets`,
and `CatAutsets` category refinements. These live in separate files:
`cat/homsets.py`, `cat/endsets.py`, and `cat/autsets.py`.

## Constructors

`Cat().Constructors()` owns category-object constructor entry points. It currently
exposes:

- `EmptyCategory()`: the bottom category object used by `Cat().meet([])` and by any
  surface that needs the empty category as a category object.

Ordinary category objects are registered by being Sage/project `Category` instances.
Functors are registered by being Sage `Functor` or `ConstructionFunctor` instances and
by lying in the relevant functor homset.

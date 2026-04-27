# Cat Sage Inventory

This inventory is the source grounding for the `cat/` subtree. `Cat()` is a
category of category objects, so the relevant Sage surface is Sage's category
implementation itself plus Sage's functor and functorial-construction machinery.

Installed Sage source root:

`/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/categories/`

## Category Objects

### `sage.categories.category.Category`

Source: `category.py`

Relevant methods and signatures:

| Line | Method | Cat use |
| --- | --- | --- |
| 643 | `_subcategory_hook_(self, category)` | Fast path for subcategory checks. |
| 687 | `__contains__(self, x)` | Sage membership checks `x.category().is_subcategory(self)`. |
| 1492 | `_make_named_class(self, name, method_provider, cache=False, picklable=True)` | Builds dynamic parent/element/morphism classes from nested method providers. |
| 1664 | `parent_class(self)` | Exposes `ParentMethods` inheritance for objects in a category. |
| 1714 | `element_class(self)` | Exposes `ElementMethods` inheritance for elements. |
| 1765 | `morphism_class(self)` | Exposes `MorphismMethods` inheritance for morphisms. |
| 1788 | `required_methods(self)` | Reports required and optional abstract parent/element methods. |
| 1803 | `is_subcategory(self, c)` | Sage's category-order predicate: natural forgetful functor from `self` to `c`. |
| 2089 | `_with_axiom(self, axiom)` | Constructs axiom subcategories. |
| 2125 | `_with_axioms(self, axioms)` | Constructs multiple axiom subcategories. |
| 2332 | `join(categories, as_list=False, ignore_axioms=(), axioms=())` | Join/intersection operation in the category lattice. |
| 2536 | `category(self)` | Sage currently places category objects in `Objects()`. |

Consequence for `cat/`: `Cat.ParentMethods` is the right place to declare the
uniform containment hooks that later categories should inherit or copy:
`_sage_super_categories`, `_sage_object_classes`, `_sage_morphism_classes`, and
`__contains__`.

### `sage.categories.category_singleton.Category_singleton`

Source: `category_singleton.py`

Use: base class for singleton category objects such as `Cat()`.

## Functors

### `sage.categories.functor.Functor`

Source: `functor.pyx`

Relevant methods and signatures:

| Line | Method | Cat use |
| --- | --- | --- |
| 63 | `cdef class Functor(SageObject)` | Base class for functors between categories. |
| 164 | `__init__(self, domain, codomain)` | Domain and codomain must be Sage `Category` instances. |
| 216 | `_apply_functor(self, x)` | Object-level functor action; subclasses should override. |
| 235 | `_apply_functor_to_morphism(self, f)` | Morphism-level functor action; default builds induced hom. |
| 272 | `_coerce_into_domain(self, x)` | Domain membership/coercion hook. |
| 320 | `__call__(self, x)` | Dispatches to morphism action or object action, then checks codomain. |
| 389 | `domain(self)` | Source category. |
| 401 | `codomain(self)` | Target category. |
| 451 | `ForgetfulFunctor_generic(Functor)` | Sage's forgetful functor class. |
| 541 | `IdentityFunctor_generic(ForgetfulFunctor_generic)` | Sage's identity functor class. |
| 626 | `IdentityFunctor(C)` | Public identity-functor constructor. |
| 646 | `ForgetfulFunctor(domain, codomain)` | Public forgetful-functor constructor; requires subcategory relation. |

Consequence for `cat/`: functors are morphism-like objects in `Cat()`. The
spec mirrors Sage's `_coerce_into_domain`, `_apply_functor`,
`_apply_functor_to_morphism`, `domain`, `codomain`, and `__call__` hooks.

### `sage.categories.pushout.ConstructionFunctor`

Source: `pushout.py`

Relevant methods and signatures:

| Line | Method | Cat use |
| --- | --- | --- |
| 45 | `class ConstructionFunctor(Functor)` | Construction functors are functors with coercion/pushout rules. |
| 128 | `__mul__(self, other)` | Composition in functorial notation. |
| 163 | `pushout(self, other)` | Rank-ordered composition for construction towers. |
| 187 | `__eq__(self, other)` | Mathematical-equivalence comparison, usually refined in subclasses. |
| 223 | `__hash__(self)` | Hash by representation. |
| 239 | `_repr_(self)` | Default construction-functor representation. |
| 259 | `merge(self, other) -> Self | None` | Combines compatible construction functors. |
| 284 | `commutes(self, other)` | Rank-tie commutation hook. |
| 309 | `expand(self)` | Decomposes composite constructions. |
| 333 | `coercion_reversed = False` | Direction flag used by coercion/pushout logic. |
| 335 | `common_base(self, other_functor, self_bases, other_bases)` | Last-resort common-base hook. |
| 378 | `_raise_common_base_exception_(...)` | Standard coercion error path. |

Consequence for `cat/`: construction functors are a distinguished morphism
surface, but they are still Sage `Functor` instances. `Cat()` records the extra
pushout/merge/commutation methods without rebuilding Sage's coercion model.

## Functorial Construction Categories

### `sage.categories.covariant_functorial_construction.FunctorialConstructionCategory`

Source: `covariant_functorial_construction.py`

Relevant methods:

| Line | Method | Cat use |
| --- | --- | --- |
| 231 | `class FunctorialConstructionCategory(Category)` | Abstract base for categories `F_Cat`. |
| 238 | `_base_category_class(cls)` | Recovers the base category class for non-nested constructions. |
| 298 | `__classcall__(cls, category=None, *args)` | Makes `F(C)` a shorthand for `C.F()`. |
| 328 | `__classget__(cls, base_category, base_category_class)` | Descriptor hook for nested construction categories. |
| 389 | `category_of(cls, category, *args)` | Canonical construction-category entry point. |
| 423 | `__init__(self, category, *args)` | Stores `base_category` and construction arguments. |
| 447 | `base_category(self)` | Returns the source category. |
| 462 | `extra_super_categories(self)` | Additional construction-specific supers. |
| 477 | `super_categories(self)` | Joins defaults with extra supers. |
| 492 | `_repr_object_names(self)` | Standard representation. |
| 501 | `_latex_(self)` | Standard LaTeX representation. |

### `CovariantConstructionCategory` and `RegressiveCovariantConstructionCategory`

Source: `covariant_functorial_construction.py`

Relevant methods:

| Line | Method | Cat use |
| --- | --- | --- |
| 516 | `class CovariantConstructionCategory(FunctorialConstructionCategory)` | Base for covariant construction categories. |
| 523 | `default_super_categories(cls, category, *args)` | Joins constructions on supercategories of `category`. |
| 592 | `is_construction_defined_by_base(self)` | Detects whether the base category defines the construction. |
| 629 | `additional_structure(self) -> Self | None` | Determines whether the construction adds structure. |
| 662 | `class RegressiveCovariantConstructionCategory(CovariantConstructionCategory)` | Base for constructions whose objects remain in the base category. |
| 669 | `default_super_categories(cls, category, *args)` | Adds the base category itself to the construction's supercategories. |

Consequence for `cat/`: standard category constructions should use
`category_of(...)` entry points. Subobjects, quotients, subquotients, objects over,
objects under, and Cartesian products should not use ad hoc category factories.

## Standard Construction Categories

### `sage.categories.subobjects.SubobjectsCategory`

Source: `subobjects.py`

Relevant surface:

| Line | Method | Cat use |
| --- | --- | --- |
| 20 | `class SubobjectsCategory(RegressiveCovariantConstructionCategory)` | Base for `C.Subobjects()`. |
| 25 | `default_super_categories(cls, category)` | Joins `category.Subquotients()` with regressive defaults. |

### `sage.categories.quotients.QuotientsCategory`

Source: `quotients.py`

Relevant surface:

| Line | Method | Cat use |
| --- | --- | --- |
| 20 | `class QuotientsCategory(RegressiveCovariantConstructionCategory)` | Base for `C.Quotients()`. |
| 25 | `default_super_categories(cls, category)` | Joins `category.Subquotients()` with regressive defaults. |

### `sage.categories.subquotients.SubquotientsCategory`

Source: `subquotients.py`

Relevant surface:

| Line | Method | Cat use |
| --- | --- | --- |
| 19 | `class SubquotientsCategory(RegressiveCovariantConstructionCategory)` | Base for `C.Subquotients()`. |

### `sage.categories.cartesian_product.CartesianProductsCategory`

Source: `cartesian_product.py`

Relevant surface:

| Line | Method | Cat use |
| --- | --- | --- |
| 226 | `class CartesianProductsCategory(CovariantConstructionCategory)` | Base for `C.CartesianProducts()`. |
| 243 | `_repr_object_names(self)` | Standard names for Cartesian-product categories. |
| 253 | `CartesianProducts(self) -> Self` | Idempotence by associativity of products. |
| 269 | `base_ring(self)` | Delegates base ring to the underlying category. |

### `sage.categories.homsets.HomsetsCategory`

Source: `homsets.py`

Relevant surface:

| Line | Method | Cat use |
| --- | --- | --- |
| 19 | `class HomsetsCategory(FunctorialConstructionCategory, CategoryWithParameters)` | Base for `C.Homsets()`. |
| 24 | `default_super_categories(cls, category)` | Uses full supercategories, nested homsets, or a `HomsetsOf` fallback. |
| 123 | `_test_homsets_category(self, **options)` | Generic homsets-category test. |
| 141 | `base(self)` | Finds base object for based hom categories. |
| 158 | `_make_named_class_key(self, name)` | Keys named classes by the base category's corresponding class. |

Consequence for `cat/`: `CatHomsets` is a small wrapper around functor homsets.
It should stay compatible with the repository's generic `homsets/` vocabulary, but
it must not pretend Sage has a separate upstream `Autsets` category.

## Local Cat Files

| File | Purpose |
| --- | --- |
| `cat/__init__.py` | Declares `Cat()`, uniform containment hooks, construction navigation, and functor surfaces. |
| `cat/homsets.py` | Declares functor homsets, endofunctor sets, autofunctor sets, and construction-functor method surface. |
| `cat/subcategories/constructions/subobjects.py` | Category-level subobjects: subcategories. |
| `cat/subcategories/constructions/quotients.py` | Category-level quotients. |
| `cat/subcategories/constructions/subquotients.py` | Category-level subquotients. |
| `cat/subcategories/constructions/objects_over.py` | Slice categories: categories equipped with a functor to a fixed category. |
| `cat/subcategories/constructions/objects_under.py` | Coslice categories: categories equipped with a functor from a fixed category. |
| `cat/subcategories/constructions/cartesian_products.py` | Product categories. |

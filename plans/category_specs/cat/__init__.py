r"""Category of categories.

This subtree introduces ``Cat()`` as the singleton category whose objects are
categories.  It is deliberately small: the immediate goal is to standardize
category-object vocabulary and common boilerplate, not to build a full
subcategory hierarchy for categories.

Public surface:

```
Cat()
|-- Subobjects()
|-- Quotients()
|-- Subquotients()
|-- ObjectsOver()
|-- ObjectsUnder()
|-- CartesianProducts()
`-- Homsets()
    |-- Endset()
    `-- Autset()
```
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, final

from sage.categories.functor import Functor
from sage.categories.pushout import ConstructionFunctor
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from .base_category_types import (
    Category,
    CategoryWithAxiom,
    CategoryWithAxiom_over_base_ring,
    CategoryWithParameters,
    Category_ideal,
    Category_module,
    Category_over_base,
    Category_over_base_ring,
    Category_singleton,
    Homsets,
    HomsetsCategory,
    HomsetsOf,
    _SageCategory,
    _SageCategoryIdeal,
    _SageCategoryModule,
    _SageCategoryOverBase,
    _SageCategoryOverBaseRing,
    _SageCategorySingleton,
    _SageCategoryWithParameters,
    _SageCategoryWithAxiom,
    _SageCategoryWithAxiomOverBaseRing,
    _SageCategoryWithAxiomSingleton,
    _SageHomsets,
    _SageHomsetsCategory,
    _SageHomsetsOf,
    _register_category_class_from_classcall,
    _undynamic_category_class,
)

if TYPE_CHECKING:
    from ..types import CategoryOfAutsets, CategoryOfEndsets, CategoryOfHomsets

_REGRESSIVE_CONSTRUCTION_NAMES = (
    "Subobjects",
    "Quotients",
    "Subquotients",
    "ObjectsOver",
    "ObjectsUnder",
    "CartesianProducts",
)

class _CategorySubcategoryMethodMixins:
    r"""Universal ``SubcategoryMethods`` bodies for registered category objects."""

    @cached_method
    def Subobjects(self) -> Category:
        return Cat.construction_class(self, "Subobjects").category_of(self)

    @cached_method
    def Quotients(self) -> Category:
        return Cat.construction_class(self, "Quotients").category_of(self)

    @cached_method
    def Subquotients(self) -> Category:
        return Cat.construction_class(self, "Subquotients").category_of(self)

    @cached_method
    def ObjectsOver(self, structure_object: Any) -> Category:
        return Cat.construction_class(self, "ObjectsOver").category_of(self, structure_object)

    @cached_method
    def ObjectsUnder(self, structure_object: Any) -> Category:
        return Cat.construction_class(self, "ObjectsUnder").category_of(self, structure_object)

    Slice = ObjectsOver
    Coslice = ObjectsUnder

    @cached_method
    def CartesianProducts(self) -> Category:
        return Cat.construction_class(self, "CartesianProducts").category_of(self)


class _GenericCategoryObjectMethods:
    r"""Baseline methods on objects X of any registered category C."""

    # Object-level hom/end/aut selectors:
    # for an object X in a category C, X.Hom(Y), X.End(), and X.Aut()
    # are the parents Hom_C(X, Y), End_C(X), and Aut_C(X). These are
    # mixed into C.ParentMethods for every category object C registered in Cat.

    @abstract_method
    def Hom(self, codomain: Any): ...

    def End(self):
        return self.Hom(self)

    def Aut(self):
        return self.End().Aut()


class _CategoryObjectMethods:
    r"""Methods on objects of ``Cat()``, i.e. category objects."""

    # Category-level hom/end/aut selectors:
    # mathematically, for a category C, C.Hom(), C.End(), and C.Aut()
    # (currently exposed here as Homsets(), Endsets(), and Autsets())
    # are categories whose objects are Hom_C(X, Y), End_C(X), and Aut_C(X).
    # These are not the object-level methods X.Hom(Y), X.End(), and X.Aut().

    @abstract_method
    def Subobjects(self) -> Category: ...

    @abstract_method
    def Quotients(self) -> Category: ...

    @abstract_method
    def Subquotients(self) -> Category: ...

    @abstract_method
    def ObjectsOver(self, structure_object: Any) -> Category: ...

    @abstract_method
    def ObjectsUnder(self, structure_object: Any) -> Category: ...

    @abstract_method
    def CartesianProducts(self) -> Category: ...

    @abstract_method
    def Homsets(self) -> CategoryOfHomsets: ...

    @cached_method
    def Endsets(self) -> CategoryOfEndsets:
        return self.Homsets().Endset()

    @cached_method
    def Autsets(self) -> CategoryOfAutsets:
        return self.Homsets().Autset()

    @cached_method
    def Hom(self) -> CategoryOfHomsets:
        return self.Homsets()

    @cached_method
    def End(self) -> CategoryOfEndsets:
        return self.Endsets()

    @cached_method
    def Aut(self) -> CategoryOfAutsets:
        return self.Autsets()

    def _sage_super_categories(self) -> tuple[Category, ...]:
        r"""Return Sage categories this category intentionally extends."""
        return ()

    def _sage_object_classes(self) -> tuple[type, ...]:
        r"""Return Sage parent classes whose instances are objects of this category."""
        return ()

    def _sage_morphism_classes(self) -> tuple[type, ...]:
        r"""Return Sage morphism classes whose instances are morphisms of this category."""
        return ()

    def _contains_subcategory(self, candidate: Any) -> bool:
        return isinstance(candidate, _SageCategory) and candidate.is_subcategory(self)

    def _contains_object(self, candidate: Any) -> bool:
        sage_classes = self._sage_object_classes()
        if isinstance(candidate, sage_classes) or any(candidate in C for C in self._sage_super_categories()):
            return True
        try:
            category = candidate.category()
        except AttributeError:
            return False
        return category.is_subcategory(self)

    def _contains_morphism(self, candidate: Any) -> bool:
        return isinstance(candidate, self._sage_morphism_classes())

    @final
    def __contains__(self, candidate: Any) -> bool:
        if isinstance(candidate, _SageCategory):
            return self._contains_subcategory(candidate)
        return (
            self._contains_object(candidate)
            or self._contains_morphism(candidate)
        )

    def leq(self, other: Category) -> bool:
        r"""Return whether ``self`` is a subcategory of ``other``."""
        return self.is_subcategory(other)

    def geq(self, other: Category) -> bool:
        r"""Return whether ``self`` contains ``other`` as a subcategory."""
        return other.is_subcategory(self)

    __le__ = leq
    __ge__ = geq


class _CategoryElementMethods(_GenericCategoryObjectMethods):
    r"""Baseline methods mixed into ParentMethods of registered categories."""


class _CategoryMorphismMethods:
    r"""Methods on morphisms in ``Cat()``, i.e. functors."""

    @abstract_method
    def __call__(self, category: Category) -> Category: ...

    @abstract_method
    def _coerce_into_domain(self, category: Category) -> Category: ...

    @abstract_method
    def _apply_functor(self, category: Category) -> Category: ...

    @abstract_method
    def _apply_functor_to_morphism(self, functor: Functor) -> Functor: ...


class _CategoryConstructionFunctorMethods(_CategoryMorphismMethods):
    r"""Additional Sage construction-functor surface relevant to ``Cat()``."""

    coercion_reversed: bool = False

    @abstract_method
    def pushout(self, other: ConstructionFunctor) -> ConstructionFunctor: ...

    @abstract_method
    def merge(self, other: ConstructionFunctor) -> ConstructionFunctor | None: ...

    @abstract_method
    def commutes(self, other: ConstructionFunctor) -> bool: ...

    @abstract_method
    def expand(self) -> list[ConstructionFunctor]: ...

    @abstract_method
    def common_base(self, other_functor: ConstructionFunctor, self_bases, other_bases): ...


class Cat(_SageCategorySingleton):
    r"""Singleton category whose objects are Sage/project category objects."""

    _registered_category_classes: ClassVar[set[type[Category]]] = set()
    _known_sage_category_classes: ClassVar[tuple[type[_SageCategory], ...]] = (
        _SageCategory,
        _SageCategoryWithParameters,
        _SageCategorySingleton,
        _SageCategoryWithAxiom,
        _SageCategoryWithAxiomSingleton,
        _SageCategoryWithAxiomOverBaseRing,
        _SageCategoryOverBase,
        _SageCategoryOverBaseRing,
        _SageCategoryModule,
        _SageCategoryIdeal,
        _SageHomsets,
        _SageHomsetsCategory,
        _SageHomsetsOf,
    )

    def __contains__(self, candidate: Any) -> bool:
        if not isinstance(candidate, _SageCategory):
            return False
        return (
            self._is_registered_category_object(candidate)
            or isinstance(candidate, self._known_sage_category_classes)
        )

    @classmethod
    def _is_registered_category_object(cls, candidate: _SageCategory) -> bool:
        candidate_cls = _undynamic_category_class(candidate.__class__)
        return any(
            getattr(category_cls, "_cat_parent_category", None) is cls
            for category_cls in candidate_cls.mro()
        )

    leq = _CategoryObjectMethods.leq
    geq = _CategoryObjectMethods.geq
    __le__ = leq
    __ge__ = geq

    @final
    def super_categories(self) -> list[Category]:
        return []

    @final
    def additional_structure(self):
        return None

    @cached_method
    def Homsets(self) -> CategoryOfHomsets:
        from .homsets import CatHomsets

        return CatHomsets.category_of(self)

    @cached_method
    def Endsets(self) -> CategoryOfEndsets:
        return self.Homsets().Endset()

    @cached_method
    def Autsets(self) -> CategoryOfAutsets:
        return self.Homsets().Autset()

    @cached_method
    def Hom(self) -> CategoryOfHomsets:
        return self.Homsets()

    @cached_method
    def End(self) -> CategoryOfEndsets:
        return self.Endsets()

    @cached_method
    def Aut(self) -> CategoryOfAutsets:
        return self.Autsets()

    @classmethod
    def register_category(
        cls,
        category_cls: type[_SageCategory],
        *,
        require_constructions: bool | None = None,
    ) -> type[Category]:
        r"""Register ``category_cls`` as a category object with universal methods."""
        if not isinstance(category_cls, type) or not issubclass(category_cls, _SageCategory):
            raise TypeError(f"expected a Sage Category class, got {category_cls!r}")

        constructions = cls._registered_constructions_for(category_cls, require_constructions)
        category_cls._cat_registered_constructions = constructions
        category_cls._cat_parent_category = cls
        category_cls.SubcategoryMethods = cls._mixed_subcategory_methods_for(category_cls)
        cls._registered_category_classes.add(category_cls)
        return category_cls

    @classmethod
    def construction_class(cls, category: Category, name: str):
        r"""Return the construction class registered for ``category``."""
        return cls._construction_class_for(category, name, set())

    @classmethod
    def _construction_class_for(cls, category: Category, name: str, seen: set[int]):
        current = category
        while isinstance(current, _SageCategory) and id(current) not in seen:
            seen.add(id(current))
            for category_cls in current.__class__.mro():
                constructions = category_cls.__dict__.get("_cat_registered_constructions")
                if constructions is not None and name in constructions:
                    return constructions[name]

            base_category = getattr(current, "base_category", None)
            if not callable(base_category):
                break
            try:
                next_category = base_category()
            except (AttributeError, TypeError, NotImplementedError, ValueError):
                break
            if next_category is current:
                break
            current = next_category

        super_categories = getattr(category, "super_categories", None)
        if callable(super_categories):
            try:
                candidates = super_categories()
            except (AttributeError, TypeError, NotImplementedError, ValueError):
                candidates = ()
            for super_category in candidates:
                try:
                    return cls._construction_class_for(super_category, name, seen)
                except NotImplementedError:
                    continue

        raise NotImplementedError(f"{category!r} has no registered {name} construction")

    @classmethod
    def _registered_constructions_for(
        cls,
        category_cls: type[Category],
        require_constructions: bool | None,
    ) -> dict[str, type[Category]]:
        raw_constructions = {name: cls._raw_class_attribute(category_cls, name) for name in _REGRESSIVE_CONSTRUCTION_NAMES}
        constructions = {name: construction for name, construction in raw_constructions.items() if construction is not None}
        if require_constructions is None:
            require_constructions = bool(constructions)
        if require_constructions:
            missing = tuple(name for name, construction in raw_constructions.items() if construction is None)
            if missing:
                names = ", ".join(missing)
                raise TypeError(f"{category_cls.__name__} must define required Cat construction(s): {names}")

        invalid = tuple(name for name, construction in constructions.items() if not hasattr(construction, "category_of"))
        if invalid:
            names = ", ".join(invalid)
            raise TypeError(f"{category_cls.__name__} construction(s) lack category_of: {names}")
        return constructions

    @staticmethod
    def _raw_class_attribute(category_cls: type, name: str) -> Any | None:
        for cls in category_cls.mro():
            if name in cls.__dict__:
                return cls.__dict__[name]
        return None

    @classmethod
    def _mixed_subcategory_methods_for(cls, category_cls: type[Category]) -> type:
        namespace: dict[str, Any] = {}
        method_provider = getattr(category_cls, "SubcategoryMethods", None)
        if method_provider is not None:
            for provider_cls in reversed(method_provider.mro()):
                if provider_cls is object:
                    continue
                for name, value in vars(provider_cls).items():
                    if name.startswith("__") and name.endswith("__"):
                        continue
                    if name == "_abc_impl":
                        continue
                    namespace[name] = value

        for name in (
            "Subobjects",
            "Quotients",
            "Subquotients",
            "ObjectsOver",
            "ObjectsUnder",
            "Slice",
            "Coslice",
            "CartesianProducts",
        ):
            if hasattr(_CategorySubcategoryMethodMixins, name):
                namespace[name] = getattr(_CategorySubcategoryMethodMixins, name)
            else:
                namespace[name] = getattr(_CategoryObjectMethods, name)

        namespace["__module__"] = category_cls.__module__
        namespace["__doc__"] = f"Subcategory methods for {category_cls.__name__}, mixed by Cat.register_category."
        return type("SubcategoryMethods", (), namespace)

    SubcategoryMethods = _CategorySubcategoryMethodMixins
    ParentMethods = _CategoryObjectMethods
    ElementMethods = _CategoryElementMethods
    MorphismMethods = _CategoryMorphismMethods
    ConstructionFunctorMethods = _CategoryConstructionFunctorMethods
    Subobjects = LazyImport("category_specs.cat.subcategories.constructions.subobjects", "_Subobjects")
    Quotients = LazyImport("category_specs.cat.subcategories.constructions.quotients", "_Quotients")
    Subquotients = LazyImport("category_specs.cat.subcategories.constructions.subquotients", "_Subquotients")
    ObjectsOver = LazyImport("category_specs.cat.subcategories.constructions.objects_over", "_ObjectsOver")
    ObjectsUnder = LazyImport("category_specs.cat.subcategories.constructions.objects_under", "_ObjectsUnder")
    CartesianProducts = LazyImport(
        "category_specs.cat.subcategories.constructions.cartesian_products",
        "_CartesianProducts",
    )
    _cat_registered_constructions = {
        "Subobjects": Subobjects,
        "Quotients": Quotients,
        "Subquotients": Subquotients,
        "ObjectsOver": ObjectsOver,
        "ObjectsUnder": ObjectsUnder,
        "CartesianProducts": CartesianProducts,
    }

    class Constructors:
        r"""Constructor namespace for category-level entry points.

        ``Cat()`` has no direct object constructors yet. Category objects are
        registered by being Sage/project ``Category`` instances, and functors by
        being Sage ``Functor`` or ``ConstructionFunctor`` instances.
        """

        def __init__(self, category: Cat) -> None:
            self._category = category

        def __repr__(self) -> str:
            return "Cat constructors"

    _Constructors = Constructors

    @cached_method
    def Constructors(self) -> Cat.Constructors:
        r"""Return the currently empty constructor namespace for ``Cat()``."""
        return self.__class__._Constructors(self)


Categories = Cat

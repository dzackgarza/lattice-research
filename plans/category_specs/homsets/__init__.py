r"""Generic homset, endset, and autset category specs.

Hierarchy:

```
Homsets()
+-- Homsets().Endset()
+-- Homsets().Autset()
```

This subtree extends Sage's existing
``sage.categories.homsets.HomsetsCategory`` / ``Homsets`` construction. It owns the
generic mathematical surface shared by all subtrees:

- a homset is a set of morphisms between two objects;
- an endset is a homset ``Hom(X, X)``;
- an autset is the invertible part of an endset.

Subtrees such as ``sets``, ``rings``, and ``modules`` add category-specific
morphism laws, but they do not recreate the autset construction.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.groups import Groups as SageGroups
from sage.categories.homsets import Homsets as SageHomsets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

from .utils import refine_automorphism_set_from_endset

if TYPE_CHECKING:
    from ..types import (
        Autset,
        Automorphism,
        Cardinality,
        CategoryElement,
        CategoryObject,
        Endomorphism,
        Endset,
        Morphism,
        MorphismConstructorData,
    )


class _HomsetObjectMethods(SageHomsets.ParentMethods):
    @abstract_method
    def domain(self) -> CategoryObject: ...

    @abstract_method
    def codomain(self) -> CategoryObject: ...

    @abstract_method
    def __call__(self, *data: MorphismConstructorData, **options: MorphismConstructorData) -> Morphism: ...

    @abstract_method
    def __contains__(self, obj: Any) -> bool: ...


class _HomsetMorphismMethods:
    @abstract_method
    def domain(self) -> CategoryObject: ...

    @abstract_method
    def codomain(self) -> CategoryObject: ...

    @abstract_method
    def __call__(self, x: CategoryElement) -> CategoryElement: ...

    @abstract_method
    def image(self, domain_subset: CategoryObject | None = None) -> CategoryObject: ...

    @abstract_method
    def is_injective(self) -> bool: ...

    @abstract_method
    def is_surjective(self) -> bool: ...

    def is_bijective(self) -> bool:
        return self.is_injective() and self.is_surjective()

    def is_isomorphism(self) -> bool:
        return self.is_bijective()


class _EndsetObjectMethods(SageHomsets.Endset.ParentMethods):
    @abstract_method
    def domain(self) -> CategoryObject: ...

    @abstract_method
    def codomain(self) -> CategoryObject: ...

    @abstract_method
    def identity(self) -> Endomorphism: ...

    def Aut(self) -> Autset:
        return Homsets().Autset().from_endset(self)


class _EndomorphismMethods:
    @abstract_method
    def is_invertible(self) -> bool: ...

    @abstract_method
    def inverse(self) -> Endomorphism: ...

    @abstract_method
    def order(self) -> Cardinality: ...


class _AutsetObjectMethods:
    @abstract_method
    def endset(self) -> Endset: ...

    def domain(self) -> CategoryObject:
        return self.endset().domain()

    def codomain(self) -> CategoryObject:
        return self.endset().codomain()

    def identity(self) -> Automorphism:
        return self.endset().identity()

    def Aut(self) -> Autset:
        return self


class _AutomorphismMethods:
    def is_invertible(self) -> bool:
        return True

    def is_injective(self) -> bool:
        return True

    def is_surjective(self) -> bool:
        return True

    def is_bijective(self) -> bool:
        return True

    def is_isomorphism(self) -> bool:
        return True

    @abstract_method
    def inverse(self) -> Automorphism: ...

    @abstract_method
    def order(self) -> Cardinality: ...


class Homsets(SageHomsets):
    r"""Category of all homsets, extended with generic autsets."""

    class SubcategoryMethods(SageHomsets.SubcategoryMethods):
        @cached_method
        def Autset(self):
            r"""Return the subcategory of automorphism sets."""
            return self._with_axiom("Autset")

    ParentMethods = _HomsetObjectMethods
    ElementMethods = _HomsetMorphismMethods

    class Endset(SageHomsets.Endset):
        r"""Category of all endomorphism sets."""

        ParentMethods = _EndsetObjectMethods
        ElementMethods = _EndomorphismMethods

    class Autset(CategoryWithAxiom):
        r"""Category of automorphism sets."""

        def extra_super_categories(self) -> list:
            return [self.base_category().Endset(), SageGroups()]

        @classmethod
        def from_endset(cls, endset: Endset) -> Autset:
            return refine_automorphism_set_from_endset(endset, cls())

        class ParentMethods(_AutsetObjectMethods):
            pass

        ElementMethods = _AutomorphismMethods


__all__ = ["Homsets"]

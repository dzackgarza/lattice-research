r"""GlobalFields ring subcategory spec."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, TypeVar, cast, final, override

from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ...utils import with_axiom
from .field import _Fields as _Fields

_F = TypeVar("_F", bound=Callable[..., object])
_cached_method = cast(Callable[[_F], _F], cached_method)

if TYPE_CHECKING:
    pass


class _GlobalFields(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Field().GlobalFields()``."""

    _base_category_class_and_axiom = (_Fields, "GlobalFields")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "global fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_Fields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_global_field()

    Archimedean = LazyImport(
        "category_specs.rings.subcategories.archimedean_global_field",
        "_ArchimedeanGlobalFields",
    )
    NonArchimedean = LazyImport(
        "category_specs.rings.subcategories.nonarchimedean_global_field",
        "_NonArchimedeanGlobalFields",
    )

    class SubcategoryMethods:
        @_cached_method
        @final
        def Archimedean(self) -> Category:
            return cast(Category, with_axiom(self, "Archimedean"))

        @_cached_method
        @final
        def NonArchimedean(self) -> Category:
            return cast(Category, with_axiom(self, "NonArchimedean"))

    class ParentMethods:
        @override
        @final
        def is_global_field(self) -> bool:
            return True

    class ElementMethods: ...

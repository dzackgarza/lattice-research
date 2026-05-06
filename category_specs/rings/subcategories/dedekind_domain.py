r"""DedekindDomains ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.dedekind_domains import DedekindDomains as SageDedekindDomains

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings
from .integral_domain import _IntegralDomains as _IntegralDomains

from ._lazy_subcategories import (
    _IntegrallyClosedDomains,
    _NoetherianRings,
)

if TYPE_CHECKING:
    pass


class _DedekindDomains(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().IntegralDomains().Dedekind()``."""

    _base_category_class_and_axiom = (_IntegralDomains, "Dedekind")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "Dedekind domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [
            SageDedekindDomains(),
            _IntegralDomains(),
            _NoetherianRings(),
            _IntegrallyClosedDomains(),
            Rings().KrullDimension(1),
        ]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageDedekindDomains() or (R in self.base_category() and R.is_dedekind_domain())

    class ParentMethods:
        @override
        @final
        def is_dedekind_domain(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...

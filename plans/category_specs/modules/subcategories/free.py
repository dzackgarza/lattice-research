r"""Free modules."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.category import Category
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Cardinality, ModuleBasis


class _Free(CategoryWithAxiom_over_base_ring):
    r"""Free modules over the base ring."""

    _base_category_class_and_axiom = (Modules, "Free")
    FiniteRank = LazyImport(__name__, "_FreeFiniteRank")

    @final
    def extra_super_categories(self):
        return [self.base_category().Projective()]

    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_free()

    class SubcategoryMethods:
        @cached_method
        @final
        def FiniteRank(self) -> Category:
            return self._with_axiom("FiniteRank")

    class ParentMethods:
        @final
        def is_free(self) -> bool:
            return True

        @abstract_method
        def rank(self) -> Cardinality:
            r"""Return the cardinality of a basis."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...


class _FreeFiniteRank(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules."""

    _base_category_class_and_axiom = (_Free, "FiniteRank")

    @final
    def extra_super_categories(self):
        return [self.base_category().FinitelyGenerated()]

    class ParentMethods:
        @abstract_method
        def basis(self) -> ModuleBasis: ...

        @abstract_method
        def dimension(self) -> Cardinality: ...

    class ElementMethods: ...

    class MorphismMethods: ...

r"""Free modules."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from .. import Modules

if TYPE_CHECKING:
    from ...types import Cardinality


class _Free(CategoryWithAxiom_over_base_ring):
    r"""Free modules over the base ring."""

    _base_category_class_and_axiom = (Modules, "Free")
    FiniteRank = LazyImport(__name__, "_FreeFiniteRank")

    def extra_super_categories(self):
        return [self.base_category().Projective()]

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_free()

    class SubcategoryMethods:
        @cached_method
        def FiniteRank(self):
            return self._with_axiom("FiniteRank")

    class ParentMethods:
        def is_free(self) -> bool:
            return True

        @abstract_method
        def rank(self) -> Cardinality:
            r"""Return the cardinality of a basis."""
            ...


class _FreeFiniteRank(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules."""

    _base_category_class_and_axiom = (_Free, "FiniteRank")

    def extra_super_categories(self):
        return [self.base_category().FinitelyGenerated()]

    class ParentMethods:
        @abstract_method
        def basis(self, *args, **kwds): ...

        @abstract_method
        def dimension(self) -> Cardinality: ...

    class ElementMethods: ...

    class MorphismMethods: ...

r"""Modules with a specified basis."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import CategoryElement, ModuleBasis


class _WithBasis(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a specified basis."""

    _base_category_class_and_axiom = (Modules, "WithBasis")
    WithOrderedBasis = LazyImport(__name__, "_WithOrderedBasis")

    @final
    def extra_super_categories(self):
        return [self.base_category().Free()]

    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_basis()

    class SubcategoryMethods:
        @final
        def WithOrderedBasis(self):
            return self._with_axiom("WithOrderedBasis")

    class ParentMethods:
        @final
        def has_basis(self) -> bool:
            return True

        @abstract_method
        def basis(self) -> ModuleBasis: ...

        @final
        def basis_index_set(self):
            return self.basis().keys()

    class ElementMethods: ...
    class MorphismMethods: ...


class _WithOrderedBasis(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a specified ordered basis."""

    _base_category_class_and_axiom = (_WithBasis, "WithOrderedBasis")

    @final
    def extra_super_categories(self):
        return [self.base_category().WithOrderedGeneratingSet()]

    @final
    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.has_ordered_basis()

    class ParentMethods:
        @final
        def has_ordered_basis(self) -> bool:
            return True

        @final
        def basis_order(self) -> tuple[CategoryElement, ...]:
            return tuple(self.basis().keys())

    class ElementMethods: ...

    class MorphismMethods: ...

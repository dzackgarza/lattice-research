r"""Semisimple algebras."""

from __future__ import annotations

from typing import final
from typing import Any

from ...cat import Category, CategoryWithAxiom_over_base_ring
from sage.categories.semisimple_algebras import SemisimpleAlgebras as SageSemisimpleAlgebras

from .. import Algebras


class _SemisimpleAlgebras(CategoryWithAxiom_over_base_ring):
    r"""Algebras whose Jacobson radical is zero."""

    _base_category_class_and_axiom = (Algebras, "Semisimple")

    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [Algebras(R), SageSemisimpleAlgebras(R)]

    @final
    def __contains__(self, A: Any) -> bool:
        return A in self.base_category() and A in SageSemisimpleAlgebras(self.base_ring())

    class ParentMethods:
        @final
        def is_semisimple(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...

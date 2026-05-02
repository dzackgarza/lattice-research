r"""Quotient modules."""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import QuotientsCategory

if TYPE_CHECKING:
    from ....types import Matrix, RingElement, RModMorphism, RModule, RModuleElement


class _Quotients(QuotientsCategory):
    r"""Quotient module category.

    Canonical chain: ``Modules(R).Quotients()``.
    """

    class ParentMethods:
        @abstract_method
        def cover(self) -> RModule:
            r"""Return the module being quotiented."""
            ...

        @abstract_method
        def relations(self) -> RModule:
            r"""Return the submodule of relations defining this quotient."""
            ...

        @final
        def ambient_module(self) -> RModule:
            r"""Return the module being quotiented."""
            return self.cover()

        @abstract_method
        def projection(self) -> RModMorphism: ...

        @final
        def quotient_map(self) -> RModMorphism:
            r"""Return the quotient projection."""
            return self.projection()

        @abstract_method
        def lift_map(self) -> RModMorphism: ...

        @abstract_method
        def lift(self, x: RModuleElement) -> RModuleElement: ...

        @abstract_method
        def free_cover(self) -> RModule: ...

        @abstract_method
        def free_relations(self) -> RModule: ...

        @abstract_method
        def retract(self, x: RModuleElement) -> RModuleElement: ...

        @abstract_method
        def quotient_module(
            self,
            submodule: RModule | Matrix | Sequence[RModuleElement] | Sequence[Sequence[RingElement]],
            check: bool = True,
            already_echelonized: bool = False,
        ) -> RModule: ...

    class ElementMethods:
        @final
        def lift(self) -> RModuleElement:
            return self.projection().lift(self)

    class MorphismMethods: ...

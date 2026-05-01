r"""Quotient modules."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ....cat import QuotientsCategory

if TYPE_CHECKING:
    from ....types import RModMorphism, RModule, RModuleElement


class _Quotients(QuotientsCategory):
    r"""Quotient module category."""

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

    class ElementMethods:
        @final
        def lift(self) -> RModuleElement:
            return self.projection().lift(self)

    class MorphismMethods: ...

r"""Submodules."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.subobjects import SubobjectsCategory
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ....types import Cardinality, QuotientModule, RModule, RModuleElement, SubModule


class _Subobjects(SubobjectsCategory):
    r"""Submodule category."""

    @abstract_method
    def as_subobject_of_self(self, M: RModule) -> SubModule:
        r"""Regard M as a submodule of itself via the identity."""
        ...

    class ParentMethods:
        @abstract_method
        def ambient_module(self) -> RModule:
            r"""The ambient R-module of which ``self`` is a submodule."""
            ...

        @abstract_method
        def inclusion(self): ...

        @abstract_method
        def intersect(self, N: SubModule) -> SubModule: ...

        def __and__(self, N: SubModule) -> SubModule:
            return self.intersect(N)

        def index(self) -> Cardinality:
            return self.inclusion().index()

        def is_primitive(self) -> bool:
            return self.inclusion().is_primitive()

        def lift(self, m: RModuleElement) -> RModuleElement:
            return self.inclusion()(m)

        @abstract_method
        def saturation(self) -> SubModule: ...

        @abstract_method
        def __le__(self, other: RModule) -> bool: ...

        def quotient_module(self) -> QuotientModule:
            return self.inclusion().cokernel()

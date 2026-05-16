r"""Quotient construction category for lattices."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ....cat import QuotientsCategory

if TYPE_CHECKING:
    from ....types import LatticeElement, LatticeMorphism


class _Quotients(QuotientsCategory):
    r"""Lattice quotients for quotient objects that remain in the lattice category.

    Canonical chain: ``Lattices(R).Quotients()``.
    """

    class ParentMethods:
        @abstractmethod
        def projection(self) -> LatticeMorphism: ...

        @abstractmethod
        def lift(self, x: _Quotients.ElementMethods) -> LatticeElement: ...

    class ElementMethods:
        @abstractmethod
        def parent(self) -> _Quotients.ParentMethods: ...

        @final
        def lift(self) -> LatticeElement:
            return self.parent().lift(self)

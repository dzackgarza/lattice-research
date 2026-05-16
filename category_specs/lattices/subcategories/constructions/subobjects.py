r"""Subobject construction category for lattices."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ....cat import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Lattice, LatticeMorphism


class _Subobjects(SubobjectsCategory):
    r"""Sublattices with the restricted bilinear form.

    Canonical chain: ``Lattices(R).Subobjects()``.
    """

    @abstractmethod
    def as_subobject_of_self(self, L: Lattice) -> Lattice:
        r"""Regard ``L`` as a sublattice of itself via the identity."""
        ...

    class ParentMethods:
        @abstractmethod
        def ambient(self) -> Lattice: ...

        @abstractmethod
        def inclusion(self) -> LatticeMorphism: ...

        @abstractmethod
        def intersect(self, M: Lattice) -> Lattice: ...

        @final
        def __and__(self, M: Lattice) -> Lattice:
            return self.intersect(M)

        @abstractmethod
        def saturation(self) -> Lattice: ...

        @abstractmethod
        def orthogonal_complement(self) -> Lattice: ...

    class ElementMethods: ...

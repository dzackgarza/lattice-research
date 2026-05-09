"""Concrete bilinear module morphism wrappers.

BilinearMorphism — a linear map between formed modules that preserves
or relates the form structure. Wraps a Sage module morphism with
form-awareness for kernel/image/cokernel computation.
"""

from __future__ import annotations

from sage.structure.element import Element
from sage.categories.morphism import Morphism


class BilinearMorphism(Morphism):
    """Morphism between formed modules — linear map with form preservation."""

    def __init__(self, parent, underlying):
        self._underlying = underlying
        Morphism.__init__(self, parent)

    def _call_(self, x):
        return self._underlying(x)

    def domain(self):
        return self._underlying.domain()

    def codomain(self):
        return self._underlying.codomain()

    def is_injective(self):
        return self._underlying.is_injective()

    def is_surjective(self):
        return self._underlying.is_surjective()

    def kernel(self):
        return self._underlying.kernel()

    def image(self):
        return self._underlying.image()

    def cokernel(self):
        return self._underlying.cokernel()

    def matrix(self):
        if hasattr(self._underlying, 'matrix'):
            return self._underlying.matrix()
        raise NotImplementedError

    def __repr__(self):
        return f"morphism({self.domain()} -> {self.codomain()})"

"""Free and torsion bilinear module carriers.

FreeBilinearModule: free R-module with bilinear form.
TorsionBilinearModule: finite torsion module with bilinear form.
"""

from __future__ import annotations

from sage.structure.parent import Parent


class FreeBilinearModule(Parent):
    """Free R-module of rank n equipped with a bilinear form."""

    def __init__(self, base_ring, rank, gram_matrix=None, form=None, codomain=None):
        self._rank = rank
        self._gram = gram_matrix
        self._form = form
        self._cd = codomain
        Parent.__init__(self, base=base_ring)

    def rank(self):
        return self._rank

    def gram_matrix(self):
        return self._gram

    def form(self):
        return self._form

    def codomain(self):
        return self._cd

    def span(self, elements):
        raise NotImplementedError

    def perp(self):
        raise NotImplementedError


class TorsionBilinearModule(Parent):
    """Finite torsion R-module with bilinear form (e.g., discriminant form)."""

    def __init__(self, base_ring, invariants, gram_matrix=None, form=None, codomain=None):
        self._invariants = tuple(invariants) if invariants else ()
        self._gram = gram_matrix
        self._form = form
        self._cd = codomain
        Parent.__init__(self, base=base_ring)

    def invariants(self):
        return self._invariants

    def gram_matrix(self):
        return self._gram

    def form(self):
        return self._form

    def codomain(self):
        return self._cd

    @classmethod
    def from_invariants_and_gram(cls, base_ring, invariants, gram, codomain=None):
        return cls(base_ring, invariants, gram_matrix=gram, codomain=codomain)

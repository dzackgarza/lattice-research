from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from sage.all import QQ, ZZ, matrix

from src.lattices.validation.presentations import MorphismPresentation, matrix_has_entries_in

if TYPE_CHECKING:
    from src.lattices.core.elements import FreeBilinearModuleElement
    from src.lattices.core.integral import Lattice
    from src.lattices.core.rational import RationalLattice


class RationalLatticeHomSpace:
    def __init__(self, domain: RationalLattice, codomain: RationalLattice):
        from src.lattices.core.integral import Lattice
        from src.lattices.morphisms.lattice import LatticeMorphism, RationalLatticeMorphism

        self._domain = domain
        self._codomain = codomain
        self._element_cls = LatticeMorphism if isinstance(domain, Lattice) and isinstance(codomain, Lattice) else RationalLatticeMorphism

    def domain(self):
        return self._domain

    def codomain(self):
        return self._codomain

    def _validate_matrix(self, matrix_data):
        from src.lattices.morphisms.lattice import LatticeMorphism

        presentation = MorphismPresentation(
            module_ring=ZZ if self._element_cls is LatticeMorphism else QQ,
            value_ring=QQ,
            domain_rank=self._domain.rank(),
            codomain_rank=self._codomain.rank(),
            domain_gram=self._domain.gram_matrix(),
            codomain_gram=self._codomain.gram_matrix(),
            matrix_data=matrix_data,
        )
        assert self._element_cls is not LatticeMorphism or matrix_has_entries_in(ZZ, presentation.matrix_data), (
            "Integral lattice morphisms require integral matrix entries"
        )
        return presentation.matrix_data

    def element_from_matrix(self, matrix_data):
        return self._element_cls(self._domain, self._codomain, self._validate_matrix(matrix_data))

    def element_from_dict(self, mapping: Mapping[FreeBilinearModuleElement, FreeBilinearModuleElement]):
        columns = []
        for generator in self._domain.gens():
            image = mapping[generator]
            assert image.parent() is self._codomain, "Images in a hom-space element_from_dict must lie in the codomain"
            columns.append(image.to_vector())
        return self.element_from_matrix(matrix(QQ, columns).transpose())

    def __contains__(self, morphism):
        from src.lattices.morphisms.lattice import RationalLatticeMorphism

        return isinstance(morphism, RationalLatticeMorphism) and morphism.domain() is self._domain and morphism.codomain() is self._codomain and morphism.to_matrix().transpose() * self._codomain.gram_matrix() * morphism.to_matrix() == self._domain.gram_matrix()

r"""Integral lattices."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Literal, final, override

from sage.categories.category import Category

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Integer, Matrix, Polyhedron, RealNumber, RModuleElement


class _IntegerLattices(Category_over_base_ring):
    r"""Finite-rank integral bilinear modules with lattice algorithms.

    Constructor target: ``Modules(ZZ).Constructors().IntegerLattice(...)``
    refines here as the legacy module-side route toward ``Lattices(ZZ)``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        R = self.base_ring()
        return [
            Category.join(
                [
                    Modules(R).Subobjects(),
                    Modules(R).WithOrderedGeneratingSet(),
                    Modules(R).OverPID(),
                    Modules(R).WithForms().Bilinear(),
                ]
            )
        ]

    class ParentMethods:
        @override
        @final
        def is_lattice(self) -> bool:
            return True

        @abstractmethod
        def gram_matrix(self) -> Matrix: ...

        @abstractmethod
        def LLL(
            self,
            delta: RealNumber | None = None,
            eta: RealNumber | None = None,
            algorithm: str = "fpLLL:wrapper",
            fp: str | None = None,
            prec: Integer = 0,
            early_red: bool = False,
            use_givens: bool = False,
            use_siegel: bool = False,
            transformation: bool = False,
        ) -> Matrix:
            del delta, eta, early_red, use_givens, use_siegel, transformation
            ...

        @abstractmethod
        def BKZ(
            self,
            delta: RealNumber | None = None,
            algorithm: str = "fpLLL",
            fp: str | None = None,
            block_size: Integer = 10,
            prune: Integer = 0,
            use_givens: bool = False,
            precision: Integer = 0,
            proof: bool | None = None,
        ) -> Matrix:
            del delta, block_size, prune, use_givens
            ...

        @abstractmethod
        def shortest_vector(
            self,
            update_reduced_basis: bool = True,
            algorithm: Literal["fplll", "pari"] = "fplll",
        ) -> RModuleElement:
            del update_reduced_basis
            ...

        @abstractmethod
        def voronoi_cell(self, radius: RealNumber | None = None) -> Polyhedron: ...

    class ElementMethods: ...

    class MorphismMethods: ...

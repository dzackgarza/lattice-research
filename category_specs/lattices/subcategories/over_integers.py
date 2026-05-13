r"""Lattices over the integer ring."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, final

from ...cat import CategoryWithAxiom_over_base_ring
from .over_pid import _LatticesOverPID

if TYPE_CHECKING:
    from sage.quadratic_forms.genera.genus import GenusSymbol_global_ring

    from ...types import Integer, Matrix, RingElement, SetFamily


class _LatticesOverIntegers(CategoryWithAxiom_over_base_ring):
    r"""Integral lattices over ``ZZ``.

    Canonical chain: ``Lattices(R).OverDedekindDomain().OverPID().OverIntegers()``.
    """

    _base_category_class_and_axiom = (_LatticesOverPID, "OverIntegers")
    _defining_predicates = ("is_over_integers",)

    class ParentMethods:
        @final
        def is_over_integers(self) -> bool:
            return True

        @abstractmethod
        def genus(self) -> GenusSymbol_global_ring: ...

        @abstractmethod
        def minimum(self) -> RingElement: ...

        @abstractmethod
        def short_vectors(self, bound: RingElement) -> SetFamily:
            r"""Return vectors ``v`` whose norm ``b(v, v)`` is at most ``bound``."""
            ...

        @final
        def short_vectors_up_to_sign(self, bound: RingElement) -> SetFamily:
            r"""Return representatives for the sign orbits ``{v, -v}`` in
            ``short_vectors(bound)``.
            """
            return self.short_vectors(bound, up_to_sign_flag=True)

        @abstractmethod
        def LLL(
            self,
            delta: RingElement | None = None,
            eta: RingElement | None = None,
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

    class ElementMethods: ...

    class MorphismMethods: ...

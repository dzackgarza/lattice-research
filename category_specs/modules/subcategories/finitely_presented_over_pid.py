r"""Spec for finitely presented modules over a PID.

This category owns most module constructions in ``Modules(R)`` and the
general spec should delegate concrete representations here.

Every object is represented by an ordered list of ring elements (which may
include zero), encoding a preferred decomposition of M:

    list = [0_1, ..., 0_n, r_1, ..., r_m]
        ==> M := R \oplus ... \oplus R \oplus R/r_1 \oplus ... \oplus R/r_m
                 (n free summands)             (m torsion summands)

This representation is *not* equal to the SNF of M -- it is isomorphic to
it.  Concretely, to compute ``coker(f: M -> N)``:

    1. Compute the Smith normal form ``D = SNF(A_f)`` together with
       ``U * A_f * V = D``.
    2. Define Q to be the module abstractly determined by D, with
       generators ``q_i``.
    3. The morphism ``\pi: N -> Q`` sending the generators ``n_i`` of N to
       ``q_i`` is then represented by ``U`` with each row interpreted mod
       the corresponding ``d_i``.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, final, override

from abc import abstractmethod

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction

if TYPE_CHECKING:
    from ...types import (
        DiscriminantGroup,
        Integer,
        Matrix,
        RingElement,
        RModMorphism,
        RModule,
        RModuleElement,
    )


class FinitelyPresentedModulesOverPID(CategoryWithAxiom_over_base_ring):
    r"""Finitely presented modules over a (commutative) PID.

    Canonical chain: ``Modules(R).FinitelyPresented().OverPID()``.

    Constructor target: matrix presentations and Sage ``FGP_Module`` quotient
    constructors refine here.

    Refines ``Modules(R).FinitelyPresented()`` for ``R`` a PID, where every
    finitely presented module decomposes as a direct sum of cyclic modules.
    """

    @override
    @final
    def extra_super_categories(self):
        return [
            self.base_category().FinitelyPresented(),
            self.base_category().OverPID(),
        ]

    @classmethod
    @final
    def from_matrix(cls, module_category, matrix: Matrix) -> RModule:
        r"""Return the finitely presented module ``coker(matrix)`` over a PID."""
        return module_category.from_invariant_factors(matrix.elementary_divisors())

    # ------------------------------------------------------------------
    # ParentMethods
    # ------------------------------------------------------------------

    class ParentMethods:
        @abstractmethod
        def order(self) -> RingElement:
            r"""Generator of ``Ann_R(M)``."""
            ...

        @abstractmethod
        def invariant_factors(self) -> Sequence[RingElement]:
            r"""Return ``[0, ..., 0, r_1, ..., r_n]`` with the leading zeros
            encoding the free summands ``R^n``.
            """
            ...

        @abstractmethod
        def invariants(self, include_ones: bool = False) -> tuple[RingElement, ...]:
            r"""Return the nonzero invariant factors, optionally including unit
            factors.
            """
            del include_ones
            ...

        @abstractmethod
        def smith_form_gens(self) -> tuple[RModuleElement, ...]:
            r"""Return generators compatible with the Smith decomposition."""
            ...

        @abstractmethod
        def free_part(self) -> RModule:
            r"""Free summand ``R^k`` of ``M = R^k \oplus T``."""
            ...

        @abstractmethod
        def torsion_part(self) -> RModule:
            r"""Torsion summand ``T`` of ``M = R^k \oplus T``."""
            ...

        @final
        def free_rank(self) -> Integer:
            return sum(1 for r in self.invariant_factors() if r.is_zero())

        @abstractmethod
        def element_from_vector(self, vec: Sequence[RingElement]) -> RModuleElement:
            del vec
            ...

        @abstractmethod
        def V(self) -> RModule: ...

        @abstractmethod
        def W(self) -> RModule: ...

        @abstractmethod
        def optimized(self) -> RModule: ...

        @abstractmethod
        def hom(self, images: Sequence[RModuleElement] | Matrix) -> RModMorphism:
            del images
            ...

    # ------------------------------------------------------------------
    # ElementMethods
    # ------------------------------------------------------------------

    class ElementMethods:
        @abstractmethod
        def to_vector(self) -> Sequence[RingElement]: ...

        @abstractmethod
        def order(self) -> RingElement:
            r"""Generator of ``Ann_R(m) = Ann_R(<m>)``."""
            ...

    class MorphismMethods: ...

    # ------------------------------------------------------------------
    # Hom category
    # ------------------------------------------------------------------

    class HomCategory(HomCategoryConstruction):
        class ParentMethods:
            @abstractmethod
            def from_dict(
                self, mapping: dict[RModuleElement, RModuleElement]
            ) -> RModMorphism:
                del mapping
                ...

            @abstractmethod
            def from_matrix(self, M: Matrix) -> RModMorphism: ...

            @abstractmethod
            def from_images(self, images: Sequence[RModuleElement]) -> RModMorphism:
                del images
                ...

        class ElementMethods:
            @abstractmethod
            def to_dict(self) -> dict[RModuleElement, RModuleElement]: ...

            @abstractmethod
            def to_matrix(self) -> Matrix: ...

            @abstractmethod
            def to_list(self) -> list[RModuleElement]: ...

            @abstractmethod
            def to_tuple(self) -> tuple[RModuleElement, ...]: ...

            @abstractmethod
            def to_function(self) -> Callable[[RModuleElement], RModuleElement]: ...

        class MorphismMethods: ...

    # ------------------------------------------------------------------
    # Torsion subcategory
    # ------------------------------------------------------------------

    class Torsion(CategoryWithAxiom_over_base_ring):
        r"""Finitely presented torsion modules over a PID."""

        class ParentMethods:
            @abstractmethod
            def p_part(self, p: RingElement) -> RModule:
                r"""Factor ``(R/p)^n`` of ``T`` in the decomposition
                ``M = F + T``.
                """
                ...

            @final
            def is_p_elementary(self, p: RingElement) -> bool:
                r"""``M`` is p-elementary iff ``M == M.p_part(p)``."""
                return self == self.p_part(p)

        class ElementMethods: ...

        class MorphismMethods: ...

    # ------------------------------------------------------------------
    # Lattices subcategory
    # ------------------------------------------------------------------

    class Lattices(CategoryWithAxiom_over_base_ring):
        r"""Finitely presented torsion-free modules over a PID equipped
        with a symmetric, nondegenerate, integral bilinear form.
        """

        class ParentMethods:
            @abstractmethod
            def determinant(self) -> RingElement: ...

            @abstractmethod
            def discriminant_group(self) -> DiscriminantGroup: ...

        class ElementMethods: ...

        class MorphismMethods: ...

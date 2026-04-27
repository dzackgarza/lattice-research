r"""Symmetric bilinear modules: ``Modules(R).WithForms().Bilinear().Symmetric()``.

A symmetric bilinear form satisfies ``b(v, w) = b(w, v)`` for all ``v``, ``w``.
"""

from __future__ import annotations

from typing import Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method

from plans.category_specs.modules.subcategories.axiomatic import _BilinearModules
from plans.category_specs.types import SubModule


class _SymmetricBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a symmetric bilinear form ``b: M \times M \to S``.

    An ``R``-bilinear form ``b`` is *symmetric* iff ``b(v, w) = b(w, v)``
    for all ``v, w \in M``.  The Gram matrix ``G`` is symmetric: ``G = G^T``.

    Symmetric forms support:
    - ``orthogonal_submodule_to(S)`` — ``S^\perp``
    - ``v.perp()`` — element-level orthogonal complement

    Neither requires nondegeneracy.
    """

    _base_category_class_and_axiom = (_BilinearModules, "Symmetric")

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_symmetric()

    class ParentMethods:
        def is_symmetric(self) -> bool:
            return True

        @abstract_method
        def orthogonal_submodule_to(self, S: SubModule) -> SubModule:
            r"""Return ``S^\perp = \{v \in M : b(v, s) = 0 \,\forall s \in S\}``.

            Always a submodule of ``self``.  ``S^\perp = S`` iff ``S`` is
            totally isotropic.  Does **not** require nondegeneracy.
            """
            ...

    class ElementMethods:
        @abstract_method
        def perp(self) -> SubModule:
            r"""Return the orthogonal complement ``v^\perp`` of this element.

            ``v^\perp = \{w \in M : b(v, w) = 0\}``, a submodule of the
            parent.  Does **not** require nondegeneracy.

            EXAMPLES::

                sage: U = Lattice.U()          # not tested
                sage: e = U.gen(0)             # not tested
                sage: e.perp()                 # not tested
                Rank-1 sublattice ...
            """
            ...

    class MorphismMethods: ...

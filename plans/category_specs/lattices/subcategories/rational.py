r"""Rational bilinear modules: ``Modules(R).WithForms().Bilinear().Rational()``.

A bilinear form ``b: M \times M \to K`` is *rational* iff the codomain is
``K = \mathrm{Frac}(R)``.  This is weaker than integral (``S = R \subsetneq K``)
and strictly contains the torsion case (``S = K/R``).

Rational lattices are the primary objects of study in the theory of
quadratic forms over ``\mathbb{Q}``.
"""

from __future__ import annotations

from typing import Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method

from plans.category_specs.modules.subcategories.axiomatic import _BilinearModules


class _RationalBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Modules with a ``K = \mathrm{Frac}(R)``-valued bilinear form.

    The form takes values in the fraction field of ``R``, not necessarily
    in ``R`` itself.  An integral form is always rational; a rational form
    need not be integral.

    The primary example is a rational lattice: a free ``\mathbb{Z}``-module
    of finite rank with a ``\mathbb{Q}``-valued symmetric bilinear form.
    """

    _base_category_class_and_axiom = (_BilinearModules, "Rational")

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_rational()

    class ParentMethods:
        def is_rational(self) -> bool:
            return True

        @abstract_method
        def integral_rescaling(self):
            r"""Return the smallest positive integer ``n`` such that ``n \cdot b``
            is integral, together with the rescaled module.

            EXAMPLES::

                sage: L = RationalLattice(matrix(QQ, [[1/2, 0], [0, 1/2]]))   # not tested
                sage: L.integral_rescaling()   # not tested
                (2, IntegralLattice(...))
            """
            ...

    class ElementMethods: ...

    class MorphismMethods: ...

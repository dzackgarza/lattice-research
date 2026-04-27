r"""Indefinite bilinear modules: ``Modules(R).WithForms().Bilinear().Indefinite()``.

A symmetric bilinear form is *indefinite* iff it is neither positive-definite
nor negative-definite: there exist vectors ``v``, ``w`` with ``b(v, v) > 0``
and ``b(w, w) < 0``.  Signature ``(p, q)`` satisfies ``p > 0`` and ``q > 0``.

All hyperbolic lattices, K3 lattices, and Lorentzian lattices are indefinite.
"""

from __future__ import annotations

from typing import Any

from plans.category_specs.lattices.subcategories.symmetric import _SymmetricBilinearModules
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring


class _IndefiniteBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with an indefinite symmetric bilinear form.

    A symmetric bilinear form ``b`` over an ordered ring is *indefinite* iff
    there exist ``v, w \in M`` with ``b(v,v) > 0`` and ``b(w,w) < 0``.
    Equivalently, the signature pair ``(p, q)`` satisfies ``p \ge 1``
    and ``q \ge 1``.

    This axiom is orthogonal to ``Definite``: a form is either indefinite,
    positive-definite, or negative-definite.

    EXAMPLES::

        sage: U = Lattice.U()   # not tested; hyperbolic plane, signature (1,1)
        sage: U in Modules(ZZ).WithForms().Bilinear().Symmetric().Indefinite()   # not tested
        True
    """

    _base_category_class_and_axiom = (_SymmetricBilinearModules, "Indefinite")

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_indefinite()

    class ParentMethods:
        def is_indefinite(self) -> bool:
            return True

        def is_definite(self) -> bool:
            return False

        def is_positive_definite(self) -> bool:
            return False

        def is_negative_definite(self) -> bool:
            return False

    class ElementMethods: ...

    class MorphismMethods: ...

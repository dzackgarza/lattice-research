r"""Definite bilinear modules: ``Modules(R).WithForms().Bilinear().Definite()``.

A symmetric bilinear form is *definite* iff it is either positive-definite
(``b(v, v) > 0`` for all nonzero ``v``) or negative-definite
(``b(v, v) < 0`` for all nonzero ``v``).  Signature ``(p, q)`` satisfies
``q = 0`` (positive-definite) or ``p = 0`` (negative-definite).
"""

from __future__ import annotations

from typing import final

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .symmetric import _SymmetricBilinearModules


class _DefiniteBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a definite (positive or negative definite)

    Canonical chain: ``Modules(R).WithForms().Bilinear().Symmetric().Definite()``.
    symmetric bilinear form.

    A symmetric bilinear form ``b`` is *definite* iff every nonzero vector
    satisfies ``b(v, v) \ne 0`` with a consistent sign.  For a positive-definite
    form ``b(v, v) > 0``; for negative-definite ``b(v, v) < 0``.

    Definite forms are automatically nondegenerate: if ``b(v, v) > 0`` for
    all nonzero ``v``, then ``v \ne 0 \Rightarrow b(v, -) \ne 0``.

    EXAMPLES::

        sage: A2 = Lattice.A(2)   # not tested; root lattice, negative definite
        sage: A2 in Modules(ZZ).WithForms().Bilinear().Symmetric().Definite()   # not tested
        True
    """

    _base_category_class_and_axiom = (_SymmetricBilinearModules, "Definite")
    _defining_predicates = ("is_definite",)

    class ParentMethods:
        @final
        def is_definite(self) -> bool:
            return True

        @final
        def is_indefinite(self) -> bool:
            return False

        @final
        def is_nondegenerate(self) -> bool:
            r"""Definite implies nondegenerate."""
            return True

        @abstract_method
        def is_positive_definite(self) -> bool:
            r"""Return ``True`` iff ``b(v, v) > 0`` for all nonzero ``v``."""
            ...

        @abstract_method
        def is_negative_definite(self) -> bool:
            r"""Return ``True`` iff ``b(v, v) < 0`` for all nonzero ``v``."""
            ...

    class ElementMethods:
        @final
        def is_anisotropic(self) -> bool:
            r"""Every nonzero element of a definite module is anisotropic."""
            return not self.is_zero()

    class MorphismMethods: ...


DefiniteBilinearModulesCategory = _DefiniteBilinearModules
DefiniteBilinearModulesObject = _DefiniteBilinearModules.ParentMethods
DefiniteBilinearModulesElement = _DefiniteBilinearModules.ElementMethods
DefiniteBilinearModulesMorphism = _DefiniteBilinearModules.MorphismMethods

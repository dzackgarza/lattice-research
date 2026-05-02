r"""Alternating bilinear modules: ``Modules(R).WithForms().Bilinear().Alternating()``.

An alternating bilinear form satisfies ``b(v, v) = 0`` for all ``v``,
which implies ``b(v, w) = -b(w, v)`` (skew-symmetry) when ``2`` is invertible.
"""

from __future__ import annotations

from typing import final

from ...cat import CategoryWithAxiom_over_base_ring
from .bilinear import _BilinearModules


class _AlternatingBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with an alternating bilinear form.

    Canonical chain: ``Modules(R).WithForms().Bilinear().Alternating()``.

    An ``R``-bilinear form ``b`` is *alternating* iff ``b(v, v) = 0`` for
    all ``v \in M``.  Equivalently, ``b(v, w) = -b(w, v)`` whenever ``2``
    is invertible in ``R``.  The Gram matrix has zero diagonal.

    .. NOTE::

        Alternating forms are orthogonal to the ``Symmetric`` axiom: a form
        that is both symmetric and alternating has ``b(v, w) = 0`` for all
        ``v, w`` (assuming ``\mathrm{char}(R) \neq 2``).
    """

    _base_category_class_and_axiom = (_BilinearModules, "Alternating")
    _defining_predicates = ("is_alternating",)

    class ParentMethods:
        @final
        def is_alternating(self) -> bool:
            return True

        @final
        def is_isotropic(self) -> bool:
            r"""Every element is self-orthogonal: ``b(v, v) = 0`` by definition."""
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


AlternatingBilinearModulesCategory = _AlternatingBilinearModules
AlternatingBilinearModulesObject = _AlternatingBilinearModules.ParentMethods
AlternatingBilinearModulesElement = _AlternatingBilinearModules.ElementMethods
AlternatingBilinearModulesMorphism = _AlternatingBilinearModules.MorphismMethods

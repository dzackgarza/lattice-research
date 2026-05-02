r"""Nondegenerate bilinear modules: ``Modules(R).WithForms().Bilinear().Nondegenerate()``.

A bilinear form ``b`` is *nondegenerate* iff the map
``\phi: M \to M^* = \mathrm{Hom}_R(M, R)`` sending ``v \mapsto b(v, -)``
is injective.  For free modules of finite rank over a domain this is
equivalent to ``\det(G) \neq 0``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ...cat import CategoryWithAxiom_over_base_ring
from .bilinear import _BilinearModules

if TYPE_CHECKING:
    from ...types import SubModule


class _NondegenerateBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a nondegenerate bilinear form.

    Canonical chain: ``Modules(R).WithForms().Bilinear().Nondegenerate()``.

    Nondegeneracy means the map ``v \mapsto b(v, -)`` is injective.
    For free finitely generated modules over an integral domain this is
    equivalent to ``\det(\text{Gram matrix}) \ne 0``.

    .. NOTE::

        Nondegeneracy does NOT imply the form is symmetric, alternating,
        positive-definite, or integral.  Those are separate axioms.
    """

    _base_category_class_and_axiom = (_BilinearModules, "Nondegenerate")
    _defining_predicates = ("is_nondegenerate",)

    class ParentMethods:
        @final
        def is_nondegenerate(self) -> bool:
            return True

        @abstract_method
        def radical(self) -> SubModule:
            r"""Return the radical ``\{v \in M : b(v, w) = 0 \,\forall w \in M\}``.

            For a nondegenerate form this is the zero submodule, but
            the abstract method is declared here so implementations can
            verify it.
            """
            ...

    class ElementMethods:
        @abstract_method
        def is_anisotropic(self) -> bool:
            r"""Return ``True`` iff ``b(v, v) \ne 0``.

            For a symmetric nondegenerate form, most elements are anisotropic;
            isotropic elements form the *null cone* (light cone in physics).
            """
            ...

    class MorphismMethods: ...


NondegenerateBilinearModulesCategory = _NondegenerateBilinearModules
NondegenerateBilinearModulesObject = _NondegenerateBilinearModules.ParentMethods
NondegenerateBilinearModulesElement = _NondegenerateBilinearModules.ElementMethods
NondegenerateBilinearModulesMorphism = _NondegenerateBilinearModules.MorphismMethods

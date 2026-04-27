r"""Nondegenerate bilinear modules: ``Modules(R).WithForms().Bilinear().Nondegenerate()``.

A bilinear form ``b`` is *nondegenerate* iff the map
``\phi: M \to M^* = \mathrm{Hom}_R(M, R)`` sending ``v \mapsto b(v, -)``
is injective.  For free modules of finite rank over a domain this is
equivalent to ``\det(G) \neq 0``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    pass

from plans.category_specs.modules.subcategories.axiomatic import _BilinearModules
from plans.category_specs.types import RModuleElement, SubModule


class _NondegenerateBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Modules equipped with a nondegenerate bilinear form.

    Nondegeneracy means the map ``v \mapsto b(v, -)`` is injective.
    For free finitely generated modules over an integral domain this is
    equivalent to ``\det(\text{Gram matrix}) \ne 0``.

    .. NOTE::

        Nondegeneracy does NOT imply the form is symmetric, alternating,
        positive-definite, or integral.  Those are separate axioms.
    """

    _base_category_class_and_axiom = (_BilinearModules, "Nondegenerate")

    def __contains__(self, M: Any) -> bool:
        return M in self.base_category() and M.is_nondegenerate()

    class ParentMethods:
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

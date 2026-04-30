r"""Spec for the hom/morphism layer over ``Modules(R)``.

Defines:
    RModuleHomCategory         -- the category of R-module homs Hom_R(M, N)
    RModuleHomCategory.Forms   -- forms Hom_R(T_R(M)[p,q], S) (linear,
                                  bilinear, quadratic, symmetric, ...)
    Modules(R).EndCategory()   -- category whose objects are End_R(M)
    Modules(R).AutCategory()   -- category whose objects are Aut_R(M)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.magmatic_algebras import MagmaticAlgebras as SageMagmaticAlgebras
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import Category, CategoryWithAxiom_over_base_ring
from ..homsets import GenericAutCategory, GenericEndCategory, HomCategoryOf

if TYPE_CHECKING:
    from typing import Self

    from ..types import (
        BilinearForm,
        BilinearFormsModule,
        Cardinality,
        Integer,
        QuadraticForm,
        QuadraticFormsModule,
        QuotientModule,
        RingElement,
        RModAut,
        RModMorphism,
        RModule,
        RModuleElement,
        SubModule,
    )


# ---------------------------------------------------------------------------
# Forms-axiom helpers (wired into RModuleHomCategory.Forms below)
# ---------------------------------------------------------------------------


class _Bilinear(CategoryWithAxiom_over_base_ring):
    class ParentMethods:
        @abstract_method
        def associated_quadratic_forms(self) -> QuadraticFormsModule: ...

    class ElementMethods:
        @abstract_method
        def associated_quadratic_form(self) -> QuadraticForm: ...

        @final
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            return self.evaluate(v.tensor(w))

    class MorphismMethods: ...


class _Quadratic(CategoryWithAxiom_over_base_ring):
    class ParentMethods:
        @abstract_method
        def associated_bilinear_forms(self) -> BilinearFormsModule: ...

    class ElementMethods:
        @abstract_method
        def associated_bilinear_form(self) -> BilinearForm: ...

        @final
        def q(self, v: RModuleElement) -> RModuleElement:
            return self.evaluate(v)

    class MorphismMethods: ...


# ---------------------------------------------------------------------------
# Hom-level parent methods
# ---------------------------------------------------------------------------


class _RModHomCategoryObjectMethods:
    @cached_method
    @final
    def zero(self):
        from sage.misc.constant_function import ConstantFunction

        return self(ConstantFunction(self.codomain().zero()))

    @abstract_method
    def natural_morphism(self) -> RModMorphism:
        r"""The morphism in Hom_R(M, N) sending e_i -> f_i for all
        generators e_i of M and f_i of N.  As a matrix this is ``[Id | 0]``
        or ``[Id | 0]^t``: rectangular with 1s along the diagonal.
        """
        ...


# ---------------------------------------------------------------------------
# Morphism (element) methods
# ---------------------------------------------------------------------------


class _RModMorphisms:
    # ``parent`` is a Sage ``Element`` intrinsic and is not restated here.

    @abstract_method
    def kernel(self) -> SubModule: ...

    @abstract_method
    def cokernel(self) -> QuotientModule: ...

    @abstract_method
    def coimage(self) -> SubModule: ...

    @abstract_method
    def evaluate(self, m: RModuleElement) -> RModuleElement: ...

    @abstract_method
    def index(self) -> Cardinality: ...

    @abstract_method
    def direct_sum(self, f: Self) -> Self: ...

    @abstract_method
    def tensor(self, f: Self) -> Self: ...

    @abstract_method
    def scale(self, r: RingElement) -> Self:
        r"""``(r*f)(m) := r * f(m) = f(r.m)``."""
        ...

    @abstract_method
    def _mul_(self, data: RingElement | Self) -> Self:
        r"""Concrete impls dispatch on ``RingElement`` (-> ``scale``)
        vs another ``RModMorphism`` (-> ``tensor``).
        """
        ...

    @final
    def is_primitive(self) -> bool:
        r"""``f: M -> N`` is primitive iff coker(f) is torsionfree."""
        return self.cokernel().is_torsionfree()

    @abstract_method
    def lift(self, m: RModuleElement) -> RModuleElement:
        r"""Return any element ``m'`` such that ``f(m') = m``."""
        ...

    @abstract_method
    def dual(self) -> Self:
        r"""Given f in Hom_R(A, B), return f^* in Hom_R(B^*, A^*) where
        f^*(\phi) := \phi \circ f.  (Also called the adjoint or transpose.)
        Satisfies ``<f(m), \phi>_{nat,N} = <m, f^*(\phi)>_{nat,M}``.
        """
        ...

    @final
    def saturation(self) -> Self:
        r"""Given f in Hom_R(A, B), find the inclusion ``g`` of im(f) into
        Sat_B(im(f)) and return ``h := g \circ f`` in Hom_R(A, B) so that
        im(h) is saturated.
        """
        return self.image().saturation().inclusion().pre_compose(self)


# ---------------------------------------------------------------------------
# Endomorphism element methods
# ---------------------------------------------------------------------------


class _RModEndomorphisms:
    @abstract_method
    def __pow__(self, n: Integer) -> Self: ...


# ---------------------------------------------------------------------------
# Automorphism element methods
# ---------------------------------------------------------------------------


class _RModAutomorphisms:
    r"""Module-specific automorphism methods; generic aut-category methods are inherited."""


# ---------------------------------------------------------------------------
# Forms axiom subcategory
# ---------------------------------------------------------------------------


class _Forms(CategoryWithAxiom_over_base_ring):
    r"""R-modules of the form ``Hom_R(T_R(M)[p,q], S)`` where ``T_R(M)[p,q]``
    is the (p, q) part of the bitensor R-algebra of M and ``S`` is an
    R-submodule of ``K := Frac(R)``.
    """

    class ParentMethods:
        @abstract_method
        def form_degree(self) -> tuple[Integer, Integer]:
            r"""Return ``(p, q)``."""
            ...

        @abstract_method
        def is_integral(self) -> bool: ...

        @abstract_method
        def is_rational(self) -> bool:
            r"""True if it takes a non-integral value."""
            ...

        @abstract_method
        def base_module(self) -> RModule:
            r"""If this is ``Hom_R(T_R(M)[p,q], S)``, return ``M``."""
            ...

    class SubcategoryMethods:
        @cached_method
        @final
        def Rational(self) -> Category:
            r"""``S = K``: ``Hom_R(M, K)``."""
            return self._with_axiom("Rational")

        @cached_method
        @final
        def Integral(self) -> Category:
            r"""``S = R``: ``Hom_R(M, R)``."""
            return self._with_axiom("Integral")

        @cached_method
        @final
        def Linear(self) -> Category:
            r"""(1, 0)-forms: ``Hom_R(M, S)``."""
            return self._with_axiom("Linear")

        @cached_method
        @final
        def Bilinear(self) -> Category:
            r"""(1, 1)-forms: ``Hom_R(M \otimes_R M^*, S)``."""
            return self._with_axiom("Bilinear")

        @cached_method
        @final
        def Quadratic(self) -> Category:
            r"""Twisted (1, 0)-forms: ``Hom_R(M, S^\sigma)``."""
            return self._with_axiom("Quadratic")

        @cached_method
        @final
        def NonDegenerate(self) -> Category:
            r"""Forms with trivial kernels."""
            return self._with_axiom("NonDegenerate")

        @cached_method
        @final
        def Symmetric(self) -> Category:
            r"""Symmetric (n, 0)-forms: ``Hom_R(Sym^n_R(M), S)``."""
            return self._with_axiom("Symmetric")

        @cached_method
        @final
        def Alternating(self) -> Category:
            r"""Alternating (n, 0)-forms: ``Hom_R(\Lambda^n_R(M), S)``."""
            return self._with_axiom("Alternating")

    Bilinear = _Bilinear
    Quadratic = _Quadratic
    class ElementMethods: ...
    class MorphismMethods: ...


# ---------------------------------------------------------------------------
# RModuleHomCategory: the hom category proper
# ---------------------------------------------------------------------------


class RModuleHomCategory(HomCategoryOf):
    r"""The category of R-module homs ``Hom_R(M, N)``.

    Objects are hom parents; elements are R-module morphisms.
    """

    @final
    def extra_super_categories(self):
        r"""``Hom_R(M, N)`` is again an R-module for any M, N."""
        return [HomCategoryOf(self.base_category()), self.base_category()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Forms(self) -> Category:
            return self._with_axiom("Forms")

    ParentMethods = _RModHomCategoryObjectMethods
    ElementMethods = _RModMorphisms
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport(__name__, "RModuleEndCategory")
    Forms = _Forms


# ---------------------------------------------------------------------------
# End and aut subcategories
# ---------------------------------------------------------------------------


class RModuleEndCategory(GenericEndCategory):
    _base_category_class_and_axiom = (RModuleHomCategory, "Endset")
    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport(__name__, "RModuleAutCategory")

    @final
    def extra_super_categories(self):
        r"""End_R(M) is an R-algebra."""
        from ..algebras import Algebras
        from . import Modules

        R = self.base_category().base_category().base_ring()
        return [*super().extra_super_categories(), Algebras(R), SageMagmaticAlgebras(R), Modules(R)]

    class ParentMethods:
        @abstract_method
        def base_module(self) -> RModule:
            r"""If this is End_R(M), return M."""
            ...

        @abstract_method
        def unit_group(self) -> RModAut: ...

        # Do not define ``as_automorphism`` -- promotion of invertible
        # objects should happen automatically.

    ElementMethods = _RModEndomorphisms
    class MorphismMethods: ...


class RModuleAutCategory(GenericAutCategory):
    _base_category_class_and_axiom = (RModuleEndCategory, "Autset")

    @final
    def extra_super_categories(self):
        r"""Aut_R(M) := End_R(M)^* is the group of units of End_R(M)."""
        return super().extra_super_categories()

    class ParentMethods:
        r"""Module-specific aut parent methods; generic aut methods are inherited."""

    ElementMethods = _RModAutomorphisms
    class MorphismMethods: ...

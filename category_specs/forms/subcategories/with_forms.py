r"""Modules equipped with forms."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, cast, final, override

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from ...homsets import HomCategoryConstruction, UniversalHomElementMethods
from ...modules import Modules
from ...utils import with_axiom

if TYPE_CHECKING:
    from ...types import OrthogonalGroup, RModuleMorphism


def _form_cached_method[_FormCachedMethod: Callable[..., object]](
    method: _FormCachedMethod,
) -> _FormCachedMethod:
    return cast(_FormCachedMethod, cached_method(method))


class FormedModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Non-full category of pairs ``(M, f)`` with a form on ``M``.

    Canonical chain: ``Modules(R).WithForms()``.
    """

    _base_category_class_and_axiom = (Modules, "WithForms")
    _defining_predicates = ("has_form",)

    class ParentMethods:
        @override
        @final
        def has_form(self) -> bool:
            return True

        @abstractmethod
        def is_bilinear(self) -> bool: ...

        @abstractmethod
        def is_quadratic(self) -> bool: ...

        @abstractmethod
        def form(self) -> RModuleMorphism: ...

        @final
        def orthogonal_group(self) -> OrthogonalGroup:
            r"""Return ``Aut_C(M)`` for this formed-module category ``C``."""
            return cast("OrthogonalGroup", self.category().AutCategory().Of(self))

    class SubcategoryMethods:
        @_form_cached_method
        @final
        def Bilinear(self) -> Category:
            r"""Introduced here: select the bilinear-formed subcategory."""
            return cast(Category, with_axiom(self, "Bilinear"))

        @_form_cached_method
        @final
        def Quadratic(self) -> Category:
            r"""Introduced here: select the quadratic-formed subcategory."""
            return cast(Category, with_axiom(self, "Quadratic"))

        @_form_cached_method
        @final
        def Symmetric(self) -> Category:
            r"""Introduced here: select the symmetric-bilinear subcategory."""
            return cast(Category, with_axiom(self, "Symmetric"))

        @_form_cached_method
        @final
        def Alternating(self) -> Category:
            r"""Introduced here: select the alternating-bilinear subcategory."""
            return cast(Category, with_axiom(self, "Alternating"))

        @_form_cached_method
        @final
        def Nondegenerate(self) -> Category:
            r"""Introduced here: select the nondegenerate-bilinear subcategory."""
            return cast(Category, with_axiom(self, "Nondegenerate"))

        @_form_cached_method
        @final
        def Integral(self) -> Category:
            r"""Introduced here: select the integral-bilinear subcategory."""
            return cast(Category, with_axiom(self, "Integral"))

        @_form_cached_method
        @final
        def Rational(self) -> Category:
            r"""Introduced here: select the rational-bilinear subcategory."""
            return cast(Category, with_axiom(self, "Rational"))

    class ElementMethods: ...

    class HomCategory(HomCategoryConstruction):
        class ElementMethods(UniversalHomElementMethods):
            def is_isometry(self) -> bool:
                r"""Return whether this form-preserving morphism is an isomorphism."""
                return self.is_isomorphism()

    Bilinear = LazyImport(
        "category_specs.forms.subcategories.bilinear", "BilinearModulesCategory"
    )
    Quadratic = LazyImport(
        "category_specs.forms.subcategories.quadratic", "QuadraticModulesCategory"
    )


class OverPIDFormedModulesCategory(CategoryWithAxiom_over_base_ring):
    r"""Modules over a PID equipped with a form.

    Canonical chain: ``Modules(R).OverPID().WithForms()``.
    """

    from ...modules.subcategories.over_pid import _OverPID

    _base_category_class_and_axiom = (_OverPID, "WithForms")
    _defining_predicates = ("has_form",)

    ParentMethods = FormedModulesCategory.ParentMethods

    SubcategoryMethods = FormedModulesCategory.SubcategoryMethods

    ElementMethods = FormedModulesCategory.ElementMethods

    class HomCategory(HomCategoryConstruction):
        class ElementMethods(FormedModulesCategory.HomCategory.ElementMethods): ...

    Bilinear = LazyImport(
        "category_specs.forms.subcategories.bilinear", "OverPIDBilinearModulesCategory"
    )
    Quadratic = LazyImport(
        "category_specs.forms.subcategories.quadratic",
        "OverPIDQuadraticModulesCategory",
    )


FormedModulesObject = FormedModulesCategory.ParentMethods
FormedModulesElement = FormedModulesCategory.ElementMethods
FormedModulesMorphism = FormedModulesCategory.HomCategory.ElementMethods
OverPIDFormedModulesObject = OverPIDFormedModulesCategory.ParentMethods
OverPIDFormedModulesElement = OverPIDFormedModulesCategory.ElementMethods
OverPIDFormedModulesMorphism = OverPIDFormedModulesCategory.HomCategory.ElementMethods

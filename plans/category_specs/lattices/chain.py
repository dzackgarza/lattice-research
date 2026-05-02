r"""Named lattice axiom chain.

``Lattices(R)`` is not a parallel category with the module-with-form chain as
one of its supercategories.  It is the named endpoint of the actual axiom chain

``Modules(R).Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral().Lattice()``.

The intermediate classes below are intentionally light.  Their job is to make
each step in that chain a real Sage axiom category with the correct immediate
base category; the mathematical method surface remains in the generic module
and bilinear-form files where it is first defined.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import CategoryWithAxiom_over_base_ring
from ..modules import Modules
from ..modules.subcategories.free import _FreeFiniteRank
from .homsets import LatticeAutCategory, LatticeEndCategory, LatticeHomCategory
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients

if TYPE_CHECKING:
    from ..types import DiscriminantGroup, Lattice, Ring, RModuleElement, RModuleMorphism, SubModule


class _FiniteRankFreeModulesWithForms(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules equipped with a form."""

    _base_category_class_and_axiom = (_FreeFiniteRank, "WithForms")
    _defining_predicates = ("has_form",)

    class ParentMethods:
        @final
        def has_form(self) -> bool:
            return True

        @abstract_method
        def is_bilinear(self) -> bool: ...

        @abstract_method
        def is_quadratic(self) -> bool: ...

        @abstract_method
        def form(self) -> RModuleMorphism: ...

    class ElementMethods: ...
    class MorphismMethods: ...

    Bilinear = LazyImport(__name__, "_FiniteRankFreeBilinearModules")


class _FiniteRankFreeBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules equipped with a bilinear form."""

    _base_category_class_and_axiom = (_FiniteRankFreeModulesWithForms, "Bilinear")
    _defining_predicates = ("is_bilinear",)

    class ParentMethods:
        @final
        def is_bilinear(self) -> bool:
            return True

        @abstract_method
        def is_symmetric(self) -> bool: ...

        @abstract_method
        def is_alternating(self) -> bool: ...

        @abstract_method
        def is_nondegenerate(self) -> bool: ...

        @abstract_method
        def is_integral(self) -> bool: ...

        @abstract_method
        def is_rational(self) -> bool: ...

        @final
        def b(self, v: RModuleElement, w: RModuleElement) -> RModuleElement:
            return self.form().b(v, w)

    class ElementMethods: ...
    class MorphismMethods: ...

    Symmetric = LazyImport(__name__, "_SymmetricFiniteRankFreeBilinearModules")


class _SymmetricFiniteRankFreeBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules equipped with a symmetric bilinear form."""

    _base_category_class_and_axiom = (_FiniteRankFreeBilinearModules, "Symmetric")
    _defining_predicates = ("is_symmetric",)

    class ParentMethods:
        @final
        def is_symmetric(self) -> bool:
            return True

        @abstract_method
        def is_definite(self) -> bool: ...

        @abstract_method
        def is_indefinite(self) -> bool: ...

        @abstract_method
        def is_positive_definite(self) -> bool: ...

        @abstract_method
        def is_negative_definite(self) -> bool: ...

        @abstract_method
        def orthogonal_submodule_to(self, S: SubModule) -> SubModule: ...

    class ElementMethods: ...
    class MorphismMethods: ...

    Nondegenerate = LazyImport(__name__, "_NondegenerateSymmetricFiniteRankFreeBilinearModules")


class _NondegenerateSymmetricFiniteRankFreeBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Finite-rank free modules with a nondegenerate symmetric bilinear form."""

    _base_category_class_and_axiom = (_SymmetricFiniteRankFreeBilinearModules, "Nondegenerate")
    _defining_predicates = ("is_nondegenerate",)

    class ParentMethods:
        @final
        def is_nondegenerate(self) -> bool:
            return True

        @abstract_method
        def radical(self) -> SubModule: ...

    class ElementMethods:
        @abstract_method
        def is_anisotropic(self) -> bool: ...

    class MorphismMethods: ...

    Integral = LazyImport(__name__, "_IntegralNondegenerateSymmetricFiniteRankFreeBilinearModules")


class _IntegralNondegenerateSymmetricFiniteRankFreeBilinearModules(CategoryWithAxiom_over_base_ring):
    r"""Integral nondegenerate symmetric bilinear forms on finite-rank free modules."""

    _base_category_class_and_axiom = (_NondegenerateSymmetricFiniteRankFreeBilinearModules, "Integral")
    _defining_predicates = ("is_integral",)

    class ParentMethods:
        @final
        def is_integral(self) -> bool:
            return True

        @final
        def is_rational(self) -> bool:
            return True

        @abstract_method
        def dual_lattice(self) -> Lattice: ...

        @abstract_method
        def inclusion_morphism(self) -> RModuleMorphism: ...

        @abstract_method
        def discriminant_group(self) -> DiscriminantGroup: ...

        def is_unimodular(self) -> bool:
            return self.discriminant_group().is_trivial()

        @abstract_method
        def is_even(self) -> bool: ...

    class ElementMethods:
        @abstract_method
        def discriminant_class(self) -> RModuleElement: ...

    class MorphismMethods: ...

    class SubcategoryMethods:
        @cached_method
        @final
        def Lattice(self) -> Category:
            return self._with_axiom("Lattice")

    Lattice = LazyImport(__name__, "_Lattices")


class _Lattices(CategoryWithAxiom_over_base_ring):
    r"""Lattices over ``R`` as the named endpoint of the lattice axiom chain."""

    _base_category_class_and_axiom = (_IntegralNondegenerateSymmetricFiniteRankFreeBilinearModules, "Lattice")
    _defining_predicates = ("is_lattice",)

    @final
    def _repr_object_names(self) -> str:
        return f"lattices over {self.base_ring()}"

    class Constructors:
        r"""Lattice constructor entry points over ``self.base_ring()``."""

        @final
        def __init__(self, category: _Lattices) -> None:
            self._category = category

        @final
        def __repr__(self) -> str:
            return f"lattice constructors over {self.base_ring()}"

        @final
        def category(self) -> _Lattices:
            return self._category

        @final
        def base_ring(self) -> Ring:
            return self.category().base_ring()

    _Constructors = Constructors

    class SubcategoryMethods:
        @cached_method
        @final
        def Constructors(self) -> _Lattices.Constructors:
            return _Lattices._Constructors(self)

        @cached_method
        @final
        def OverDedekindDomain(self) -> Category:
            return self._with_axiom("OverDedekindDomain")

        @cached_method
        @final
        def OverPID(self) -> Category:
            return self._with_axiom("OverPID")

        @cached_method
        @final
        def OverIntegers(self) -> Category:
            return self._with_axiom("OverIntegers")

        @cached_method
        @final
        def Even(self) -> Category:
            return self._with_axiom("Even")

        @cached_method
        @final
        def Unimodular(self) -> Category:
            return self._with_axiom("Unimodular")

        @cached_method
        @final
        def DualLattices(self) -> Category:
            from .subcategories.constructions.dual_lattices import _DualLattices

            return _DualLattices(self.base_ring())

        @cached_method
        @final
        def Overlattices(self) -> Category:
            from .subcategories.constructions.overlattices import _Overlattices

            return _Overlattices(self.base_ring())

        @cached_method
        @final
        def OrthogonalDirectSums(self) -> Category:
            from .subcategories.constructions.orthogonal_direct_sums import _OrthogonalDirectSums

            return _OrthogonalDirectSums(self.base_ring())

        @cached_method
        @final
        def DiscriminantGroups(self) -> Category:
            from .subcategories.constructions.discriminant_groups import _DiscriminantGroups

            return _DiscriminantGroups(self.base_ring())

    class ParentMethods:
        @final
        def is_lattice(self) -> bool:
            return True

    class ElementMethods: ...
    class MorphismMethods: ...

    HomCategory = LatticeHomCategory

    OverDedekindDomain = LazyImport(
        "category_specs.lattices.subcategories.over_dedekind",
        "_LatticesOverDedekindDomain",
    )
    OverPID = LazyImport("category_specs.lattices.subcategories.over_pid", "_LatticesOverPID")
    OverIntegers = LazyImport("category_specs.lattices.subcategories.over_integers", "_LatticesOverIntegers")
    Even = LazyImport("category_specs.lattices.subcategories.even", "_EvenLattices")
    Unimodular = LazyImport("category_specs.lattices.subcategories.unimodular", "_UnimodularLattices")

    Subobjects = _Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    CartesianProducts = _CartesianProducts
    DualLattices = LazyImport("category_specs.lattices.subcategories.constructions.dual_lattices", "_DualLattices")
    Overlattices = LazyImport("category_specs.lattices.subcategories.constructions.overlattices", "_Overlattices")
    OrthogonalDirectSums = LazyImport(
        "category_specs.lattices.subcategories.constructions.orthogonal_direct_sums",
        "_OrthogonalDirectSums",
    )
    DiscriminantGroups = LazyImport(
        "category_specs.lattices.subcategories.constructions.discriminant_groups",
        "_DiscriminantGroups",
    )


def _lattice_chain(base_ring: Ring) -> Category:
    r"""Return the immediate ambient category for ``Lattices(base_ring)``."""
    return (
        Modules(base_ring, dispatch=False)
        .Free()
        .FiniteRank()
        .WithForms()
        .Bilinear()
        .Symmetric()
        .Nondegenerate()
        .Integral()
    )


def lattice_category(base_ring: Ring) -> _Lattices:
    r"""Return ``Lattices(base_ring)`` as the named lattice axiom endpoint."""
    return _lattice_chain(base_ring).Lattice()


LatticesCategory = _Lattices
LatticesObject = _Lattices.ParentMethods
LatticesElement = _Lattices.ElementMethods
LatticesMorphism = _Lattices.MorphismMethods
LatticesHomCategory = LatticeHomCategory
LatticesEndCategory = LatticeEndCategory
LatticesAutCategory = LatticeAutCategory
LatticesHom = LatticeHomCategory.ParentMethods
LatticesEnd = LatticeEndCategory.ParentMethods
LatticesAut = LatticeAutCategory.ParentMethods
LatticesEndomorphism = LatticeEndCategory.ElementMethods
LatticesAutomorphism = LatticeAutCategory.ElementMethods

r"""Formed-module category surface.

``FormedModules(R)`` is the category of ``R``-modules equipped with a form.
It is the forms-subtree owner for the existing Sage-compatible spelling
``Modules(R).WithForms()``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from ..modules.homsets import RModuleAutCategory, RModuleEndCategory, RModuleHomCategory
from . import chain as _chain
from .chain import (
    FiniteRankFreeBilinearModulesCategory as FiniteRankFreeBilinearModulesCategory,
)
from .chain import (
    FiniteRankFreeBilinearModulesElement as FiniteRankFreeBilinearModulesElement,
)
from .chain import (
    FiniteRankFreeBilinearModulesMorphism as FiniteRankFreeBilinearModulesMorphism,
)
from .chain import (
    FiniteRankFreeBilinearModulesObject as FiniteRankFreeBilinearModulesObject,
)
from .chain import (
    FiniteRankFreeFormedModulesCategory as FiniteRankFreeFormedModulesCategory,
)
from .chain import (
    FiniteRankFreeFormedModulesElement as FiniteRankFreeFormedModulesElement,
)
from .chain import (
    FiniteRankFreeFormedModulesMorphism as FiniteRankFreeFormedModulesMorphism,
)
from .chain import (
    FiniteRankFreeFormedModulesObject as FiniteRankFreeFormedModulesObject,
)
from .subcategories.bilinear import (
    BilinearModulesCategory as BilinearModulesCategory,
)
from .subcategories.bilinear import (
    BilinearModulesElement as BilinearModulesElement,
)
from .subcategories.bilinear import (
    BilinearModulesMorphism as BilinearModulesMorphism,
)
from .subcategories.bilinear import (
    BilinearModulesObject as BilinearModulesObject,
)
from .subcategories.quadratic import (
    QuadraticModulesCategory as QuadraticModulesCategory,
)
from .subcategories.quadratic import (
    QuadraticModulesElement as QuadraticModulesElement,
)
from .subcategories.quadratic import (
    QuadraticModulesMorphism as QuadraticModulesMorphism,
)
from .subcategories.quadratic import (
    QuadraticModulesObject as QuadraticModulesObject,
)
from .subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesCategory as TorsionQuadraticModulesCategory,
)
from .subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesElement as TorsionQuadraticModulesElement,
)
from .subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesMorphism as TorsionQuadraticModulesMorphism,
)
from .subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesObject as TorsionQuadraticModulesObject,
)
from .subcategories.with_forms import (
    FormedModulesCategory as FormedModulesCategory,
)
from .subcategories.with_forms import (
    FormedModulesElement as FormedModulesElement,
)
from .subcategories.with_forms import (
    FormedModulesMorphism as FormedModulesMorphism,
)
from .subcategories.with_forms import (
    FormedModulesObject as FormedModulesObject,
)

type IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory = (
    _chain.IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory
)
type IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement = (
    _chain.IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement
)
type IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = (
    _chain.IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism
)
type IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject = (
    _chain.IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject
)
type NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory = (
    _chain.NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory
)
type NondegenerateSymmetricFiniteRankFreeBilinearModulesElement = (
    _chain.NondegenerateSymmetricFiniteRankFreeBilinearModulesElement
)
type NondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = (
    _chain.NondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism
)
type NondegenerateSymmetricFiniteRankFreeBilinearModulesObject = (
    _chain.NondegenerateSymmetricFiniteRankFreeBilinearModulesObject
)
type SymmetricFiniteRankFreeBilinearModulesCategory = (
    _chain.SymmetricFiniteRankFreeBilinearModulesCategory
)
type SymmetricFiniteRankFreeBilinearModulesElement = (
    _chain.SymmetricFiniteRankFreeBilinearModulesElement
)
type SymmetricFiniteRankFreeBilinearModulesMorphism = (
    _chain.SymmetricFiniteRankFreeBilinearModulesMorphism
)
type SymmetricFiniteRankFreeBilinearModulesObject = (
    _chain.SymmetricFiniteRankFreeBilinearModulesObject
)

_IntegralNondegenerateSymmetricCategory = (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory
)
_IntegralNondegenerateSymmetricElement = (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement
)
_IntegralNondegenerateSymmetricMorphism = (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism
)
_IntegralNondegenerateSymmetricObject = (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject
)

type IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory = (
    _IntegralNondegenerateSymmetricCategory
)
type IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement = (
    _IntegralNondegenerateSymmetricElement
)
type IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = (
    _IntegralNondegenerateSymmetricMorphism
)
type IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject = (
    _IntegralNondegenerateSymmetricObject
)

if TYPE_CHECKING:
    from ..cat import Category
    from ..types import Ring


@final
def FormedModules(base_ring: Ring) -> Category:
    r"""Return the category of ``R``-modules equipped with a form."""
    from ..modules import Modules

    return Modules(base_ring, dispatch=False).WithForms()


type FormedModulesHomCategory = RModuleHomCategory
type FormedModulesEndCategory = RModuleEndCategory
type FormedModulesAutCategory = RModuleAutCategory
type FormedModulesHom = RModuleHomCategory.ParentMethods
type FormedModulesEnd = RModuleEndCategory.ParentMethods
type FormedModulesAut = RModuleAutCategory.ParentMethods
type FormedModulesEndomorphism = RModuleEndCategory.ElementMethods
type FormedModulesAutomorphism = RModuleAutCategory.ElementMethods

type BilinearModulesHomCategory = RModuleHomCategory
type BilinearModulesEndCategory = RModuleEndCategory
type BilinearModulesAutCategory = RModuleAutCategory
type BilinearModulesHom = RModuleHomCategory.ParentMethods
type BilinearModulesEnd = RModuleEndCategory.ParentMethods
type BilinearModulesAut = RModuleAutCategory.ParentMethods
type BilinearModulesEndomorphism = RModuleEndCategory.ElementMethods
type BilinearModulesAutomorphism = RModuleAutCategory.ElementMethods

type QuadraticModulesHomCategory = RModuleHomCategory
type QuadraticModulesEndCategory = RModuleEndCategory
type QuadraticModulesAutCategory = RModuleAutCategory
type QuadraticModulesHom = RModuleHomCategory.ParentMethods
type QuadraticModulesEnd = RModuleEndCategory.ParentMethods
type QuadraticModulesAut = RModuleAutCategory.ParentMethods
type QuadraticModulesEndomorphism = RModuleEndCategory.ElementMethods
type QuadraticModulesAutomorphism = RModuleAutCategory.ElementMethods

type TorsionQuadraticModulesHomCategory = RModuleHomCategory
type TorsionQuadraticModulesEndCategory = RModuleEndCategory
type TorsionQuadraticModulesAutCategory = RModuleAutCategory
type TorsionQuadraticModulesHom = RModuleHomCategory.ParentMethods
type TorsionQuadraticModulesEnd = RModuleEndCategory.ParentMethods
type TorsionQuadraticModulesAut = RModuleAutCategory.ParentMethods
type TorsionQuadraticModulesEndomorphism = RModuleEndCategory.ElementMethods
type TorsionQuadraticModulesAutomorphism = RModuleAutCategory.ElementMethods

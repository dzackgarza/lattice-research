r"""Formed-module category surface.

``FormedModules(R)`` is the category of ``R``-modules equipped with a form.
It is the forms-subtree owner for the existing Sage-compatible spelling
``Modules(R).WithForms()``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from ..modules.homsets import RModuleAutCategory, RModuleEndCategory, RModuleHomCategory
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
from .chain import (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
)
from .chain import (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement,
)
from .chain import (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism,
)
from .chain import (
    IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject,
)
from .chain import (
    NondegenerateSymmetricFiniteRankFreeBilinearModulesCategory,
)
from .chain import (
    NondegenerateSymmetricFiniteRankFreeBilinearModulesElement,
)
from .chain import (
    NondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism,
)
from .chain import (
    NondegenerateSymmetricFiniteRankFreeBilinearModulesObject,
)
from .chain import (
    SymmetricFiniteRankFreeBilinearModulesCategory,
)
from .chain import (
    SymmetricFiniteRankFreeBilinearModulesElement,
)
from .chain import (
    SymmetricFiniteRankFreeBilinearModulesMorphism,
)
from .chain import (
    SymmetricFiniteRankFreeBilinearModulesObject,
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

IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesCategory = (
    _IntegralNondegenerateSymmetricCategory
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesElement = (
    _IntegralNondegenerateSymmetricElement
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesMorphism = (
    _IntegralNondegenerateSymmetricMorphism
)
IntegralNondegenerateSymmetricFiniteRankFreeBilinearModulesObject = (
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


FormedModulesHomCategory = RModuleHomCategory
FormedModulesEndCategory = RModuleEndCategory
FormedModulesAutCategory = RModuleAutCategory
FormedModulesHom = RModuleHomCategory.ParentMethods
FormedModulesEnd = RModuleEndCategory.ParentMethods
FormedModulesAut = RModuleAutCategory.ParentMethods
FormedModulesEndomorphism = RModuleEndCategory.ElementMethods
FormedModulesAutomorphism = RModuleAutCategory.ElementMethods

BilinearModulesHomCategory = RModuleHomCategory
BilinearModulesEndCategory = RModuleEndCategory
BilinearModulesAutCategory = RModuleAutCategory
BilinearModulesHom = RModuleHomCategory.ParentMethods
BilinearModulesEnd = RModuleEndCategory.ParentMethods
BilinearModulesAut = RModuleAutCategory.ParentMethods
BilinearModulesEndomorphism = RModuleEndCategory.ElementMethods
BilinearModulesAutomorphism = RModuleAutCategory.ElementMethods

QuadraticModulesHomCategory = RModuleHomCategory
QuadraticModulesEndCategory = RModuleEndCategory
QuadraticModulesAutCategory = RModuleAutCategory
QuadraticModulesHom = RModuleHomCategory.ParentMethods
QuadraticModulesEnd = RModuleEndCategory.ParentMethods
QuadraticModulesAut = RModuleAutCategory.ParentMethods
QuadraticModulesEndomorphism = RModuleEndCategory.ElementMethods
QuadraticModulesAutomorphism = RModuleAutCategory.ElementMethods

TorsionQuadraticModulesHomCategory = RModuleHomCategory
TorsionQuadraticModulesEndCategory = RModuleEndCategory
TorsionQuadraticModulesAutCategory = RModuleAutCategory
TorsionQuadraticModulesHom = RModuleHomCategory.ParentMethods
TorsionQuadraticModulesEnd = RModuleEndCategory.ParentMethods
TorsionQuadraticModulesAut = RModuleAutCategory.ParentMethods
TorsionQuadraticModulesEndomorphism = RModuleEndCategory.ElementMethods
TorsionQuadraticModulesAutomorphism = RModuleAutCategory.ElementMethods

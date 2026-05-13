r"""Generic hom, end, and aut category specs.

This package is a three-surface category root rather than a single category
class.  The initializer is the readable public index and type-package owner;
the root class definitions deliberately remain split by mathematical surface:

    homsets.py   -- ``HomCategory`` and ``HomCategoryOf``
    endsets.py   -- ``EndCategory`` and ``EndCategoryOf``
    autsets.py   -- ``AutCategory`` and ``AutCategoryOf``

That split follows the hom/end/aut ownership rule: endomorphism and
automorphism facts are not folded into the hom-category file, and the generic
aut construction remains in this subtree rather than being reimplemented by
individual category families.
"""

from __future__ import annotations

from .autsets import (
    AutCategory,
)
from .autsets import (
    AutCategoryConstruction as AutCategoryConstruction,
)
from .autsets import (
    AutCategoryOf as AutCategoryOf,
)
from .autsets import (
    UniversalAutElementMethods as UniversalAutElementMethods,
)
from .autsets import (
    UniversalAutObjectMethods as UniversalAutObjectMethods,
)
from .endsets import (
    EndCategory,
)
from .endsets import (
    EndCategoryConstruction as EndCategoryConstruction,
)
from .endsets import (
    EndCategoryOf as EndCategoryOf,
)
from .endsets import (
    UniversalEndElementMethods as UniversalEndElementMethods,
)
from .endsets import (
    UniversalEndObjectMethods as UniversalEndObjectMethods,
)
from .homsets import (
    HomCategory,
)
from .homsets import (
    HomCategoryConstruction as HomCategoryConstruction,
)
from .homsets import (
    HomCategoryOf as HomCategoryOf,
)
from .homsets import (
    UniversalHomElementMethods as UniversalHomElementMethods,
)
from .homsets import (
    UniversalHomObjectMethods as UniversalHomObjectMethods,
)

type GenericEndCategory = EndCategoryOf
type GenericAutCategory = AutCategoryOf

type HomCategoriesCategory = HomCategory
type HomCategoriesObject = HomCategory.ParentMethods
type HomCategoriesElement = HomCategory.ElementMethods
type HomCategoriesMorphism = HomCategory.MorphismMethods

type EndCategoriesCategory = EndCategory
type EndCategoriesObject = EndCategory.ParentMethods
type EndCategoriesElement = EndCategory.ElementMethods
type EndCategoriesMorphism = EndCategory.MorphismMethods

type AutCategoriesCategory = AutCategory
type AutCategoriesObject = AutCategory.ParentMethods
type AutCategoriesElement = AutCategory.ElementMethods
type AutCategoriesMorphism = AutCategory.MorphismMethods

r"""Generic hom, end, and aut category specs."""

from __future__ import annotations

from .autsets import AutCategory, AutCategoryConstruction, AutCategoryOf, UniversalAutElementMethods, UniversalAutObjectMethods
from .endsets import EndCategory, EndCategoryConstruction, EndCategoryOf, UniversalEndElementMethods, UniversalEndObjectMethods
from .homsets import HomCategory, HomCategoryConstruction, HomCategoryOf, UniversalHomElementMethods, UniversalHomObjectMethods

GenericEndCategory = EndCategoryOf
GenericAutCategory = AutCategoryOf

HomCategoriesCategory = HomCategory
HomCategoriesObject = HomCategory.ParentMethods
HomCategoriesElement = HomCategory.ElementMethods
HomCategoriesMorphism = HomCategory.MorphismMethods

EndCategoriesCategory = EndCategory
EndCategoriesObject = EndCategory.ParentMethods
EndCategoriesElement = EndCategory.ElementMethods
EndCategoriesMorphism = EndCategory.MorphismMethods

AutCategoriesCategory = AutCategory
AutCategoriesObject = AutCategory.ParentMethods
AutCategoriesElement = AutCategory.ElementMethods
AutCategoriesMorphism = AutCategory.MorphismMethods

r"""Generic hom, end, and aut category specs."""

from __future__ import annotations

from .autsets import AutCategory, AutCategoryConstruction, AutCategoryOf, UniversalAutElementMethods, UniversalAutObjectMethods
from .endsets import EndCategory, EndCategoryConstruction, EndCategoryOf, UniversalEndElementMethods, UniversalEndObjectMethods
from .homsets import HomCategory, HomCategoryConstruction, HomCategoryOf, UniversalHomElementMethods, UniversalHomObjectMethods

GenericEndCategory = EndCategoryOf
GenericAutCategory = AutCategoryOf

r"""Generic homset, endset, and autset category specs."""

from __future__ import annotations

from .autsets import Autsets, AutsetsCategory, AutsetsOf, UniversalAutsetElementMethods, UniversalAutsetObjectMethods
from .endsets import Endsets, EndsetsCategory, EndsetsOf, UniversalEndsetElementMethods, UniversalEndsetObjectMethods
from .homsets import Homsets, HomsetsCategory, HomsetsOf, UniversalHomsetElementMethods, UniversalHomsetObjectMethods

GenericEndsets = EndsetsOf
GenericAutsets = AutsetsOf


__all__ = [
    "Autsets",
    "AutsetsCategory",
    "Endsets",
    "EndsetsCategory",
    "Homsets",
    "HomsetsCategory",
    "UniversalAutsetElementMethods",
    "UniversalAutsetObjectMethods",
    "UniversalEndsetElementMethods",
    "UniversalEndsetObjectMethods",
    "UniversalHomsetElementMethods",
    "UniversalHomsetObjectMethods",
]

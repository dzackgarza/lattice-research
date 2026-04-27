r"""Generic homset, endset, and autset category specs."""

from __future__ import annotations

from .autsets import Autsets, AutsetsCategory, AutsetsOf
from .endsets import Endsets, EndsetsCategory, EndsetsOf
from .homsets import Homsets, HomsetsCategory, HomsetsOf

GenericEndsets = EndsetsOf
GenericAutsets = AutsetsOf


__all__ = [
    "Autsets",
    "AutsetsCategory",
    "Endsets",
    "EndsetsCategory",
    "Homsets",
    "HomsetsCategory",
]

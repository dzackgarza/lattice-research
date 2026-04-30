r"""Lattice category surface."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from .chain import (
    LatticesAut,
    LatticesAutCategory,
    LatticesAutomorphism,
    LatticesCategory,
    LatticesElement,
    LatticesEnd,
    LatticesEndCategory,
    LatticesEndomorphism,
    LatticesHom,
    LatticesHomCategory,
    LatticesMorphism,
    LatticesObject,
    lattice_category,
)

if TYPE_CHECKING:
    from ..types import Ring
    from .chain import _Lattices


@final
def Lattices(base_ring: Ring) -> _Lattices:
    r"""Return the named lattice axiom category over ``base_ring``."""
    return lattice_category(base_ring)

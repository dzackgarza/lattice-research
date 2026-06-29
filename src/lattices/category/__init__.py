r"""Isolated singular lattice category subtree."""

from __future__ import annotations

from .category import Lattice, LatticeCategory
from .elements import LatticeElementMethods, LatticeParentMethods
from .homsets import (
    LatticeAutCategory,
    LatticeAutomorphismMethods,
    LatticeEndCategory,
    LatticeEndomorphismMethods,
    LatticeHomCategory,
    LatticeHomParentMethods,
    LatticeMorphismMethods,
)

type LatticeObject = LatticeParentMethods
type LatticeElement = LatticeElementMethods
type LatticeMorphism = LatticeMorphismMethods
type LatticeHom = LatticeHomParentMethods
type LatticeEndomorphism = LatticeEndomorphismMethods
type LatticeAutomorphism = LatticeAutomorphismMethods

"""Canonical public lattice export surface.

This module is the public semantic entry point for the lattice redesign.
It re-exports the split implementation hierarchy without reintroducing a
monolithic implementation file.
"""

from src.lattices.categories import BilinearModules
from src.lattices.core.abstract import BilinearModule, QuadraticModule, TorsionBilinearModules
from src.lattices.core.discriminant import DiscriminantForm, DiscriminantGroup, DiscriminantGroupElement
from src.lattices.core.elements import (
    DualLatticeElement,
    FreeBilinearModuleElement,
    LatticeElement,
    RationalLatticeElement,
)
from src.lattices.core.free import FreeBilinearModule
from src.lattices.core.integral import Lattice
from src.lattices.core.rational import DualLattice, RationalLattice
from src.lattices.core.torsion import TorsionBilinearModule
from src.lattices.groups import (
    DiscriminantOrthogonalGroup,
    DiscriminantOrthogonalSubgroup,
    LatticeOrthogonalGroup,
    LatticeOrthogonalSubgroup,
)
from src.lattices.morphisms import (
    BilinearModuleHomSpace,
    BilinearModuleMorphism,
    DiscriminantGroupHomSpace,
    DiscriminantGroupMorphism,
    LatticeHomSpace,
    LatticeMorphism,
    RationalLatticeHomSpace,
    RationalLatticeMorphism,
)

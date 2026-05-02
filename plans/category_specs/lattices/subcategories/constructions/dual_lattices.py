r"""Compatibility route for the old dual-lattice construction name."""

from __future__ import annotations

from .dual_objects import _DualObjects


_DualLattices = _DualObjects
DualLatticesCategory = _DualObjects
DualLatticesObject = _DualObjects.ParentMethods
DualLatticesElement = _DualObjects.ElementMethods
DualLatticesMorphism = _DualObjects.MorphismMethods

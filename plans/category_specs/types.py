"""Centralized type aliases for the module hierarchy.

Only aliases backed by files that exist in this tree are exposed.  The
``ModulesWithForms`` / ``TwistedForms`` aliases from earlier drafts are
dropped until those spec files land.
"""


from sage.rings.infinity import InfinityElement
from sage.rings.integer import Integer

from .rings import ModuleBaseIdeals, ModuleBaseRings
from .sage_modules import Modules

# Generic / Support
Ring = ModuleBaseRings.ParentMethods
RingElement = ModuleBaseRings.ElementMethods
RingMorphism = ModuleBaseRings.MorphismMethods

LocalRing = ModuleBaseRings.Local.ParentMethods
CompleteRing = ModuleBaseRings.Complete.ParentMethods

Cardinality = Integer | InfinityElement

# RMod = Modules(R)
RMod = Modules
RModule = Modules.ParentMethods
RModuleElement = Modules.ElementMethods
FreeModule = Modules.Free.ParentMethods
TorsionModule = Modules.Torsion.ParentMethods
ProjectiveModule = Modules.Projective.ParentMethods
SubModule = Modules.Subobjects.ParentMethods
TensorProductRModule = Modules.TensorProducts.ParentMethods

Ideal = ModuleBaseIdeals.ParentMethods

RModHomset = Modules.Homsets.ParentMethods
RModHomsetElement = Modules.Homsets.ElementMethods
RModEndset = Modules.Homsets.Endset.ParentMethods
RModEndsetElement = Modules.Homsets.Endset.ElementMethods
RModAutset = Modules.Homsets.Endset.Autset.ParentMethods
RModAutsetElement = Modules.Homsets.Endset.Autset.ElementMethods
DualModule = Modules.DualObjects.ParentMethods
RModDualElement = Modules.DualObjects.ElementMethods

"""Centralized type aliases for the module and module-with-forms hierarchies."""


from sage.rings.infinity import InfinityElement
from sage.rings.integer import Integer

from .modules import Modules
from .modules_with_forms import ModulesWithForms
from .rings import ModuleBaseRings
from .twisted_forms import TwistedForms

# Generic / Support
Ring = ModuleBaseRings.ParentMethods
RingElement = ModuleBaseRings.ElementMethods
RingMorphism = ModuleBaseRings.MorphismMethods

# Twisted Forms
TwistedFormSpace = TwistedForms.ParentMethods
TwistedForm = TwistedForms.ElementMethods
BilinearFormSpace = TwistedForms.Bilinear.ParentMethods
BilinearForm = TwistedForms.Bilinear.ElementMethods
QuadraticFormSpace = TwistedForms.Quadratic.ParentMethods
QuadraticForm = TwistedForms.Quadratic.ElementMethods

Cardinality = Integer | InfinityElement

# RMod = Modules(R)
RMod = Modules
RModule = Modules.ParentMethods
RModuleElement = Modules.ElementMethods
SubModule = Modules.Subobjects.ParentMethods
TensorProductRModule = Modules.TensorProducts.ParentMethods

from .modules import Ideals
Ideal = Ideals.ParentMethods

RModHomset = Modules.Homsets.ParentMethods
RModHomsetElement = Modules.Homsets.ElementMethods
RModEndset = Modules.Homsets.Endset.ParentMethods
RModEndsetElement = Modules.Homsets.Endset.ElementMethods
RModAutset = Modules.Homsets.Endset.Autset.ParentMethods
RModAutsetElement = Modules.Homsets.Endset.Autset.ElementMethods
DualModule = Modules.DualObjects.ParentMethods
DualModuleElement = Modules.DualObjects.ElementMethods

# RModWithForm = ModulesWithForms(R)
RModWithForm = ModulesWithForms
RModuleWithForm = ModulesWithForms.ParentMethods
RModuleWithFormElement = ModulesWithForms.ElementMethods
RModWithFormHomset = ModulesWithForms.Homsets.ParentMethods
RModWithFormHomsetElement = ModulesWithForms.Homsets.ElementMethods
RModWithFormEndset = ModulesWithForms.Homsets.Endset.ParentMethods
RModWithFormEndsetElement = ModulesWithForms.Homsets.Endset.ElementMethods
RModWithFormAutset = ModulesWithForms.Homsets.Endset.Autset.ParentMethods
RModWithFormAutsetElement = ModulesWithForms.Homsets.Endset.Autset.ElementMethods
DualModuleWithForm = ModulesWithForms.DualObjects.ParentMethods
DualModuleWithFormElement = ModulesWithForms.DualObjects.ElementMethods

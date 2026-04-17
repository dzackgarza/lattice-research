"""Centralized type aliases for the module and module-with-forms hierarchies."""

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from sage.rings.integer import Integer
    from sage.rings.infinity import InfinityElement
    
    from .modules import Modules
    from .modules_with_forms import ModulesWithForms
    from .rings import ModuleBaseRings
    from .bilinear_form import BilinearForms
    
    # Generic / Support
    Ring = ModuleBaseRings.ParentMethods
    RingElement = ModuleBaseRings.ElementMethods
    BilinearForm = BilinearForms.ParentMethods
    Cardinality = Union[Integer, InfinityElement]

    # Optional: we don't have QuadraticForms defined yet in a separate module, 
    # but based on the plan we alias it. It might be defined in modules_with_forms
    from .modules_with_forms import QuadraticForm
    
    # RMod = Modules(R)
    RMod = Modules
    RModule = Modules.ParentMethods
    RModuleElement = Modules.ElementMethods
    SubModule = Modules.Subobjects.ParentMethods
    
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

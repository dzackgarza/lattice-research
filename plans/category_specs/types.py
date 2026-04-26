"""Centralized type aliases for the module hierarchy.

Only aliases backed by files that exist in this tree are exposed.  The
``ModulesWithForms`` / ``TwistedForms`` aliases from earlier drafts are
dropped until those spec files land.
"""

from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.groups.group import Group as SageGroup
from sage.monoids.monoid import Monoid_class
from sage.rings.complex_interval import ComplexIntervalFieldElement
from sage.rings.infinity import InfinityElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial as SagePolynomial
from sage.rings.real_mpfi import RealIntervalFieldElement
from sage.rings.valuation.valuation import DiscretePseudoValuation

from .rings import Rings, _RingIdeals
from .modules import Modules

# Generic / Support
Ring = Rings.ParentMethods
Field = Rings.Fields.ParentMethods
RingElement = Rings.ElementMethods
RingMorphism = Rings.MorphismMethods
RingHomset = Rings.Homsets.ParentMethods
RingHomsetElement = Rings.MorphismMethods
RingEndset = Rings.Homsets.Endset.ParentMethods
RingEndsetElement = Rings.Homsets.Endset.ElementMethods
RingAutset = Rings.Homsets.Endset.Autset.ParentMethods
RingAutsetElement = Rings.Homsets.Endset.Autset.ElementMethods
Group = SageGroup
AbelianGroup = AbelianGroup_class
Monoid = Monoid_class
Polynomial = SagePolynomial
RealInterval = RealIntervalFieldElement
ComplexInterval = ComplexIntervalFieldElement
Interval = RealInterval | ComplexInterval
Valuation = DiscretePseudoValuation

LocalRing = Rings.Local.ParentMethods
CompleteRing = Rings.Complete.ParentMethods

Cardinality = Integer | InfinityElement

RMod = Modules
RModule = Modules.ParentMethods
RModuleElement = Modules.ElementMethods
FreeModule = Modules.Free.ParentMethods
TorsionModule = Modules.Torsion.ParentMethods
ProjectiveModule = Modules.Projective.ParentMethods
SubModule = Modules.Subobjects.ParentMethods
TensorProductRModule = Modules.TensorProducts.ParentMethods

Ideal = _RingIdeals.ParentMethods
PrimeIdeal = Ideal
MaximalIdeal = PrimeIdeal

RModHomset = Modules.Homsets.ParentMethods
RModHomsetElement = Modules.Homsets.ElementMethods
RModEndset = Modules.Homsets.Endset.ParentMethods
RModEndsetElement = Modules.Homsets.Endset.ElementMethods
RModAutset = Modules.Homsets.Endset.Autset.ParentMethods
RModAutsetElement = Modules.Homsets.Endset.Autset.ElementMethods
DualModule = Modules.DualObjects.ParentMethods
RModDualElement = Modules.DualObjects.ElementMethods

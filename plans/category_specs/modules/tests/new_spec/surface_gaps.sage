# Normative spec checks for method-surface gaps.
#
# These assertions intentionally record where existing Sage-backed objects do
# not satisfy the ABC surface declared in plans/category_specs/modules/named.py.

import logging
import sys
sys.path.insert(0, '/home/dzack/research')

from pytest import raises
from plans.category_specs.modules import Modules
from plans.category_specs.rings import Rings

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

ZZ = Rings().Constructors().ZZ()
MZZ = Modules(ZZ).Constructors()

# ---------------------------------------------------------------------------
# FGP quotient modules: required surface in _FinitelyGeneratedPIDQuotientModules
# ---------------------------------------------------------------------------

V = MZZ.span([[1, 2, 5], [2, 2, 2]])
W = V.span([V.gen(0)])
Q = MZZ.quotient_of_free_modules(V, W)

logger.warning(
    "Spec mismatch: _FinitelyGeneratedPIDQuotientModules requires free_part(), "
    "but the current Sage FGP quotient object still raises NotImplementedError."
)
with raises(NotImplementedError):
    Q.free_part()

logger.warning(
    "Spec mismatch: _FinitelyGeneratedPIDQuotientModules requires torsion_part(), "
    "but the current Sage FGP quotient object still raises NotImplementedError."
)
with raises(NotImplementedError):
    Q.torsion_part()

logger.warning(
    "Spec mismatch: _FinitelyGeneratedPIDQuotientModules requires element_from_vector(...), "
    "but the current Sage FGP quotient object still raises NotImplementedError."
)
with raises(NotImplementedError):
    Q.element_from_vector([0])

logger.warning(
    "Spec mismatch: _FinitelyGeneratedPIDQuotientModules types optimized() as an R-module object, "
    "but the current Sage FGP quotient object returns a plain tuple."
)
with raises(AssertionError):
    assert Q.optimized() in Modules(ZZ)

# ---------------------------------------------------------------------------
# Ring objects as modules: required surface in _RingObjectsAsModules
# ---------------------------------------------------------------------------

S = MZZ.polynomial_ring_as_module('x')

logger.warning(
    "Spec mismatch: _RingObjectsAsModules requires module_generators(), "
    "but the wrapped Sage polynomial ring still raises NotImplementedError."
)
with raises(NotImplementedError):
    S.module_generators()

# Normative spec checks for category refinement gaps.
#
# These assertions intentionally encode current failures of the wrapped Sage
# implementations against the local module-category spec in
# plans/category_specs/modules/named.py.

import logging
import sys
sys.path.insert(0, '/home/dzack/research')

from pytest import raises
from sage.all import QQ
from plans.category_specs.modules import Modules

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

MQQ = Modules(QQ).NamedModules()

# ---------------------------------------------------------------------------
# QuotientModuleWithBasis should refine to quotient / generating-set surfaces
# ---------------------------------------------------------------------------

X = MQQ.CombinatorialFreeModule(range(3), prefix='x')
x = X.basis()
Y = MQQ.quotient_module(
    X,
    X.submodule([x[0] - x[1], x[1] - x[2]], already_echelonized=True),
    already_echelonized=True,
)

logger.warning(
    "Spec mismatch: modules-with-basis quotients should lie in Modules(QQ).Quotients(), "
    "but the wrapped Sage quotient currently does not refine into that subcategory."
)
with raises(AssertionError):
    assert Y in Modules(QQ).Quotients()

logger.warning(
    "Spec mismatch: quotient refinement should compose under axiom chaining, so a modules-with-basis "
    "quotient should lie in Modules(QQ).Quotients().WithOrderedGeneratingSet(), but the current "
    "wrapped Sage quotient does not."
)
with raises(AssertionError):
    assert Y in Modules(QQ).Quotients().WithOrderedGeneratingSet()

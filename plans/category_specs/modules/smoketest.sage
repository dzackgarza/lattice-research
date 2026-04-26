from pathlib import Path
import logging
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.utils import refine_category
from category_specs.modules import Modules


logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
logger = logging.getLogger("category_specs.modules.smoketest")

failures = []


def expect_in(obj, category):
    assert obj in category, f"{type(obj).__name__} not in {category}"
    return obj


def smoke_case(label, build):
    try:
        build()
    except Exception as exc:
        message = (
            f"{label}: failed to instantiate/refine the target spec surface "
            f"({type(exc).__name__}: {exc})"
        )
        failures.append(message)
        logger.warning(message)


R6 = IntegerModRing(6)
NM6 = Modules(R6).NamedModules()
smoke_case(
    "modules.FreeModulesWithStandardBasis via Modules(Zmod(6)).NamedModules().FreeModule(2)",
    lambda: expect_in(NM6.FreeModule(2), NM6.FreeModulesWithStandardBasis()),
)

PZ = PolynomialRing(ZZ, "x")
NMPZ = Modules(PZ).NamedModules()
smoke_case(
    "modules.FreeModulesOverIntegralDomains via Modules(ZZ['x']).NamedModules().FreeModule(2)",
    lambda: expect_in(NMPZ.FreeModule(2), NMPZ.FreeModulesOverIntegralDomains()),
)

NMZZ = Modules(ZZ).NamedModules()
smoke_case(
    "modules.FreeModulesOverPIDs via Modules(ZZ).NamedModules().FreeModule(2)",
    lambda: expect_in(NMZZ.FreeModule(2), NMZZ.FreeModulesOverPIDs()),
)

NMQQ = Modules(QQ).NamedModules()
smoke_case(
    "modules.VectorSpaces via Modules(QQ).NamedModules().VectorSpace(2)",
    lambda: expect_in(NMQQ.VectorSpace(2), NMQQ.VectorSpaces()),
)
smoke_case(
    "modules.RealDoubleVectorSpaces via refine_category(FreeModule(RDF, 2), RealDoubleVectorSpaces())",
    lambda: expect_in(
        refine_category(FreeModule(RDF, 2), Modules(RDF).NamedModules().RealDoubleVectorSpaces()),
        Modules(RDF).NamedModules().RealDoubleVectorSpaces(),
    ),
)
smoke_case(
    "modules.ComplexDoubleVectorSpaces via refine_category(FreeModule(CDF, 2), ComplexDoubleVectorSpaces())",
    lambda: expect_in(
        refine_category(FreeModule(CDF, 2), Modules(CDF).NamedModules().ComplexDoubleVectorSpaces()),
        Modules(CDF).NamedModules().ComplexDoubleVectorSpaces(),
    ),
)

V = VectorSpace(QQ, 3)
W = V.subspace([V.gen(0), V.gen(1)])
Wb = V.subspace_with_basis([V.gen(0), V.gen(1)])
Q = V.quotient_module(W)

smoke_case(
    "modules.VectorSubspaces via refine_category(V.subspace(...), VectorSubspaces())",
    lambda: expect_in(refine_category(W, NMQQ.VectorSubspaces()), NMQQ.VectorSubspaces()),
)
smoke_case(
    "modules.VectorSubspacesWithOrderedGeneratingSet via refine_category(V.subspace_with_basis(...), VectorSubspacesWithOrderedGeneratingSet())",
    lambda: expect_in(
        refine_category(Wb, NMQQ.VectorSubspacesWithOrderedGeneratingSet()),
        NMQQ.VectorSubspacesWithOrderedGeneratingSet(),
    ),
)
smoke_case(
    "modules.VectorSpaceQuotients via refine_category(V.quotient_module(W), VectorSpaceQuotients())",
    lambda: expect_in(refine_category(Q, NMQQ.VectorSpaceQuotients()), NMQQ.VectorSpaceQuotients()),
)

smoke_case(
    "modules.FreeQuadraticModules via Modules(ZZ).NamedModules().FreeQuadraticModule(2, [[2, 1], [1, 2]])",
    lambda: expect_in(
        NMZZ.FreeQuadraticModule(2, matrix(ZZ, [[2, 1], [1, 2]])),
        NMZZ.FreeQuadraticModules(),
    ),
)
smoke_case(
    "modules.CombinatorialFreeModules via Modules(QQ).NamedModules().CombinatorialFreeModule(['a', 'b'])",
    lambda: expect_in(NMQQ.CombinatorialFreeModule(["a", "b"]), NMQQ.CombinatorialFreeModules()),
)
smoke_case(
    "modules.FiniteRankFreeModules via Modules(QQ).NamedModules().FiniteRankFreeModule(2)",
    lambda: expect_in(NMQQ.FiniteRankFreeModule(2), NMQQ.FiniteRankFreeModules()),
)

M = FreeModule(ZZ, 3)
S = M.submodule([2 * M.gen(0), 3 * M.gen(1)])
Sb = M.submodule_with_basis([2 * M.gen(0), 3 * M.gen(1)])
Qfree = M.quotient_module(S)

smoke_case(
    "modules.FreeModuleSubmodules via refine_category(M.submodule(...), FreeModuleSubmodules())",
    lambda: expect_in(refine_category(S, NMZZ.FreeModuleSubmodules()), NMZZ.FreeModuleSubmodules()),
)
smoke_case(
    "modules.FreeModuleSubmodulesWithOrderedGeneratingSet via refine_category(M.submodule_with_basis(...), FreeModuleSubmodulesWithOrderedGeneratingSet())",
    lambda: expect_in(
        refine_category(Sb, NMZZ.FreeModuleSubmodulesWithOrderedGeneratingSet()),
        NMZZ.FreeModuleSubmodulesWithOrderedGeneratingSet(),
    ),
)
smoke_case(
    "modules.FreeModuleQuotients via refine_category(M.quotient_module(S), FreeModuleQuotients())",
    lambda: expect_in(refine_category(Qfree, NMZZ.FreeModuleQuotients()), NMZZ.FreeModuleQuotients()),
)

C = CombinatorialFreeModule(QQ, ["a", "b"])
a = C.monomial("a")
b = C.monomial("b")
CS = C.submodule([a + b])
CQ = C.quotient_module(CS)

smoke_case(
    "modules.SubmodulesWithOrderedGeneratingSet via refine_category(C.submodule([a + b]), SubmodulesWithOrderedGeneratingSet())",
    lambda: expect_in(
        refine_category(CS, NMQQ.SubmodulesWithOrderedGeneratingSet()),
        NMQQ.SubmodulesWithOrderedGeneratingSet(),
    ),
)
smoke_case(
    "modules.QuotientModulesWithOrderedGeneratingSet via refine_category(C.quotient_module(CS), QuotientModulesWithOrderedGeneratingSet())",
    lambda: expect_in(
        refine_category(CQ, NMQQ.QuotientModulesWithOrderedGeneratingSet()),
        NMQQ.QuotientModulesWithOrderedGeneratingSet(),
    ),
)

smoke_case(
    "modules.RepresentationModules via refine_category(SymmetricGroup(3).regular_representation(QQ), RepresentationModules())",
    lambda: expect_in(
        refine_category(SymmetricGroup(3).regular_representation(QQ), NMQQ.RepresentationModules()),
        NMQQ.RepresentationModules(),
    ),
)

Wfg = M.submodule([2 * M.gen(0), 4 * M.gen(1), M.gen(2)])
Mfg = M / Wfg

smoke_case(
    "modules.FinitelyGeneratedPIDQuotientModules via refine_category(M / W, FinitelyGeneratedPIDQuotientModules())",
    lambda: expect_in(
        refine_category(Mfg, NMZZ.FinitelyGeneratedPIDQuotientModules()),
        NMZZ.FinitelyGeneratedPIDQuotientModules(),
    ),
)

E = ExteriorAlgebra(QQ, names=("x", "y"))
xE, yE = E.gens()
NME = Modules(E).NamedModules()

smoke_case(
    "modules.FreeGradedModules via Modules(ExteriorAlgebra(QQ)).NamedModules().FreeGradedModule(E, (-1, 3))",
    lambda: expect_in(NME.FreeGradedModule(E, (-1, 3)), NME.FreeGradedModules()),
)
smoke_case(
    "modules.FinitelyPresentedGradedModules via Modules(ExteriorAlgebra(QQ)).NamedModules().FPModule(E, [0, 1], [[x, 1]])",
    lambda: expect_in(
        NME.FPModule(E, [0, 1], [[xE, E.one()]]),
        NME.FinitelyPresentedGradedModules(),
    ),
)

K = GF(5**3, "z")
z = K.gen()
Sore = OrePolynomialRing(K, K.frobenius_endomorphism(), names="X")
X = Sore.gen()
NMK = Modules(K).NamedModules()

smoke_case(
    "modules.OreModules via Modules(GF(5^3)).NamedModules().OreQuotientModule(S, X^2 + z)",
    lambda: expect_in(NMK.OreQuotientModule(Sore, X**2 + z), NMK.OreModules()),
)
smoke_case(
    "modules.IntegerLattices via Modules(ZZ).NamedModules().IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]])",
    lambda: expect_in(
        NMZZ.IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]]),
        NMZZ.IntegerLattices(),
    ),
)
smoke_case(
    "modules.TorsionQuadraticModules via Modules(ZZ).NamedModules().TorsionQuadraticForm([[1, 1/2], [1/2, 1]])",
    lambda: expect_in(
        NMZZ.TorsionQuadraticForm(matrix(QQ, [[1, QQ(1) / 2], [QQ(1) / 2, 1]])),
        NMZZ.TorsionQuadraticModules(),
    ),
)
smoke_case(
    "modules.RingObjectsAsModules via Modules(ZZ).NamedModules().polynomial_ring_as_module('t')",
    lambda: expect_in(NMZZ.polynomial_ring_as_module("t"), NMZZ.RingObjectsAsModules()),
)

assert not failures, "\n".join(failures)

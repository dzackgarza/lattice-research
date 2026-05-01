from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.modules import Modules
from category_specs.sets import Sets
from category_specs.utils import assert_smoke_statements, refine_category


R6 = IntegerModRing(6)
NM6 = Modules(R6).Constructors()

PZ = PolynomialRing(ZZ, "x")
NMPZ = Modules(PZ).Constructors()

NMZZ = Modules(ZZ).Constructors()
NMQQ = Modules(QQ).Constructors()

V = VectorSpace(QQ, 3)
W = V.subspace([V.gen(0), V.gen(1)])
Wb = V.subspace_with_basis([V.gen(0), V.gen(1)])
Q = V.quotient_module(W)

M = FreeModule(ZZ, 3)
S = M.submodule([2 * M.gen(0), 3 * M.gen(1)])
Sb = M.submodule_with_basis([2 * M.gen(0), 3 * M.gen(1)])
Qfree = M.quotient_module(S)

C = CombinatorialFreeModule(QQ, ["a", "b"])
a = C.monomial("a")
b = C.monomial("b")
CS = C.submodule([a + b])
CQ = C.quotient_module(CS)

Wfg = M.submodule([2 * M.gen(0), 4 * M.gen(1), M.gen(2)])
Mfg = M / Wfg

E = ExteriorAlgebra(QQ, names=("x", "y"))
xE, yE = E.gens()
NME = Modules(E).Constructors()

K = GF(5**3, "z")
z = K.gen()
Sore = OrePolynomialRing(K, K.frobenius_endomorphism(), names="X")
X = Sore.gen()
NMK = Modules(K).Constructors()

SMOKE_STATEMENTS = (
    (
        "Modules(Zmod(6)).Constructors().FreeModule(2) has standard basis category",
        lambda _: NM6.FreeModule(2) in NM6.FreeModulesWithStandardBasis(),
    ),
    ("Modules(Zmod(6)).Constructors().FreeModule(2) has base ring Zmod(6)", lambda _: NM6.FreeModule(2).base_ring() is R6),
    ("Modules(Zmod(6)).Constructors().FreeModule(2) has rank 2", lambda _: NM6.FreeModule(2).rank() == 2),
    (
        "Modules(ZZ['x']).Constructors().FreeModule(2) is free over an integral domain",
        lambda _: NMPZ.FreeModule(2) in NMPZ.FreeModulesOverIntegralDomains(),
    ),
    ("Modules(ZZ['x']).Constructors().FreeModule(2) has base ring ZZ['x']", lambda _: NMPZ.FreeModule(2).base_ring() is PZ),
    ("Modules(ZZ['x']).Constructors().FreeModule(2) has rank 2", lambda _: NMPZ.FreeModule(2).rank() == 2),
    (
        "Modules(ZZ).Constructors().FreeModule(2) is free over a PID",
        lambda _: NMZZ.FreeModule(2) in NMZZ.FreeModulesOverPIDs(),
    ),
    ("Modules(ZZ).Constructors().FreeModule(2) has base ring ZZ", lambda _: NMZZ.FreeModule(2).base_ring() is ZZ),
    ("Modules(ZZ).Constructors().FreeModule(2) has rank 2", lambda _: NMZZ.FreeModule(2).rank() == 2),
    ("Modules(QQ).Constructors().VectorSpace(2) is a vector space", lambda _: NMQQ.VectorSpace(2) in NMQQ.VectorSpaces()),
    ("Modules(QQ).Constructors().VectorSpace(2) has base ring QQ", lambda _: NMQQ.VectorSpace(2).base_ring() is QQ),
    ("Modules(QQ).Constructors().VectorSpace(2) has dimension 2", lambda _: NMQQ.VectorSpace(2).dimension() == 2),
    (
        "refine_category(FreeModule(RDF, 2), RealDoubleVectorSpaces()) is a real double vector space",
        lambda _: refine_category(FreeModule(RDF, 2), Modules(RDF).Constructors().RealDoubleVectorSpaces())
        in Modules(RDF).Constructors().RealDoubleVectorSpaces(),
    ),
    (
        "refine_category(FreeModule(CDF, 2), ComplexDoubleVectorSpaces()) is a complex double vector space",
        lambda _: refine_category(FreeModule(CDF, 2), Modules(CDF).Constructors().ComplexDoubleVectorSpaces())
        in Modules(CDF).Constructors().ComplexDoubleVectorSpaces(),
    ),
    (
        "refine_category(V.subspace(...), VectorSubspaces()) is a vector subspace",
        lambda _: refine_category(W, NMQQ.VectorSubspaces()) in NMQQ.VectorSubspaces(),
    ),
    ("refined V.subspace(...) has ambient vector space V", lambda _: refine_category(W, NMQQ.VectorSubspaces()).ambient_vector_space() is V),
    (
        "refine_category(V.subspace_with_basis(...), VectorSubspacesWithOrderedGeneratingSet()) has ordered generators",
        lambda _: refine_category(Wb, NMQQ.VectorSubspacesWithOrderedGeneratingSet())
        in NMQQ.VectorSubspacesWithOrderedGeneratingSet(),
    ),
    (
        "refine_category(V.quotient_module(W), VectorSpaceQuotients()) is a vector-space quotient",
        lambda _: refine_category(Q, NMQQ.VectorSpaceQuotients()) in NMQQ.VectorSpaceQuotients(),
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(...) is a free quadratic module",
        lambda _: NMZZ.FreeQuadraticModule(2, matrix(ZZ, [[2, 1], [1, 2]])) in NMZZ.FreeQuadraticModules(),
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(...) has rank 2",
        lambda _: NMZZ.FreeQuadraticModule(2, matrix(ZZ, [[2, 1], [1, 2]])).rank() == 2,
    ),
    (
        "Modules(QQ).Constructors().CombinatorialFreeModule({a, b}) is free with ordered generators",
        lambda _: (
            NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])) in Modules(QQ).Free()
            and NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"]))
            in Modules(QQ).WithOrderedGeneratingSet()
        ),
    ),
    (
        "Modules(QQ).Constructors().CombinatorialFreeModule({a, b}) has two basis keys",
        lambda _: NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis().keys().cardinality()
        == 2,
    ),
    (
        "Modules(QQ).Constructors().FiniteRankFreeModule(2) is finite-rank free",
        lambda _: NMQQ.FiniteRankFreeModule(2) in NMQQ.FiniteRankFreeModules(),
    ),
    ("Modules(QQ).Constructors().FiniteRankFreeModule(2) has rank 2", lambda _: NMQQ.FiniteRankFreeModule(2).rank() == 2),
    (
        "refine_category(M.submodule(...), FreeModuleSubmodules()) is a free-module submodule",
        lambda _: refine_category(S, NMZZ.FreeModuleSubmodules()) in NMZZ.FreeModuleSubmodules(),
    ),
    ("refined M.submodule(...) has ambient module M", lambda _: refine_category(S, NMZZ.FreeModuleSubmodules()).ambient_module() is M),
    (
        "refine_category(M.submodule_with_basis(...), FreeModuleSubmodulesWithOrderedGeneratingSet()) has ordered generators",
        lambda _: refine_category(Sb, NMZZ.FreeModuleSubmodulesWithOrderedGeneratingSet())
        in NMZZ.FreeModuleSubmodulesWithOrderedGeneratingSet(),
    ),
    (
        "refine_category(M.quotient_module(S), FreeModuleQuotients()) is a free-module quotient",
        lambda _: refine_category(Qfree, NMZZ.FreeModuleQuotients()) in NMZZ.FreeModuleQuotients(),
    ),
    (
        "refine_category(C.submodule([a + b]), SubmodulesWithOrderedGeneratingSet()) has ordered generators",
        lambda _: refine_category(CS, NMQQ.SubmodulesWithOrderedGeneratingSet()) in NMQQ.SubmodulesWithOrderedGeneratingSet(),
    ),
    (
        "refine_category(C.quotient_module(CS), QuotientModulesWithOrderedGeneratingSet()) has ordered generators",
        lambda _: refine_category(CQ, NMQQ.QuotientModulesWithOrderedGeneratingSet())
        in NMQQ.QuotientModulesWithOrderedGeneratingSet(),
    ),
    (
        "refine_category(SymmetricGroup(3).regular_representation(QQ), RepresentationModules()) is a representation module",
        lambda _: refine_category(SymmetricGroup(3).regular_representation(QQ), NMQQ.RepresentationModules())
        in NMQQ.RepresentationModules(),
    ),
    (
        "refine_category(M / Wfg, FinitelyGeneratedPIDQuotientModules()) is finitely generated over a PID",
        lambda _: refine_category(Mfg, NMZZ.FinitelyGeneratedPIDQuotientModules())
        in NMZZ.FinitelyGeneratedPIDQuotientModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FreeGradedModule(E, (-1, 3)) is free graded",
        lambda _: NME.FreeGradedModule(E, (-1, 3)) in NME.FreeGradedModules(),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModule(...) is finitely presented graded",
        lambda _: NME.FPModule(E, [0, 1], [[xE, E.one()]]) in NME.FinitelyPresentedGradedModules(),
    ),
    (
        "Modules(GF(5^3)).Constructors().OreQuotientModule(S, X^2 + z) is an Ore module",
        lambda _: NMK.OreQuotientModule(Sore, X**2 + z) in NMK.OreModules(),
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(...) is an integer lattice",
        lambda _: NMZZ.IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]]) in NMZZ.IntegerLattices(),
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(...) has rank 3",
        lambda _: NMZZ.IntegerLattice([[1, 0, 3], [0, 2, 1], [0, 2, 7]]).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().TorsionQuadraticForm(...) is a torsion quadratic module",
        lambda _: NMZZ.TorsionQuadraticForm(matrix(QQ, [[1, QQ(1) / 2], [QQ(1) / 2, 1]]))
        in NMZZ.TorsionQuadraticModules(),
    ),
    (
        "Modules(ZZ).Constructors().polynomial_ring_as_module(name='t') is a ring object as a module",
        lambda _: NMZZ.polynomial_ring_as_module(name="t") in NMZZ.RingObjectsAsModules(),
    ),
    (
        "Modules(ZZ).Constructors().polynomial_ring_as_module(name='t') has base ring ZZ",
        lambda _: NMZZ.polynomial_ring_as_module(name="t").base_ring() is ZZ,
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)

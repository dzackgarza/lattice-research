r"""Mathematical-fact obligations for the module category subtree.

Each statement instantiates an object through the module DSL and asserts a real
mathematical value it must recover: a base ring, a rank, a dimension, a Gram matrix, a
basis cardinality, a recovered ambient object, an isomorphism witness, a triviality of a
cokernel, or a coefficient/monomial computation. A statement passes only when the backend
computes the value; it is red while the backend is incomplete. No statement asserts
category-graph structure (category membership `obj in C`, method ownership via
`abstract_method_has_name`, subcategory placement, axiom-owner identity, or type-package
aliases `X is Y`) — that is a property of the spec *source*, enforced by the validators in
`category_specs/validators/`. The dominant block of `obj in Cat()` membership assertions,
`abstract_method_has_name(...)` method-ownership checks, `Modules.X is _Y` class-identity
checks, the `_WithBasis._base_category_class_and_axiom == (...)` axiom-owner check, and the
predicate-witness method-existence check were removed here; migrating any structural
invariant they encoded into validator coverage is the separate "framework tests ->
validators" workstream (tracked, not silently dropped).

Citations (per the `What A Test Cites` contract): every kept obligation here is an
elementary computed fact about a constructed Sage object (rank, dimension, base ring,
Gram matrix, basis cardinality, recovered ambient, cokernel triviality, inverse-witness
roundtrip, term/coefficient values), so none carries a literature citation.
"""

from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.modules import Modules
from category_specs.modules.subcategories.constructions.quotients import _Quotients as ModuleQuotients
from category_specs.rings import Rings
from category_specs.sets import Sets
from category_specs.utils import assert_category_statements, refine_category
from sage.modules.fp_graded.free_module import FreeGradedModule


NR = Rings().Constructors()

R6 = NR.IntegerModRing(order=6)
NM6 = Modules(R6).Constructors()

PZ = NR.PolynomialRing(base_ring=ZZ, name="x")
NMPZ = Modules(PZ).Constructors()

NMZZ = Modules(ZZ).Constructors()
NMQQ = Modules(QQ).Constructors()
MZZCat = Modules(ZZ)
MQQCat = Modules(QQ)

V = NMQQ.VectorSpace(dimension=3)
W = V.subspace([V.gen(0), V.gen(1)])

M = NMZZ.FreeModule(rank=3)
S = M.submodule([2 * M.gen(0), 3 * M.gen(1)])

C = CombinatorialFreeModule(QQ, ["a", "b"])
a = C.monomial("a")
b = C.monomial("b")

E = ExteriorAlgebra(QQ, names=("x", "y"))
NME = Modules(E).Constructors()


def fp_module_from_identity_cokernel():
    F = FreeGradedModule(E, [0, 1])
    return NME.FPModule(defining_map=Hom(F, F).identity())


def integer_lattice_from_cyclotomic_order_element():
    K5 = NR.CyclotomicField(n=5, names="zeta")
    O5 = K5.ring_of_integers()
    return NMZZ.IntegerLattice(basis=O5(K5.gen()))


def rank_one_module_isomorphisms_are_inverse_witnesses():
    M1, from_M1, to_M1 = NM6.rank_one_module_with_ring_isomorphisms(basis=R6(5))
    x = R6(2)
    v = M1([x])
    return from_M1(to_M1(x)) == x and to_M1(from_M1(v)) == v


def rational_quotient_split_methods_have_one_dimensional_outputs():
    V = NMQQ.VectorSpace(dimension=3)
    W = V.subspace([V.gen(2)])
    Q = V.quotient_module(W)
    methods = ModuleQuotients.ParentMethods
    relation_matrix = matrix(QQ, [[1, 0]])
    quotient_by_submodule = methods.quotient_by_submodule(Q, Q.subspace([Q.gen(0)]))
    quotient_by_generators = methods.quotient_by_generators(Q, [Q.gen(0)])
    quotient_by_relation_matrix = methods.quotient_by_relation_matrix(Q, relation_matrix)
    quotient_by_relation_rows = methods.quotient_by_relation_rows(Q, [[1, 0]])
    assert quotient_by_submodule.dimension() == 1
    assert quotient_by_generators.dimension() == 1
    assert quotient_by_relation_matrix.dimension() == 1
    assert quotient_by_relation_rows.dimension() == 1
    return True


def refine_for_membership(parent, categories):
    return refine_category(parent, categories, test=False)


CATEGORY_STATEMENTS = (
    ("Modules(Zmod(6)).Constructors().FreeModule(rank=2) has base ring Zmod(6)", lambda _: NM6.FreeModule(rank=2).base_ring() is R6),
    ("Modules(Zmod(6)).Constructors().FreeModule(rank=2) has rank 2", lambda _: NM6.FreeModule(rank=2).rank() == 2),
    (
        "Modules(QQ).Constructors().FreeModule(basis_keys={a, b}) has two basis keys",
        lambda _: NMQQ.FreeModule(basis_keys=Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis().keys().cardinality()
        == 2,
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(rank=2, with_basis=None) has rank 2",
        lambda _: NM6.FreeModule(rank=2, with_basis=None).rank() == 2,
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(inner_product_rows=...) records the Gram matrix",
        lambda _: NM6.FreeModule(rank=2, inner_product_rows=[[1, 0], [0, 1]]).inner_product_matrix()
        == matrix(R6, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(Zmod(6)).Constructors().FreeModule(inner_product_entries=...) records the Gram matrix",
        lambda _: NM6.FreeModule(rank=2, inner_product_entries=[1, 0, 0, 1]).inner_product_matrix()
        == matrix(R6, [[1, 0], [0, 1]]),
    ),
    ("Modules(ZZ['x']).Constructors().FreeModule(rank=2) has base ring ZZ['x']", lambda _: NMPZ.FreeModule(rank=2).base_ring() is PZ),
    ("Modules(ZZ['x']).Constructors().FreeModule(rank=2) has rank 2", lambda _: NMPZ.FreeModule(rank=2).rank() == 2),
    ("Modules(ZZ).Constructors().FreeModule(rank=2) has base ring ZZ", lambda _: NMZZ.FreeModule(rank=2).base_ring() is ZZ),
    ("Modules(ZZ).Constructors().FreeModule(rank=2) has rank 2", lambda _: NMZZ.FreeModule(rank=2).rank() == 2),
    ("Modules(QQ).Constructors().VectorSpace(dimension=2) has base ring QQ", lambda _: NMQQ.VectorSpace(dimension=2).base_ring() is QQ),
    ("Modules(QQ).Constructors().VectorSpace(dimension=2) has dimension 2", lambda _: NMQQ.VectorSpace(dimension=2).dimension() == 2),
    (
        "Modules(QQ).Constructors().VectorSpace(basis_keys={a, b}) has two basis keys",
        lambda _: NMQQ.VectorSpace(basis_keys=Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis().keys().cardinality()
        == 2,
    ),
    (
        "Modules(QQ).Constructors().VectorSpace(dimension=2, with_basis=None) has dimension 2",
        lambda _: NMQQ.VectorSpace(dimension=2, with_basis=None).dimension() == 2,
    ),
    (
        "Modules(QQ).Constructors().VectorSpace(inner_product_rows=...) records the Gram matrix",
        lambda _: NMQQ.VectorSpace(dimension=2, inner_product_rows=[[1, 0], [0, 1]]).inner_product_matrix()
        == matrix(QQ, [[1, 0], [0, 1]]),
    ),
    (
        "Modules(QQ).Constructors().VectorSpace(inner_product_entries=...) records the Gram matrix",
        lambda _: NMQQ.VectorSpace(dimension=2, inner_product_entries=[1, 0, 0, 1]).inner_product_matrix()
        == matrix(QQ, [[1, 0], [0, 1]]),
    ),
    (
        # UNSURE: asserts that a refined subspace recovers its ambient vector space object,
        # a computed structural value of the construction (not category-graph placement).
        "refined V.subspace(...) has ambient vector space V",
        lambda _: refine_for_membership(W, MQQCat.Subobjects()).ambient_vector_space() is V,
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(...) has rank 2",
        lambda _: NMZZ.FreeQuadraticModule(rank=2, inner_product_matrix=matrix(ZZ, [[2, 1], [1, 2]])).rank() == 2,
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(inner_product_rows=...) records the form",
        lambda _: NMZZ.FreeQuadraticModule(rank=2, inner_product_rows=[[2, 1], [1, 2]]).inner_product_matrix()
        == matrix(ZZ, [[2, 1], [1, 2]]),
    ),
    (
        "Modules(ZZ).Constructors().FreeQuadraticModule(inner_product_entries=...) records the form",
        lambda _: NMZZ.FreeQuadraticModule(rank=2, inner_product_entries=[2, 1, 1, 2]).inner_product_matrix()
        == matrix(ZZ, [[2, 1], [1, 2]]),
    ),
    (
        "Modules(QQ).Constructors().CombinatorialFreeModule({a, b}) has two basis keys",
        lambda _: NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis().keys().cardinality()
        == 2,
    ),
    ("Modules(QQ).Constructors().FiniteRankFreeModule(2) has rank 2", lambda _: NMQQ.FiniteRankFreeModule(2).rank() == 2),
    (
        # UNSURE: asserts that a refined submodule recovers its ambient free module object,
        # a computed structural value of the construction (not category-graph placement).
        "refined M.submodule(...) has ambient module M",
        lambda _: refine_for_membership(S, MZZCat.Subobjects()).ambient_module() is M,
    ),
    (
        "Modules(QQ).Quotients().ParentMethods quotient_by_* split methods produce one-dimensional quotient vectorspaces",
        lambda _: rational_quotient_split_methods_have_one_dimensional_outputs(),
    ),
    (
        "CombinatorialFreeModule basis element surfaces expose terms and coefficients",
        lambda _: C.term("a", QQ(3)) == 3 * a
        and (2 * a + 5 * b).coefficient("a") == 2
        and (2 * a + 5 * b).monomials() == [a, b],
    ),
    (
        "category constructors expose basis index and ordered basis order through refined modules",
        lambda _: list(NMQQ.CombinatorialFreeModule(Sets().Constructors().FiniteEnumeratedSet(["a", "b"])).basis_index_set())
        == ["a", "b"]
        and NMQQ.VectorSpace(dimension=2).basis_order() == (0, 1),
    ),
    (
        "Modules(ExteriorAlgebra(QQ)).Constructors().FPModule(defining_map=identity) is trivial",
        lambda _: fp_module_from_identity_cokernel().is_trivial(),
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(...) has rank 3",
        lambda _: NMZZ.IntegerLattice(basis=[[1, 0, 3], [0, 2, 1], [0, 2, 7]]).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(basis=matrix(...)) has rank 3",
        lambda _: NMZZ.IntegerLattice(basis=matrix(ZZ, [[1, 0, 3], [0, 2, 1], [0, 2, 7]])).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(basis=rows) has rank 3",
        lambda _: NMZZ.IntegerLattice(basis=[[1, 0, 3], [0, 2, 1], [0, 2, 7]]).rank() == 3,
    ),
    (
        "Modules(ZZ).Constructors().IntegerLattice(basis=zeta_5) has rank 4",
        lambda _: integer_lattice_from_cyclotomic_order_element().rank() == 4,
    ),
    (
        "Modules(Zmod(6)).Constructors().rank_one_module_with_ring_isomorphisms(basis=5) gives inverse witnesses",
        lambda _: rank_one_module_isomorphisms_are_inverse_witnesses(),
    ),
    (
        "Modules(ZZ).Constructors().polynomial_ring_as_module(name='t') has base ring ZZ",
        lambda _: NMZZ.polynomial_ring_as_module(name="t").base_ring() is ZZ,
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)

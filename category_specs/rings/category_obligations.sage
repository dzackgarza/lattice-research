r"""Mathematical-fact obligations for the ring category subtree.

Each statement instantiates an object through the ring DSL (``Rings().Constructors()``)
and asserts a real mathematical value it must recover: a characteristic, a finiteness or
algebraic-closure predicate, an order/cardinality, a field degree, a residue prime, a
working precision, a number of generators, a base ring, a divisibility relation, a
trace-pairing discriminant, an integral basis, or a concrete matrix. A statement passes
only when the backend computes the value; it is red while the backend is incomplete. No
statement asserts category-graph structure (subcategory membership ``obj in Cat()``,
method ownership ``abstract_method_has_name(...)``, category/type-package identity
``X is Y()`` / ``... is ZZ``, or base-category-and-axiom routing). That is a property of
the spec *source*, enforced by the validators in ``category_specs/validators/``
(super_categories, banned_spec_patterns, constructor_name_inventory). The category-graph
meta-assertions that previously dominated this file were removed here; migrating any
structural invariant they encoded into validator coverage is the separate "framework
tests -> validators" workstream (tracked, not silently dropped).

Citations (per the ``What A Test Cites`` contract): every expected value below is an
elementary computed fact (characteristic of ZZ/QQ, precision of a 53-bit float field,
order of Z/6, cardinality of GF(5), degree of a number field, residue prime of a p-adic
ring, a scalar matrix), so none carries a literature citation.
"""

from pathlib import Path
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.rings import Rings
from category_specs.utils import assert_category_statements
from sage.all import ZZ, QQ, identity_matrix, matrix


NR = Rings().Constructors()
PQ = NR.PolynomialRing(base_ring=QQ, name="x")
x = PQ.gen()


CATEGORY_STATEMENTS = (
    ("Constructors().ZZ() has characteristic 0", lambda _: NR.ZZ().characteristic() == 0),
    ("Constructors().ZZ() is not finite", lambda _: not NR.ZZ().is_finite()),
    ("ring element 2 divides 4 (elementary divisibility)", lambda _: ZZ(2).divides(ZZ(4))),
    ("Constructors().QQ() has characteristic 0", lambda _: NR.QQ().characteristic() == 0),
    ("Constructors().QQ() is a number field", lambda _: NR.QQ().is_number_field()),
    ("Constructors().QQ().trace_pairing_discriminant([1]) is 1", lambda _: NR.QQ().trace_pairing_discriminant([QQ(1)]) == 1),
    ("Constructors().QQ().integral_basis_at_prime(2) is [1]", lambda _: tuple(NR.QQ().integral_basis_at_prime(2)) == (QQ(1),)),
    ("Constructors().QQ().integral_basis_at_primes([2, 3]) is [1]", lambda _: tuple(NR.QQ().integral_basis_at_primes([2, 3])) == (QQ(1),)),
    ("Constructors().QQbar() has characteristic 0", lambda _: NR.QQbar().characteristic() == 0),
    ("Constructors().QQbar() is algebraically closed", lambda _: NR.QQbar().is_algebraically_closed()),
    ("Constructors().AA() has characteristic 0", lambda _: NR.AA().characteristic() == 0),
    ("Constructors().RR() has characteristic 0", lambda _: NR.RR().characteristic() == 0),
    ("Constructors().RR() has precision 53", lambda _: NR.RR().precision() == 53),
    ("Constructors().CC() has characteristic 0", lambda _: NR.CC().characteristic() == 0),
    ("Constructors().CC() has precision 53", lambda _: NR.CC().precision() == 53),
    ("Constructors().RDF() has characteristic 0", lambda _: NR.RDF().characteristic() == 0),
    ("Constructors().RDF() has precision 53", lambda _: NR.RDF().precision() == 53),
    ("Constructors().CDF() has characteristic 0", lambda _: NR.CDF().characteristic() == 0),
    ("Constructors().CDF() has precision 53", lambda _: NR.CDF().precision() == 53),
    ("Constructors().RealField(prec=100) has precision 100", lambda _: NR.RealField(prec=100).precision() == 100),
    ("Constructors().ComplexField(prec=100) has precision 100", lambda _: NR.ComplexField(prec=100).precision() == 100),
    ("Constructors().RealBallField(prec=100) has precision 100", lambda _: NR.RealBallField(prec=100).precision() == 100),
    ("Constructors().ComplexBallField(prec=100) has precision 100", lambda _: NR.ComplexBallField(prec=100).precision() == 100),
    ("Constructors().IntegerModRing(order=6) has order 6", lambda _: NR.IntegerModRing(order=6).order() == 6),
    ("Constructors().IntegerModRing(order=6) has characteristic 6", lambda _: NR.IntegerModRing(order=6).characteristic() == 6),
    ("Constructors().Zmod(order=6) has order 6", lambda _: NR.Zmod(order=6).order() == 6),
    ("Constructors().Integers(order=6) has order 6", lambda _: NR.Integers(order=6).order() == 6),
    ("Constructors().GF(order=5) has cardinality 5", lambda _: NR.GF(order=5).cardinality() == 5),
    ("Constructors().GF(order=5) has characteristic 5", lambda _: NR.GF(order=5).characteristic() == 5),
    ("Constructors().FiniteField(order=5) has cardinality 5", lambda _: NR.FiniteField(order=5).cardinality() == 5),
    ("Constructors().NumberField(polynomial=x^3 - 2, name='a') has degree 3", lambda _: NR.NumberField(polynomial=x**3 - 2, name="a").degree() == 3),
    (
        "Constructors().NumberFieldTower([x^2 + 1, x^2 + 2], ['a', 'b']) has absolute degree 4",
        lambda _: NR.NumberFieldTower(polynomials=[x**2 + 1, x**2 + 2], names=["a", "b"]).absolute_degree() == 4,
    ),
    ("Constructors().QuadraticField(D=5, name='a') has degree 2", lambda _: NR.QuadraticField(D=5, name="a").degree() == 2),
    ("Constructors().CyclotomicField(n=5) has degree 4", lambda _: NR.CyclotomicField(n=5).degree() == 4),
    ("Constructors().Zp(p=5) has prime 5", lambda _: NR.Zp(p=5).prime() == 5),
    ("Constructors().Zp(p=5, relative_cap=4, absolute_cap=8, type='lattice-cap') has prime 5", lambda _: NR.Zp(p=5, relative_cap=4, absolute_cap=8, type="lattice-cap").prime() == 5),
    ("Constructors().Zp(p=5, default_prec=4, halting_prec=8, type='relaxed') has prime 5", lambda _: NR.Zp(p=5, default_prec=4, halting_prec=8, type="relaxed").prime() == 5),
    ("Constructors().Qp(p=5) has prime 5", lambda _: NR.Qp(p=5).prime() == 5),
    ("Constructors().Qp(p=5, relative_cap=4, absolute_cap=8, type='lattice-cap') has prime 5", lambda _: NR.Qp(p=5, relative_cap=4, absolute_cap=8, type="lattice-cap").prime() == 5),
    ("Constructors().Qp(p=5, default_prec=4, halting_prec=8, type='relaxed') has prime 5", lambda _: NR.Qp(p=5, default_prec=4, halting_prec=8, type="relaxed").prime() == 5),
    ("Constructors().Zq(p=5, degree=2, names='a') has prime 5", lambda _: NR.Zq(p=5, degree=2, names="a").prime() == 5),
    (
        "Constructors().Zq(factorization=[(5, 2)], names='a') has prime 5",
        lambda _: NR.Zq(factorization=[(5, 2)], names="a").prime() == 5,
    ),
    ("Constructors().Qq(p=5, degree=2, names='a') has prime 5", lambda _: NR.Qq(p=5, degree=2, names="a").prime() == 5),
    (
        "Constructors().Qq(factorization=[(5, 2)], names='a') has prime 5",
        lambda _: NR.Qq(factorization=[(5, 2)], names="a").prime() == 5,
    ),
    ("Constructors().PolynomialRing(ZZ, name='t') has base ring ZZ", lambda _: NR.PolynomialRing(base_ring=ZZ, name="t").base_ring() is ZZ),
    ("Constructors().PolynomialRing(ZZ, name='t') has one generator", lambda _: NR.PolynomialRing(base_ring=ZZ, name="t").ngens() == 1),
    ("Constructors().PowerSeriesRing(ZZ, 't') has base ring ZZ", lambda _: NR.PowerSeriesRing(base_ring=ZZ, name="t").base_ring() is ZZ),
    (
        "Constructors().MultivariatePowerSeriesRing(ZZ, names=('x', 'y')) has two generators",
        lambda _: NR.MultivariatePowerSeriesRing(base_ring=ZZ, names=("x", "y")).ngens() == 2,
    ),
    (
        "Constructors().MultivariatePowerSeriesRingWithGeneratorPrefix(ZZ, prefix='x', num_gens=2) has two generators",
        lambda _: NR.MultivariatePowerSeriesRingWithGeneratorPrefix(base_ring=ZZ, prefix="x", num_gens=2).ngens() == 2,
    ),
    ("Constructors().LaurentSeriesRing(ZZ, 't') has base ring ZZ", lambda _: NR.LaurentSeriesRing(base_ring=ZZ, name="t").base_ring() is ZZ),
    (
        "Constructors().LaurentSeriesRing(power_series_ring=...) has base ring ZZ",
        lambda _: NR.LaurentSeriesRing(power_series_ring=NR.PowerSeriesRing(base_ring=ZZ, name="u")).base_ring() is ZZ,
    ),
    ("Constructors().PuiseuxSeriesRing(QQ, 't') has base ring QQ", lambda _: NR.PuiseuxSeriesRing(base_ring=QQ, name="t").base_ring() is QQ),
    (
        "Constructors().PuiseuxSeriesRing(laurent_series_ring=...) has base ring QQ",
        lambda _: NR.PuiseuxSeriesRing(laurent_series_ring=NR.LaurentSeriesRing(base_ring=QQ, name="u")).base_ring() is QQ,
    ),
    ("Constructors().MatrixRing(base_ring=ZZ, n=2) has 2 rows", lambda _: NR.MatrixRing(base_ring=ZZ, n=2).nrows() == 2),
    ("Constructors().MatrixRing(base_ring=ZZ, n=2) has 2 columns", lambda _: NR.MatrixRing(base_ring=ZZ, n=2).ncols() == 2),
    ("Constructors().MatrixRing(base_ring=ZZ, n=2) has base ring ZZ", lambda _: NR.MatrixRing(base_ring=ZZ, n=2).base_ring() is ZZ),
    (
        "Constructors().MatrixRing(ZZ, 2).matrix_from_matrix(...) returns the same matrix",
        lambda _: NR.MatrixRing(base_ring=ZZ, n=2).matrix_from_matrix(matrix(ZZ, [[1, 2], [3, 4]]))
        == matrix(ZZ, [[1, 2], [3, 4]]),
    ),
    (
        "Constructors().MatrixRing(ZZ, 2).matrix_from_entries(...) uses row-major entries",
        lambda _: NR.MatrixRing(base_ring=ZZ, n=2).matrix_from_entries([1, 2, 3, 4]) == matrix(ZZ, [[1, 2], [3, 4]]),
    ),
    (
        "Constructors().MatrixRing(ZZ, 2).matrix_from_rows(...) uses row data",
        lambda _: NR.MatrixRing(base_ring=ZZ, n=2).matrix_from_rows([[1, 2], [3, 4]]) == matrix(ZZ, [[1, 2], [3, 4]]),
    ),
    (
        "Constructors().MatrixRing(ZZ, 2).scalar_matrix(3) is 3 times the identity",
        lambda _: NR.MatrixRing(base_ring=ZZ, n=2).scalar_matrix(3) == 3 * identity_matrix(ZZ, 2),
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)

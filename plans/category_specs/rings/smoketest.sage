from pathlib import Path
import logging
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.rings import Rings


logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
logger = logging.getLogger("category_specs.rings.smoketest")

failures = []


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


NR = Rings().NamedRings()
PQ = PolynomialRing(QQ, "x")
x = PQ.gen()

smoke_case("rings._ZZ via NamedRings().ZZ()", lambda: NR.ZZ())
smoke_case("rings._QQ via NamedRings().QQ()", lambda: NR.QQ())
smoke_case("rings._QQbar via NamedRings().QQbar()", lambda: NR.QQbar())
smoke_case("rings._AA via NamedRings().AA()", lambda: NR.AA())
smoke_case("rings._RR via NamedRings().RR()", lambda: NR.RR())
smoke_case("rings._CC via NamedRings().CC()", lambda: NR.CC())
smoke_case("rings._RealDoubleFields via NamedRings().RDF()", lambda: NR.RDF())
smoke_case("rings._ComplexDoubleFields via NamedRings().CDF()", lambda: NR.CDF())
smoke_case("rings._RealIntervalFields via NamedRings().RIF()", lambda: NR.RIF())
smoke_case("rings._ComplexIntervalFields via NamedRings().CIF()", lambda: NR.CIF())
smoke_case("rings._RealFields via NamedRings().RealField(100)", lambda: NR.RealField(100))
smoke_case(
    "rings._ComplexFields via NamedRings().ComplexField(100)",
    lambda: NR.ComplexField(100),
)
smoke_case(
    "rings._RealBallFields via NamedRings().RealBallField(100)",
    lambda: NR.RealBallField(100),
)
smoke_case(
    "rings._ComplexBallFields via NamedRings().ComplexBallField(100)",
    lambda: NR.ComplexBallField(100),
)
smoke_case(
    "rings._IntegerModRings via NamedRings().IntegerModRing(6)",
    lambda: NR.IntegerModRing(6),
)
smoke_case("rings._FiniteFields via NamedRings().GF(5)", lambda: NR.GF(5))
smoke_case(
    "rings._NumberFields via NamedRings().NumberField(x^3 - 2, 'a')",
    lambda: NR.NumberField(x**3 - 2, "a"),
)
smoke_case(
    "rings._QuadraticNumberFields via NamedRings().QuadraticField(5, 'a')",
    lambda: NR.QuadraticField(5, "a"),
)
smoke_case(
    "rings._CyclotomicFields via NamedRings().CyclotomicField(5)",
    lambda: NR.CyclotomicField(5),
)
smoke_case("rings._Zp via NamedRings().Zp(5)", lambda: NR.Zp(5))
smoke_case("rings._Qp via NamedRings().Qp(5)", lambda: NR.Qp(5))
smoke_case(
    "rings._Zp via NamedRings().Zq((5, 2), names='a')",
    lambda: NR.Zq((5, 2), names="a"),
)
smoke_case(
    "rings._Qp via NamedRings().Qq((5, 2), names='a')",
    lambda: NR.Qq((5, 2), names="a"),
)
smoke_case(
    "rings._PolynomialRings via NamedRings().PolynomialRing(ZZ, 't')",
    lambda: NR.PolynomialRing(ZZ, "t"),
)
smoke_case(
    "rings._PowerSeriesRings via NamedRings().PowerSeriesRing(ZZ, 't')",
    lambda: NR.PowerSeriesRing(ZZ, "t"),
)
smoke_case(
    "rings._LaurentSeriesRings via NamedRings().LaurentSeriesRing(ZZ, 't')",
    lambda: NR.LaurentSeriesRing(ZZ, "t"),
)
smoke_case(
    "rings._PuiseuxSeriesRings via NamedRings().PuiseuxSeriesRing(QQ, 't')",
    lambda: NR.PuiseuxSeriesRing(QQ, "t"),
)
smoke_case(
    "rings._MatrixAlgebras via NamedRings().MatrixRing(ZZ, 2)",
    lambda: NR.MatrixRing(ZZ, 2),
)

assert not failures, "\n".join(failures)

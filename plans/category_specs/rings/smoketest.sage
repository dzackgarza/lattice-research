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


NR = Rings().Constructors()
PQ = PolynomialRing(QQ, "x")
x = PQ.gen()

smoke_case("rings._ZZ via Constructors().ZZ()", lambda: NR.ZZ())
smoke_case("rings._QQ via Constructors().QQ()", lambda: NR.QQ())
smoke_case("rings._QQbar via Constructors().QQbar()", lambda: NR.QQbar())
smoke_case("rings._AA via Constructors().AA()", lambda: NR.AA())
smoke_case("rings._RR via Constructors().RR()", lambda: NR.RR())
smoke_case("rings._CC via Constructors().CC()", lambda: NR.CC())
smoke_case("rings._RealDoubleFields via Constructors().RDF()", lambda: NR.RDF())
smoke_case("rings._ComplexDoubleFields via Constructors().CDF()", lambda: NR.CDF())
smoke_case("rings._RealIntervalFields via Constructors().RIF()", lambda: NR.RIF())
smoke_case("rings._ComplexIntervalFields via Constructors().CIF()", lambda: NR.CIF())
smoke_case("rings._RealFields via Constructors().RealField(100)", lambda: NR.RealField(100))
smoke_case(
    "rings._ComplexFields via Constructors().ComplexField(100)",
    lambda: NR.ComplexField(100),
)
smoke_case(
    "rings._RealBallFields via Constructors().RealBallField(100)",
    lambda: NR.RealBallField(100),
)
smoke_case(
    "rings._ComplexBallFields via Constructors().ComplexBallField(100)",
    lambda: NR.ComplexBallField(100),
)
smoke_case(
    "rings._IntegerModRings via Constructors().IntegerModRing(6)",
    lambda: NR.IntegerModRing(6),
)
smoke_case("rings._FiniteFields via Constructors().GF(5)", lambda: NR.GF(5))
smoke_case(
    "rings._NumberFields via Constructors().NumberField(x^3 - 2, 'a')",
    lambda: NR.NumberField(x**3 - 2, "a"),
)
smoke_case(
    "rings._QuadraticNumberFields via Constructors().QuadraticField(5, 'a')",
    lambda: NR.QuadraticField(5, "a"),
)
smoke_case(
    "rings._CyclotomicFields via Constructors().CyclotomicField(5)",
    lambda: NR.CyclotomicField(5),
)
smoke_case("rings._Zp via Constructors().Zp(5)", lambda: NR.Zp(5))
smoke_case("rings._Qp via Constructors().Qp(5)", lambda: NR.Qp(5))
smoke_case(
    "rings._Zp via Constructors().Zq((5, 2), names='a')",
    lambda: NR.Zq((5, 2), names="a"),
)
smoke_case(
    "rings._Qp via Constructors().Qq((5, 2), names='a')",
    lambda: NR.Qq((5, 2), names="a"),
)
smoke_case(
    "rings._PolynomialRings via Constructors().PolynomialRing(ZZ, 't')",
    lambda: NR.PolynomialRing(ZZ, "t"),
)
smoke_case(
    "rings._PowerSeriesRings via Constructors().PowerSeriesRing(ZZ, 't')",
    lambda: NR.PowerSeriesRing(ZZ, "t"),
)
smoke_case(
    "rings._LaurentSeriesRings via Constructors().LaurentSeriesRing(ZZ, 't')",
    lambda: NR.LaurentSeriesRing(ZZ, "t"),
)
smoke_case(
    "rings._PuiseuxSeriesRings via Constructors().PuiseuxSeriesRing(QQ, 't')",
    lambda: NR.PuiseuxSeriesRing(QQ, "t"),
)
smoke_case(
    "rings._MatrixAlgebras via Constructors().MatrixRing(ZZ, 2)",
    lambda: NR.MatrixRing(ZZ, 2),
)

assert not failures, "\n".join(failures)

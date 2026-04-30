import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.algebras import Algebras
from category_specs.cat import Cat
from sage.all import ZZ


failures = []


def require(condition, label="condition failed"):
    if not condition:
        raise AssertionError(label)


def smoke_case(label, build):
    try:
        build()
    except Exception as exc:
        failures.append(f"{label}: {type(exc).__name__}: {exc}")


A = Algebras(ZZ)

smoke_case("Algebras(ZZ) is an object of Cat()", lambda: require(A in Cat()))
smoke_case("Algebras(ZZ).Commutative()", lambda: A.Commutative())
smoke_case("Algebras(ZZ).WithBasis()", lambda: A.WithBasis())
smoke_case("Algebras(ZZ).FiniteDimensional()", lambda: A.FiniteDimensional())
smoke_case("Algebras(ZZ).Semisimple()", lambda: A.Semisimple())
smoke_case("Algebras(ZZ).Subobjects()", lambda: A.Subobjects())
smoke_case("Algebras(ZZ).Quotients()", lambda: A.Quotients())
smoke_case("Algebras(ZZ).Subquotients()", lambda: A.Subquotients())
smoke_case("Algebras(ZZ).CartesianProducts()", lambda: A.CartesianProducts())
smoke_case("Algebras(ZZ).TensorProducts()", lambda: A.TensorProducts())
smoke_case("Algebras(ZZ).DualObjects()", lambda: A.DualObjects())
smoke_case("Algebras(ZZ).Homsets()", lambda: A.Homsets())
smoke_case(
    "Algebras(ZZ).Constructors() has admitted constructor cases",
    lambda: require(
        False,
        "no algebra constructors have been admitted; decide first concrete constructor cases in NEEDS_DECISIONS.md",
    ),
)

assert not failures, "\n".join(failures)

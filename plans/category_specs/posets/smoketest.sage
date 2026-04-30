import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.posets import Posets


failures = []


def require(condition, label="condition failed"):
    if not condition:
        raise AssertionError(label)


def smoke_case(label, build):
    try:
        build()
    except Exception as exc:
        failures.append(f"{label}: {type(exc).__name__}: {exc}")


P = Posets()

smoke_case("Posets() is an object of Cat()", lambda: require(P in Cat()))
smoke_case("Posets().Finite()", lambda: P.Finite())
smoke_case("Posets().Lattice()", lambda: P.Lattice())
smoke_case("Posets().Lattice().Finite()", lambda: P.Lattice().Finite())
smoke_case("Posets().Subobjects()", lambda: P.Subobjects())
smoke_case("Posets().Quotients()", lambda: P.Quotients())
smoke_case("Posets().Subquotients()", lambda: P.Subquotients())
smoke_case("Posets().CartesianProducts()", lambda: P.CartesianProducts())
smoke_case("Posets().Homsets()", lambda: P.Homsets())
smoke_case("Posets().Constructors() exists", lambda: P.Constructors())
smoke_case(
    "Posets().Constructors() has admitted constructor cases",
    lambda: require(
        False,
        "no poset constructors have been admitted; decide the constructor inventory in NEEDS_DECISIONS.md",
    ),
)

assert not failures, "\n".join(failures)

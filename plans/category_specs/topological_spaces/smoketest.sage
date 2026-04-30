import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.topological_spaces import TopologicalSpaces


failures = []


def require(condition, label="condition failed"):
    if not condition:
        raise AssertionError(label)


def smoke_case(label, build):
    try:
        build()
    except Exception as exc:
        failures.append(f"{label}: {type(exc).__name__}: {exc}")


T = TopologicalSpaces()
smoke_case("TopologicalSpaces() is an object of Cat()", lambda: require(T in Cat()))
smoke_case("TopologicalSpaces().Metric() is an object of Cat()", lambda: require(T.Metric() in Cat()))
smoke_case("TopologicalSpaces().Subobjects()", lambda: T.Subobjects())
smoke_case("TopologicalSpaces().Quotients()", lambda: T.Quotients())
smoke_case("TopologicalSpaces().Subquotients()", lambda: T.Subquotients())
smoke_case(
    "TopologicalSpaces().Constructors() has admitted constructor cases",
    lambda: require(
        False,
        "no topological-space constructors have been admitted; decide the constructor inventory in NEEDS_DECISIONS.md",
    ),
)

assert not failures, "\n".join(failures)

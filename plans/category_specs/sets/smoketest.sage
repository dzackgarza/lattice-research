from pathlib import Path
import logging
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.sets import Sets


logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
logger = logging.getLogger("category_specs.sets.smoketest")

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


NS = Sets().NamedSets()

smoke_case(
    "sets.SetObjects via Set(ZZ)",
    lambda: NS.Set(ZZ),
)
smoke_case(
    "sets.SetObjectsEnumerated via Set([1, 2, 3])",
    lambda: NS.Set([1, 2, 3]),
)
smoke_case(
    "sets.FiniteEnumeratedSetObjects via FiniteEnumeratedSet([1, 2, 3])",
    lambda: NS.FiniteEnumeratedSet([1, 2, 3]),
)
smoke_case(
    "sets.IntegerRangeSets via IntegerRange(5)",
    lambda: NS.IntegerRange(5),
)
smoke_case(
    "sets.NonNegativeIntegersSets via NonNegativeIntegers()",
    lambda: NS.NonNegativeIntegers(),
)
smoke_case(
    "sets.PositiveIntegersSets via PositiveIntegers()",
    lambda: NS.PositiveIntegers(),
)
smoke_case(
    "sets.PrimesSets via Primes()",
    lambda: NS.Primes(),
)
smoke_case(
    "sets.RealSets via RealSet((0, 1))",
    lambda: NS.RealSet((0, 1)),
)
smoke_case(
    "sets.RecursivelyEnumeratedSets via RecursivelyEnumeratedSet([0], n |-> [n + 1])",
    lambda: NS.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth"),
)
smoke_case(
    "sets.DisjointUnionEnumeratedSets via DisjointUnionEnumeratedSets(Family(...))",
    lambda: NS.DisjointUnionEnumeratedSets(
        NS.Family([0, 1], lambda i: NS.FiniteEnumeratedSet([i, i + 1]))
    ),
)
smoke_case(
    "sets.CartesianProductSets via CartesianProduct([IntegerRange(2), IntegerRange(3)])",
    lambda: NS.CartesianProduct([NS.IntegerRange(2), NS.IntegerRange(3)]),
)
smoke_case(
    "sets.ConditionSets via ConditionSet(ZZ, even predicate)",
    lambda: NS.ConditionSet(ZZ, lambda n: n % 2 == 0),
)
smoke_case(
    "sets.ImageSets via ImageSubobject(n |-> n + 1, IntegerRange(3))",
    lambda: NS.ImageSubobject(lambda n: n + 1, NS.IntegerRange(3)),
)
smoke_case(
    "sets.TotallyOrderedFiniteSets via TotallyOrderedFiniteSet(['a', 'b', 'c'])",
    lambda: NS.TotallyOrderedFiniteSet(["a", "b", "c"]),
)
smoke_case(
    "sets.FiniteSetMapsSets via FiniteSetMaps(IntegerRange(2), IntegerRange(2))",
    lambda: NS.FiniteSetMaps(NS.IntegerRange(2), NS.IntegerRange(2)),
)
smoke_case(
    "sets.FamilySets via Family(IntegerRange(3), i |-> i^2)",
    lambda: NS.Family(NS.IntegerRange(3), lambda i: i**2),
)
smoke_case(
    "sets.EnumeratedSetsFromIterator via EnumeratedSetFromIterator(lambda: iter([0, 1, 2]))",
    lambda: NS.EnumeratedSetFromIterator(lambda: iter([0, 1, 2])),
)
smoke_case(
    "sets.CartesianProductSets via cartesian_product(IntegerRange(2), IntegerRange(3))",
    lambda: NS.cartesian_product(NS.IntegerRange(2), NS.IntegerRange(3)),
)

assert not failures, "\n".join(failures)

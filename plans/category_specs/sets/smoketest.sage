from pathlib import Path
import logging
import sys

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.sets import Sets
from sage.sets.real_set import RealSet as SageRealSet


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


C = Sets().Constructors()

smoke_case(
    "sets.SetObjects via Set(ZZ)",
    lambda: C.Set(ZZ),
)
smoke_case(
    "sets.SetObjectsEnumerated via Set([1, 2, 3])",
    lambda: C.Set([1, 2, 3]),
)
smoke_case(
    "sets.FiniteEnumeratedSetObjects via FiniteEnumeratedSet([1, 2, 3])",
    lambda: C.FiniteEnumeratedSet([1, 2, 3]),
)
smoke_case(
    "sets.IntegerRangeSets via IntegerRange(5)",
    lambda: C.IntegerRange(5),
)
smoke_case(
    "sets.NonNegativeIntegersSets via NonNegativeIntegers()",
    lambda: C.NonNegativeIntegers(),
)
smoke_case(
    "sets.PositiveIntegersSets via PositiveIntegers()",
    lambda: C.PositiveIntegers(),
)
smoke_case(
    "sets.PrimesSets via Primes()",
    lambda: C.Primes(),
)
smoke_case(
    "sets.RealSets via RealSet([RealSet.open(0, 1).get_interval(0)])",
    lambda: C.RealSet([SageRealSet.open(0, 1).get_interval(0)]),
)
smoke_case(
    "sets.RecursivelyEnumeratedSets via RecursivelyEnumeratedSet([0], n |-> [n + 1])",
    lambda: C.RecursivelyEnumeratedSet([0], lambda n: [n + 1], enumeration="breadth"),
)
smoke_case(
    "sets.DisjointUnionEnumeratedSets via DisjointUnionEnumeratedSets(Family(...))",
    lambda: C.DisjointUnionEnumeratedSets(
        C.Family([0, 1], lambda i: C.FiniteEnumeratedSet([i, i + 1]))
    ),
)
smoke_case(
    "sets.CartesianProductSets via CartesianProduct([IntegerRange(2), IntegerRange(3)])",
    lambda: C.CartesianProduct([C.IntegerRange(2), C.IntegerRange(3)]),
)
smoke_case(
    "sets.ConditionSets via ConditionSet(ZZ, even predicate)",
    lambda: C.ConditionSet(ZZ, [lambda n: n % 2 == 0]),
)
smoke_case(
    "sets.ImageSets via ImageSubobject(n |-> n + 1, IntegerRange(3))",
    lambda: C.ImageSubobject(lambda n: n + 1, C.IntegerRange(3)),
)
smoke_case(
    "sets.TotallyOrderedFiniteSets via TotallyOrderedFiniteSet(['a', 'b', 'c'])",
    lambda: C.TotallyOrderedFiniteSet(["a", "b", "c"]),
)
smoke_case(
    "sets.FiniteSetMapsSets via FiniteSetMaps(IntegerRange(2), IntegerRange(2))",
    lambda: C.FiniteSetMaps(C.IntegerRange(2), C.IntegerRange(2)),
)
smoke_case(
    "sets.FamilySets via Family(IntegerRange(3), i |-> i^2)",
    lambda: C.Family(C.IntegerRange(3), lambda i: i**2),
)
smoke_case(
    "sets.EnumeratedSetsFromIterator via EnumeratedSetFromIterator(lambda: iter([0, 1, 2]))",
    lambda: C.EnumeratedSetFromIterator(lambda: iter([0, 1, 2])),
)
smoke_case(
    "sets.CartesianProductSets via cartesian_product([IntegerRange(2), IntegerRange(3)])",
    lambda: C.cartesian_product([C.IntegerRange(2), C.IntegerRange(3)]),
)

assert not failures, "\n".join(failures)

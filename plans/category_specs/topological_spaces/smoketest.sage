import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.topological_spaces import TopologicalSpaces
from category_specs.utils import assert_smoke_statements


T = TopologicalSpaces()

SMOKE_STATEMENTS = (
    ("TopologicalSpaces() is an object of Cat()", lambda _: T in Cat()),
    ("TopologicalSpaces().Metric() is an object of Cat()", lambda _: T.Metric() in Cat()),
    ("TopologicalSpaces().Metric() is a subcategory of TopologicalSpaces()", lambda _: T.Metric().is_subcategory(T)),
    ("TopologicalSpaces().Subobjects() is an object of Cat()", lambda _: T.Subobjects() in Cat()),
    ("TopologicalSpaces().Quotients() is an object of Cat()", lambda _: T.Quotients() in Cat()),
    ("TopologicalSpaces().Subquotients() is an object of Cat()", lambda _: T.Subquotients() in Cat()),
    (
        "TopologicalSpaces().Constructors() has admitted mathematical constructor cases",
        lambda _: False,
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)

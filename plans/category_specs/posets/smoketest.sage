import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.posets import Posets
from category_specs.utils import assert_smoke_statements


P = Posets()

SMOKE_STATEMENTS = (
    ("Posets() is an object of Cat()", lambda _: P in Cat()),
    ("Posets().Finite() is an object of Cat()", lambda _: P.Finite() in Cat()),
    ("Posets().Lattice() is an object of Cat()", lambda _: P.Lattice() in Cat()),
    ("Posets().Lattice().Finite() is an object of Cat()", lambda _: P.Lattice().Finite() in Cat()),
    ("Posets().Finite() is a subcategory of Posets()", lambda _: P.Finite().is_subcategory(P)),
    ("Posets().Lattice() is a subcategory of Posets()", lambda _: P.Lattice().is_subcategory(P)),
    ("Posets().Lattice().Finite() is a subcategory of Posets().Lattice()", lambda _: P.Lattice().Finite().is_subcategory(P.Lattice())),
    ("Posets().Subobjects() is an object of Cat()", lambda _: P.Subobjects() in Cat()),
    ("Posets().Quotients() is an object of Cat()", lambda _: P.Quotients() in Cat()),
    ("Posets().Subquotients() is an object of Cat()", lambda _: P.Subquotients() in Cat()),
    ("Posets().CartesianProducts() is an object of Cat()", lambda _: P.CartesianProducts() in Cat()),
    ("Posets().HomCategory() is an object of Cat()", lambda _: P.HomCategory() in Cat()),
    (
        "Posets().Constructors() has admitted mathematical constructor cases",
        lambda _: False,
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)

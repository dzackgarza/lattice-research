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
    ("Posets().MeetSemilattice() is an object of Cat()", lambda _: P.MeetSemilattice() in Cat()),
    ("Posets().MeetSemilattice().Finite() is an object of Cat()", lambda _: P.MeetSemilattice().Finite() in Cat()),
    ("Posets().JoinSemilattice() is an object of Cat()", lambda _: P.JoinSemilattice() in Cat()),
    ("Posets().JoinSemilattice().Finite() is an object of Cat()", lambda _: P.JoinSemilattice().Finite() in Cat()),
    ("Posets().Lattice() is an object of Cat()", lambda _: P.Lattice() in Cat()),
    ("Posets().Lattice().Finite() is an object of Cat()", lambda _: P.Lattice().Finite() in Cat()),
    ("Posets().Finite() is a subcategory of Posets()", lambda _: P.Finite().is_subcategory(P)),
    ("Posets().MeetSemilattice() is a subcategory of Posets()", lambda _: P.MeetSemilattice().is_subcategory(P)),
    ("Posets().JoinSemilattice() is a subcategory of Posets()", lambda _: P.JoinSemilattice().is_subcategory(P)),
    ("Posets().Lattice() is a subcategory of Posets()", lambda _: P.Lattice().is_subcategory(P)),
    (
        "Posets().Lattice() is a subcategory of Posets().MeetSemilattice()",
        lambda _: P.Lattice().is_subcategory(P.MeetSemilattice()),
    ),
    (
        "Posets().Lattice() is a subcategory of Posets().JoinSemilattice()",
        lambda _: P.Lattice().is_subcategory(P.JoinSemilattice()),
    ),
    (
        "Posets().MeetSemilattice().Finite() is a subcategory of Posets().MeetSemilattice()",
        lambda _: P.MeetSemilattice().Finite().is_subcategory(P.MeetSemilattice()),
    ),
    (
        "Posets().JoinSemilattice().Finite() is a subcategory of Posets().JoinSemilattice()",
        lambda _: P.JoinSemilattice().Finite().is_subcategory(P.JoinSemilattice()),
    ),
    ("Posets().Lattice().Finite() is a subcategory of Posets().Lattice()", lambda _: P.Lattice().Finite().is_subcategory(P.Lattice())),
    ("Posets().Subobjects() is an object of Cat()", lambda _: P.Subobjects() in Cat()),
    ("Posets().Quotients() is an object of Cat()", lambda _: P.Quotients() in Cat()),
    ("Posets().Subquotients() is an object of Cat()", lambda _: P.Subquotients() in Cat()),
    ("Posets().CartesianProducts() is an object of Cat()", lambda _: P.CartesianProducts() in Cat()),
    ("Posets().HomCategory() is an object of Cat()", lambda _: P.HomCategory() in Cat()),
)

assert_smoke_statements(SMOKE_STATEMENTS)

r"""Mathematical smoke surface for the lattice category subtree."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Cat
from category_specs.lattices import Lattices
from category_specs.modules import Modules
from category_specs.utils import assert_smoke_statements
from sage.all import ZZ


C = Cat()
MZZ = Modules(ZZ, dispatch=False)
LATTICE_AMBIENT = MZZ.Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()
LZZ = Lattices(ZZ)

SMOKE_STATEMENTS = (
    ("Lattices(ZZ) is an object of Cat()", lambda _: LZZ in C),
    ("Lattices(ZZ) is registered as a Cat subobject", lambda _: LZZ in C.Subobjects()),
    ("Lattices(ZZ) records the explicit lattice chain as ambient category", lambda _: LZZ.ambient_category() is LATTICE_AMBIENT),
    ("Lattices(ZZ) exposes is_lattice as its defining predicate", lambda _: LZZ.defining_predicates() == ("is_lattice",)),
    ("Lattices(ZZ).HomCategory() is an object of Cat()", lambda _: LZZ.HomCategory() in C),
    ("Lattices(ZZ).EndCategory() is an object of Cat()", lambda _: LZZ.EndCategory() in C),
    ("Lattices(ZZ).AutCategory() is an object of Cat()", lambda _: LZZ.AutCategory() in C),
    ("Lattices(ZZ).Subobjects() is an object of Cat()", lambda _: LZZ.Subobjects() in C),
    ("Lattices(ZZ).DualObjects() is an object of Cat()", lambda _: LZZ.DualObjects() in C),
    ("Lattices(ZZ).DualLattices() aliases DualObjects()", lambda _: LZZ.DualLattices() is LZZ.DualObjects()),
    ("Lattices(ZZ).Even() exposes is_even as its defining predicate", lambda _: LZZ.Even().defining_predicates() == ("is_even",)),
)

assert_smoke_statements(SMOKE_STATEMENTS)

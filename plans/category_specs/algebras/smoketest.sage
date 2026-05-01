import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.algebras import Algebras
from category_specs.cat import Cat
from category_specs.utils import assert_smoke_statements
from sage.all import ZZ


A = Algebras(ZZ)
SMOKE_STATEMENTS = (
    ("Algebras(ZZ) is an object of Cat()", lambda _: A in Cat()),
    ("Algebras(ZZ) has base ring ZZ", lambda _: A.base_ring() is ZZ),
    ("Algebras(ZZ).Commutative() is an object of Cat()", lambda _: A.Commutative() in Cat()),
    ("Algebras(ZZ).WithBasis() is an object of Cat()", lambda _: A.WithBasis() in Cat()),
    ("Algebras(ZZ).FiniteDimensional() is an object of Cat()", lambda _: A.FiniteDimensional() in Cat()),
    ("Algebras(ZZ).Semisimple() is an object of Cat()", lambda _: A.Semisimple() in Cat()),
    ("Algebras(ZZ).Commutative() is a subcategory of Algebras(ZZ)", lambda _: A.Commutative().is_subcategory(A)),
    ("Algebras(ZZ).WithBasis() is a subcategory of Algebras(ZZ)", lambda _: A.WithBasis().is_subcategory(A)),
    ("Algebras(ZZ).FiniteDimensional() is a subcategory of Algebras(ZZ)", lambda _: A.FiniteDimensional().is_subcategory(A)),
    ("Algebras(ZZ).Semisimple() is a subcategory of Algebras(ZZ)", lambda _: A.Semisimple().is_subcategory(A)),
    ("Algebras(ZZ).Subobjects() is an object of Cat()", lambda _: A.Subobjects() in Cat()),
    ("Algebras(ZZ).Quotients() is an object of Cat()", lambda _: A.Quotients() in Cat()),
    ("Algebras(ZZ).Subquotients() is an object of Cat()", lambda _: A.Subquotients() in Cat()),
    ("Algebras(ZZ).CartesianProducts() is an object of Cat()", lambda _: A.CartesianProducts() in Cat()),
    ("Algebras(ZZ).TensorProducts() is an object of Cat()", lambda _: A.TensorProducts() in Cat()),
    ("Algebras(ZZ).DualObjects() is an object of Cat()", lambda _: A.DualObjects() in Cat()),
    ("Algebras(ZZ).HomCategory() is an object of Cat()", lambda _: A.HomCategory() in Cat()),
    (
        "Algebras(ZZ).Constructors().free_algebra_from_set is admitted",
        lambda _: A.Constructors().free_algebra_from_set,
    ),
    (
        "Algebras(ZZ).Constructors().from_multiplication_tensor is admitted",
        lambda _: A.Constructors().from_multiplication_tensor,
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)

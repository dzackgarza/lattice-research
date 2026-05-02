import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.algebras import Algebras
from category_specs.cat import Cat
from category_specs.sets import Sets
from category_specs.tensor_algebra_components import TensorAlgebraComponents
from category_specs.utils import assert_smoke_statements
from sage.all import GF, IntegerModRing, ZZ
from sage.categories.magmas import Magmas
from sage.categories.semigroups import Semigroups
from sage.groups.perm_gps.permgroup_named import CyclicPermutationGroup
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule


def A():
    return Algebras(ZZ)


def multiplicative_monoid_source():
    return IntegerModRing(3)


def multiplicative_group_source():
    return CyclicPermutationGroup(3)


def additive_source():
    return GF(3)


def multiplication_tensor():
    M = FiniteRankFreeModule(ZZ, 2, name="M")
    e = M.basis("e")
    return TensorAlgebraComponents(ZZ).Constructors().from_module_element_matrix(
        M,
        [
            [e[0], e[1]],
            [e[1], e[0]],
        ],
        name="mu",
    )


SMOKE_STATEMENTS = (
    ("Algebras(ZZ) is an object of Cat()", lambda _: A() in Cat()),
    ("Algebras(ZZ) has base ring ZZ", lambda _: A().base_ring() is ZZ),
    ("Algebras(ZZ).Commutative() is an object of Cat()", lambda _: A().Commutative() in Cat()),
    ("Algebras(ZZ).WithBasis() is an object of Cat()", lambda _: A().WithBasis() in Cat()),
    ("Algebras(ZZ).FiniteDimensional() is an object of Cat()", lambda _: A().FiniteDimensional() in Cat()),
    ("Algebras(ZZ).Semisimple() is an object of Cat()", lambda _: A().Semisimple() in Cat()),
    ("Algebras(ZZ).Commutative() is a subcategory of Algebras(ZZ)", lambda _: A().Commutative().is_subcategory(A())),
    ("Algebras(ZZ).WithBasis() is a subcategory of Algebras(ZZ)", lambda _: A().WithBasis().is_subcategory(A())),
    ("Algebras(ZZ).FiniteDimensional() is a subcategory of Algebras(ZZ)", lambda _: A().FiniteDimensional().is_subcategory(A())),
    ("Algebras(ZZ).Semisimple() is a subcategory of Algebras(ZZ)", lambda _: A().Semisimple().is_subcategory(A())),
    ("Algebras(ZZ).Subobjects() is an object of Cat()", lambda _: A().Subobjects() in Cat()),
    ("Algebras(ZZ).Quotients() is an object of Cat()", lambda _: A().Quotients() in Cat()),
    ("Algebras(ZZ).Subquotients() is an object of Cat()", lambda _: A().Subquotients() in Cat()),
    ("Algebras(ZZ).CartesianProducts() is an object of Cat()", lambda _: A().CartesianProducts() in Cat()),
    ("Algebras(ZZ).TensorProducts() is an object of Cat()", lambda _: A().TensorProducts() in Cat()),
    ("Algebras(ZZ).DualObjects() is an object of Cat()", lambda _: A().DualObjects() in Cat()),
    ("Algebras(ZZ).HomCategory() is an object of Cat()", lambda _: A().HomCategory() in Cat()),
    ("Algebras(ZZ).ParentMethods.subalgebra is admitted", lambda _: A().ParentMethods.subalgebra),
    ("Algebras(ZZ).ParentMethods.left_ideal is admitted", lambda _: A().ParentMethods.left_ideal),
    ("Algebras(ZZ).ParentMethods.right_ideal is admitted", lambda _: A().ParentMethods.right_ideal),
    ("Algebras(ZZ).ParentMethods.two_sided_ideal is admitted", lambda _: A().ParentMethods.two_sided_ideal),
    ("Algebras(ZZ).ParentMethods.principal_left_ideal is admitted", lambda _: A().ParentMethods.principal_left_ideal),
    ("Algebras(ZZ).ParentMethods.principal_right_ideal is admitted", lambda _: A().ParentMethods.principal_right_ideal),
    ("Algebras(ZZ).ParentMethods.principal_two_sided_ideal is admitted", lambda _: A().ParentMethods.principal_two_sided_ideal),
    (
        "Algebras(ZZ).Constructors().free_algebra_from_set({x, y}) is an algebra with basis",
        lambda _: A().Constructors().free_algebra_from_set(Sets().Constructors().FiniteEnumeratedSet(["x", "y"]))
        in A().WithBasis(),
    ),
    (
        "Algebras(ZZ).Constructors().free_algebra_from_magma constructs Sage magmatic algebra before the project target gap",
        lambda _: A().Constructors().free_algebra_from_magma(Magmas().example()) in A(),
    ),
    (
        "Algebras(ZZ).Constructors().free_algebra_from_semigroup constructs Sage associative algebra before the project target gap",
        lambda _: A().Constructors().free_algebra_from_semigroup(Semigroups().example()) in A(),
    ),
    (
        "Algebras(ZZ).Constructors().free_algebra_from_monoid(Z/3Z) executes the Sage monoid-algebra route",
        lambda _: A().Constructors().free_algebra_from_monoid(multiplicative_monoid_source()) in A().WithBasis(),
    ),
    (
        "Algebras(ZZ).Constructors().free_algebra_from_group(C3) executes the Sage group-algebra route",
        lambda _: A().Constructors().free_algebra_from_group(multiplicative_group_source()) in A().WithBasis(),
    ),
    (
        "Algebras(ZZ).Constructors().free_algebra_from_additive_semigroup constructs Sage associative algebra before the project target gap",
        lambda _: A().Constructors().free_algebra_from_additive_semigroup(additive_source()) in A(),
    ),
    (
        "Algebras(ZZ).Constructors().free_algebra_from_additive_monoid(GF(3), +) executes the Sage additive-monoid route",
        lambda _: A().Constructors().free_algebra_from_additive_monoid(additive_source()) in A().WithBasis(),
    ),
    (
        "Algebras(ZZ).Constructors().free_algebra_from_additive_group(GF(3), +) executes the Sage additive-group route",
        lambda _: A().Constructors().free_algebra_from_additive_group(additive_source()) in A().WithBasis(),
    ),
    (
        "Algebras(ZZ).Constructors().from_multiplication_tensor is wired to the project tensor surface",
        lambda _: A().Constructors().from_multiplication_tensor(multiplication_tensor()) in A(),
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)

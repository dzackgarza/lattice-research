r"""Smoke surface for the category-of-categories subtree."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Cat
from category_specs.algebras import Algebras
from category_specs.modules import Modules
from category_specs.rings import Rings
from category_specs.sets import Sets
from category_specs.topological_spaces import TopologicalSpaces
from sage.all import ZZ
from sage.categories.functor import IdentityFunctor


failures = []


def smoke_case(label, build):
    try:
        build()
    except Exception as exc:
        failures.append(f"{label}: {type(exc).__name__}: {exc}")


def require(condition):
    if not condition:
        raise AssertionError("condition failed")


C = Cat()
registered_roots = (Cat(), Sets(), Rings(), Modules(ZZ), Algebras(ZZ), TopologicalSpaces())

smoke_case("Cat singleton", lambda: Cat())
smoke_case("Cat constructor namespace", lambda: C.Constructors())
smoke_case("Sets() is an object of Cat()", lambda: require(Sets() in C))
smoke_case("Sets().Finite() is an object of Cat()", lambda: require(Sets().Finite() in C))
smoke_case("ordinary Sage objects are not objects of Cat()", lambda: require(ZZ not in C))
smoke_case("functors are not objects of Cat()", lambda: require(IdentityFunctor(Sets()) not in C))

for category in registered_roots:
    smoke_case(f"{category} is an object of Cat()", lambda category=category: require(category in C))
    smoke_case(
        f"{category}.Subobjects() uses Cat registration",
        lambda category=category: require(
            category.Subobjects() is Cat.construction_class(category, "Subobjects").category_of(category)
        ),
    )

smoke_case("Modules(ZZ).OverPID().Subobjects() uses registered base", lambda: Modules(ZZ).OverPID().Subobjects())
smoke_case("Cat().Subobjects()", lambda: C.Subobjects())
smoke_case("Cat().Quotients()", lambda: C.Quotients())
smoke_case("Cat().Subquotients()", lambda: C.Subquotients())
smoke_case("Cat().ObjectsOver(Sets())", lambda: C.ObjectsOver(Sets()))
smoke_case("Cat().ObjectsUnder(Sets())", lambda: C.ObjectsUnder(Sets()))
smoke_case("Cat().CartesianProducts()", lambda: C.CartesianProducts())
smoke_case("Cat().Homsets()", lambda: C.Homsets())
smoke_case("Cat().Endsets()", lambda: C.Endsets())
smoke_case("Cat().Autsets()", lambda: C.Autsets())

assert not failures, "\n".join(failures)

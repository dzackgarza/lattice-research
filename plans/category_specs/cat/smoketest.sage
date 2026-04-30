r"""Mathematical smoke surface for the category-of-categories subtree.

This file exercises category behavior, not implementation internals.  It should
instantiate the category constructions this subtree claims to expose and let
missing or miswired implementations fail naturally.
"""

import pathlib
import sys
import traceback

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Category, Cat
from category_specs.homsets import Homsets as GenericHomsets
from category_specs.algebras import Algebras
from category_specs.modules import Modules
from category_specs.posets import Posets
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
        trace = traceback.format_exc(limit=8)
        failures.append(f"{label}: {type(exc).__name__}: {exc}\n{trace}")


def require(condition, label="condition failed"):
    if not condition:
        raise AssertionError(label)


def require_subobject_category(category):
    subobjects = category.Subobjects()
    require(subobjects in C)


def require_homset_categories(category):
    require(category.Homsets() in C, f"{category}.Homsets() not in Cat()")
    require(category.Endsets() in C, f"{category}.Endsets() not in Cat()")
    require(category.Autsets() in C, f"{category}.Autsets() not in Cat()")
    require(category.Hom() in C, f"{category}.Hom() not in Cat()")
    require(category.End() in C, f"{category}.End() not in Cat()")
    require(category.Aut() in C, f"{category}.Aut() not in Cat()")


def require_object_hom(category):
    homset = category.Hom(category)
    require(homset.domain() is category, f"{category}.Hom({category}).domain() mismatch: {homset.domain()!r}")
    require(homset.codomain() is category, f"{category}.Hom({category}).codomain() mismatch: {homset.codomain()!r}")


def require_cat_constructions(category):
    require(category.Subobjects() in C)
    require(category.Quotients() in C)
    require(category.Subquotients() in C)
    require(category.ObjectsOver(Sets()) in C)
    require(category.ObjectsUnder(Sets()) in C)
    require(category.CartesianProducts() in C)


C = Cat()
category_objects = (Sets(), Rings(), Modules(ZZ), Algebras(ZZ), TopologicalSpaces())
joined_category = Category.join([Rings(), Posets()])
empty_category = C.Constructors().EmptyCategory()

smoke_case("Cat singleton", lambda: Cat())
smoke_case("Cat() is not an object of itself", lambda: require(C not in C))
smoke_case("singleton category positional reconstruction", lambda: require(Sets() is Sets().__class__()))
smoke_case("singleton axiom category passes Sage axiom test", lambda: Sets().Finite()._test_category_with_axiom())
smoke_case("base-ring category positional reconstruction", lambda: require(Modules(ZZ) is Modules(ZZ).__class__(ZZ)))
smoke_case("axiom category positional reconstruction", lambda: require(Sets().Finite() is Sets().Finite().__class__(Sets())))
smoke_case(
    "generic homsets positional reconstruction",
    lambda: require(GenericHomsets().Of(Cat()) is GenericHomsets().Of(Cat()).__class__(Cat())),
)
smoke_case("Cat constructor namespace", lambda: C.Constructors())
smoke_case("Cat().Constructors().EmptyCategory()", lambda: C.Constructors().EmptyCategory())
smoke_case("EmptyCategory() is an object of Cat()", lambda: require(empty_category in C))
smoke_case("EmptyCategory() is empty", lambda: require(Sets() not in empty_category and ZZ not in empty_category))
smoke_case("EmptyCategory() is below Sets()", lambda: require(empty_category.is_subcategory(Sets())))
smoke_case("EmptyCategory() is below Rings()", lambda: require(empty_category.is_subcategory(Rings())))
smoke_case("ordinary categories are not below EmptyCategory()", lambda: require(not Sets().is_subcategory(empty_category)))
smoke_case("Cat().meet([]) is EmptyCategory()", lambda: require(C.meet([]) is empty_category))
smoke_case("Cat().join(...) returns a join category", lambda: require(C.join([Rings(), Posets()]) in C.JoinCategories()))
smoke_case(
    "Cat().meet(...) delegates to Sage category meet",
    lambda: require(C.meet([Rings(), Posets()]) == Category.meet([Rings(), Posets()])),
)
smoke_case(
    "Cat().JoinCategories() recognizes Sage join categories",
    lambda: require(joined_category in C.JoinCategories() and Sets() not in C.JoinCategories()),
)
smoke_case("join category is recognized through Cat surface", lambda: require(joined_category in C.JoinCategories()))
smoke_case("ordinary category predicate rejects join category", lambda: require(not Sets().is_join_category()))
smoke_case("functors are not objects of Cat()", lambda: require(IdentityFunctor(Sets()) not in C))
smoke_case(
    "HomsetsOf join category repr uses Cat join-category surface",
    lambda: require(GenericHomsets().Of(joined_category)._repr_object_names() == "homsets of rings and posets"),
)
smoke_case("Sets() is an object of Cat()", lambda: require(Sets() in C))
smoke_case("Sets().Finite() is an object of Cat()", lambda: require(Sets().Finite() in C))
smoke_case("ordinary Sage objects are not objects of Cat()", lambda: require(ZZ not in C))
for category in category_objects:
    smoke_case(f"{category} is an object of Cat()", lambda category=category: require(category in C))
    smoke_case(
        f"{category}.Subobjects() constructs a category",
        lambda category=category: require_subobject_category(category),
    )
    smoke_case(
        f"{category}.Homsets/Endsets/Autsets/Hom/End/Aut construct categories",
        lambda category=category: require_homset_categories(category),
    )
    smoke_case(
        f"{category}.Hom({category}) constructs the object-level homspace",
        lambda category=category: require_object_hom(category),
    )

smoke_case("Modules(ZZ).OverPID().Subobjects()", lambda: Modules(ZZ).OverPID().Subobjects())
smoke_case("Modules(ZZ).OverPID() is an object of Cat()", lambda: require(Modules(ZZ).OverPID() in C))
smoke_case(
    "Modules(ZZ).OverPID() refines Modules(ZZ)",
    lambda: require(Modules(ZZ).OverPID().is_subcategory(Modules(ZZ))),
)
smoke_case("Sets().Hom(Sets()) has the expected domain", lambda: require(Sets().Hom(Sets()).domain() is Sets()))
smoke_case("Sets().Hom(Sets()) has the expected codomain", lambda: require(Sets().Hom(Sets()).codomain() is Sets()))
smoke_case("Cat().Subobjects()", lambda: C.Subobjects())
smoke_case("Cat().Quotients()", lambda: C.Quotients())
smoke_case("Cat().Subquotients()", lambda: C.Subquotients())
smoke_case("Cat().ObjectsOver(Sets())", lambda: C.ObjectsOver(Sets()))
smoke_case("Cat().ObjectsUnder(Sets())", lambda: C.ObjectsUnder(Sets()))
smoke_case("Cat().CartesianProducts()", lambda: C.CartesianProducts())
smoke_case("Cat().Homsets()", lambda: C.Homsets())
smoke_case("Cat().Endsets()", lambda: C.Endsets())
smoke_case("Cat().Autsets()", lambda: C.Autsets())
smoke_case("Cat().Hom()", lambda: C.Hom())
smoke_case("Cat().End()", lambda: C.End())
smoke_case("Cat().Aut()", lambda: C.Aut())
smoke_case("Cat constructions are category objects", lambda: require_cat_constructions(C))

assert not failures, "\n".join(failures)

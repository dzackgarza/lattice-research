r"""Mathematical smoke surface for the generic homsets subtree."""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.cat import Cat
from category_specs.homsets import Autsets, Endsets, Homsets
from category_specs.modules import Modules
from category_specs.posets import Posets
from category_specs.rings import Rings
from category_specs.sets import Sets
from category_specs.topological_spaces import TopologicalSpaces
from sage.all import ZZ


failures = []


def require(condition, label="condition failed"):
    if not condition:
        raise AssertionError(label)


def subcategory_label(left, right):
    super_categories = left.super_categories()
    super_details = [
        f"{super_category!r} ({super_category.__class__!r}, is target: {super_category is right})"
        for super_category in super_categories
    ]
    return f"{left} not below {right} ({right.__class__!r}); immediate supercategories: {super_details}"


def has_declared_supercategory(left, right, seen=None):
    seen = set() if seen is None else seen
    if left is right:
        return True
    if id(left) in seen:
        return False
    seen.add(id(left))
    return any(has_declared_supercategory(super_category, right, seen) for super_category in left.super_categories())


def smoke_case(label, build):
    try:
        build()
    except Exception as exc:
        failures.append(f"{label}: {type(exc).__name__}: {exc}")


def require_root_homsets():
    require(Homsets() in Cat())
    require(Homsets().Endset() in Cat())
    require(Homsets().Autset() in Cat())
    require(Homsets().Of(Cat()) in Cat())
    require(Endsets().Of(Cat()) in Cat())
    require(Autsets().Of(Cat()) in Cat())


def require_category_homsets(category):
    homsets = category.Homsets()
    endsets = homsets.Endset()
    autsets = homsets.Autset()
    require(homsets in Cat(), f"{homsets} is not an object of Cat()")
    require(endsets in Cat(), f"{endsets} is not an object of Cat()")
    require(autsets in Cat(), f"{autsets} is not an object of Cat()")
    require(Endsets().Of(category) is endsets, f"Endsets().Of({category}) did not route through Homsets().Endset()")
    require(Autsets().Of(category) is autsets, f"Autsets().Of({category}) did not route through Endset().Autset()")


def require_set_enriched_homsets(category):
    homsets = category.Homsets()
    endsets = homsets.Endset()
    autsets = homsets.Autset()
    set_homsets = Sets().Homsets()
    set_endsets = set_homsets.Endset()
    set_autsets = set_homsets.Autset()
    require(has_declared_supercategory(homsets, set_homsets), subcategory_label(homsets, set_homsets))
    require(has_declared_supercategory(endsets, set_endsets), subcategory_label(endsets, set_endsets))
    require(has_declared_supercategory(autsets, set_autsets), subcategory_label(autsets, set_autsets))


C = Cat()
H = C.Hom()
E = C.End()
A = C.Aut()

smoke_case("root homsets/endsets/autsets are category objects", require_root_homsets)
smoke_case("Cat().Hom/End/Aut route to category-level constructions", lambda: require(H is C.Homsets()))
smoke_case("Cat().End() routes through Cat().Hom().Endset()", lambda: require(E is H.Endset()))
smoke_case("Cat().Aut() routes through Cat().End().Autset()", lambda: require(A is E.Autset()))

set_like_categories = (Sets(), Rings(), Posets(), TopologicalSpaces(), Modules(ZZ))
for category in set_like_categories:
    smoke_case(f"{category}.Homsets/Endsets/Autsets are category objects", lambda category=category: require_category_homsets(category))
    smoke_case(f"{category}.Homsets/Endsets/Autsets refine set homsets", lambda category=category: require_set_enriched_homsets(category))

assert not failures, "\n".join(failures)

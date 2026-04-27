r"""Smoke surface for the generic homsets subtree."""

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
from sage.misc.abstract_method import AbstractMethod


failures = []
PROJECT_MODULE_PREFIX = "category_specs."


def require(condition, label="condition failed"):
    if not condition:
        raise AssertionError(label)


def require_methods(category, method_names):
    for method_name in method_names:
        require(hasattr(category.element_class, method_name), f"{category} lacks element method {method_name}")


def method_owner(cls, method_name):
    for owner in cls.__mro__:
        if method_name in owner.__dict__:
            return owner
    return None


def require_provider_method(mixed_class, provider_class, method_name):
    require(provider_class in mixed_class.__mro__, f"{mixed_class} does not mix in {provider_class}")
    require(method_name in provider_class.__dict__, f"{provider_class} does not declare {method_name}")
    owner = method_owner(mixed_class, method_name)
    require(owner is provider_class, f"{mixed_class}.{method_name} resolves from {owner}, expected {provider_class}")


def require_no_reabstracted_methods(category, mixed_class):
    owners_by_name = {}
    for cls in mixed_class.__mro__:
        if not getattr(cls, "__module__", "").startswith(PROJECT_MODULE_PREFIX):
            continue
        for name, attr in cls.__dict__.items():
            if isinstance(attr, AbstractMethod):
                owners_by_name.setdefault(name, []).append(cls)
    collisions = {
        name: owners
        for name, owners in owners_by_name.items()
        if len(owners) > 1
    }
    details = ", ".join(
        f"{name}: {' > '.join(owner.__name__ for owner in owners)}"
        for name, owners in sorted(collisions.items())
    )
    require(not collisions, f"{category} re-declares abstract method(s): {details}")


def require_clean_method_mixins(category):
    require_no_reabstracted_methods(category, category.parent_class)
    require_no_reabstracted_methods(category, category.element_class)


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


Homsets()
Homsets().Endset()
Homsets().Autset()
Homsets().Of(Cat())
Endsets().Of(Cat())
Autsets().Of(Cat())

C = Cat()
H = C.Hom()
E = C.End()
A = C.Aut()

require(H is C.Homsets())
require(E is C.Endsets())
require(A is C.Autsets())
require(E is H.Endset())
require(A is E.Autset())
require(hasattr(Homsets.ElementMethods, "is_endomorphism"))
require(not hasattr(Homsets.ElementMethods, "is_injective"))
require(not hasattr(Autsets.ElementMethods, "is_injective"))

generic_morphism_methods = (
    "is_endomorphism",
    "is_invertible",
    "is_isomorphism",
    "is_automorphism",
)
set_map_methods = (
    "pre_image",
    "is_injective",
    "is_surjective",
    "is_bijective",
)

set_like_categories = (Sets(), Rings(), Posets(), TopologicalSpaces(), Modules(ZZ))
for category in set_like_categories:
    homsets = category.Homsets()
    endsets = homsets.Endset()
    autsets = homsets.Autset()
    set_homsets = Sets().Homsets()
    set_endsets = set_homsets.Endset()
    set_autsets = set_homsets.Autset()

    require(has_declared_supercategory(homsets, set_homsets), subcategory_label(homsets, set_homsets))
    require(has_declared_supercategory(endsets, set_endsets), subcategory_label(endsets, set_endsets))
    require(has_declared_supercategory(autsets, set_autsets), subcategory_label(autsets, set_autsets))
    for hom_category in (homsets, endsets, autsets):
        require_clean_method_mixins(hom_category)
        require_methods(hom_category, generic_morphism_methods)
        require_methods(hom_category, set_map_methods)

module_homsets = Modules(ZZ).Homsets()
module_element_class = module_homsets.element_class
require_provider_method(module_element_class, Homsets().element_class, "is_endomorphism")
require_provider_method(module_element_class, Sets().Homsets().element_class, "is_injective")
require_provider_method(module_element_class, module_homsets.element_class, "kernel")
require_provider_method(module_element_class, module_homsets.element_class, "evaluate")
require_provider_method(module_homsets.parent_class, Homsets().parent_class, "domain")
require_provider_method(module_homsets.parent_class, module_homsets.parent_class, "natural_morphism")

assert not failures, "\n".join(failures)

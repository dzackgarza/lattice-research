from __future__ import annotations

import pathlib
import sys
from abc import ABCMeta

from sage.all import ZZ
from sage.categories.category import Category

ROOT = pathlib.Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.lattices import Lattices
from category_specs.lattices.homsets import LatticeHomCategory as SpecLatticeHomCategory
from category_specs.modules import Modules
from src.lattices.category import (
    Lattice,
    LatticeAutCategory,
    LatticeAutomorphismMethods,
    LatticeCategory,
    LatticeElementMethods,
    LatticeEndCategory,
    LatticeEndomorphismMethods,
    LatticeHomCategory,
    LatticeHomParentMethods,
    LatticeMorphismMethods,
    LatticeParentMethods,
)


def method_names(provider: type) -> set[str]:
    return {
        name
        for name, value in vars(provider).items()
        if callable(value) or isinstance(value, (classmethod, staticmethod, property))
    }


def is_abstract_method(provider: type, name: str) -> bool:
    value = vars(provider)[name]
    return bool(getattr(value, "__isabstractmethod__", False))


C = Lattice(ZZ)

assert isinstance(C, LatticeCategory)
assert isinstance(C, Category)
assert C.base_ring() == ZZ
assert Lattices(ZZ) in C.super_categories()

assert C.ParentMethods is LatticeParentMethods
assert C.ElementMethods is LatticeElementMethods
assert C.HomCategory is LatticeHomCategory

assert {
    "gram_matrix",
    "rank",
    "gens",
    "b",
    "q",
    "dual_lattice",
    "discriminant_group",
    "orthogonal_group",
}.issubset(method_names(LatticeParentMethods))
assert is_abstract_method(LatticeParentMethods, "gram_matrix")
assert is_abstract_method(LatticeParentMethods, "b")

assert {
    "parent",
    "to_vector",
    "b",
    "q",
    "perp",
}.issubset(method_names(LatticeElementMethods))
assert is_abstract_method(LatticeElementMethods, "to_vector")

HC = C.HomCategory()
assert isinstance(HC, LatticeHomCategory)
assert SpecLatticeHomCategory(Lattices(ZZ)) in HC.extra_super_categories()
assert Modules(ZZ).HomCategory() in HC.extra_super_categories()
assert HC.ParentMethods is LatticeHomParentMethods
assert HC.ElementMethods is LatticeMorphismMethods
assert HC.Endset is LatticeEndCategory

assert {
    "domain",
    "codomain",
    "from_matrix",
    "from_images",
    "identity",
    "zero",
}.issubset(method_names(LatticeHomParentMethods))
assert is_abstract_method(LatticeHomParentMethods, "from_matrix")
assert is_abstract_method(LatticeHomParentMethods, "from_images")

assert {
    "domain",
    "codomain",
    "__call__",
    "to_matrix",
    "is_isometry",
    "is_form_preserving",
}.issubset(method_names(LatticeMorphismMethods))
assert is_abstract_method(LatticeMorphismMethods, "to_matrix")
assert is_abstract_method(LatticeMorphismMethods, "__call__")

assert isinstance(LatticeParentMethods, ABCMeta)
assert isinstance(LatticeElementMethods, ABCMeta)
assert isinstance(LatticeHomParentMethods, ABCMeta)
assert isinstance(LatticeMorphismMethods, ABCMeta)

EC = HC.EndCategory()
assert isinstance(EC, LatticeEndCategory)
assert EC.ElementMethods is LatticeEndomorphismMethods
assert EC.Autset is LatticeAutCategory

AC = EC.AutCategory()
assert isinstance(AC, LatticeAutCategory)
assert AC.ElementMethods is LatticeAutomorphismMethods

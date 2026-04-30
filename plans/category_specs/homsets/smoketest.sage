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
from category_specs.utils import assert_smoke_statements
from sage.all import ZZ


C = Cat()

SMOKE_STATEMENTS = (
    ("Homsets() is a category", lambda _: Homsets() in C),
    ("Homsets().Endset() is a category", lambda _: Homsets().Endset() in C),
    ("Homsets().Autset() is a category", lambda _: Homsets().Autset() in C),
    ("Homsets().Of(Cat()) is a category", lambda _: Homsets().Of(Cat()) in C),
    ("Endsets().Of(Cat()) is a category", lambda _: Endsets().Of(Cat()) in C),
    ("Autsets().Of(Cat()) is a category", lambda _: Autsets().Of(Cat()) in C),
    ("Cat().Hom() is Cat().Homsets()", lambda _: C.Hom() is C.Homsets()),
    ("Cat().End() is Cat().Hom().Endset()", lambda _: C.End() is C.Hom().Endset()),
    ("Cat().Aut() is Cat().End().Autset()", lambda _: C.Aut() is C.End().Autset()),
    ("Sets().Homsets() is a category", lambda _: Sets().Homsets() in C),
    ("Sets().Homsets().Endset() is a category", lambda _: Sets().Homsets().Endset() in C),
    ("Sets().Homsets().Endset().Autset() is a category", lambda _: Sets().Homsets().Endset().Autset() in C),
    ("Endsets().Of(Sets()) is Sets().Homsets().Endset()", lambda _: Endsets().Of(Sets()) is Sets().Homsets().Endset()),
    ("Autsets().Of(Sets()) is Sets().Homsets().Endset().Autset()", lambda _: Autsets().Of(Sets()) is Sets().Homsets().Endset().Autset()),
    ("Sets().Homsets() refines set homsets", lambda _: Sets().Homsets().is_subcategory(Sets().Homsets())),
    ("Sets().Endsets() refines set endsets", lambda _: Sets().Endsets().is_subcategory(Sets().Homsets().Endset())),
    ("Sets().Autsets() refines set autsets", lambda _: Sets().Autsets().is_subcategory(Sets().Homsets().Endset().Autset())),
    ("Rings().Homsets() is a category", lambda _: Rings().Homsets() in C),
    ("Rings().Homsets().Endset() is a category", lambda _: Rings().Homsets().Endset() in C),
    ("Rings().Homsets().Endset().Autset() is a category", lambda _: Rings().Homsets().Endset().Autset() in C),
    ("Endsets().Of(Rings()) is Rings().Homsets().Endset()", lambda _: Endsets().Of(Rings()) is Rings().Homsets().Endset()),
    ("Autsets().Of(Rings()) is Rings().Homsets().Endset().Autset()", lambda _: Autsets().Of(Rings()) is Rings().Homsets().Endset().Autset()),
    ("Rings().Homsets() refines set homsets", lambda _: Rings().Homsets().is_subcategory(Sets().Homsets())),
    ("Rings().Endsets() refines set endsets", lambda _: Rings().Endsets().is_subcategory(Sets().Homsets().Endset())),
    ("Rings().Autsets() refines set autsets", lambda _: Rings().Autsets().is_subcategory(Sets().Homsets().Endset().Autset())),
    ("Posets().Homsets() is a category", lambda _: Posets().Homsets() in C),
    ("Posets().Homsets().Endset() is a category", lambda _: Posets().Homsets().Endset() in C),
    ("Posets().Homsets().Endset().Autset() is a category", lambda _: Posets().Homsets().Endset().Autset() in C),
    ("Endsets().Of(Posets()) is Posets().Homsets().Endset()", lambda _: Endsets().Of(Posets()) is Posets().Homsets().Endset()),
    ("Autsets().Of(Posets()) is Posets().Homsets().Endset().Autset()", lambda _: Autsets().Of(Posets()) is Posets().Homsets().Endset().Autset()),
    ("Posets().Homsets() refines set homsets", lambda _: Posets().Homsets().is_subcategory(Sets().Homsets())),
    ("Posets().Endsets() refines set endsets", lambda _: Posets().Endsets().is_subcategory(Sets().Homsets().Endset())),
    ("Posets().Autsets() refines set autsets", lambda _: Posets().Autsets().is_subcategory(Sets().Homsets().Endset().Autset())),
    ("TopologicalSpaces().Homsets() is a category", lambda _: TopologicalSpaces().Homsets() in C),
    ("TopologicalSpaces().Homsets().Endset() is a category", lambda _: TopologicalSpaces().Homsets().Endset() in C),
    ("TopologicalSpaces().Homsets().Endset().Autset() is a category", lambda _: TopologicalSpaces().Homsets().Endset().Autset() in C),
    (
        "Endsets().Of(TopologicalSpaces()) is TopologicalSpaces().Homsets().Endset()",
        lambda _: Endsets().Of(TopologicalSpaces()) is TopologicalSpaces().Homsets().Endset(),
    ),
    (
        "Autsets().Of(TopologicalSpaces()) is TopologicalSpaces().Homsets().Endset().Autset()",
        lambda _: Autsets().Of(TopologicalSpaces()) is TopologicalSpaces().Homsets().Endset().Autset(),
    ),
    (
        "TopologicalSpaces().Homsets() refines set homsets",
        lambda _: TopologicalSpaces().Homsets().is_subcategory(Sets().Homsets()),
    ),
    (
        "TopologicalSpaces().Endsets() refines set endsets",
        lambda _: TopologicalSpaces().Endsets().is_subcategory(Sets().Homsets().Endset()),
    ),
    (
        "TopologicalSpaces().Autsets() refines set autsets",
        lambda _: TopologicalSpaces().Autsets().is_subcategory(Sets().Homsets().Endset().Autset()),
    ),
    ("Modules(ZZ).Homsets() is a category", lambda _: Modules(ZZ).Homsets() in C),
    ("Modules(ZZ).Homsets().Endset() is a category", lambda _: Modules(ZZ).Homsets().Endset() in C),
    ("Modules(ZZ).Homsets().Endset().Autset() is a category", lambda _: Modules(ZZ).Homsets().Endset().Autset() in C),
    ("Endsets().Of(Modules(ZZ)) is Modules(ZZ).Homsets().Endset()", lambda _: Endsets().Of(Modules(ZZ)) is Modules(ZZ).Homsets().Endset()),
    (
        "Autsets().Of(Modules(ZZ)) is Modules(ZZ).Homsets().Endset().Autset()",
        lambda _: Autsets().Of(Modules(ZZ)) is Modules(ZZ).Homsets().Endset().Autset(),
    ),
    ("Modules(ZZ).Homsets() refines set homsets", lambda _: Modules(ZZ).Homsets().is_subcategory(Sets().Homsets())),
    ("Modules(ZZ).Endsets() refines set endsets", lambda _: Modules(ZZ).Endsets().is_subcategory(Sets().Homsets().Endset())),
    ("Modules(ZZ).Autsets() refines set autsets", lambda _: Modules(ZZ).Autsets().is_subcategory(Sets().Homsets().Endset().Autset())),
)

assert_smoke_statements(SMOKE_STATEMENTS)

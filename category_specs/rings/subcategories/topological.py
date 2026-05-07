r"""TopologicalRings ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.rings import Rings as SageRings
from sage.misc.lazy_import import LazyImport
from sage.misc.cachefunc import cached_method

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ...topological_spaces import TopologicalSpaceRuntimeGapObjectMethods
from ...topological_spaces import TopologicalSpaces
from .. import Rings

from ._lazy_subcategories import _CompleteRings

if TYPE_CHECKING:
    pass


class _TopologicalRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Topological()``."""

    _base_category_class_and_axiom = (Rings, "Topological")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "topological rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageRings().Topological(), TopologicalSpaces(), Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageRings().Topological() or (
            R in self.base_category() and R.is_topological_ring()
        )

    Complete = LazyImport(
        "category_specs.rings.subcategories.complete", "_CompleteRings"
    )

    class SubcategoryMethods:
        @cached_method
        @final
        def Complete(self) -> Category:
            return self._with_axiom("Complete")

    class ParentMethods:
        _missing_topology_adapter = (
            TopologicalSpaceRuntimeGapObjectMethods._missing_topology_adapter
        )
        is_connected = TopologicalSpaceRuntimeGapObjectMethods.is_connected
        closure = TopologicalSpaceRuntimeGapObjectMethods.closure
        interior = TopologicalSpaceRuntimeGapObjectMethods.interior
        boundary = TopologicalSpaceRuntimeGapObjectMethods.boundary
        is_open = TopologicalSpaceRuntimeGapObjectMethods.is_open
        is_closed = TopologicalSpaceRuntimeGapObjectMethods.is_closed
        is_compact = TopologicalSpaceRuntimeGapObjectMethods.is_compact

        @override
        @final
        def is_topological_ring(self) -> bool:
            return True

    class ElementMethods: ...

    class MorphismMethods: ...

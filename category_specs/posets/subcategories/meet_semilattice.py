r"""Order-theoretic meet-semilattice poset subcategory."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, final, overload, override

from sage.misc.lazy_import import LazyImport

from ...cat import Category
from .. import Posets

if TYPE_CHECKING:
    from ...types import PosetElement

if TYPE_CHECKING:
    def foldable_operation[MethodT: Callable[..., object]](
        function: MethodT,
    ) -> MethodT: ...

    def cached_method[MethodT: Callable[..., object]](method: MethodT) -> MethodT: ...
else:
    from sage.misc.cachefunc import cached_method

    from ...utils import foldable_operation


class _MeetSemilatticePosets(Category):
    r"""Posets in which every pair has a meet.

    Canonical chain: ``Posets().MeetSemilattice()``.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return posets as the strict supercategory of meet-semilattices."""
        return [Posets()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Finite(self) -> Category:
            r"""Return the finite meet-semilattice subcategory."""
            return self._with_axiom("Finite")

    Finite = LazyImport(
        "category_specs.posets.subcategories.finite_meet_semilattice",
        "_FiniteMeetSemilatticePosets",
    )

    class ParentMethods:
        @overload
        def meet(self, x: PosetElement, y: PosetElement) -> PosetElement: ...

        @overload
        def meet(self, elements: Sequence[PosetElement]) -> PosetElement: ...

        @abstractmethod
        @foldable_operation
        def meet(self, x: PosetElement, y: PosetElement) -> PosetElement:
            r"""Return the greatest lower bound of ``x`` and ``y``.

            ``MeetSemilattice`` introduces ``meet`` as the primitive binary
            operation; the sequence overload folds this binary operation.
            """
            ...

    class ElementMethods: ...

    class MorphismMethods: ...

r"""Slice construction category of algebras over a fixed algebra."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Algebra, AlgebraMorphism


class _ObjectsOver(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Algebras ``B`` equipped with an algebra morphism ``B -> A``.

    Canonical chain: ``Algebras(R).ObjectsOver(T)``.
    """

    _functor_category = "ObjectsOver"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"algebras over {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_algebra(self) -> Algebra:
            r"""Return the target algebra of this object-over structure."""
            ...

        @abstract_method
        def structure_map(self) -> AlgebraMorphism:
            r"""Return the algebra morphism from this algebra to the target."""
            ...

        @final
        def structure_domain(self) -> Algebra:
            r"""Return the domain algebra of the structure map."""
            return self

        @final
        def structure_codomain(self) -> Algebra:
            r"""Return the codomain algebra of the structure map."""
            return self.structure_algebra()

    class ElementMethods: ...
    class MorphismMethods: ...

r"""Slice construction category of algebras under a fixed algebra."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method

from ....cat import Category_over_base, RegressiveCovariantConstructionCategory

if TYPE_CHECKING:
    from ....types import Algebra, AlgebraMorphism


class _ObjectsUnder(RegressiveCovariantConstructionCategory, Category_over_base):
    r"""Algebras ``B`` equipped with an algebra morphism ``A -> B``.

    Canonical chain: ``Algebras(R).ObjectsUnder(T)``.
    """

    _functor_category = "ObjectsUnder"

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"algebras under {self.base()}"

    class ParentMethods:
        @abstract_method
        def structure_algebra(self) -> Algebra:
            r"""Return the source algebra of this object-under structure."""
            ...

        @abstract_method
        def structure_map(self) -> AlgebraMorphism:
            r"""Return the algebra morphism from the source to this algebra."""
            ...

        @final
        def structure_domain(self) -> Algebra:
            r"""Return the domain algebra of the structure map."""
            return self.structure_algebra()

        @final
        def structure_codomain(self) -> Algebra:
            r"""Return the codomain algebra of the structure map."""
            return self

    class ElementMethods: ...
    class MorphismMethods: ...

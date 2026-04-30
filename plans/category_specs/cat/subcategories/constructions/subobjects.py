r"""Subobject construction category for categories."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.misc.abstract_method import abstract_method

from ... import SubobjectsCategory

if TYPE_CHECKING:
    from ....types import Category, CategoryObject


class _Subobjects(SubobjectsCategory):
    r"""Subcategories viewed as subobjects in ``Cat()``."""

    @final
    def __contains__(self, candidate: Any) -> bool:
        r"""Return whether ``candidate`` is registered as a subcategory object."""
        from ... import Cat

        if candidate not in Cat():
            return False
        if not hasattr(candidate, "ambient_category"):
            return False
        if not hasattr(candidate, "defining_predicates"):
            return False
        ambient = candidate.ambient_category()
        predicates = candidate.defining_predicates()
        return ambient in Cat() and candidate.is_subcategory(ambient) and bool(predicates)

    class ParentMethods:
        @abstract_method
        def ambient_category(self) -> Category:
            r"""Return the category in which this subcategory is defined."""
            ...

        @abstract_method
        def defining_predicates(self) -> tuple[str, ...]:
            r"""Return the object predicates defining this full subcategory."""
            ...

        @abstract_method
        def defining_predicate(self, candidate: CategoryObject) -> bool:
            r"""Return whether ``candidate`` satisfies all defining predicates."""
            ...

    class ElementMethods: ...
    class MorphismMethods: ...


Subcategories = _Subobjects

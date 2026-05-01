r"""Ring objects regarded as modules."""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.misc.abstract_method import abstract_method

from ...cat import Category_over_base_ring
from .. import Modules

if TYPE_CHECKING:
    from ...types import Ring, RingMorphism, RModuleElement



class _RingObjectsAsModules(Category_over_base_ring):
    r"""Ring objects regarded as modules over their structure ring."""

    @final
    def super_categories(self):
        R = self.base_ring()
        return [Modules(R)]

    class ParentMethods:
        @final
        def is_ring_object_as_module(self) -> bool:
            return True

        @abstract_method
        def structure_ring(self) -> Ring: ...

        @abstract_method
        def structure_map(self) -> RingMorphism: ...

        @abstract_method
        def module_generators(self) -> tuple[RModuleElement, ...]: ...

    class ElementMethods: ...
    class MorphismMethods: ...

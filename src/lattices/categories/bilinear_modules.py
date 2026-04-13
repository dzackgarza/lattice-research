from __future__ import annotations

from sage.categories.category_types import Category_module
from sage.categories.homsets import HomsetsCategory
from sage.categories.modules import Modules
from sage.misc.cachefunc import cached_method


class BilinearModules(Category_module):
    def super_categories(self):
        return [Modules(self.base_ring())]

    def additional_structure(self):
        return None

    class ParentMethods:
        def _Hom_(self, codomain, category=None):
            from src.lattices.core.integral import Lattice
            from src.lattices.core.rational import RationalLattice
            from src.lattices.morphisms.homspaces import BilinearModuleHomSpace, LatticeHomSpace, RationalLatticeHomSpace

            if isinstance(self, Lattice) and isinstance(codomain, Lattice):
                return LatticeHomSpace(self, codomain, category=category)
            if isinstance(self, RationalLattice) and isinstance(codomain, RationalLattice):
                return RationalLatticeHomSpace(self, codomain, category=category)
            return BilinearModuleHomSpace(self, codomain, category=category)

    class Homsets(HomsetsCategory):
        def extra_super_categories(self):
            return [Modules(self.base_category().base_ring())]

        class ParentMethods:
            @cached_method
            def base_ring(self):
                return self.domain().base_ring()

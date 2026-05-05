import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.forms import FormedModules
from category_specs.forms.subcategories.bilinear import BilinearModulesCategory as FormsBilinearModulesCategory
from category_specs.forms.subcategories.quadratic import QuadraticModulesCategory as FormsQuadraticModulesCategory
from category_specs.forms.subcategories.symmetric import (
    SymmetricBilinearModulesCategory as FormsSymmetricBilinearModulesCategory,
)
from category_specs.forms.subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesCategory as FormsTorsionQuadraticModulesCategory,
)
from category_specs.forms.subcategories.with_forms import FormedModulesCategory as FormsWithFormsCategory
from category_specs.lattices.subcategories.symmetric import (
    SymmetricBilinearModulesCategory as LatticeSymmetricBilinearModulesCategory,
)
from category_specs.modules import Modules
from category_specs.modules.subcategories.bilinear import BilinearModulesCategory as ModuleBilinearModulesCategory
from category_specs.modules.subcategories.quadratic import QuadraticModulesCategory as ModuleQuadraticModulesCategory
from category_specs.modules.subcategories.torsion_quadratic_modules import (
    TorsionQuadraticModulesCategory as ModuleTorsionQuadraticModulesCategory,
)
from category_specs.modules.subcategories.with_forms import FormedModulesCategory as ModuleWithFormsCategory
from category_specs.utils import assert_smoke_statements


MZZ = Modules(ZZ, dispatch=False)
FZZ = FormedModules(ZZ)
LATTICE_AMBIENT = MZZ.Free().FiniteRank().WithForms().Bilinear().Symmetric().Nondegenerate().Integral()

SMOKE_STATEMENTS = (
    ("FormedModules(ZZ) is an object of Cat()", lambda _: FZZ in Cat()),
    ("FormedModules(ZZ) is Modules(ZZ).WithForms()", lambda _: FZZ == MZZ.WithForms()),
    ("module WithForms shim resolves to forms owner", lambda _: ModuleWithFormsCategory is FormsWithFormsCategory),
    (
        "module Bilinear shim resolves to forms owner",
        lambda _: ModuleBilinearModulesCategory is FormsBilinearModulesCategory,
    ),
    (
        "module Quadratic shim resolves to forms owner",
        lambda _: ModuleQuadraticModulesCategory is FormsQuadraticModulesCategory,
    ),
    (
        "module TorsionQuadraticModules shim resolves to forms owner",
        lambda _: ModuleTorsionQuadraticModulesCategory is FormsTorsionQuadraticModulesCategory,
    ),
    (
        "lattice symmetric compatibility path resolves to forms owner",
        lambda _: LatticeSymmetricBilinearModulesCategory is FormsSymmetricBilinearModulesCategory,
    ),
    ("FormedModules(ZZ).Bilinear() is below FormedModules(ZZ)", lambda _: FZZ.Bilinear().is_subcategory(FZZ)),
    ("FormedModules(ZZ).Quadratic() is below FormedModules(ZZ)", lambda _: FZZ.Quadratic().is_subcategory(FZZ)),
    (
        "finite-rank lattice ambient chain remains formed-module based",
        lambda _: LATTICE_AMBIENT.is_subcategory(MZZ.Free().FiniteRank().WithForms()),
    ),
)

assert_smoke_statements(SMOKE_STATEMENTS)

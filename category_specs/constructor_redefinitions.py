"""Install top-level Sage constructor redefinitions for category refinement."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from sage.combinat.free_module import (
    CombinatorialFreeModule as _SageCombinatorialFreeModule,
)
from sage.matrix.matrix_space import MatrixSpace as _SageMatrixSpace
from sage.modules.free_module import FreeModule as _SageFreeModule
from sage.modules.free_module import VectorSpace as _SageVectorSpace
from sage.rings.finite_rings.finite_field_constructor import GF as _SageGF
from sage.rings.finite_rings.finite_field_constructor import (
    FiniteField as _SageFiniteField,
)
from sage.rings.finite_rings.integer_mod_ring import (
    IntegerModRing as _SageIntegerModRing,
)
from sage.rings.number_field.number_field import QuadraticField as _SageQuadraticField
from sage.rings.padics.factory import Zp as _SageZp
from sage.rings.polynomial.laurent_polynomial_ring import (
    LaurentPolynomialRing as _SageLaurentPolynomialRing,
)
from sage.rings.polynomial.polynomial_ring_constructor import (
    PolynomialRing as _SagePolynomialRing,
)
from sage.rings.power_series_ring import PowerSeriesRing as _SagePowerSeriesRing

if TYPE_CHECKING:
    from .types import Integer, Matrix, Polynomial, Ring, RingElement, RModule

_INSTALLED = False


def FreeModule(
    base_ring: "Ring",
    rank: "Integer",
    sparse: bool = False,
    *,
    inner_product_matrix: "Matrix | None" = None,
) -> "RModule":
    from .modules import Modules
    from .utils import refine_category

    M = _SageFreeModule(base_ring, rank, sparse, inner_product_matrix)
    return cast(
        "RModule",
        refine_category(
            M,
            [Modules(base_ring).Free().FinitelyPresented().FiniteRank()],
            test=False,
        ),
    )


def VectorSpace(
    base_ring: "Ring",
    dimension: "Integer",
    sparse: bool = False,
    *,
    inner_product_matrix: "Matrix | None" = None,
) -> "RModule":
    from .modules import Modules
    from .utils import refine_category

    M = _SageFreeModule(base_ring, dimension, sparse, inner_product_matrix)
    return cast(
        "RModule",
        refine_category(
            M,
            [
                Modules(base_ring).Free().FinitelyPresented().FiniteRank(),
                Modules(base_ring).OverField(),
            ],
            test=False,
        ),
    )


def MatrixSpace(
    base_ring: "Ring",
    nrows: "Integer",
    ncols: "Integer | None" = None,
    sparse: bool = False,
    implementation: str | type[Any] | None = None,
) -> "RModule":
    from .modules import Modules
    from .utils import refine_category

    if ncols is None:
        ncols = nrows
    M = _SageMatrixSpace(
        base_ring,
        nrows,
        ncols,
        sparse=sparse,
        implementation=implementation,
    )
    return cast(
        "RModule",
        refine_category(
            M,
            [Modules(base_ring).Free().FinitelyPresented().FiniteRank()],
            test=False,
        ),
    )


def CombinatorialFreeModule(
    base_ring: "Ring",
    basis_keys: Any = None,
    element_class: type[Any] | None = None,
    category: Any | None = None,
    prefix: str | None = None,
    names: str | tuple[str, ...] | None = None,
) -> "RModule":
    from .modules import Modules
    from .utils import refine_category

    M = _SageCombinatorialFreeModule(
        base_ring,
        basis_keys,
        element_class=element_class,
        category=category,
        prefix=prefix,
        names=names,
    )
    return cast(
        "RModule",
        refine_category(
            M,
            [
                Modules(base_ring).Free(),
                Modules(base_ring).WithBasis(),
                Modules(base_ring).WithOrderedGeneratingSet(),
            ],
            test=False,
        ),
    )


def GF(
    order: "Integer",
    name: str | None = None,
    modulus: "Polynomial | str | None" = None,
    names: str | None = None,
    impl: str | None = None,
    proof: bool | None = None,
    check_prime: bool = True,
    check_irreducible: bool = True,
    prefix: str | None = None,
    repr: str | None = None,
    elem_cache: bool | None = None,
) -> "Ring":
    from .rings import Rings, _FiniteFields
    from .utils import refine_category

    R = _SageGF(
        order,
        name=name,
        modulus=modulus,
        names=names,
        impl=impl,
        proof=proof,
        check_prime=check_prime,
        check_irreducible=check_irreducible,
        prefix=prefix,
        repr=repr,
        elem_cache=elem_cache,
    )
    return cast("Ring", refine_category(R, [Rings(), _FiniteFields()], test=False))


def FiniteField(
    order: "Integer",
    name: str | None = None,
    modulus: "Polynomial | str | None" = None,
    names: str | None = None,
    impl: str | None = None,
    proof: bool | None = None,
    check_prime: bool = True,
    check_irreducible: bool = True,
    prefix: str | None = None,
    repr: str | None = None,
    elem_cache: bool | None = None,
) -> "Ring":
    from .rings import Rings, _FiniteFields
    from .utils import refine_category

    R = _SageFiniteField(
        order,
        name=name,
        modulus=modulus,
        names=names,
        impl=impl,
        proof=proof,
        check_prime=check_prime,
        check_irreducible=check_irreducible,
        prefix=prefix,
        repr=repr,
        elem_cache=elem_cache,
    )
    return cast("Ring", refine_category(R, [Rings(), _FiniteFields()], test=False))


def IntegerModRing(
    order: "Integer" = 0,
    is_field: bool = False,
    category: Any | None = None,
) -> "Ring":
    from .rings import Rings, _IntegerModRings
    from .utils import refine_category

    R = _SageIntegerModRing(order, is_field=is_field, category=category)
    return cast(
        "Ring",
        refine_category(
            R,
            [Rings(), _IntegerModRings(), ModulesZZ().FinitelyPresented()],
            test=False,
        ),
    )


def Zp(
    p: "Integer",
    prec: "Integer | None" = None,
    type: str = "capped-rel",
    print_mode: str | None = None,
    names: str | None = None,
) -> "Ring":
    from .rings import Rings, _Zp
    from .utils import refine_category

    R = _SageZp(
        p,
        prec=prec,
        type=type,
        print_mode=print_mode,
        names=names,
    )
    return cast("Ring", refine_category(R, [Rings(), _Zp()], test=False))


def PolynomialRing(
    base_ring: "Ring",
    name: str | tuple[str, ...] | None = None,
    *,
    n: "Integer | None" = None,
    names: str | tuple[str, ...] | None = None,
    sparse: bool | None = None,
    order: str = "degrevlex",
    implementation: str | None = None,
) -> "Ring":
    from sage.categories.fields import Fields

    from .rings import Rings, _PolynomialRings
    from .utils import refine_category

    if names is None and name is not None:
        names = name
    if isinstance(names, tuple):
        return cast(
            "Ring",
            _SagePolynomialRing(
                base_ring,
                names,
                sparse=sparse,
                order=order,
                implementation=implementation,
            ),
        )
    if names is None:
        raise TypeError("PolynomialRing expects a variable name")
    R = _SagePolynomialRing(
        base_ring,
        names,
        sparse=sparse,
        order=order,
        implementation=implementation,
    )
    if base_ring not in Fields():
        return cast("Ring", R)
    return cast(
        "Ring",
        refine_category(
            R,
            [Rings(), _PolynomialRings().RingsUnder(R.base_ring())],
            test=False,
        ),
    )


def LaurentPolynomialRing(
    base_ring: "Ring",
    name: str,
    sparse: bool = False,
) -> "Ring":
    from .rings import Rings, _LaurentSeriesRings
    from .utils import refine_category

    R = _SageLaurentPolynomialRing(base_ring, name, sparse=sparse)
    return cast(
        "Ring",
        refine_category(
            R,
            [Rings(), _LaurentSeriesRings().RingsUnder(R.base_ring())],
            test=False,
        ),
    )


def PowerSeriesRing(
    base_ring: "Ring",
    name: str,
    *,
    sparse: bool = False,
    default_prec: "Integer | None" = None,
    implementation: str | None = None,
) -> "Ring":
    from .rings import Rings, _PowerSeriesRings
    from .utils import refine_category

    R = _SagePowerSeriesRing(
        base_ring,
        name,
        sparse=sparse,
        default_prec=default_prec,
        implementation=implementation,
    )
    return cast(
        "Ring",
        refine_category(
            R,
            [Rings(), _PowerSeriesRings().RingsUnder(R.base_ring())],
            test=False,
        ),
    )


def QuadraticField(
    D: "RingElement | Integer",
    name: str = "a",
    check: bool = True,
    embedding: bool | "RingElement" = True,
    latex_name: str = "sqrt",
) -> "Ring":
    from sage.categories.dedekind_domains import DedekindDomains

    from .rings import Rings, _QuadraticNumberFields
    from .utils import refine_category

    R = _SageQuadraticField(
        D,
        name=name,
        check=check,
        embedding=embedding,
        latex_name=latex_name,
    )
    refined = refine_category(
        R,
        [Rings(), _QuadraticNumberFields()],
        test=False,
    )
    refine_category(refined.ring_of_integers(), [DedekindDomains()], test=False)
    return cast("Ring", refined)


def ModulesZZ() -> Any:
    from sage.all import ZZ

    from .modules import Modules

    return Modules(ZZ)


def install_constructor_redefinitions() -> None:
    global _INSTALLED
    if _INSTALLED:
        return

    import sage.all as sage_all
    import sage.combinat.free_module as combinat_free_module
    import sage.modules.free_module as free_module_module
    import sage.rings.finite_rings.finite_field_constructor as finite_field_module
    import sage.rings.finite_rings.integer_mod_ring as integer_mod_ring_module
    import sage.rings.number_field.number_field as number_field_module
    import sage.rings.padics.factory as padic_factory_module
    import sage.rings.polynomial.laurent_polynomial_ring as laurent_poly_module
    import sage.rings.polynomial.polynomial_ring_constructor as poly_module
    import sage.rings.power_series_ring as power_series_module

    free_module_module.FreeModule = FreeModule
    free_module_module.VectorSpace = VectorSpace
    combinat_free_module.CombinatorialFreeModule = CombinatorialFreeModule
    finite_field_module.GF = GF
    finite_field_module.FiniteField = FiniteField
    integer_mod_ring_module.IntegerModRing = IntegerModRing
    padic_factory_module.Zp = Zp
    poly_module.PolynomialRing = PolynomialRing
    laurent_poly_module.LaurentPolynomialRing = LaurentPolynomialRing
    power_series_module.PowerSeriesRing = PowerSeriesRing
    number_field_module.QuadraticField = QuadraticField

    sage_all.FreeModule = FreeModule
    sage_all.VectorSpace = VectorSpace
    sage_all.CombinatorialFreeModule = CombinatorialFreeModule
    sage_all.MatrixSpace = MatrixSpace
    sage_all.GF = GF
    sage_all.FiniteField = FiniteField
    sage_all.IntegerModRing = IntegerModRing
    sage_all.Zp = Zp
    sage_all.PolynomialRing = PolynomialRing
    sage_all.LaurentPolynomialRing = LaurentPolynomialRing
    sage_all.PowerSeriesRing = PowerSeriesRing
    sage_all.QuadraticField = QuadraticField

    _INSTALLED = True

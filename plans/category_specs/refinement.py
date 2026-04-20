"""Eager seed enrollment and constructor hooks for ``ModuleBaseRings``.

``install()`` is called once, at package import, from ``rings.py``.  It:

1. Refines a fixed list of seed ring parents (``ZZ``, ``QQ``, ``RR``, ``CC``,
   ``QQbar`` plus a handful of ``GF(p)`` / ``Zp(p)`` / ``Qp(p)``).
2. Monkey-patches common ring- and module-valued constructors so that parents
   they return are refined into ``ModuleBaseRings()`` (for rings) or
   ``Modules(R).Free()`` (for modules like ``FreeModule(R, n)``).

The lazy-enrollment path ``ensure_refined`` is additionally called from
``Modules.__classcall_private__``, so *any* ring referenced as
``Modules(R)`` is enrolled on first touch.

All refinement actions are idempotent.
"""

from __future__ import annotations

import importlib
from typing import Any, Callable

_INSTALLED = False

SEED_PRIMES: tuple[int, ...] = (2, 3, 5, 7, 11, 13)


# ---------------------------------------------------------------------------
# Refinement primitives
# ---------------------------------------------------------------------------

def refine_ring(R: Any) -> None:
    """Idempotently refine ``R`` into ``ModuleBaseRings()``."""
    from sage.categories.category import Category

    from .rings import ModuleBaseRings

    if isinstance(R, Category):
        return
    target = ModuleBaseRings()
    cat = R.category()
    if cat.is_subcategory(target):
        return
    R._refine_category_(target)


def ensure_refined(R: Any) -> None:
    """Enroll ``R`` if it satisfies the ``Modules(R)`` contract.

    Called from ``Modules.__classcall_private__`` so every ``Modules(R)``
    reference lazily refines ``R``.  Silent for categories (admissible as
    a ``base_ring`` surrogate) and for parents that do not satisfy the
    PID+Commutative gate.
    """
    from sage.categories.category import Category
    from sage.categories.principal_ideal_domains import PrincipalIdealDomains

    if isinstance(R, Category):
        return
    try:
        if R in PrincipalIdealDomains():
            refine_ring(R)
    except Exception:
        return


def _refine_free_module(parent: Any) -> None:
    """Refine a ``FreeModule(R, n)``-style parent into ``Modules(R).Free()``."""
    from .rings import ModuleBaseRings
    from .sage_modules import Modules

    R = parent.base_ring()
    ensure_refined(R)
    if R in ModuleBaseRings():
        parent._refine_category_(Modules(R).Free())


# ---------------------------------------------------------------------------
# Seed enrollment
# ---------------------------------------------------------------------------

def _seed() -> None:
    """Eagerly refine the core rings used across the lattice surface."""
    from sage.rings.integer_ring import ZZ
    from sage.rings.rational_field import QQ
    from sage.rings.real_mpfr import RR
    from sage.rings.cc import CC
    from sage.rings.qqbar import QQbar

    for R in (ZZ, QQ, RR, CC, QQbar):
        try:
            refine_ring(R)
        except Exception:
            continue

    try:
        from sage.rings.finite_rings.finite_field_constructor import GF
        from sage.rings.padics.factory import Qp, Zp
    except ImportError:
        return

    for p in SEED_PRIMES:
        for ctor in (GF, Zp, Qp):
            try:
                refine_ring(ctor(p))
            except Exception:
                continue


# ---------------------------------------------------------------------------
# Constructor wrapping
# ---------------------------------------------------------------------------

def _wrap_callable(
    module_paths: tuple[str, ...],
    name: str,
    refiner: Callable[[Any], None],
) -> None:
    """Replace ``mod.name`` in each module in ``module_paths`` with a wrapper
    that runs the original and then calls ``refiner(result)``.  Idempotent
    via a ``_mbr_wrapped`` attribute on the wrapper.
    """
    targets: list[tuple[Any, Any]] = []
    base_orig: Any = None
    for path in module_paths:
        try:
            mod = importlib.import_module(path)
        except ImportError:
            continue
        orig = getattr(mod, name, None)
        if orig is None:
            continue
        if getattr(orig, "_mbr_wrapped", False):
            continue
        targets.append((mod, orig))
        if base_orig is None:
            base_orig = orig

    if not targets or base_orig is None:
        return

    def wrapped(*args: Any, _orig: Any = base_orig, **kwds: Any) -> Any:
        result = _orig(*args, **kwds)
        try:
            refiner(result)
        except Exception:
            pass
        return result

    wrapped._mbr_wrapped = True  # type: ignore[attr-defined]
    wrapped.__wrapped__ = base_orig  # type: ignore[attr-defined]

    for mod, _ in targets:
        try:
            setattr(mod, name, wrapped)
        except Exception:
            continue


_RING_CONSTRUCTORS: tuple[tuple[tuple[str, ...], str], ...] = (
    (("sage.rings.polynomial.laurent_polynomial_ring", "sage.all"),
     "LaurentPolynomialRing"),
    (("sage.rings.power_series_ring", "sage.all"), "PowerSeriesRing"),
    (("sage.rings.laurent_series_ring", "sage.all"), "LaurentSeriesRing"),
    (("sage.rings.number_field.number_field", "sage.all"), "NumberField"),
    (("sage.rings.number_field.number_field", "sage.all"), "CyclotomicField"),
    (("sage.rings.number_field.number_field", "sage.all"), "QuadraticField"),
    (("sage.rings.finite_rings.finite_field_constructor", "sage.all"), "GF"),
    (("sage.rings.finite_rings.finite_field_constructor", "sage.all"),
     "FiniteField"),
    (("sage.rings.finite_rings.integer_mod_ring", "sage.all"), "IntegerModRing"),
    (("sage.rings.finite_rings.integer_mod_ring", "sage.all"), "Integers"),
    (("sage.rings.padics.factory", "sage.all"), "Zp"),
    (("sage.rings.padics.factory", "sage.all"), "Qp"),
    (("sage.rings.padics.factory", "sage.all"), "ZpFM"),
    (("sage.rings.padics.factory", "sage.all"), "Zq"),
    (("sage.rings.padics.factory", "sage.all"), "Qq"),
)

_MODULE_CONSTRUCTORS: tuple[tuple[tuple[str, ...], str], ...] = (
    (("sage.modules.free_module", "sage.all"), "FreeModule"),
    (("sage.matrix.matrix_space", "sage.all"), "MatrixSpace"),
)


# ---------------------------------------------------------------------------
# Install
# ---------------------------------------------------------------------------

def install() -> None:
    """Idempotently seed + hook constructors.  Safe to call from any module."""
    global _INSTALLED
    if _INSTALLED:
        return
    _INSTALLED = True
    _seed()
    for paths, name in _RING_CONSTRUCTORS:
        _wrap_callable(paths, name, refine_ring)
    for paths, name in _MODULE_CONSTRUCTORS:
        _wrap_callable(paths, name, _refine_free_module)

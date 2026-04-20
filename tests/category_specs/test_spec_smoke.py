"""Spec smoke for ``plans.category_specs``.

Two concerns, intentionally separated:

1. **Instantiation** — importing the package and running the three
   canonical constructions (``ZZ ** 2``, ``ZZ.quotient(6 * ZZ)``,
   ``ZZ.ideal(6)``) must succeed.  These exercise the super+refine glue
   in ``ModuleBaseRings.ParentMethods``.

2. **Abstract-method discovery** — every ``@abstract_method`` on the
   parent-side / element-side surface must fail uniformly, i.e. raise
   a ``NotImplementedError`` (the standard failure emitted by Sage's
   ``abstract_method`` decorator).  The list this test produces *is* the
   implementation backlog.  Any method that returns ``None`` or raises a
   different exception type signals a spec gap (missing decorator or
   silent ``...`` body) that must be fixed.
"""

from __future__ import annotations

import importlib
from typing import Any

import pytest
from sage.all import GF, QQ, ZZ, FiniteField
from sage.rings.padics.factory import Zp

# Eagerly import the spec package so ``refinement.install()`` runs.
importlib.import_module("plans.category_specs")

from plans.category_specs.rings import ModuleBaseIdeals, ModuleBaseRings  # noqa: E402
from plans.category_specs.sage_modules import Modules  # noqa: E402


# ---------------------------------------------------------------------------
# 1. Instantiation
# ---------------------------------------------------------------------------

class TestInstantiation:
    def test_pow_returns_free_module(self):
        M = ZZ ** 2
        assert M is not None
        assert M.rank() == 2

    def test_quotient_returns_ring(self):
        Q = ZZ.quotient(6 * ZZ)
        assert Q is not None

    def test_ideal_returns_ideal(self):
        I = ZZ.ideal(6)
        assert I.gens() == (6,)


# ---------------------------------------------------------------------------
# 2. Seed enrollment + idempotent install
# ---------------------------------------------------------------------------

class TestSeedEnrollment:
    @pytest.mark.parametrize("R", [ZZ, QQ])
    def test_core_ring_is_refined(self, R):
        assert R in ModuleBaseRings()

    def test_gf_is_refined(self):
        assert GF(7) in ModuleBaseRings()

    def test_zp_is_refined(self):
        assert Zp(5) in ModuleBaseRings()

    def test_install_is_idempotent(self):
        from plans.category_specs import refinement
        # Calling install() a second time must be a no-op.
        refinement.install()
        refinement.install()
        assert ZZ in ModuleBaseRings()


# ---------------------------------------------------------------------------
# 3. Non-regression sanity
# ---------------------------------------------------------------------------

class TestNonRegression:
    def test_ideal_gens_round_trip(self):
        assert ZZ.ideal(6).gens() == (6,)

    def test_free_module_rank(self):
        assert (ZZ ** 2).rank() == 2

    def test_zp_precision_cap(self):
        assert Zp(5).precision_cap() > 0


# ---------------------------------------------------------------------------
# 4. Abstract-method discovery sweep
# ---------------------------------------------------------------------------
# For each surface we instantiate a concrete parent/element from Sage's
# existing implementation and then try to invoke every ``@abstract_method``
# declared on the corresponding ``ParentMethods`` / ``ElementMethods``.
# Every call is expected to raise ``NotImplementedError`` — the uniform
# failure mode produced by ``sage.misc.abstract_method``.  Any other result
# (``None``, ``AttributeError``, ``TypeError`` from a ``...``-returns-None
# chain) is a spec gap and fails the test.

def _abstract_names(methods_class: Any) -> list[str]:
    """Return the names of ``@abstract_method``-decorated functions on a
    spec ``*Methods`` class.
    """
    from sage.misc.abstract_method import AbstractMethod
    result = []
    for name, member in methods_class.__dict__.items():
        if isinstance(member, AbstractMethod):
            result.append(name)
    return sorted(result)


def _call_and_record(target: Any, name: str) -> dict[str, Any]:
    """Invoke ``target.name(...)`` with a small probe and record the outcome."""
    method = getattr(target, name, None)
    record: dict[str, Any] = {"name": name, "outcome": None, "detail": None}
    if method is None:
        record["outcome"] = "missing"
        return record
    # Minimal positional probes: most abstracts take no args or one arg.
    probes = [(), (target,), (0,)]
    for args in probes:
        try:
            method(*args)
        except NotImplementedError as exc:
            record["outcome"] = "not_implemented"
            record["detail"] = str(exc)
            return record
        except TypeError:
            # Signature mismatch — try the next probe.
            continue
        except Exception as exc:  # noqa: BLE001 — spec-gap reporter
            record["outcome"] = type(exc).__name__
            record["detail"] = str(exc)
            return record
        else:
            record["outcome"] = "returned_without_raise"
            return record
    record["outcome"] = "no_matching_signature"
    return record


class TestAbstractMethodSweep:
    """For each category ``*Methods`` surface, invoke every abstract method
    on an instantiated object and verify the uniform failure mode.
    """

    def test_rings_parent_methods_abstracts_are_loud(self):
        names = _abstract_names(ModuleBaseRings.ParentMethods)
        results = [_call_and_record(ZZ, n) for n in names]
        # The surface MUST declare at least some abstracts.
        assert names, "No abstract methods on ModuleBaseRings.ParentMethods"
        # Every abstract must be loud (NotImplementedError) — no silent Nones.
        silent = [r for r in results if r["outcome"] == "returned_without_raise"]
        assert not silent, f"Silent abstracts (return None): {silent}"

    def test_modules_parent_methods_abstracts_are_loud(self):
        names = _abstract_names(Modules.ParentMethods)
        assert names
        M = ZZ ** 2
        results = [_call_and_record(M, n) for n in names]
        silent = [r for r in results if r["outcome"] == "returned_without_raise"]
        assert not silent, f"Silent abstracts (return None): {silent}"

    def test_modules_element_methods_abstracts_are_loud(self):
        names = _abstract_names(Modules.ElementMethods)
        assert names
        m = (ZZ ** 2).zero()
        results = [_call_and_record(m, n) for n in names]
        silent = [r for r in results if r["outcome"] == "returned_without_raise"]
        assert not silent, f"Silent abstracts (return None): {silent}"

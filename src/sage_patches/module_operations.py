"""Free/torsion decomposition and generator operations for enriched FGP modules.

Adds free_part() and torsion_part() methods to FGP_Module_class using
Sage's existing Smith normal form invariants.
"""

from __future__ import annotations

from typing import Any

from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module import FreeModule

_installed = False


def _fgp_free_part(self: Any) -> Any:
    """Return the free part of this FGP module as a free module over the base ring.

    Uses Smith normal form invariants: zero invariants correspond to free generators.
    """
    invs = self.invariants()
    free_rank = sum(1 for x in invs if x == 0)
    R = self.base_ring()
    return FreeModule(R, free_rank)


def _fgp_torsion_part(self: Any) -> Any:
    """Return the torsion part of this FGP module as an FGP module."""
    invs = self.invariants()
    torsion_invs = tuple(x for x in invs if x != 0)
    if not torsion_invs:
        # Trivial torsion part: zero module
        V = FreeModule(self.base_ring(), 1)
        return V.quotient(V)
    R = self.base_ring()
    V = FreeModule(R, len(torsion_invs))
    sub = V.submodule([V.gen(i) * torsion_invs[i] for i in range(len(torsion_invs))])
    return V.quotient(sub)


def install() -> None:
    """Install free_part/torsion_part on FGP module class.

    Idempotent: safe to call multiple times.
    """
    global _installed
    if _installed:
        return

    FGP_Module_class.free_part = _fgp_free_part
    FGP_Module_class.torsion_part = _fgp_torsion_part

    _installed = True

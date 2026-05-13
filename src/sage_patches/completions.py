"""Completion and localization refinement for ModuleBaseRings.

Adds stable alias methods (complete, localize, fraction_field) to
ModuleBaseRings ring parents, ensuring returned ring objects retain
ModuleBaseRings category refinement.

Gate: only active on rings installed with ModuleBaseRings.
"""

from __future__ import annotations

from typing import Any

_installed = False


def _refine_returned_ring(result: Any, base_ring: Any) -> Any:
    """Refine a returned ring parent into ModuleBaseRings scope."""
    try:
        if hasattr(result, "_refine_category_"):
            import src.sage_patches.ring_base_category as mbr

            result._refine_category_(mbr._ModuleBaseRings())
    except Exception:
        pass
    return result


def _module_base_complete(self: Any, *args: Any, **kwds: Any) -> Any:
    """Completion of this ring at a prime/ideal, with ModuleBaseRings refinement."""
    result = self.completion(*args, **kwds)
    return _refine_returned_ring(result, self)


def _module_base_localize(self: Any, *args: Any, **kwds: Any) -> Any:
    """Localization of this ring, with ModuleBaseRings refinement."""
    result = self.localization(*args, **kwds)
    return _refine_returned_ring(result, self)


def _module_base_fraction_field(self: Any, *args: Any, **kwds: Any) -> Any:
    """Fraction field of this ring, with ModuleBaseRings refinement."""
    result = self.fraction_field(*args, **kwds)
    return _refine_returned_ring(result, self)


def install() -> None:
    """Install completion/localization/fraction_field refinement.

    Idempotent: safe to call multiple times.
    """
    global _installed
    if _installed:
        return

    import src.sage_patches.ring_base_category as mbr

    cat = mbr._ModuleBaseRings()

    # Add aliases to ModuleBaseRings.ParentMethods
    if not hasattr(cat.ParentMethods, "complete"):
        cat.ParentMethods.complete = _module_base_complete
    if not hasattr(cat.ParentMethods, "localize"):
        cat.ParentMethods.localize = _module_base_localize
    if not hasattr(cat.ParentMethods, "fraction_field"):
        cat.ParentMethods.fraction_field = _module_base_fraction_field

    _installed = True

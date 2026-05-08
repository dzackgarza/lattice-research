"""Thin element wrappers backed by category mixins.

BilinearModuleElement, FreeBilinearModuleElement, TorsionBilinearModuleElement,
and quadratic variants — thin wrappers over Sage module elements that defer
semantics to ModulesWithForms category ElementMethods.
"""

from __future__ import annotations

from sage.structure.element import Element, ModuleElement


class BilinearModuleElement(ModuleElement):
    """Element of a formed module — thin wrapper backed by category mixins."""

    def __init__(self, parent, vector):
        self._vector = vector
        ModuleElement.__init__(self, parent)

    def to_vector(self):
        return self._vector

    def to_coordinates(self):
        return list(self._vector)

    def _add_(self, other):
        return self.__class__(self.parent(), self._vector + other._vector)

    def _sub_(self, other):
        return self.__class__(self.parent(), self._vector - other._vector)

    def _neg_(self):
        return self.__class__(self.parent(), -self._vector)

    def _rmul_(self, scalar):
        return self.__class__(self.parent(), scalar * self._vector)

    def _lmul_(self, scalar):
        return self.__class__(self.parent(), scalar * self._vector)

    def _mul_(self, other):
        """Dispatch to parent form for bilinear evaluation."""
        parent = self.parent()
        if hasattr(parent, 'form') and parent.form() is not None:
            return parent.form().evaluate(self, other)
        raise NotImplementedError("no form data on parent")

    def is_isotropic(self):
        try:
            return self._mul_(self) == 0
        except Exception:
            return False

    def _hash_(self):
        return hash((self.parent(), tuple(self._vector)))

    def _richcmp_(self, other, op):
        from sage.structure.richcmp import richcmp
        if not isinstance(other, BilinearModuleElement):
            return NotImplemented
        return richcmp(self._vector, other._vector, op)

    def __repr__(self):
        return f"element({list(self._vector)}) in {self.parent()}"


class FreeBilinearModuleElement(BilinearModuleElement):
    """Element of a free bilinear module."""

    def additive_order(self):
        return 0  # torsion-free


class TorsionBilinearModuleElement(BilinearModuleElement):
    """Element of a torsion bilinear module."""

    def additive_order(self):
        parent = self.parent()
        if hasattr(parent, 'invariants'):
            return parent.invariants()[0]  # simplified
        return 1

"""Bilinear and quadratic form helper objects.

Thin wrappers that coerce raw evaluations into the FormCodomain value space.
BilinearForm evaluates on pairs; QuadraticForm evaluates on single vectors
and provides polar_form().
"""

from __future__ import annotations


class BilinearForm:
    """Bilinear form on a module, valued in a FormCodomain."""

    def __init__(self, module, codomain):
        self._module = module
        self._codomain = codomain

    def codomain(self):
        return self._codomain

    def evaluate(self, u, v):
        """Evaluate the form on two module elements, coercing into codomain."""
        raise NotImplementedError("subclass must implement evaluate")


class QuadraticForm:
    """Quadratic form on a module, valued in a FormCodomain."""

    def __init__(self, module, codomain):
        self._module = module
        self._codomain = codomain

    def codomain(self):
        return self._codomain

    def evaluate(self, v):
        """Evaluate the quadratic form on a module element."""
        raise NotImplementedError("subclass must implement evaluate")

    def polar_form(self):
        """Return the associated bilinear form (q(x+y)-q(x)-q(y))/2."""
        raise NotImplementedError("subclass must implement polar_form")

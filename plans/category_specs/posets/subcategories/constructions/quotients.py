r"""Quotient construction category for posets."""

from __future__ import annotations

from ....cat import QuotientsCategory


class _Quotients(QuotientsCategory):
    r"""Quotient posets."""

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

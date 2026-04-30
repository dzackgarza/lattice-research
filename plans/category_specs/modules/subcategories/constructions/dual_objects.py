r"""Dual modules."""

from __future__ import annotations

from typing import final

from ....cat import DualObjectsCategory


class _DualObjects(DualObjectsCategory):
    r"""Dual modules M^* := Hom_R(M, R) viewed as integral linear forms."""

    @final
    def extra_super_categories(self):
        r"""The dual M^* is an integral linear form."""
        return [self.base_category().Homsets().Forms().Linear().Integral()]

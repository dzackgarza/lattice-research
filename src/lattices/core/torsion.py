from __future__ import annotations

from abc import abstractmethod

from src.lattices.core.abstract import BilinearModule


class TorsionBilinearModule(BilinearModule):
    @abstractmethod
    def invariants(self):
        ...

    def rank(self) -> int:
        return len(self.invariants())

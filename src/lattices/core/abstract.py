from __future__ import annotations

from abc import ABC, abstractmethod

from sage.all import ZZ


class BilinearModule(ABC):
    def base_ring(self):
        return ZZ

    @abstractmethod
    def rank(self) -> int:
        ...

    @abstractmethod
    def gens(self):
        ...

    @abstractmethod
    def element_from(self, coordinates):
        ...

    def gen(self, index: int):
        return self.gens()[index]

    def __call__(self, coordinates):
        return self.element_from(coordinates)

    def b(self, left, right):
        return left.bilinear_product_with(right)

    def q(self, value):
        return value.q()


class QuadraticModule(ABC):
    @abstractmethod
    def q(self, value):
        ...

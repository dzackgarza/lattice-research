from __future__ import annotations

from typing import TYPE_CHECKING

from sage.all import QQ, ZZ, Integer, vector

from src.lattices.validation.presentations import CoordinatePresentation

if TYPE_CHECKING:
    from src.lattices.core.free import FreeBilinearModule


class FreeBilinearModuleElement:
    def __init__(self, parent: FreeBilinearModule, coordinates):
        self._parent = parent
        presentation = CoordinatePresentation(module_ring=QQ, rank=parent.rank(), coordinates=coordinates)
        self._coordinates = presentation.coordinates

    def parent(self):
        return self._parent

    def to_vector(self):
        return self._coordinates

    def to_coordinates(self):
        return self.to_vector()

    def _ambient_vector(self):
        return self.parent()._ambient_coordinates_of(self.to_vector())

    def bilinear_product_with(self, other):
        assert isinstance(other, FreeBilinearModuleElement) and other.parent() is self.parent(), (
            "Bilinear products are defined only for elements of the same parent"
        )
        return (self.to_vector() * self.parent().gram_matrix() * other.to_vector().column())[0]

    def inner_product(self, other):
        return self.bilinear_product_with(other)

    def q(self):
        return self * self

    def is_isotropic(self):
        return self.q().is_zero()

    def span(self):
        return self.parent().span((self,))

    def perp(self):
        return self.span()._inclusion.perp()

    def __iter__(self):
        return iter(self._coordinates)

    def __len__(self):
        return len(self._coordinates)

    def __getitem__(self, index):
        return self._coordinates[index]

    def __neg__(self):
        return self.parent().element_from(-self.to_vector())

    def __add__(self, other):
        assert isinstance(other, FreeBilinearModuleElement) and other.parent() is self.parent(), (
            "Addition is defined only for elements of the same parent"
        )
        return self.parent().element_from(self.to_vector() + other.to_vector())

    def __sub__(self, other):
        assert isinstance(other, FreeBilinearModuleElement) and other.parent() is self.parent(), (
            "Subtraction is defined only for elements of the same parent"
        )
        return self.parent().element_from(self.to_vector() - other.to_vector())

    def __mul__(self, other):
        if isinstance(other, FreeBilinearModuleElement):
            return self.bilinear_product_with(other)
        return self.parent()._scalar_multiple(self, other)

    def __rmul__(self, scalar):
        return self.parent()._scalar_multiple(self, scalar)

    def __truediv__(self, scalar):
        return self.parent()._scalar_multiple(self, QQ.one() / QQ(scalar))

    def __eq__(self, other):
        return isinstance(other, FreeBilinearModuleElement) and self.parent() is other.parent() and self.to_vector() == other.to_vector()

    def __hash__(self):
        return hash((id(self.parent()), tuple(self.to_vector())))

    def __repr__(self):
        pieces = []
        for coefficient, name in zip(self.to_vector(), self.parent().generator_names(), strict=True):
            if coefficient == 0:
                continue
            if coefficient == 1:
                pieces.append(name)
            elif coefficient == -1:
                pieces.append(f"-{name}")
            else:
                pieces.append(f"{coefficient}*{name}")
        if not pieces:
            return "0"
        rendered = pieces[0]
        for piece in pieces[1:]:
            if piece.startswith("-"):
                rendered = f"{rendered} - {piece[1:]}"
            else:
                rendered = f"{rendered} + {piece}"
        return rendered


class RationalLatticeElement(FreeBilinearModuleElement):
    ...


class DualLatticeElement(RationalLatticeElement):
    def discriminant_class(self):
        return self.parent().project_to_discriminant(self)


class LatticeElement(RationalLatticeElement):
    def to_vector(self):
        return vector(ZZ, [Integer(entry) for entry in super().to_vector()])

    def divisibility(self):
        pairings = tuple(self * generator for generator in self.parent().gens())
        return ZZ.ideal(pairings).gen()

    def is_primitive(self):
        coordinates = tuple(Integer(entry) for entry in self.to_vector())
        return ZZ.ideal(coordinates).gen() == 1

    def discriminant_class(self):
        return self.parent().discriminant_group().zero()

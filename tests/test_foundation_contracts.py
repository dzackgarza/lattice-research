"""
Contract tests for the trusted lattice foundation API.

Validates that all canonical constructors, coercions, morphisms, and
discriminant group operations on ``coble_geometry_foundation`` work correctly.
"""

from __future__ import annotations

from sage.all import IntegralLattice

from coble_geometry_foundation import DiscriminantGroup, FreeBilinearModule, Lattice


class TestCanonicalConstructors:
    """Verify all Lattice factory methods produce correct objects."""

    def test_positive_line_from_twist(self):
        native = IntegralLattice("A1")
        scale = next(iter(native.basis())).inner_product(next(iter(native.basis())))
        L = Lattice.Z().twist(scale)
        assert L.is_isometric_to(native)

    def test_negative_line_is_even(self):
        assert Lattice.A(1).is_even()

    def test_e8_is_even(self):
        assert Lattice.E(8).is_even()

    def test_hyperbolic_plane_is_even(self):
        U = Lattice.U()
        assert U.is_even()

    def test_coble_picard_is_even(self):
        assert Lattice.coble_picard().is_even()

    def test_coble_transcendental_is_even(self):
        assert Lattice.coble_transcendental().is_even()

    def test_k3_lattice_is_even(self):
        assert Lattice.k3().is_even()


class TestLatticeElements:
    """Verify element-level operations: divisibility, primitivity, isotropy."""

    def test_positive_line_generator_divisibility_one(self):
        native = IntegralLattice("A1")
        scale = next(iter(native.basis())).inner_product(next(iter(native.basis())))
        L = Lattice.Z().twist(scale)
        gen = next(iter(L.gens()))
        assert gen.divisibility().is_one()

    def test_positive_line_generator_is_primitive(self):
        native = IntegralLattice("A1")
        scale = next(iter(native.basis())).inner_product(next(iter(native.basis())))
        L = Lattice.Z().twist(scale)
        gen = next(iter(L.gens()))
        assert gen.is_primitive()

    def test_hyperbolic_plane_has_isotropic_generator(self):
        U = Lattice.U()
        ambient = FreeBilinearModule.from_sage(U.ambient_module())
        gen = next(iter(ambient.gens()))
        assert gen.is_isotropic()


class TestFromSage:
    """Verify Lattice.from_sage roundtrip."""

    def test_from_sage_preserves_evenness(self):
        native = IntegralLattice("A1")
        L = Lattice.from_sage(native)
        assert L.is_even()

    def test_from_sage_preserves_divisibility(self):
        native = IntegralLattice("A1")
        L = Lattice.from_sage(native)
        gen = next(iter(L.gens()))
        assert gen.divisibility().is_one()

    def test_from_sage_isometric_to_original(self):
        native = IntegralLattice("A1")
        L = Lattice.from_sage(native)
        assert L.is_isometric_to(native)


class TestDiscriminantGroups:
    """Verify discriminant group construction and element operations."""

    def test_discriminant_group_from_lattice(self):
        L = Lattice.Z().twist(2)  # A1 positive
        dg = DiscriminantGroup.from_lattice(L)
        assert not dg.cardinality().is_one()
        assert dg.cardinality().is_prime_power()

    def test_discriminant_group_from_sage(self):
        native = IntegralLattice("A1")
        dg = DiscriminantGroup.from_sage(native.discriminant_group())
        assert not dg.cardinality().is_one()
        assert dg.cardinality().is_prime_power()

    def test_discriminant_generator_not_isotropic(self):
        L = Lattice.Z().twist(2)
        dg = L.discriminant_group()
        gen = next(iter(dg.gens()))
        assert not gen.is_isotropic()

    def test_lattice_generator_discriminant_class_is_zero(self):
        native = IntegralLattice("A1")
        scale = next(iter(native.basis())).inner_product(next(iter(native.basis())))
        L = Lattice.Z().twist(scale)
        dg = L.discriminant_group()
        gen = next(iter(L.gens()))
        dc = gen.discriminant_class()
        assert dc.parent() is dg
        assert dc.is_isotropic()
        assert dc.is_zero()


class TestMorphisms:
    """Verify lattice and discriminant group morphisms."""

    def test_lattice_identity_morphism(self):
        U = Lattice.U()
        identity = U.hom(U, U.gens())
        img = identity.image_lattice()
        assert img.is_even()
        assert img.discriminant_group().cardinality().is_one()
        assert img.is_isometric_to(U)
        assert identity.orthogonal_complement_of_image().rank().is_zero()

    def test_discriminant_group_identity_morphism(self):
        native = IntegralLattice("A1")
        scale = next(iter(native.basis())).inner_product(next(iter(native.basis())))
        L = Lattice.Z().twist(scale)
        dg = L.discriminant_group()
        identity = dg.hom(dg, dg.gens())
        imgs = identity.image_generators()
        assert imgs
        assert next(iter(imgs)).parent() is dg
        assert identity.is_identity()
        assert not next(iter(imgs)).is_isotropic()

from __future__ import annotations

from src.coble_geometry_foundation import Lattice


def _hyperbolic_plane():
    return Lattice.U()


def _two_hyperbolic_planes():
    return Lattice.from_sage(Lattice.U().direct_sum(Lattice.U()))


def _is_totally_isotropic(basis):
    return all(v.is_isotropic() for v in basis) and all(
        basis[i].inner_product(basis[j]).is_zero()
        for i in range(len(basis))
        for j in range(i + 1, len(basis))
    )


class TestIsotropicLineSplitting:
    def test_ambient_orthogonal_group_of_u_has_one_isotropic_line_orbit(self):
        U = _hyperbolic_plane()
        assert len(U.orthogonal_group().isotropic_line_orbits()) == 1

    def test_special_orthogonal_group_of_u_splits_into_two_line_orbits(self):
        U = _hyperbolic_plane()
        SO = U.orthogonal_group().special_orthogonal_subgroup()
        orbits = SO.isotropic_line_orbits()
        assert len(orbits) == 2
        assert all(v.is_isotropic() for v in orbits)

    def test_ambient_group_identifies_the_two_standard_isotropic_lines(self):
        U = _hyperbolic_plane()
        e = U([1, 0])
        f = U([0, 1])
        assert U.orthogonal_group().isotropic_lines_are_equivalent(e, f)

    def test_special_orthogonal_group_separates_the_two_standard_isotropic_lines(self):
        U = _hyperbolic_plane()
        e = U([1, 0])
        f = U([0, 1])
        SO = U.orthogonal_group().special_orthogonal_subgroup()
        assert not SO.isotropic_lines_are_equivalent(e, f)


class TestIsotropicPlaneAndFlagSplitting:
    def test_ambient_orthogonal_group_of_u_plus_u_has_one_plane_orbit(self):
        lattice = _two_hyperbolic_planes()
        orbits = lattice.orthogonal_group().isotropic_plane_orbits()
        assert len(orbits) == 1
        assert _is_totally_isotropic(orbits[0])

    def test_special_orthogonal_group_of_u_plus_u_has_two_plane_orbits(self):
        lattice = _two_hyperbolic_planes()
        SO = lattice.orthogonal_group().special_orthogonal_subgroup()
        orbits = SO.isotropic_plane_orbits()
        assert len(orbits) == 2
        assert all(_is_totally_isotropic(orbit) for orbit in orbits)

    def test_ambient_orthogonal_group_of_u_plus_u_has_one_flag_orbit(self):
        lattice = _two_hyperbolic_planes()
        orbits = lattice.orthogonal_group().isotropic_flag_orbits(2)
        assert len(orbits) == 1
        assert _is_totally_isotropic(orbits[0])

    def test_special_orthogonal_group_of_u_plus_u_has_two_flag_orbits(self):
        lattice = _two_hyperbolic_planes()
        SO = lattice.orthogonal_group().special_orthogonal_subgroup()
        orbits = SO.isotropic_flag_orbits(2)
        assert len(orbits) == 2
        assert all(_is_totally_isotropic(orbit) for orbit in orbits)

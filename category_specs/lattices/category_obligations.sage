r"""Mathematical-fact obligations for the lattice category subtree.

Each statement instantiates an object through the lattice DSL and asserts a real
mathematical value it must recover. A statement passes only when the backend computes the
value; it is red while the backend is incomplete. No statement asserts category-graph
structure (method ownership, subcategory placement, type-package aliases, defining
predicates) — that is a property of the spec *source*, enforced by the validators in
`category_specs/validators/` (super_categories, banned_spec_patterns,
constructor_name_inventory). The ~24 `abstract_method_has_name(...)` / `X is
Y.ParentMethods` / `obj in Cat()` meta-assertions that previously dominated this file were
removed here; migrating any structural invariant they encoded into validator coverage is
the separate "framework tests -> validators" workstream (tracked, not silently dropped).

Citations (per the `What A Test Cites` contract) — literature-sourced expected values cite
a Zotero item + text/markdown extraction attachment + verified line; elementary computed
facts (determinants, a gluing gram matrix, a finite group-action orbit) carry no literature
citation:
  - Conway & Sloane, SPLAG (1999): Zotero item D5P2XVRN, extraction TCJKXU3D, line 4676 —
    the hexagonal lattice A_2 has kissing number tau = 6 (its 6 minimal vectors are the
    roots), so A_2 has 6 roots and 3 up to sign.
"""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from category_specs.lattices import Lattices
from category_specs.lattices.subcategories.over_integers import _LatticesOverIntegers as LatticesOverIntegers
from category_specs.lattices.subcategories.constructions.discriminant_form_actions import (
    discriminant_form_orbit,
    discriminant_form_stabilizer,
    discriminant_form_subset_orbits,
)
from category_specs.utils import assert_category_statements
from sage.all import ZZ, identity_matrix, matrix
from sage.modules.torsion_quadratic_module import TorsionQuadraticForm


LZZ = Lattices(ZZ)
LCONSTRUCTORS = LZZ.Constructors()


def a2_short_vectors_below_three():
    return LCONSTRUCTORS.IntegralLattice(cartan_type="A2").short_vectors(3)


def a2_short_vectors_below_three_up_to_sign():
    return LatticesOverIntegers.ParentMethods.short_vectors_up_to_sign(
        LCONSTRUCTORS.IntegralLattice(cartan_type="A2"), 3
    )


def integral_lattice_direct_sum_discriminant():
    L1 = LCONSTRUCTORS.IntegralLattice(gram_matrix=matrix(ZZ, [[2]]))
    L2 = LCONSTRUCTORS.IntegralLattice(hyperbolic_plane="U")
    return LCONSTRUCTORS.IntegralLatticeDirectSum(lattices=[L1, L2]).discriminant()


def integral_lattice_gluing_gram_matrix():
    L = LCONSTRUCTORS.IntegralLattice(gram_matrix=matrix(ZZ, [[4]]))
    g = L.discriminant_group().gens()[0]
    return LCONSTRUCTORS.IntegralLatticeGluing(lattices=[L], glue=[[2 * g]]).gram_matrix()


def discriminant_form_action_conversion():
    # Elementary finite group action: the discriminant form (Z/2)^2 with the coordinate
    # swap acting; orbit of a generator has size 2, the pointwise stabilizer is trivial.
    D = TorsionQuadraticForm(identity_matrix(2) / 2)
    G = D.orthogonal_group(gens=[matrix(2, [0, 1, 1, 0])])
    x = D.gen(0)
    y = D.gen(1)
    orbit = discriminant_form_orbit(G, x)
    orbits = discriminant_form_subset_orbits(G, (x, y))
    stabilizer = discriminant_form_stabilizer(G, x)
    return (
        len(orbit) == 2
        and x in orbit
        and y in orbit
        and len(orbits) == 1
        and x in orbits[0]
        and y in orbits[0]
        and stabilizer.order() == 1
        and stabilizer.gens() == ()
    )


CATEGORY_STATEMENTS = (
    (
        "A_2 has six roots of norm 2 (SPLAG TCJKXU3D:4676, kissing number tau=6)",
        lambda _: len(a2_short_vectors_below_three()[2]) == 6,
    ),
    (
        "A_2 has three roots up to sign (the six roots in +/- pairs; SPLAG TCJKXU3D:4676)",
        lambda _: len(a2_short_vectors_below_three_up_to_sign()[2]) == 3,
    ),
    (
        "discriminant of <2> (+) U is 2 (elementary: det<2>=2, U unimodular)",
        lambda _: integral_lattice_direct_sum_discriminant() == 2,
    ),
    (
        "gluing <4> by twice its discriminant generator yields the unimodular <1> "
        "(elementary index-two overlattice computation)",
        lambda _: integral_lattice_gluing_gram_matrix() == matrix(ZZ, [[1]]),
    ),
    (
        "finite discriminant-form (Z/2)^2 under coordinate swap: generator orbit size 2, "
        "trivial pointwise stabilizer (elementary group action)",
        lambda _: discriminant_form_action_conversion(),
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)

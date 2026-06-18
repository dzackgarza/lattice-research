"""Mathematical facts for the root lattices A_2 and E_8, computed through the lattice
category constructor.

Citation contract (see the `What A Test Cites` memory): every expected value cites a
registered Zotero key + its extraction under ``theory/references/literature/`` + the
SPECIFIC line range that states (or, with an explicit derivation, implies) the value.

Verified extraction lines used here:
  - ``theory/references/literature/conway1999sphere.md``
      :4379  "The glue group is L*/L, of order det L"  (glue group = discriminant group)
      :4655  for A_n: glue group is cyclic C_{n+1}; norm of glue vector [i] is i*j/(n+1)
      :4682  the A_2 section: "Glue group = C_3"
    Derivation for A_2 (n=2): glue group C_3 = Z/3; glue vector [1] has i=1, j=2, so
    norm = 1*2/3 = 2/3 in Q/2Z.
  - ``theory/references/literature/nikulin1979integral.md``
      :120   "U and E_8 ... the even unimodular lattices of signatures (1,1) and (0,8)"

BLOCKER (must be resolved before this is contract-compliant): the keys
``conway1999sphere`` and ``nikulin1979integral`` are NOT yet registered in
``theory/references/references.bib`` (the extraction files exist; the bib keys do not).
The bibliographic_key field below is therefore pending registration — it is not invented
here. Do not run this as a gating test until the keys are registered.

Each assertion is a real mathematical computation. The test passes only when the backend
correctly recovers the cited value; it is red while the backend is incomplete. It never
asserts software properties (raises, non-None, type, source-string).
"""

from __future__ import annotations

import importlib

from sage.all import ZZ

importlib.import_module("category_specs")
Lattices = importlib.import_module("category_specs.lattices").Lattices


def _ctor():
    return Lattices(ZZ).Constructors()


class TestA2:
    """A_2 root lattice. Source: conway1999sphere.md:4379,4655,4682 (key pending)."""

    def test_discriminant_group_is_cyclic_order_three(self) -> None:
        # conway1999sphere.md:4682 "Glue group = C_3"; :4379 glue group = L*/L.
        # :4655 norm of [1] = 1*2/3 = 2/3 in Q/2Z.
        D = _ctor().IntegralLattice(cartan_type="A2").discriminant_group()
        assert D.cardinality() == 3
        assert D.gens()[0].q() == ZZ(2) / ZZ(3)

    def test_is_not_unimodular(self) -> None:
        # nikulin1979integral.md:118 unimodular iff discr = +/-1; A_2 has det 3 (glue
        # group C_3 nontrivial, conway1999sphere.md:4682), hence not unimodular.
        assert _ctor().IntegralLattice(cartan_type="A2").is_unimodular() is False

    def test_inclusion_into_dual_is_not_an_isomorphism(self) -> None:
        # conway1999sphere.md:4379 the canonical L -> L* has cokernel the glue group L*/L,
        # which for A_2 is C_3 (nontrivial), so the inclusion is not an isomorphism.
        L = _ctor().IntegralLattice(cartan_type="A2")
        iota = L.inclusion_morphism()
        assert iota.domain() == L
        assert iota.codomain() == L.dual_lattice()
        assert iota.is_isomorphism() is False


class TestE8:
    """E_8 root lattice. Source: nikulin1979integral.md:120 (key pending)."""

    def test_is_even_unimodular(self) -> None:
        # nikulin1979integral.md:120 E_8 is the even unimodular lattice of signature (0,8).
        assert _ctor().IntegralLattice(cartan_type="E8").is_unimodular() is True

    def test_discriminant_group_is_trivial(self) -> None:
        # Unimodular (nikulin1979integral.md:120) => discriminant group L*/L is trivial
        # (conway1999sphere.md:4379: glue group has order det L = 1).
        assert _ctor().IntegralLattice(cartan_type="E8").discriminant_group().cardinality() == 1

    def test_inclusion_into_dual_is_an_isomorphism(self) -> None:
        # E_8 = E_8* (unimodular), so the canonical inclusion is an isomorphism.
        assert _ctor().IntegralLattice(cartan_type="E8").inclusion_morphism().is_isomorphism() is True

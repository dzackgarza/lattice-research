"""Exact algebraic geometry nouns for the Coble project.

This module provides general nouns for algebraic varieties, divisors, morphisms,
and their specializations to curves and surfaces relevant to the Coble moduli.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Self

from coble_geometry_foundation import Lattice

if TYPE_CHECKING:
    from sage.matrix.matrix import Matrix
    from sage.rings.ideal import Ideal
    from sage.rings.polynomial.multi_polynomial import MPolynomial
    from sage.rings.ring import Ring

_LOGGER = logging.getLogger(__name__)


# ============================================================================
# FOUNDATIONAL NOUNS: ABSTRACT INTERFACES
# ============================================================================


class Variety(ABC):
    """Base class for any algebraic variety.

    Implementation notes:
    - Each Variety should maintain an underlying Sage scheme object
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/scheme.html)
      for computations. Use self._sage_scheme to access e.g. dimension(),
      Hom spaces, point enumeration, Jacobian, etc.
    - For embedded varieties (e.g. curves in P^2, surfaces in P^3),
      maintain the embedding context: self._embedding maps to the
      ambient projective space, so we can compute adjunction, normal
      bundles, etc.
    - Concrete implementations should provide classmethods:
      - from_equations(equations: list, ambient: Variety) -> Self
      - from_ideal(ideal: Ideal, ambient: Variety) -> Self
    - Sage's algebraic schemes compute Jacobian, codimension(),
      defining ideals, irreducible components automatically.
    """

    # _sage_scheme: sage.schemes.generic.scheme.Scheme
    #   The underlying Sage scheme object (e.g., Scheme, AlgebraicScheme)
    # _embedding: dict  # { 'into': Variety, 'by': morphism }

    @abstractmethod
    def dimension(self) -> int:
        """Return the dimension of this variety.

        Delegates to self._sage_scheme.dimension().
        """
        ...

@abstractmethod
def is_irreducible(self) -> bool:
    """Check if the variety is irreducible.

    Delegates to self._sage_scheme.is_irreducible().
    """
    ...

@abstractmethod
def is_smooth(self) -> bool:
    """Check if the variety is smooth (non-singular)."""
    ...

@abstractmethod
def is_reduced(self) -> bool:
    """Check if the variety is reduced."""
    ...

@abstractmethod
def is_normal(self) -> bool:
    """Check if the variety is normal."""
    ...

@abstractmethod
def is_complete(self) -> bool:
    """Check if the variety is complete (proper)."""
    ...

@abstractmethod
def is_projective(self) -> bool:
    """Check if the variety is projective."""
    ...

@abstractmethod
def is_affine(self) -> bool:
    """Check if the variety is affine."""
    ...

@abstractmethod
def is_quasi_projective(self) -> bool:
    """Check if the variety is quasi-projective."""
    ...

@abstractmethod
def singular_locus(self) -> Subvariety:
    """Return the singular locus as a subvariety."""
    ...

@abstractmethod
def smooth_locus(self) -> Variety:
    """Return the smooth locus (complement of singular locus)."""
    ...

@abstractmethod
def is_snc(self) -> bool:
    """Check if the variety is simple normal crossing (snc)."""
    ...

@abstractmethod
def is_hypersurface(self) -> bool:
    """Check if the variety is a hypersurface in its ambient space.

    See https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/hypersurface.html
    """
    ...

@abstractmethod
def is_complete_intersection(self) -> bool:
    """Check if the variety is a complete intersection."""
    ...

@abstractmethod
def is_calabi_yau(self) -> bool:
    """Check if the variety is a Calabi-Yau (trivial canonical bundle)."""
    ...

@abstractmethod
def is_general_type(self) -> bool:
    """Check if the variety is of general type (big canonical bundle)."""
    ...

@abstractmethod
def is_rational(self) -> bool:
    """Check if the variety is rational (birational to P^n)."""
    ...

@abstractmethod
def is_unirational(self) -> bool:
    """Check if the variety is unirational."""
    ...

# -------------------------------------------------------------------------
# Numerical invariants
# -------------------------------------------------------------------------

@abstractmethod
def kodaira_dimension(self) -> int:
    """Return the Kodaira dimension $\\kappa(X)$."""
    ...

@abstractmethod
def hilbert_polynomial(self) -> "MPolynomial":
    """Return the Hilbert polynomial."""
    ...

@abstractmethod
def holomorphic_euler_characteristic(self) -> int:
    """Return the holomorphic Euler characteristic $\\chi(\\mathcal{O}_X)$."""
    ...

@abstractmethod
def hodge_number(self, p: int, q: int) -> int:
    """Return the Hodge number $h^{p,q}$."""
    ...

# -------------------------------------------------------------------------
# Base ring
# -------------------------------------------------------------------------

@abstractmethod
def base_ring(self) -> Ring:
        """Return the base ring (typically ZZ or a field)."""
        ...

    # -------------------------------------------------------------------------
    # Hodge-theoretic invariants (well-defined for proper varieties)
    # -------------------------------------------------------------------------

    @abstractmethod
    def p_arithmetic(self) -> int:
        r"""
        Return the arithmetic genus $p_a(X) = (-1)^{\dim X}(\chi(\mathcal{O}_X) - 1)$.

        For curves: $p_a = g - \delta$ where $g$ is geometric genus and $\delta$ is
        the number of nodes.
        """
        ...

    @abstractmethod
    def p_geometric(self) -> int:
        r"""
        Return the geometric genus $p_g = h^0(X, K_X)$.

        For surfaces: $p_g = h^{2,0}$.
        """
        ...

    @abstractmethod
    def q(self) -> int:
        """Return the irregularity $q = h^1(\\mathcal{O}_X)$."""
        ...

    @abstractmethod
    def canonical_class(self) -> Divisor:
        r"""Return the canonical class $K_X$."""
        ...

    def canonical_divisor(self) -> Divisor:
        """Alias for canonical_class()."""
        return self.canonical_class()

    # -------------------------------------------------------------------------
    # Picard group (for proper varieties)
    # -------------------------------------------------------------------------

    @abstractmethod
    def picard_group(self) -> PicardGroup:
        r"""Return the Picard group $\mathrm{Pic}(X)$ as divisor classes modulo linear equivalence."""
        ...

    @abstractmethod
    def picard_lattice(self) -> PicardeLattice:
        r"""Return the Picard lattice with intersection form."""
        ...

    # -------------------------------------------------------------------------
    # Birational operations
    # -------------------------------------------------------------------------

    @abstractmethod
    def blowup(self, center: Subvariety) -> Variety:
        """Return the blowup of this variety along the center."""
        ...

    @abstractmethod
    def resolve_singularities(self) -> Variety:
        """Return a resolution of singularities."""
        ...


class Subvariety(ABC):
    """A closed subscheme of a variety.

    Implementation notes:
    - Each Subvariety should maintain an underlying Sage subscheme object
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/algebraic_scheme.html)
      accessible via self._sage_subscheme.
    - Sage's algebraic schemes provide: Jacobian matrix, codimension(),
      defining_ideal(), irreducible_components(), is_irreducible(), etc.
    """

    # _sage_subscheme: sage.schemes.generic.algebraic_scheme.AlgebraicScheme_subscheme

    @abstractmethod
    def ambient(self) -> Variety:
        """Return the ambient variety containing this subvariety."""
        ...

    @abstractmethod
    def defining_ideal(self) -> Ideal:
        """Return the defining ideal in the coordinate ring of the ambient."""
        ...

    @abstractmethod
    def dimension(self) -> int:
        """Return the dimension of this subvariety."""
        ...

    @abstractmethod
    def codimension(self) -> int:
        """Return the codimension in the ambient variety."""
        ...


class Point(ABC):
    """A rational point on a variety.

    Implementation notes:
    - Each Point should maintain an underlying Sage scheme point
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/point.html)
      accessible via self._sage_point.
    - The Sage point provides coordinate access, reduction modulo
      prime ideals, etc.
    """

    # _sage_point: sage.schemes.generic.point.SchemePoint

    @abstractmethod
    def variety(self) -> Variety:
        """Return the variety on which this point lies."""
        ...

    @abstractmethod
    def coordinates(self, chart: str | None = None) -> list:
        r"""
        Return coordinates of this point.

        Args:
            chart: Choose an affine or projective chart, e.g., "affine_xy",
                   "projective_xyz", "D(x0)", etc.
        """
        ...

    @abstractmethod
    def coordinate_ring(self) -> Ring:
        """Return the coordinate ring of the point (local ring)."""
        ...


class Divisor(ABC):
    """A Weil/Cartier divisor = integer linear combination of prime divisors.

    Implementation notes:
    - Concrete implementations should maintain an underlying Sage divisor
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/divisor.html)
      accessible via self._sage_divisor.
    - Sage divisors provide: is_effective(), intersection(),
      linear_equivalence(), coefficients(), etc.
    """

    # _sage_divisor: sage.schemes.generic.divisor.Divisor

    @abstractmethod
    def as_prime_divisor(self) -> PrimeDivisor:
        """Return as a prime divisor if applicable, raise otherwise."""
        ...

    def is_prime(self) -> bool:
        """Check if this divisor is prime (an irreducible codimension 1 subvariety)."""
        try:
            self.as_prime_divisor()
            return True
        except (TypeError, ValueError):
            return False

    @abstractmethod
    def coefficients(self) -> dict[PrimeDivisor, int]:
        """Return the dictionary of prime divisors and their coefficients."""
        ...

    @abstractmethod
    def is_principal(self) -> bool:
        """Check if linearly equivalent to 0."""
        ...

    @abstractmethod
    def is_effective(self) -> bool:
        """Check if $D \geq 0$ (effective divisor)."""
        ...

    @abstractmethod
    def is_ample(self) -> bool:
        """Check if the divisor is ample."""
        ...

    @abstractmethod
    def is_nef(self) -> bool:
        """Check if numerically effective (nef)."""
        ...

    @abstractmethod
    def self_intersection(self) -> int:
        """Return the self-intersection $D^2$."""
        ...

@abstractmethod
def intersection(self, other: Divisor) -> int:
    """Return the intersection number $D \cdot E$."""
    ...

# -------------------------------------------------------------------------
# Riemann-Roch and linear systems
# -------------------------------------------------------------------------

@abstractmethod
def riemann_roch_space_dimension(self) -> int:
    r"""Return $\ell(D) = \dim H^0(X, \mathcal{O}_X(D))$."""
    ...

@abstractmethod
def index_of_speciality(self) -> int:
    r"""Return the index of speciality $i = \ell(K_X - D)$."""
    ...

# -------------------------------------------------------------------------
# Divisor properties
# -------------------------------------------------------------------------

@abstractmethod
def is_weyl_divisor(self) -> bool:
    """Check if this is a Weil divisor (codimension 1 subvariety)."""
    ...

@abstractmethod
def is_cartier_divisor(self) -> bool:
    """Check if this is a Cartier divisor (locally principal)."""
    ...

@abstractmethod
def is_numerically_effective(self) -> bool:
    """Alias for is_nef: numerically effective."""
    ...

# -------------------------------------------------------------------------
# Divisor operations
# -------------------------------------------------------------------------

@classmethod
@abstractmethod
def from_meromorphic_function(cls, f: "MPolynomial", domain: Variety) -> Self:
    """Construct the divisor of a meromorphic function $f$."""
    ...

@abstractmethod
def is_linearly_equivalent_to(self, other: Divisor) -> bool:
    """Check if this divisor is linearly equivalent to another."""
    ...

@abstractmethod
def is_canonical_divisor(self) -> bool:
    """Check if this divisor is a canonical divisor $K_X$."""
    ...

@abstractmethod
def is_prime_divisor(self) -> bool:
    """Check if this is a prime divisor (irreducible)."""
    ...

@abstractmethod
def ord_D(self, f: "MPolynomial") -> int:
    r"""Return the order of vanishing of $f$ along $D$, i.e. $\mathrm{ord}_D(f)$.

    This is the length of $\mathcal{O}_{X,D}/(f)$.
    """
    ...

@abstractmethod
def to_coherent_sheaf(self) -> "CoherentSheaf":
    r"""Return the associated rank-1 coherent sheaf $\mathcal{O}_X(D)$."""
    ...

@abstractmethod
def pullback(self, f: Morphism) -> Divisor:
    """Return the pullback $f^*(D)$."""
    ...

@abstractmethod
def pushforward(self, f: Morphism) -> Divisor:
    """Return the pushforward $f_*(D)$."""
    ...


class PrimeDivisor(Divisor):
    """An irreducible codimension 1 subvariety (prime divisor)."""

    @abstractmethod
    def underlying_subvariety(self) -> Subvariety:
        """Return the underlying subvariety."""
        ...


class AbelianGroup(ABC):
    """Abstract base for abelian groups."""

    @abstractmethod
    def rank(self) -> int:
        """Return the rank (free part)."""
        ...

    @abstractmethod
    def torsion(self) -> list:
        """Return the torsion part as a list of cyclic groups."""
        ...

    @abstractmethod
    def generators(self) -> list:
        """Return a set of generators."""
        ...


class PicardGroup(AbelianGroup):
    """Divisor classes modulo linear equivalence: $\mathrm{Pic}(X) \cong \mathbb{Z}^r \oplus \mathrm{Tors}$."""

    @abstractmethod
    def variety(self) -> Variety:
        """Return the variety whose Picard group this is."""
        ...

    @abstractmethod
    def intersection_matrix(self) -> Matrix:
        """Return the intersection form matrix on generators."""
        ...


class PicardeLattice(Lattice):
    """The Picard lattice $\mathrm{Pic}(X)$ equipped with the intersection form."""

    @abstractmethod
    def underlying_picard_group(self) -> PicardGroup:
        """Return the underlying Picard group."""
        ...


class LinearSystem(ABC):
    """Complete linear system $|D| = \mathbb{P}H^0(X, \mathcal{O}(D))$."""

    @abstractmethod
    def divisor(self) -> Divisor:
        """Return the divisor $D$ such that this is $|D|$."""
        ...

    @abstractmethod
    def dimension(self) -> int:
        r"""Return $\dim |D| = h^0(\mathcal{O}(D)) - 1$."""
        ...

    @abstractmethod
    def base_locus(self) -> Subvariety:
        """Return the base locus (fixed component)."""
        ...

    @abstractmethod
    def general_element(self) -> Divisor:
        """Return a general element of the linear system."""
        ...


class Morphism(ABC):
    """A morphism of varieties $f: X \to Y$.

    Implementation notes:
    - Concrete implementations should maintain an underlying Sage morphism
      (see https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/morphism.html)
      accessible via self._sage_morphism.
    - Sage morphisms provide: degree(), is_finite(), fiber(),
      exceptional_locus(), etc.
    """

    # _sage_morphism: sage.schemes.generic.morphism.SchemeMorphism

    @abstractmethod
    def domain(self) -> Variety:
        """Return the source variety $X$."""
        ...

    @abstractmethod
    def codomain(self) -> Variety:
        """Return the target variety $Y$."""
        ...

    @abstractmethod
    def degree(self) -> int:
        """Return the degree of the morphism."""
        ...

    @abstractmethod
    def is_finite(self) -> bool:
        """Check if the morphism is finite."""
        ...

    @abstractmethod
    def is_étale(self) -> bool:
        """Check if the morphism is étale."""
        ...


class BirationalMap(ABC):
    """A birational map $X \dashrightarrow Y$."""

    @abstractmethod
    def is_morphism(self) -> bool:
        """Check if the map is actually a regular morphism."""
        ...

    @abstractmethod
    def as_morphism(self) -> Morphism:
        """Return as a regular morphism if possible."""
        ...

    @abstractmethod
    def inverse(self) -> BirationalMap:
        """Return the inverse birational map."""
        ...

    @abstractmethod
    def exceptional_divisor(self) -> Divisor:
        """Return the exceptional divisor of the birational map."""
        ...


# ============================================================================
# SPECIALIZATIONS: DIMENSION 1 (CURVES)
# ============================================================================


class Curve(Variety):
    """Algebraic curve (dimension 1)."""

    @abstractmethod
    def genus(self) -> int:
        """Return the geometric genus $g = p_g$ for curves."""
        ...

    @abstractmethod
    def arithmetic_genus(self) -> int:
        """Return the arithmetic genus $p_a$."""
        ...

    @abstractmethod
    def degree(self) -> int:
        """Return the degree as a curve in projective space."""
        ...

    @abstractmethod
    def normalization(self) -> Curve:
        """Return the normalization (smooth model)."""
        ...

    def dimension(self) -> int:
        return 1


class PlaneCurve(Curve):
    """A curve embedded in the projective plane $\mathbb{P}^2$."""

    @abstractmethod
    def equation(self) -> MPolynomial:
        """Return the homogeneous equation $F(x,y,z) = 0$ defining the curve."""
        ...

    @abstractmethod
    def degree(self) -> int:
        """Return the degree of the curve."""
        ...

    @abstractmethod
    def dual_curve(self) -> PlaneCurve:
        """Return the dual plane curve in $(\mathbb{P}^2)^\vee$."""
        ...


class RationalSextic(PlaneCurve):
    """A rational plane sextic curve of degree 6."""

    @abstractmethod
    def is_nodal(self) -> bool:
        """Check if the sextic is nodal (has only nodes as singularities)."""
        ...

    @abstractmethod
    def nodes(self) -> list[Point]:
        """Return the list of node singularities as points in $\mathbb{P}^2$."""
        ...

    @abstractmethod
    def normalization(self) -> Curve:
        """Return the normalization, which is $\mathbb{P}^1$ for rational curves."""
        ...


# ============================================================================
# SPECIALIZATIONS: DIMENSION 2 (SURFACES)
# ============================================================================


class Surface(Variety):
    """Algebraic surface (dimension 2)."""

    def dimension(self) -> int:
        return 1  # sic: dimension returns the dimension of the variety

    @abstractmethod
    def birational_involution(self) -> Morphism:
        """Return a birational involution if present (e.g., for Enriques surfaces)."""
        ...


class ProjectivePlane(Surface):
    """The projective plane $\mathbb{P}^2$."""

    @classmethod
    def standard(cls) -> Self:
        """Return the standard $\mathbb{P}^2$."""
        ...


class Blowup(Surface):
    """A blowup of a surface at a center (points or curves)."""

    @abstractmethod
    def original_surface(self) -> Surface:
        """Return the original surface before blowing up."""
        ...

    @abstractmethod
    def center(self) -> Subvariety:
        """Return the center being blown up."""
        ...

    @abstractmethod
    def exceptional_divisor(self) -> PrimeDivisor:
        """Return the exceptional divisor (or their union)."""
        ...


class CobleSurface(Blowup):
    r"""Coble surface $= \mathrm{Bl}_{p_1,\dots,p_{10}}\mathbb{P}^2$.

    The surface obtained by blowing up $\mathbb{P}^2$ at the 10 nodes of a rational
    sextic curve. The Picard lattice is $S_{\mathrm{Co}} \cong \langle 2 \rangle
    \oplus \langle -2 \rangle^{10}$ with signature $(1, 10)$.
    """

    @classmethod
    @abstractmethod
    def from_singular_sextic(cls, sextic: RationalSextic) -> Self:
        """Construct as blowup at the nodes of a singular sextic curve."""
        ...

    @classmethod
    @abstractmethod
    def from_nodes(cls, points: list[Point]) -> Self:
        r"""Construct from 10 points in $\mathbb{P}^2$.

        The 10 points should be the nodes of some rational sextic.
        """
        ...

    @abstractmethod
    def underlying_curve(self) -> RationalSextic:
        """Return the rational sextic whose nodes were blown up."""
        ...

    @abstractmethod
    def exceptional_divisors(self) -> list[PrimeDivisor]:
        """Return the 10 exceptional divisors $E_1, \dots, E_{10}$."""
        ...

    @abstractmethod
    def coble_lattice(self) -> PicardeLattice:
        r"""Return the Coble Picard lattice $\langle 2 \rangle \oplus \langle -2 \rangle^{10}$."""
        ...


# ============================================================================
# BRANCHED COVER CONSTRUCTIONS
# ============================================================================


class BranchedCoverConstruction(ABC):
    r"""A branched cover $Y \to X$ branched over a divisor $D \subset X$."""

    @abstractmethod
    def base(self) -> Variety:
        """Return the base variety $X$."""
        ...

    @abstractmethod
    def branch_divisor(self) -> Divisor:
        r"""Return the branch divisor $D \subset X$."""
        ...

    @abstractmethod
    def ramification_divisor(self) -> Divisor:
        r"""Return the ramification divisor $R \subset Y$ where $\pi$ is ramified."""
        ...

    @abstractmethod
    def degree(self) -> int:
        """Return the degree of the covering."""
        ...

    @abstractmethod
    def total_space(self) -> Variety:
        """Return the total space $Y$ (the covering variety)."""
        ...


class DoubleCover(BranchedCoverConstruction):
    r"""A double (2-sheeted) cover branched over an even-degree divisor."""

    def degree(self) -> int:
        return 2


class K3DoubleCover(DoubleCover):
    r"""Double cover of $\mathbb{P}^2$ branched over a sextic curve.

    The covering surface is a K3 surface $X$ given by $w^2 = F(x,y,z)$ in
    the weighted projective space $\mathbb{P}(1,1,1,3)$.
    """

    @abstractmethod
    def branch_sextic(self) -> RationalSextic:
        """Return the branch sextic curve."""
        ...

    @abstractmethod
    def cover_surface(self) -> Surface:
        """Return the K3 surface."""
        ...


class EnriquesQuotient(ABC):
    r"""Quotient of a K3 surface by a fixed-point-free involution.

    The quotient $Z = X/\iota_{\mathrm{En}}$ is an Enriques surface with
    $2K_Z \sim 0$.
    """

    @abstractmethod
    def k3_cover(self) -> Surface:
        """Return the covering K3 surface $X$."""
        ...

    @abstractmethod
    def involution(self) -> Morphism:
        r"""Return the Enriques involution $\iota_{\mathrm{En}}: X \to X$."""
        ...

@abstractmethod
def quotient_surface(self) -> Surface:
    """Return the Enriques surface $Z = X/\iota_{\mathrm{En}}$."""
    ...


# ============================================================================
# COHERENT SHEAVES
# ============================================================================


class CoherentSheaf(ABC):
    """A coherent sheaf on a variety.

    Implementation notes:
    - Concrete implementations wrap Sage sheaves
      (see sage.categories.sheaves Sheaf) and provide
      h^0, h^1, Euler characteristic, Chern class, etc.
    """

    @abstractmethod
    def variety(self) -> Variety:
        """Return the variety on which this sheaf is defined."""
        ...

    @abstractmethod
    def rank(self) -> int:
        """Return the rank of the sheaf."""
        ...

    @abstractmethod
    def h0(self) -> int:
        r"""Return $h^0(\mathcal{F}) = \dim H^0(X, \mathcal{F})$."""
        ...

    @abstractmethod
    def h1(self) -> int:
        r"""Return $h^1(\mathcal{F}) = \dim H^1(X, \mathcal{F})$."""
        ...

    @abstractmethod
    def euler_characteristic(self) -> int:
        r"""Return $\chi(\mathcal{F}) = \sum (-1)^i h^i(\mathcal{F})$."""
        ...


# ============================================================================
# FAMILIES OF VARIETIES
# ============================================================================


class FamilyOfVarieties(ABC):
    r"""A family of varieties $\mathcal{X} \to S$ over a base scheme.

    This represents a morphism $f: \mathcal{X} \to S$ where each fiber
    $X_s = f^{-1}(s)$ is a variety. Used for degenerations, moduli,
    and specialization.

    Implementation notes:
    - Maintains the total space and base scheme
    - Provides methods for Specialization, monodromy, etc.
    """

    @abstractmethod
    def total_space(self) -> Variety:
        r"""Return the total space $\mathcal{X}$."""
        ...

    @abstractmethod
    def base(self) -> Variety:
        """Return the base scheme $S$."""
        ...

    @abstractmethod
    def morphism(self) -> Morphism:
        r"""Return the structure morphism $\mathcal{X} \to S$."""
        ...

    @abstractmethod
    def fiber(self, s: Point) -> Variety:
        r"""Return the fiber $X_s$ over the point $s \in S$."""
        ...

    @abstractmethod
    def specialization(self, s: Point) -> Variety:
        r"""Return the specialized variety at the point $s$.

        For example, at a point in the boundary of a compactification,
        this returns the special fiber (stable model).
        See https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/generic/algebraic_scheme.html
        for degeneration handling.
        """
        ...

    @abstractmethod
    def monodromy(self, loop: Point) -> list:
        r"""Return the monodromy action on cohomology around a loop."""
        ...

    @abstractmethod
    def limit_period(self, boundary_point: Point) -> "Variety":
        """Return the limiting period ( Hodge structure) at a boundary point."""
        ...


# ============================================================================
# RAMIFICATION (for branched covers)
# ============================================================================


class BranchedCoverConstruction(ABC):
    r"""A branched cover $Y \to X$ branched over a divisor $D \subset X$."""

    @abstractmethod
    def base(self) -> Variety:
        """Return the base variety $X$."""
        ...

    @abstractmethod
    def branch_divisor(self) -> Divisor:
        r"""Return the branch divisor $D \subset X$."""
        ...

    @abstractmethod
    def ramification_divisor(self) -> Divisor:
        r"""Return the ramification divisor $R \subset Y$ where $\pi$ is ramified."""
        ...

    @abstractmethod
    def degree(self) -> int:
        """Return the degree of the covering."""
        ...

    @abstractmethod
    def total_space(self) -> Variety:
        """Return the total space $Y$ (the covering variety)."""
        ...

    # -------------------------------------------------------------------------
    # Ramification data
    # -------------------------------------------------------------------------

    @abstractmethod
    def ramification_index(self, point: Point) -> int:
        r"""Return the ramification index $e_p$ at a point $p \in Y$.

        For a point $p \in Y$ lying over $q \in X$, the ramification index
        is the integer $e_p$ such that $\pi^*(t) = u \cdot t^{e_p}$ locally,
        where $t$ is a uniformizer at $q$.
        """
        ...

    @abstractmethod
    def ramification_divisor_as_divisor(self) -> Divisor:
        r"""Return the ramification divisor as a divisor $R = \sum (e_p - 1) p$."""
        ...

    @abstractmethod
    def branch_divisor_as_divisor(self) -> Divisor:
        r"""Return the branch divisor as a divisor $B = \sum m_q q$."""
        ...

    @abstractmethod
    def satisfies_riemann_hurwitz(self) -> bool:
        r"""Verify that the Riemann-Hurwitz formula holds:

        $\chi(Y) = d \cdot \chi(X) + \sum_p (e_p - 1)$

        for degree $d$ cover with ramification indices $e_p$.
        """
        ...


# Ring, Ideal, Matrix, MPolynomial are imported from Sage in concrete implementations
# See TYPE_CHECKING block at top of file

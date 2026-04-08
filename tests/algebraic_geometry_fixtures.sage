# ============================================================================
# ALGEBRAIC GEOMETRY FIXTURES
#
# Comprehensive standard examples with all classical invariants asserted
# concretely.  Properties follow from adjunction, Riemann-Roch, Noether,
# the degree-genus formula, Hodge theory, and related classical results.
#
# Hodge diamond convention (matching variety_interface_spec.sage):
#   Matrix entry (p, q) = h^{p,q},  rows indexed by p from 0 upward.
#
# ============================================================================


# ============================================================================
# 1. PROJECTIVE SPACES PP^1, PP^2, PP^3
# ============================================================================

# K_{PP^n} = -(n+1)H  (general adjunction formula for projective space)
# Hodge numbers: h^{p,q}(PP^n) = delta_{p,q}  (only diagonal entries non-zero)
# Pic(PP^n) = ZZ * H  (Lefschetz; rank 1)
# Kodaira dimension: -Infinity  (K anti-ample)
# Hilbert polynomial: P(t) = C(t+n, n) = (t+1)(t+2)...(t+n)/n!

t = polygen(QQ, 't')

# --- PP^1 -------------------------------------------------------------------

P1 = ProjectiveSpace(1, CC)
assert P1.dimension() == 1
assert P1.is_smooth() and P1.is_projective()
assert P1.is_rational() and not P1.is_elliptic()
assert P1.geometric_genus() == 0 and P1.arithmetic_genus() == 0
assert P1.irregularity() == 0
assert P1.kodaira_dimension() == -Infinity

H1 = P1.hyperplane_class()      # class of a point; deg(H) = 1
assert P1.canonical_divisor() == -2 * H1   # K_{PP^1} = -2H

# Pic(PP^1) = ZZ * H
assert P1.picard_group().rank() == 1
assert H1.self_intersection() == 1   # two points on PP^1 "meet" with multiplicity 1

# Hodge diamond for PP^1:
#   p\q  0  1
#    0  [1  0]
#    1  [0  1]
assert P1.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])

# Noether for a curve: deg K_C = 2g - 2  =>  deg(-2H) = -2 = 2*0 - 2 ✓
assert P1.canonical_divisor().degree() == -2

assert P1.hilbert_polynomial(t) == t + 1

# Riemann-Roch on PP^1: for D = d*H, chi(O(d)) = d + 1
for d in range(-3, 6):
    D = d * H1
    assert D.hirzebruch_riemann_roch() == d + 1


# --- PP^2 -------------------------------------------------------------------

P2 = ProjectiveSpace(2, CC)
assert P2.dimension() == 2
assert P2.is_smooth() and P2.is_projective()
assert P2.is_rational()
assert P2.geometric_genus() == 0 and P2.irregularity() == 0
assert P2.kodaira_dimension() == -Infinity

H2 = P2.hyperplane_class()      # class of a line in PP^2
assert P2.canonical_divisor() == -3 * H2   # K_{PP^2} = -3H

# H^2 = 1  (two general lines in PP^2 meet in one point)
assert H2.self_intersection() == 1

# Pic(PP^2) = ZZ * H
assert P2.picard_group().rank() == 1

# Hodge diamond:
#   p\q  0  1  2
#    0  [1  0  0]
#    1  [0  1  0]
#    2  [0  0  1]
assert P2.hodge_diamond() == Matrix(ZZ, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# Noether: K^2 + chi_top = 12*chi(O)  =>  9 + 3 = 12*1 ✓
assert P2.canonical_divisor().self_intersection() == 9
assert P2.topological_euler_characteristic() == 3
assert P2.holomorphic_euler_characteristic() == 1

# Hilbert polynomial: P(t) = (t+1)(t+2)/2
assert P2.hilbert_polynomial(t) == (t + 1) * (t + 2) / 2

# Riemann-Roch on PP^2: for D = d*H, chi(O_{PP^2}(d)) = (d+1)(d+2)/2
for d in range(0, 6):
    D = d * H2
    assert D.hirzebruch_riemann_roch() == (d + 1) * (d + 2) // 2


# --- PP^3 -------------------------------------------------------------------

P3 = ProjectiveSpace(3, CC)
assert P3.dimension() == 3
assert P3.is_smooth() and P3.is_projective()
assert P3.is_rational()
assert P3.kodaira_dimension() == -Infinity

H3 = P3.hyperplane_class()
assert P3.canonical_divisor() == -4 * H3   # K_{PP^3} = -4H

# Hodge diamond:
#   p\q  0  1  2  3
#    0  [1  0  0  0]
#    1  [0  1  0  0]
#    2  [0  0  1  0]
#    3  [0  0  0  1]
assert P3.hodge_diamond() == Matrix(ZZ, [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

assert P3.holomorphic_euler_characteristic() == 1
assert P3.picard_group().rank() == 1


# ============================================================================
# 2. SMOOTH PLANE CURVES IN PP^2
# ============================================================================

# For a smooth plane curve C of degree d in PP^2 (adjunction):
#   K_C = (K_{PP^2} + C)|_C = (-3H + dH)|_C = (d-3) H|_C
#   deg K_C = (d-3)*d
#   genus: g = (d-1)(d-2)/2
#   chi(O_C) = 1 - g
#   Kodaira dimension:
#     d <= 2 (g = 0): kappa = -Infinity  (rational)
#     d = 3  (g = 1): kappa = 0          (elliptic)
#     d >= 4 (g >= 3): kappa = 1         (general type)

R3.<x,y,z> = PolynomialRing(CC, 3)

# --- Degree 1: Line V(x) in PP^2 -------------------------------------------

L = Variety(x)
assert L.degree() == 1
assert L.is_smooth() and L.dimension() == 1
assert L.arithmetic_genus() == 0 and L.geometric_genus() == 0
assert L.irregularity() == 0

# K_L = (1-3)H|_L = -2H|_L  (same as K_{PP^1}; deg = -2)
H_L = L.hyperplane_class()
assert L.canonical_divisor() == -2 * H_L
assert L.canonical_divisor().degree() == -2

assert L.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert L.kodaira_dimension() == -Infinity
assert L.is_rational() and L.is_isomorphic_to(PP^1(CC))
assert L.holomorphic_euler_characteristic() == 1

assert L.hilbert_polynomial(t) == t + 1    # d*t + (1 - p_a) = t + 1


# --- Degree 2: Smooth Conic V(x^2 + y^2 + z^2) ----------------------------
# Smooth conic in PP^2 is isomorphic to PP^1 (rational normal curve of degree 2)

conic = Variety(x^2 + y^2 + z^2)
assert conic.degree() == 2
assert conic.is_smooth() and conic.dimension() == 1
assert conic.arithmetic_genus() == 0 and conic.geometric_genus() == 0

H_conic = conic.hyperplane_class()
# K = (2-3)H|_conic = -H|_conic, deg = -2
assert conic.canonical_divisor() == -1 * H_conic
assert conic.canonical_divisor().degree() == -2

assert conic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert conic.kodaira_dimension() == -Infinity
assert conic.is_rational() and conic.is_isomorphic_to(PP^1(CC))
assert conic.holomorphic_euler_characteristic() == 1

assert conic.hilbert_polynomial(t) == 2*t + 1


# --- Degree 3: Smooth Elliptic Curve V(x^3 + y^3 + z^3) -------------------
# Smooth plane cubic: g = 1, Calabi-Yau curve, K = 0

elliptic = Variety(x^3 + y^3 + z^3)
assert elliptic.degree() == 3
assert elliptic.is_smooth() and elliptic.dimension() == 1
assert elliptic.arithmetic_genus() == 1 and elliptic.geometric_genus() == 1
assert elliptic.irregularity() == 1   # q = h^{0,1} = g = 1

H_ell = elliptic.hyperplane_class()
# K_C = (3-3)H|_C = 0: trivial canonical bundle
assert elliptic.canonical_divisor() == 0
assert elliptic.canonical_divisor().degree() == 0

# Hodge diamond for genus-1 curve:
#   p\q  0  1
#    0  [1  1]
#    1  [1  1]
assert elliptic.hodge_diamond() == Matrix(ZZ, [[1, 1], [1, 1]])

assert elliptic.kodaira_dimension() == 0   # K trivial: Calabi-Yau
assert elliptic.is_elliptic() and elliptic.is_calabi_yau()
assert not elliptic.is_rational()
assert elliptic.holomorphic_euler_characteristic() == 0   # chi = 1 - g = 0

# Hilbert polynomial: 3*t  (since p_a=1, chi(O_C(t)) = 3t + 1 - 1 = 3t)
assert elliptic.hilbert_polynomial(t) == 3*t

# Riemann-Roch: chi(O_C(dH)) = 3d for any integer d
for d in range(0, 5):
    D = d * H_ell
    assert D.hirzebruch_riemann_roch() == 3*d


# --- Degree 4: Smooth Quartic Curve V(x^4 + y^4 + z^4) --------------------
# Smooth plane quartic: g = 3, general type

quartic_curve = Variety(x^4 + y^4 + z^4)
assert quartic_curve.degree() == 4
assert quartic_curve.is_smooth() and quartic_curve.dimension() == 1
assert quartic_curve.arithmetic_genus() == 3 and quartic_curve.geometric_genus() == 3
assert quartic_curve.irregularity() == 3

H_qc = quartic_curve.hyperplane_class()
# K_C = (4-3)H = H, deg K_C = 4
assert quartic_curve.canonical_divisor() == H_qc
assert quartic_curve.canonical_divisor().degree() == 4

# Hodge diamond for genus-3 curve
assert quartic_curve.hodge_diamond() == Matrix(ZZ, [[1, 3], [3, 1]])
assert quartic_curve.kodaira_dimension() == 1   # general type
assert quartic_curve.is_general_type() and not quartic_curve.is_rational()
assert quartic_curve.holomorphic_euler_characteristic() == -2   # 1 - 3 = -2


# --- Degree 5: Smooth Quintic Curve V(x^5 + y^5 + z^5) --------------------
# g = (5-1)(5-2)/2 = 6

quintic_curve = Variety(x^5 + y^5 + z^5)
assert quintic_curve.degree() == 5
assert quintic_curve.is_smooth() and quintic_curve.dimension() == 1
assert quintic_curve.arithmetic_genus() == 6 and quintic_curve.geometric_genus() == 6
assert quintic_curve.irregularity() == 6

H_q5c = quintic_curve.hyperplane_class()
# K_C = 2H, deg = 10
assert quintic_curve.canonical_divisor() == 2 * H_q5c
assert quintic_curve.canonical_divisor().degree() == 10

assert quintic_curve.hodge_diamond() == Matrix(ZZ, [[1, 6], [6, 1]])
assert quintic_curve.kodaira_dimension() == 1
assert quintic_curve.holomorphic_euler_characteristic() == -5


# --- Degree-genus loop: d = 1..6 (uniform verification) --------------------
# Consolidates the formulas above.  Smooth model is the Fermat curve x^d+y^d+z^d=0.

smooth_plane_curves = {
    1: x,
    2: x^2 + y^2 + z^2,
    3: x^3 + y^3 + z^3,
    4: x^4 + y^4 + z^4,
    5: x^5 + y^5 + z^5,
    6: x^6 + y^6 + z^6,
}

for d, f in smooth_plane_curves.items():
    C  = Variety(f)
    g  = (d - 1) * (d - 2) // 2    # degree-genus formula
    HC = C.hyperplane_class()

    assert C.is_smooth() and C.dimension() == 1 and C.degree() == d
    assert C.arithmetic_genus() == g and C.geometric_genus() == g
    assert C.irregularity() == g
    assert C.holomorphic_euler_characteristic() == 1 - g
    assert C.canonical_divisor().degree() == (d - 3) * d

    # Kodaira dimension by genus
    if g == 0:
        assert C.kodaira_dimension() == -Infinity and C.is_rational()
    elif g == 1:
        assert C.kodaira_dimension() == 0 and C.is_elliptic()
    else:
        assert C.kodaira_dimension() == 1 and C.is_general_type()

    # Hodge diamond
    assert C.hodge_diamond() == Matrix(ZZ, [[1, g], [g, 1]])

    # Hilbert polynomial: P(t) = d*t + (1 - g)
    assert C.hilbert_polynomial(t) == d * t + (1 - g)

    # Riemann-Roch: chi(O_C(kH)) = k*d + 1 - g  for k = 0,1,2,3
    for k in range(4):
        assert (k * HC).hirzebruch_riemann_roch() == k * d + 1 - g


# ============================================================================
# 3. SINGULAR PLANE CURVES
# ============================================================================

# --- Nodal cubic: y^2*z - x^2*(x - z) = 0 ---------------------------------
# Affine equation y^2 = x^2*(x-1); node at [0:0:1].
# p_a = 1  (from degree),  p_g = p_a - #nodes = 0.
# Normalization: PP^1.

f_node = y^2*z - x^2*(x - z)    # = -x^3 + x^2*z + y^2*z
nodal_cubic = Variety(f_node)
p_node = nodal_cubic([0, 0, 1])

assert nodal_cubic.degree() == 3
assert nodal_cubic.is_singular()
assert nodal_cubic.singular_locus() == p_node

assert p_node.is_node() and p_node.singularity_type() == Singularity("A1")
assert not p_node.is_cusp()

assert nodal_cubic.arithmetic_genus() == 1    # from degree formula
assert nodal_cubic.geometric_genus() == 0     # p_g = p_a - #nodes = 1 - 1 = 0
assert nodal_cubic.normalization().is_isomorphic_to(PP^1(CC))

# Hodge diamond uses geometric genus: p_g = q = 0
assert nodal_cubic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert nodal_cubic.kodaira_dimension() == -Infinity


# --- Cuspidal cubic: y^2*z - x^3 = 0 --------------------------------------
# Affine equation y^2 = x^3; cusp at [0:0:1].
# p_a = 1, p_g = 0.  Normalization: PP^1.

f_cusp = y^2*z - x^3
cuspidal_cubic = Variety(f_cusp)
p_cusp = cuspidal_cubic([0, 0, 1])

assert cuspidal_cubic.degree() == 3
assert cuspidal_cubic.is_singular()
assert cuspidal_cubic.singular_locus() == p_cusp

assert p_cusp.is_cusp() and p_cusp.singularity_type() == Singularity("A2")
assert not p_cusp.is_node()
# Milnor number of A2 cusp: mu = 2
assert p_cusp.milnor_number() == 2

assert cuspidal_cubic.arithmetic_genus() == 1
assert cuspidal_cubic.geometric_genus() == 0
assert cuspidal_cubic.normalization().is_isomorphic_to(PP^1(CC))

assert cuspidal_cubic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert cuspidal_cubic.kodaira_dimension() == -Infinity


# --- Rational sextic with 10 nodes -----------------------------------------
# A degree-6 curve with p_g = 0 must have p_a - p_g = 10 - 0 = 10 nodes.
# (Same curve as in variety_interface_spec, section 7.)
# p_a = (6-1)(6-2)/2 = 10,  p_g = 10 - 10 = 0.

F_sextic = (
    137*x^6
    - 79*x^5*y - 61*x^5*z
    - 244*x^4*y^2 - 423*x^4*y*z - 134*x^4*z^2
    - 438*x^3*y^3 - 585*x^3*y^2*z - 128*x^3*y*z^2 + 19*x^3*z^3
    - 279*x^2*y^4 - 606*x^2*y^3*z - 395*x^2*y^2*z^2 - 61*x^2*y*z^3 + 7*x^2*z^4
    - 137*x*y^5 - 386*x*y^4*z - 550*x*y^3*z^2 - 479*x*y^2*z^3 - 212*x*y*z^4 - 34*x*z^5
    + 9*y^6 - 54*y^5*z - 256*y^4*z^2 - 385*y^3*z^3 - 276*y^2*z^4 - 97*y*z^5 - 13*z^6
)
rational_sextic = Variety(F_sextic)

assert rational_sextic.degree() == 6
assert rational_sextic.is_singular()
assert rational_sextic.arithmetic_genus() == 10
assert rational_sextic.geometric_genus() == 0

C_sing = rational_sextic.singular_locus()
assert C_sing.cardinality() == 10
assert all(q.singularity_type() == Singularity("A1") for q in C_sing)
assert rational_sextic.normalization().geometric_genus() == 0
assert rational_sextic.kodaira_dimension() == -Infinity


# ============================================================================
# 4. SMOOTH SURFACES IN PP^3
# ============================================================================

# For a smooth degree-d surface S in PP^3 (adjunction):
#   K_S   = (d - 4) H|_S
#   K_S^2 = (d-4)^2 * d   (since H|_S^2 = d)
#   chi_top(S) = d(d^2 - 4d + 6)
#   q = h^{1,0} = 0   (Lefschetz: smooth hypersurface in PP^3 is simply connected)
#   p_g = h^{2,0}:  0 for d<4,  1 for d=4,  C(d-1, 3) for d>=5
#   chi(O_S) = 1 + p_g
#   h^{1,1} = chi_top - 2 - 2*p_g   (from the Hodge decomposition of H^2)
#   Noether: K_S^2 + chi_top = 12*chi(O_S)

R4.<x,y,z,w> = PolynomialRing(CC, 4)

# --- Degree 2: Smooth Quadric Surface in PP^3 --------------------------------
# Q ≅ PP^1 × PP^1 (smooth quadric surface is rational)
# K_Q = -2H, K^2 = 8, chi_top = 4, p_g = 0, chi(O) = 1

Q = Variety(x^2 + y^2 + z^2 + w^2)
H_Q = Q.hyperplane_class()   # H|_Q has H^2 = deg(Q) = 2

assert Q.degree() == 2 and Q.dimension() == 2
assert Q.is_smooth()
assert Q.canonical_divisor() == -2 * H_Q
assert Q.canonical_divisor().self_intersection() == 8   # (d-4)^2 * d = 4*2

assert Q.topological_euler_characteristic() == 4     # 2*(4-8+6)
assert Q.geometric_genus() == 0
assert Q.irregularity() == 0
assert Q.holomorphic_euler_characteristic() == 1

# Noether: K^2 + chi_top = 12*chi(O)  =>  8 + 4 = 12 ✓
assert (Q.canonical_divisor().self_intersection()
        + Q.topological_euler_characteristic()
        == 12 * Q.holomorphic_euler_characteristic())

# Hodge diamond (h^{1,1} = 4 - 2 - 0 = 2):
#   p\q  0  1  2
#    0  [1  0  0]
#    1  [0  2  0]
#    2  [0  0  1]
assert Q.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,2,0],[0,0,1]])

assert Q.kodaira_dimension() == -Infinity
assert Q.is_rational()

# Picard group: two rulings l, m with l^2 = 0, m^2 = 0, l*m = 1.
# Gram matrix in (l, m) basis: [[0, 1], [1, 0]]  (hyperbolic lattice H)
Pic_Q = Q.picard_group().as_lattice()
assert Pic_Q.rank() == 2
assert Pic_Q.gram_matrix() == Matrix(ZZ, [[0, 1], [1, 0]])

# Anti-canonical class -K = 2H is ample (positive degree); K = -2H is anti-ample
assert (-Q.canonical_divisor()).is_ample()
assert Q.canonical_divisor().is_anti_ample()

# Riemann-Roch: chi(O_Q(nH)) = chi(O_Q) + nH*(nH - K_Q)/2
#   = 1 + n*2*(n+2)/2 = 1 + n(n+2) = (n+1)^2
for n in range(0, 6):
    D = n * H_Q
    assert D.hirzebruch_riemann_roch() == (n + 1)^2


# --- Degree 3: Smooth Cubic Surface in PP^3 (del Pezzo dP_3) ----------------
# Isomorphic to Bl_6 PP^2; has exactly 27 lines.
# K_S = -H, K^2 = 3, chi_top = 9, p_g = 0, chi(O) = 1

S3 = Variety(x^3 + y^3 + z^3 + w^3)
H_S3 = S3.hyperplane_class()

assert S3.degree() == 3 and S3.dimension() == 2
assert S3.is_smooth()
assert S3.canonical_divisor() == -1 * H_S3
assert S3.canonical_divisor().self_intersection() == 3   # (3-4)^2 * 3

assert S3.topological_euler_characteristic() == 9     # 3*(9-12+6)
assert S3.geometric_genus() == 0
assert S3.irregularity() == 0
assert S3.holomorphic_euler_characteristic() == 1

# Noether: 3 + 9 = 12 ✓
assert (S3.canonical_divisor().self_intersection()
        + S3.topological_euler_characteristic()
        == 12 * S3.holomorphic_euler_characteristic())

# Hodge diamond (h^{1,1} = 9 - 2 - 0 = 7):
assert S3.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,7,0],[0,0,1]])

assert S3.kodaira_dimension() == -Infinity
assert S3.is_rational()

# -K = H is ample: cubic surface is a del Pezzo surface of degree 3
assert (-S3.canonical_divisor()).is_ample()

# Riemann-Roch: chi(O_{S3}(nH)) = chi(O) + nH*(nH - K)/2
#   K = -H, so nH - K = (n+1)H.  H^2 = 3 on S3.
#   chi(nH) = 1 + n*(n+1)*3/2  =  (3n^2 + 3n + 2)/2
for n in range(0, 5):
    D = n * H_S3
    chi_expected = 1 + n * (n + 1) * 3 // 2    # integer for all n >= 0
    assert D.hirzebruch_riemann_roch() == chi_expected


# --- Degree 4: Fermat Quartic Surface (K3) ----------------------------------
# K_S = 0, K^2 = 0, chi_top = 24, p_g = 1, chi(O) = 2

S4 = Variety(x^4 + y^4 + z^4 + w^4)
H_S4 = S4.hyperplane_class()

assert S4.degree() == 4 and S4.dimension() == 2
assert S4.is_smooth()
assert S4.is_k3() and S4.is_calabi_yau()

assert S4.canonical_divisor() == 0
assert S4.canonical_divisor().self_intersection() == 0

assert S4.topological_euler_characteristic() == 24   # 4*(16-16+6)
assert S4.geometric_genus() == 1     # p_g = 1: unique holomorphic 2-form
assert S4.irregularity() == 0
assert S4.holomorphic_euler_characteristic() == 2   # 1 - 0 + 1

# Noether: 0 + 24 = 12*2 ✓
assert (S4.canonical_divisor().self_intersection()
        + S4.topological_euler_characteristic()
        == 12 * S4.holomorphic_euler_characteristic())

# K3 Hodge diamond (h^{1,1} = 24 - 2 - 2 = 20):
#   p\q  0   1  2
#    0  [1   0  1]
#    1  [0  20  0]
#    2  [1   0  1]
assert S4.hodge_diamond() == Matrix(ZZ, [[1,0,1],[0,20,0],[1,0,1]])

assert S4.kodaira_dimension() == 0   # K trivial

# K = 0 is nef but not ample; H is ample (embedding in PP^3)
assert S4.canonical_divisor().is_nef() and not S4.canonical_divisor().is_ample()
assert H_S4.is_ample() and H_S4.is_nef() and H_S4.is_big()

# Riemann-Roch: chi(O_{S4}(nH)) = chi(O) + (nH)^2/2  (since K = 0)
#   = 2 + n^2*4/2 = 2 + 2n^2
for n in range(0, 5):
    D = n * H_S4
    assert D.hirzebruch_riemann_roch() == 2 + 2 * n^2


# --- Degree 5: Smooth Quintic Surface in PP^3 (general type) ---------------
# K_S = H, K^2 = 5, chi_top = 55, p_g = 4, chi(O) = 5

S5 = Variety(x^5 + y^5 + z^5 + w^5)
H_S5 = S5.hyperplane_class()

assert S5.degree() == 5 and S5.dimension() == 2
assert S5.is_smooth()

assert S5.canonical_divisor() == H_S5
assert S5.canonical_divisor().self_intersection() == 5   # (5-4)^2 * 5

assert S5.topological_euler_characteristic() == 55   # 5*(25-20+6)
assert S5.geometric_genus() == 4     # h^0(O_{PP^3}(1)) restricted = 4
assert S5.irregularity() == 0
assert S5.holomorphic_euler_characteristic() == 5   # 1 + 4

# Noether: 5 + 55 = 60 = 12*5 ✓
assert (S5.canonical_divisor().self_intersection()
        + S5.topological_euler_characteristic()
        == 12 * S5.holomorphic_euler_characteristic())

# Hodge diamond (h^{1,1} = 55 - 2 - 8 = 45):
#   p\q  0   1  2
#    0  [1   0  4]
#    1  [0  45  0]
#    2  [4   0  1]
assert S5.hodge_diamond() == Matrix(ZZ, [[1,0,4],[0,45,0],[4,0,1]])

assert S5.kodaira_dimension() == 2   # K = H ample => general type
assert S5.is_general_type()
assert S5.canonical_divisor().is_ample() and S5.canonical_divisor().is_big()

# Riemann-Roch: chi(O_{S5}(nH)) = chi(O) + nH*(nH - K)/2
#   K = H; nH*(nH - H) = n(n-1)*H^2 = n(n-1)*5
#   chi(nH) = 5 + 5*n*(n-1)/2
for n in range(0, 5):
    D = n * H_S5
    assert D.hirzebruch_riemann_roch() == 5 + 5 * n * (n - 1) // 2


# --- Noether loop for d = 2..5 (uniform verification) ----------------------

surfaces_in_PP3 = {
    2: x^2 + y^2 + z^2 + w^2,
    3: x^3 + y^3 + z^3 + w^3,
    4: x^4 + y^4 + z^4 + w^4,
    5: x^5 + y^5 + z^5 + w^5,
}

def _surface_pg(d):
    if d < 4:
        return 0
    elif d == 4:
        return 1
    else:
        k = d - 4
        return binomial(k + 3, 3)

for d, f in surfaces_in_PP3.items():
    S   = Variety(f)
    pg  = _surface_pg(d)
    chi_top = d * (d^2 - 4*d + 6)
    K2  = (d - 4)^2 * d
    chi_O = 1 + pg    # q = 0

    assert S.is_smooth() and S.dimension() == 2 and S.degree() == d
    assert S.geometric_genus() == pg and S.irregularity() == 0
    assert S.holomorphic_euler_characteristic() == chi_O
    assert S.topological_euler_characteristic() == chi_top
    assert S.canonical_divisor() == (d - 4) * S.hyperplane_class()
    assert S.canonical_divisor().self_intersection() == K2
    # Noether's formula
    assert K2 + chi_top == 12 * chi_O
    assert S.hodge_diamond() == Matrix(ZZ, [[1, 0, pg], [0, chi_top - 2 - 2*pg, 0], [pg, 0, 1]])


# ============================================================================
# 5. BLOWUPS OF PP^2
# ============================================================================

# For a blowup pi: Bl_k PP^2 -> PP^2 at k smooth points p_1,...,p_k:
#   Pic(Bl_k PP^2) = ZZ*Hp + ZZ*E_1 + ... + ZZ*E_k
#   Gram matrix: diag(1, -1, ..., -1)  (the lattice I_{1,k})
#   K_{Bl_k PP^2} = -3*Hp + E_1 + ... + E_k
#   K^2 = 9 - k
#   chi_top(Bl_k PP^2) = chi(PP^2) + k = 3 + k
#   p_g = q = 0, chi(O) = 1  (rational surface)

# --- Blowup at one point: Bl_1 PP^2  (del Pezzo dP_8) ----------------------

p0 = PP^2(CC).point([0, 0, 1])
pi1 = PP^2(CC).blowup(p0)
S_dP8 = pi1.domain()

assert S_dP8.is_smooth() and S_dP8.is_rational() and S_dP8.dimension() == 2
assert S_dP8.geometric_genus() == 0 and S_dP8.irregularity() == 0
assert S_dP8.holomorphic_euler_characteristic() == 1
assert S_dP8.topological_euler_characteristic() == 4    # 3 + 1

E1 = pi1.exceptional_divisor()       # unique exceptional (-1)-curve
Hp1 = pi1.pullback(PP^2(CC).hyperplane_class())

assert E1.is_isomorphic_to(PP^1(CC))
assert E1.self_intersection() == -1

# Pic(Bl_1 PP^2): Gram matrix diag(1, -1) in basis (Hp1, E1)
Pic_dP8 = S_dP8.picard_group().as_lattice()
assert Pic_dP8.rank() == 2
assert Pic_dP8.gram_matrix() == Matrix(ZZ, [[1, 0], [0, -1]])

# K = -3*Hp + E,  K^2 = 9 - 1 = 8
K_dP8 = S_dP8.canonical_divisor()
assert K_dP8 == -3 * Hp1 + E1.as_divisor()
assert K_dP8.self_intersection() == 8

# Noether: 8 + 4 = 12*1 ✓
assert K_dP8.self_intersection() + S_dP8.topological_euler_characteristic() == 12

# Hodge diamond: h^{1,1} = 4 - 2 = 2
assert S_dP8.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,2,0],[0,0,1]])

# -K = 3Hp - E is ample on Bl_1 PP^2 (del Pezzo of degree 8).
# (-K)·E = (3Hp-E)·E = 3*0 - (-1) = 1 > 0, and there are no (-2)-curves
# (one blowup at a generic point introduces none), so -K passes the Nakai
# criterion and is ample.
assert (-K_dP8).is_ample()
assert (-K_dP8).is_nef() and (-K_dP8).is_big()

# E is not nef: E^2 = -1 < 0
assert not E1.as_divisor().is_nef()

# Riemann-Roch: chi(O(D)) = chi(O) + D*(D-K)/2
# For D = Hp: D^2 = 1, D*K = -3; D*(D-K)/2 = (1+3)/2 = 2; chi = 1 + 2 = 3
assert Hp1.hirzebruch_riemann_roch() == 3
# For D = -K = 3Hp-E: D^2 = 8, D*K = -8; D*(D-K)/2 = (8+8)/2 = 8; chi = 9
assert (-K_dP8).hirzebruch_riemann_roch() == 9
# For D = E: D^2 = -1, D*K = E*(-3Hp+E) = -3*0 + (-1) = -1
#   D*(D-K)/2 = (-1-(-1))/2 = 0; chi = 1
assert E1.as_divisor().hirzebruch_riemann_roch() == 1


# --- Blowup at six points: Bl_6 PP^2  (isomorphic to a cubic surface) ------

pts6 = [PP^2(CC).point(p) for p in [
    [1,0,0], [0,1,0], [0,0,1], [1,1,0], [1,0,1], [0,1,1]
]]
pi6 = PP^2(CC).blowup(pts6)
S_dP3 = pi6.domain()

assert S_dP3.is_smooth() and S_dP3.is_rational() and S_dP3.dimension() == 2
assert S_dP3.holomorphic_euler_characteristic() == 1
assert S_dP3.topological_euler_characteristic() == 9    # 3 + 6

Eis6 = pi6.exceptional_locus()
assert Eis6.cardinality() == 6
assert all(Ei.self_intersection() == -1 for Ei in Eis6)

Hp6 = pi6.pullback(PP^2(CC).hyperplane_class())

# Pic = ZZ*Hp + ZZ*E_1 + ... + ZZ*E_6, gram matrix diag(1,-1,...,-1) = I_{1,6}
Pic_dP3 = S_dP3.picard_group().as_lattice()
assert Pic_dP3.rank() == 7
assert Pic_dP3.is_isometric_to(Lattice.I(1, 6))

# K = -3*Hp + E_1 + ... + E_6,  K^2 = 9 - 6 = 3
K_dP3 = S_dP3.canonical_divisor()
assert K_dP3 == -3 * Hp6 + sum(Ei.as_divisor() for Ei in Eis6)
assert K_dP3.self_intersection() == 3

# Noether: 3 + 9 = 12*1 ✓
assert K_dP3.self_intersection() + S_dP3.topological_euler_characteristic() == 12

# Hodge diamond: h^{1,1} = 9 - 2 = 7
assert S_dP3.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,7,0],[0,0,1]])

# -K is ample (del Pezzo degree 3; no (-2)-curves for 6 points in general position)
assert (-K_dP3).is_ample()


# --- Blowup loop: K^2 and chi_top decrease by 1 per blown-up point ----------

PP2 = PP^2(CC)
for k in range(1, 9):
    # k generic points (no special position assumed for correctness of K^2)
    # Here we only verify topological data, not ampleness.
    pts_k = [PP2.point([Integer(i), Integer(i^2 % 7), 1]) for i in range(k)]
    pi_k  = PP2.blowup(pts_k)
    Sk    = pi_k.domain()

    assert Sk.topological_euler_characteristic() == 3 + k
    assert Sk.holomorphic_euler_characteristic() == 1
    assert Sk.geometric_genus() == 0 and Sk.irregularity() == 0

    Hp_k = pi_k.pullback(PP2.hyperplane_class())
    Eks  = pi_k.exceptional_locus()
    K_k  = Sk.canonical_divisor()

    assert K_k == -3 * Hp_k + sum(Ei.as_divisor() for Ei in Eks)
    assert K_k.self_intersection() == 9 - k
    assert K_k.self_intersection() + Sk.topological_euler_characteristic() == 12

    # h^{1,1} = k+1 for Bl_k PP^2 (rational surface: p_g = q = 0)
    assert Sk.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,k+1,0],[0,0,1]])

    Pic_k = Sk.picard_group().as_lattice()
    assert Pic_k.rank() == k + 1
    assert Pic_k.is_isometric_to(Lattice.I(1, k))


# ============================================================================
# 6. K3 SURFACES: COMPLETE INTERSECTIONS
# ============================================================================

# A smooth complete intersection of type (d_1,...,d_r) in PP^{r+2} is K3 iff
#   sum(d_i) = r + 3  (adjunction: K = (sum d_i - (r+3)) H = 0)
# The complete K3 list:
#   (4)     in PP^3   (quartic hypersurface)
#   (2, 3)  in PP^4   (quadric ∩ cubic)
#   (2,2,2) in PP^5   (three quadrics)
# All have: K = 0, p_g = 1, q = 0, chi(O) = 2, chi_top = 24, h^{1,1} = 20.

R5.<u0,u1,u2,u3,u4> = PolynomialRing(CC, 5)

# --- (2,3) complete intersection K3 in PP^4 ---------------------------------
# Adjunction: K = (2+3-5)H = 0.  Degree = 2*3 = 6.

K3_23 = Variety([u0^2 + u1^2 + u2^2 + u3^2 + u4^2,
                 u0^3 + u1^3 + u2^3 + u3^3 + u4^3])

assert K3_23.dimension() == 2
assert K3_23.is_smooth()
assert K3_23.is_k3() and K3_23.is_calabi_yau()
assert K3_23.canonical_divisor() == 0
assert K3_23.degree() == 6     # product of degrees: 2*3
assert K3_23.geometric_genus() == 1 and K3_23.irregularity() == 0
assert K3_23.holomorphic_euler_characteristic() == 2
assert K3_23.topological_euler_characteristic() == 24
assert K3_23.hodge_diamond() == Matrix(ZZ, [[1,0,1],[0,20,0],[1,0,1]])

# Noether: K^2 + chi_top = 0 + 24 = 12*2 ✓
assert (K3_23.canonical_divisor().self_intersection()
        + K3_23.topological_euler_characteristic()
        == 12 * K3_23.holomorphic_euler_characteristic())

# Riemann-Roch for L = nH on K3: chi(O_{K3}(nH)) = chi(O) + (nH)^2/2 = 2 + n^2*d/2
# For d=6: chi(nH) = 2 + 3n^2
for n in range(0, 5):
    D = n * K3_23.hyperplane_class()
    assert D.hirzebruch_riemann_roch() == 2 + 3 * n^2


# --- (2,2,2) complete intersection K3 in PP^5 --------------------------------
# Adjunction: K = (2+2+2-6)H = 0.  Degree = 2^3 = 8.

R6.<v0,v1,v2,v3,v4,v5> = PolynomialRing(CC, 6)

K3_222 = Variety([
    v0^2 + v1^2 + v2^2 + v3^2 + v4^2 + v5^2,
    v0^2 + 2*v1^2 + 3*v2^2 + 4*v3^2 + 5*v4^2 + 6*v5^2,
    v0^2 + 4*v1^2 + 9*v2^2 + 16*v3^2 + 25*v4^2 + 36*v5^2,
])

assert K3_222.dimension() == 2
assert K3_222.is_smooth()
assert K3_222.is_k3() and K3_222.is_calabi_yau()
assert K3_222.canonical_divisor() == 0
assert K3_222.degree() == 8     # 2*2*2
assert K3_222.geometric_genus() == 1 and K3_222.irregularity() == 0
assert K3_222.holomorphic_euler_characteristic() == 2
assert K3_222.topological_euler_characteristic() == 24
assert K3_222.hodge_diamond() == Matrix(ZZ, [[1,0,1],[0,20,0],[1,0,1]])

# Riemann-Roch: chi(nH) = 2 + n^2*8/2 = 2 + 4n^2
for n in range(0, 5):
    D = n * K3_222.hyperplane_class()
    assert D.hirzebruch_riemann_roch() == 2 + 4 * n^2


# --- K3 Picard group (rank 1 base case) --------------------------------------
# A "general" (Picard-number-1) K3 with polarisation H: Pic = ZZ*H,
# with H^2 = 2g-2 for genus g >= 2.  The simplest case: H^2 = 2 (g=2).
# h^0(H) = g = 2 by Riemann-Roch on K3: chi(H) = 2 + H^2/2 = 2 + 1 = 3;
# by Kodaira vanishing h^2(H) = h^0(K-H) = h^0(-H) = 0 and h^1(H) = 0,
# so h^0(H) = 3 for a (2,0)-polarised K3.

# For the quartic K3 S4 (above): H^2 = 4, Pic ≥ rank 1.
# The hyperplane class satisfies H^2 = 4; by R-R chi(nH) = 2 + 2n^2 as verified.


# ============================================================================
# 7. ENRIQUES SURFACES
# ============================================================================

# An Enriques surface Y has:
#   K_Y ≠ 0 but 2*K_Y = 0  (torsion canonical class of order 2)
#   p_g = 0, q = 0, chi(O_Y) = 1
#   chi_top = 12, K^2 = 0
#   Kodaira dimension: 0
#   Universal K3 cover: the unramified double cover pi: X -> Y with X a K3 surface
#   Hodge diamond:
#     p\q  0  1  2
#      0  [1  0  0]
#      1  [0 10  0]
#      2  [0  0  1]

# An EnriquesSurface object carries the universal K3 cover; the Enriques
# involution iota is the deck transformation of pi.

Y = EnriquesSurface(...)          # any concrete Enriques surface

assert Y.dimension() == 2
assert Y.is_smooth()
assert Y.is_enriques()

assert Y.geometric_genus() == 0
assert Y.irregularity() == 0
assert Y.holomorphic_euler_characteristic() == 1
assert Y.topological_euler_characteristic() == 12

# Canonical class: torsion of order 2 (2K_Y ~ 0 but K_Y ≁ 0)
K_Y = Y.canonical_divisor()
assert (2 * K_Y).is_linearly_equivalent_to(0)
assert not K_Y.is_linearly_equivalent_to(0)
assert K_Y.order_in_picard_group() == 2

# Hodge diamond (h^{1,1} = 12 - 2 - 0 = 10):
assert Y.hodge_diamond() == Matrix(ZZ, [[1,0,0],[0,10,0],[0,0,1]])

assert Y.kodaira_dimension() == 0   # K torsion

# Noether: K^2 + chi_top = 0 + 12 = 12*1 ✓
assert K_Y.self_intersection() == 0
assert K_Y.self_intersection() + Y.topological_euler_characteristic() == 12

# Unramified K3 double cover
f_k3 = Y.k3_cover()              # unramified degree-2 morphism pi: X -> Y
X_k3 = f_k3.domain()
assert f_k3.codomain() == Y
assert X_k3.is_k3()
assert f_k3.degree() == 2
assert f_k3.branch_divisor() == Variety.empty()    # unramified: no branch locus

# Deck transformation = Enriques involution iota
iota = Y.enriques_involution()
assert iota.order() == 2
assert iota.fixed_locus() == Variety.empty()       # free action
assert X_k3.quotient(iota) == Y                    # X / iota ≅ Y


# ============================================================================
# 8. AMPLENESS, NEF-NESS, BIG-NESS
# ============================================================================

# Ample <=> Kodaira embedding theorem (positive curvature)
# Nef   <=> D·C >= 0 for all effective curves C
# Big   <=> h^0(nD) grows like n^dim

# Ample => Nef, Ample => Big.  Nef + Big does NOT imply Ample.

P2  = ProjectiveSpace(2, CC)
H2  = P2.hyperplane_class()
assert H2.is_ample() and H2.is_nef() and H2.is_big()
assert (-H2).is_anti_ample() and not (-H2).is_nef() and not (-H2).is_big()

# Quartic K3: K = 0 is nef but not ample, not big
assert S4.canonical_divisor().is_nef()
assert not S4.canonical_divisor().is_ample()
assert not S4.canonical_divisor().is_big()
# H|_{S4} is the ample generator of the polarisation
assert H_S4.is_ample() and H_S4.is_nef() and H_S4.is_big()

# Quintic surface: K = H is ample and big (general type)
assert S5.canonical_divisor().is_ample() and S5.canonical_divisor().is_big()

# Cubic surface: K = -H is anti-ample; -K = H is ample
assert S3.canonical_divisor().is_anti_ample()
assert (-S3.canonical_divisor()).is_ample()

# Quadric surface: K = -2H is anti-ample
assert Q.canonical_divisor().is_anti_ample()

# On Bl_1 PP^2: E^2 = -1 so E is not nef; -K = 3Hp-E is ample
assert not E1.as_divisor().is_nef()
assert (-K_dP8).is_ample() and (-K_dP8).is_nef() and (-K_dP8).is_big()


# ============================================================================
# 9. RATIONALITY AND UNIRATIONALITY
# ============================================================================

# Rational:   birational to PP^n
# Unirational: dominant rational map PP^n --> X
# Rational => Unirational

# Curves: rational iff genus 0
assert P1.is_rational() and P1.is_unirational()
assert conic.is_rational() and conic.is_unirational()
assert not elliptic.is_rational() and not elliptic.is_unirational()   # g=1
assert not quartic_curve.is_rational() and not quartic_curve.is_unirational()  # g=3

# Surfaces: classical rationality results
assert Q.is_rational() and Q.is_unirational()    # smooth quadric ≅ PP^1 × PP^1
assert S3.is_rational() and S3.is_unirational()  # smooth cubic surface (Cayley-Salmon)
assert not S4.is_rational()   # K3 surface (Kodaira dim 0, non-trivial 2-form)
assert not S5.is_rational() and not S5.is_unirational()  # general type

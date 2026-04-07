
# Union of 2 transverse lines in AA^2, A_1 singularity
R.<x,y> = PolynomialRing(CC, 2)
f(x,y) = (x-y) * (x+y)
assert f.gradient() == vector(R, [2*x, -2*y])
X = Variety(f) # Automatically convert to ideal
# NB: union of x=y and x=-y, two lines, SNC at zero.
assert X.is_affine() and not X.is_projective()
assert X.ambient_variety() == AA^2(CC) and X.is_subset_of(AA^2(CC)) and X.is_subvariety_of(AA^2(CC))
assert X.is_hypersurface() # In AA^2_CC naturally
p = X([0,0]) # Affine point
assert p.is_singular()
X_sing = X.singular_locus()
X_sm = X.smooth_locus()
assert p in X_sing and p not in X_sm
assert X_sing == set([p]) and X_sing.is_finite() and X_sing.is_closed() # Points are closed in the Zariski topology
assert X_sing = Variety((x-0, y-0)) # V((x-p,y-q)) = (p,q)
assert X_sing.union(X_sm) == X
assert X_sing.complement() == X_sm and X_sm.complement() == X_sing
assert X - X_sing == X_sm and X - X_sm == X_sing # Convenience
assert X_sm.is_smooth() and not X_sm.is_singular()
assert not X_sing.is_smooth() and X_sing.is_singular()
assert not X.is_smooth() and X.is_singular()

assert p.singularity_type() == Singularities("A1")
assert p.is_node() and p.is_ordinary_double_point()
assert p.canonical_form() == Variety(xy).point([0,0]) # Local standard form: uv=0
assert not p.is_cusp()

assert X.is_snc()

# TODO: assert on X.blowup(p)
# TODO: assert X.blowup(p).is_smooth(), is_normal(), equals X.resolution()
assert X.coordinate_ring() == CC


assert p.local_ring() == X.local_ring(p) # TODO: what is this ring?
R = p.local_ring()

# Single line in AA^2
X = Variety(x-y)
assert X.is_smooth() and not X.is_singular() and X.smooth_locus() == X and X.singular_locus() == Variety.empty()
assert X.is_snc()
assert X.is_isomorphic_to(AA^1(CC)) # TODO: isomorphism witness.
assert X.resolution() == X == X.normalization() # Resolutions for curves are just normalizations


# (0,0) in AA^2
X = Variety((x-y, x+y))
assert X.cardinality() == 1 and X == X.point((0,0)) and AA^2(CC).point((0,0)) in X and AA^2(CC).point((1,1)) not in X
p = X.point((0,0))
R = p.local_ring()
assert R.is_local() and R.is_regular() and R.dimension() == 0 and R.is_field() and R == CC
assert X.singular_locus() == Variety.empty() and X.smooth_locus() == X and X.is_smooth() and X == X.resolution() and X.dimension() == 0

# A_2 singularity
X = Variety(y^2-x^3)
p = X((0,0)) # Convenience method for points.
assert X.is_singular() and X.singular_locus() == p # Convenience: treat a finite list of points as a variety.
assert p.singularity_type() == Singularities("A2")
assert not p.is_node() and p.is_cusp()


# A_n singularities
for n in range(10):
	X = Variety(y^2-x^n)
	p = X((0,0))
	assert p.singularity_type() == Singularities(f"A{n}")

# TODO: compute Milnor-style invariants, homotopy type of links, etc
# TODO: standard forms for types D and E

# Projective curves
C = Curve((x-y)*(x+y)).projective_closure()
assert C.ambient_space() == PP^2(CC)
assert not C.is_affine() and C.is_projective() 
assert C.dimension() == 1
assert C.is_nodal() and not C.is_cuspidal()
assert C == Variety((x-y)*(x+y)) # Curves are subclasses of varieties, and the constructor should specialize
assert C.genus() == ...
assert C.geometric_genus() == ...
assert C.arithemetic_genus() == ...
assert not C.is_elliptic() and not C.is_abelian_variety()

assert C.irregularity() == ...
assert [C.plurigenus(n) for n in range(10)] == ...
assert C.hodge_diamond() == Matrix(ZZ, ...) # Entry p,q == h^{p, q}(C)
assert C.hilbert_polynomial() == ...
assert C.kodaira_dimension() == ...
assert C.is_rational() and not C.is_elliptic() and not C.is_calabi_yau() and not C.is_hyperbolic() and not C.is_general_type()



R.<x,y,z,w> = PolynomialRing(CC, 4)
f(x,y,z,w) = x^4 + y^4 + z^4 + w^4 
X = Variety(f) # Fermat quartic surface
assert X.degree() == 4
assert X.ambient_variety() == PP^3(CC)
assert X.is_projective() and X.is_quasiprojective()
assert X.is_k3() and X.is_calabi_yau()
assert X.is_smooth() and X.smooth_locus() == X and X.singular_locus() == Variety.empty()
K_X = X.canonical_divisor()
Pic_X = X.picard_group()
assert K_X in Pic_X
assert K_X.is_linearly_equivalent_to(Pic_X(0)) # Coerce obvious data to divisors
assert K_X == 0 # Convenience: linear equivalence of divisors
assert X.hodge_diamond() == ... # h^1(OO_X) = 0, etc
assert X.is_hypersurface()
X_PP3= X.as_divisor() # In PP^3
H = PP^3(CC).hyperplane_class() # PP^n has special methods
assert X_PP3.is_linearly_equivalent_to(4*H) # Adjunction
assert X.canonical_divosr() == (PP^3(CC).canonical_divisor() + X_PP3).restrict_to(X)
assert PP^3(CC).canonical_divisor() == -4*H



# Coble surfaces
C = Curve(...) # Define a rational sextic with 10 nodes
assert C.is_singular()
assert C.ambient_variety() == PP^2(CC)
C_sing = C.singular_locus()
assert C_sing.cardinality() == 10
assert all(p.singularity_type() == Singularity("A1") for p in C_sing)
f = PP^2(CC).blowup(C_sing)
S = X.domain() # Coble surface
assert S.is_rational()
assert S.picard_group().as_lattice().is_isometric_to(
	Lattice.I(1, 10)
)
K_S = S.canonical_divisor()
assert (-K_S).h0() == 0 and (-2*K_S).h0() == 1
assert (-K_S).linear_system() == emptyset() and not (-2*K_S).linear_system() != emptyset()


Eis= f.exceptional_locus()
assert Eis.cardinality() == 10
assert all(Ei.as_divisor()^2 == -2 for Ei in Eis) # Enumerate irreducible components
assert Variety(f(Ei) for Ei in Eis) == C_sing
assert Variety(f.pullback(pi) for pi in C_sing) == Eis

Hp = f.pullback_divisor(PP^2(CC).hyperplane_class())
assert K_S == -3*Hp + sum(Ei.as_divisor() for Ei in Eis)

C_tilde = f.proper_transform(C)
assert C_tilde.as_divisor() == 6*Hp -2*sum(Ei.as_divisor() for Ei in Eis)
assert C_tilde.as_divisor() == -2*K_S

B = C_tilde # This will be the branch divisor.
assert B in (-2*K_S).linear_system()
assert B.is_linearly_equivalent_to(-2*K_S)

f = VarietyMorphism.branched_double_cover(B)
X = f.domain()
assert X.is_k3() and f.codomain() == S
assert X.hodge_diamond() == ... # Standard hodge diamond for K3s: 1s on corners, 20 in middle.

iota_X = f.covering_involution()
assert iota_X in X.Aut()
assert iota_X.order() == 2
assert X/iota_X == S
assert f.branch_locus() == B
R_X = f.ramification_locus()
assert R_X in X.picard_group() # Ramification locus is a divisor

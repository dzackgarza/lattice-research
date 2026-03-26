"""
Central Geometry Module for Coble Project
================================================================================

This module provides common lattice constructions and verification functions
used across the Coble moduli space project.

Lattices:
  - U: Hyperbolic plane
  - E8: E8 root lattice (Cartan matrix)
  - Lambda_K3: K3 lattice U^3 + E8(-1)^2
  - S_Co: Coble Picard lattice diag(2, -2^10)
  - T_Co: Coble transcendental lattice diag(2^2, -2^9)

Utilities:
  - is_primitive_embedding: Check if M is a primitive embedding
  - is_node: Verify A1 singularity using 3x3 Hessian rank
"""

from sage.all import *

def hyperbolic_plane():
    """Hyperbolic plane U with Gram matrix [[0,1],[1,0]]."""
    return matrix(ZZ, [[0, 1], [1, 0]])

def E8_lattice(negative=True):
    """E8 root lattice with Cartan matrix, optionally negated."""
    E8_cartan = matrix(ZZ, [
        [ 2, -1,  0,  0,  0,  0,  0,  0],
        [-1,  2, -1,  0,  0,  0,  0,  0],
        [ 0, -1,  2, -1,  0,  0,  0,  0],
        [ 0,  0, -1,  2, -1,  0,  0,  0],
        [ 0,  0,  0, -1,  2, -1,  0, -1],
        [ 0,  0,  0,  0, -1,  2, -1,  0],
        [ 0,  0,  0,  0,  0, -1,  2,  0],
        [ 0,  0,  0,  0, -1,  0,  0,  2]
    ])
    return -E8_cartan if negative else E8_cartan

def K3_lattice():
    """K3 lattice Λ_K3 = U^3 + E8(-1)^2."""
    U = hyperbolic_plane()
    E8_neg = E8_lattice(negative=True)
    return block_diagonal_matrix([U, U, U, E8_neg, E8_neg])

def S_Co_gram():
    """Coble Picard lattice Gram matrix diag(2, -2, ..., -2)."""
    return diagonal_matrix(ZZ, [2] + [-2]*10)

def T_Co_gram():
    """Coble transcendental lattice expected Gram matrix diag(2, 2, -2, ..., -2)."""
    return diagonal_matrix(ZZ, [2, 2] + [-2]*9)

def stabilizer_reflection_generators(T_En_gram, h_Co, theta):
    """Find reflection generators in the stabilizer Γ_Co of the Coble polarization."""
    n = T_En_gram.nrows()
    
    def reflection_matrix(r, G):
        r_norm = int(r * G * r)
        s_r = matrix(QQ, n, n)
        Gr = G * r
        for i in range(n):
            for j in range(n):
                s_r[i,j] = (1 if i == j else 0) - QQ(2 * r[i] * Gr[j]) / r_norm
        return s_r.change_ring(ZZ)

    # Search for -2 roots
    roots = []
    for i in range(n):
        v = zero_vector(ZZ, n); v[i] = 1; roots.append(v)
    
    # Simple search for short roots (norm -2) in Enriques transcendental
    gamma_gens = []
    for r in roots:
        try:
            s_r = reflection_matrix(r, T_En_gram)
            if s_r.transpose() * T_En_gram * s_r == T_En_gram:
                if (s_r * h_Co == h_Co) and (s_r * theta == theta * s_r):
                    if s_r not in gamma_gens:
                        gamma_gens.append(s_r)
        except: pass
    return gamma_gens

def is_primitive_embedding(M):
    """Check if integer matrix M defines a primitive embedding into a lattice."""
    S, U, V = M.smith_form()
    # The Smith diagonal should have as many 1s as the rank (number of columns)
    diagonal = [S[i,i] for i in range(min(S.nrows(), S.ncols()))]
    return all(d == 1 for d in diagonal)

def saturate_embedding(M, L_gram):
    """
    Saturate the sublattice spanned by columns of M in lattice with L_gram.
    Returns a basis for (span(M) \otimes Q) \cap Z^n.
    """
    # M is n x k
    n, k = M.nrows(), M.ncols()
    D, U, V = M.smith_form()
    # M = U^-1 * D * V^-1
    U_inv = U.inverse()
    # Ensure it is integer matrix
    return U_inv.change_ring(ZZ)[:, :k]

def is_node_at_point(F, pt):
    """
    Verify if a singular point is a node (A1) using 3x3 Hessian rank.
    
    A point p is a node of a plane curve F(x,y,z)=0 iff rank(H(F)(p)) = 2.
    """
    R = F.parent()
    x, y, z = R.gens()
    
    px, py, pz = pt
    
    # Second partial derivatives
    H = matrix(QQbar, 3, 3)
    vars = [x, y, z]
    for i in range(3):
        for j in range(3):
            H[i,j] = F.derivative(vars[i], vars[j]).substitute(x=px, y=py, z=pz)
    
    return H.rank() == 2

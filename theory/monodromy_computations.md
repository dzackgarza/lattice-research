# Monodromy Computation for Algebraic Families

This document surveys available tools for computing the **homological monodromy** of a
one-parameter family f(x₁,...,xₙ, t) = 0 over a punctured disc Δ* = Δ \ {0}.

The object of interest is the monodromy operator

  M ∈ Aut(Hₖ(F_{t₀}, ℤ))  (for k = dim F_t, symplectic for k odd)

where F_{t₀} = V(f(·, t₀)) is the fiber over a basepoint. Since π₁(Δ*, t₀) ≅ ℤ,
the monodromy is a single matrix.

Two cases are treated separately:
- **Families of curves** (n=2): Sage's `RiemannSurface` machinery is directly applicable.
- **Families of surfaces** (n=3, e.g. K3 families): requires the Picard-Fuchs ODE
  approach via `ore_algebra`.

---

## Case 1: Families of curves — RiemannSurface parallel transport

**Setup**: f(z, w, t) ∈ ZZ[z, w, t] (or QQ[z,w,t]). For each rational or QQ[i] value
of t, the specialization f(z, w, t_k) ∈ QQ[z,w] (or QQ[i][z,w]) is a bivariate
polynomial over an exact ring, which `RiemannSurface` accepts directly.

**Key Sage classes and methods** (all in `sage.schemes.riemann_surfaces.riemann_surface`):
- `RiemannSurface(f, prec=100)` — constructs from f ∈ k[z,w], k = QQ or number field
  with complex embedding. Computes branch locus (discriminant roots), Voronoi graph,
  homology basis, cohomology basis.
- `S.period_matrix()` — g × 2g complex matrix of periods ∫_{γⱼ} ωᵢ.
- `S.riemann_matrix()` — g × g normalized period matrix (Siegel upper half-space).
- `S.symplectic_isomorphisms(other)` — finds all M ∈ Sp(2g, ZZ) such that
  Ω(S) ≈ Ω(other) · M. Uses `homomorphism_basis` (LLL on the period matrices via
  `integer_matrix_relations`) then filters for M · Rosati(M) = I. Returns a list.
- `S.homomorphism_basis(other)` — ZZ-basis of the full Hom(Jac(S), Jac(other)) as
  2g × 2g integer matrices. Calls `integer_matrix_relations(Ω_other, Ω_self)`.
- `C.riemann_surface(**kwargs)` — convenience method on any Sage affine or projective
  curve object (both `AffinePlaneCurve` and `ProjectivePlaneCurve` have this).

**What `integer_matrix_relations(M1, M2)` does**: finds integer matrices (D,B;C,A) such
that B + M1·A = (D + M1·C)·M2. This is a purely numerical LLL computation — it does NOT
require the two surfaces to be isomorphic. Isomorphisms are the subset with det(R) = 1
and R·Rosati(R) = I.

**The algorithm**:

For a loop around t=0 (the critical value), choose a canonical polygonal path with
vertices at rational or QQ[i] points, away from all critical values of
  Δ(t) = Res_z(f(z,w,t), ∂f/∂z(z,w,t))  (the discriminant in z).

Canonical path: the unit square in QQ[i],
  t_0 = 1,  t_1 = -i,  t_2 = -1,  t_3 = i,  t_4 = 1
or scaled: ε·{1, -i, -1, i} if critical values are near the origin.
Subdivide each edge into N rational steps if needed to avoid passing near branch points
of Δ.

At each step k:
1. Compute S_k = RiemannSurface(f(z, w, t_k), prec=p)
2. Compute S_{k+1} = RiemannSurface(f(z, w, t_{k+1}), prec=p)
3. Call `isos = S_k.symplectic_isomorphisms(S_{k+1})`
   - This returns all Sp(2g,ZZ) matrices relating Ω(S_k) to Ω(S_{k+1}).
   - For small steps (no critical t between t_k and t_{k+1}), the surfaces have
     isomorphic Jacobians and the list is non-empty.
   - The local parallel transport is the element M_k ∈ isos closest to the identity
     (minimising ||M_k - I||).
4. Compose: M = M_{N-1} · ... · M_1 · M_0.

**Why this works**: At each step, since no critical value of Δ(t) lies between t_k and
t_{k+1}, the family is a smooth deformation of Riemann surfaces. The Jacobian Jac(S_k)
and Jac(S_{k+1}) are isomorphic as complex tori. `symplectic_isomorphisms` finds ALL
Sp(2g,ZZ) isomorphisms; the one closest to identity is the analytic continuation matrix
(since for a small step the transport is close to the identity in the archimedean norm).
After composing all steps around the full loop, M is the monodromy.

**Base ring note**: When t ∈ QQ[i], set K = NumberField(x^2+1, embedding=CC(I)), then
f(z, w, t_k) ∈ K[z,w], and RiemannSurface accepts K.

**Limitations of `symplectic_isomorphisms`**:
- Requires the two surfaces to have isomorphic Jacobians (automatic for small enough steps).
- LLL lattice reduction over the period matrix — cost scales as O(g^6) roughly, so fast
  for g=1,2, feasible for g≤4.
- Precision parameter `prec` must be large enough for LLL to resolve the answer: use
  `prec=100` or higher for genus ≥ 2.
- Returns the FULL GROUP of Sp(2g,ZZ) automorphisms when S_k = S_{k+1} (trivial step);
  for distinct nearby surfaces typically returns a singleton or very small set.

**Explicit code sketch**:

```python
from sage.schemes.riemann_surfaces.riemann_surface import RiemannSurface
from sage.rings.number_field.number_field import NumberField
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.matrix.constructor import identity_matrix
from sage.rings.integer_ring import ZZ

def monodromy_curve_family(f_zwt, t_vals, prec=100):
    """
    Compute the monodromy of f(z, w, t)=0 along the loop t_vals[0]->...->t_vals[-1].

    f_zwt: polynomial in QQ[z, w, t] (or ZZ[z, w, t])
    t_vals: list of (rational or QQ[i]) values forming a closed loop,
            e.g. [1, -I, -1, I, 1] (unit square in QQ[i]) or finer subdivision.
            No critical value of Disc_z(f) should lie strictly between consecutive points.
    """
    R = f_zwt.parent()
    z, w, t_var = R.gens()

    def surface_at(t_val):
        f_zw = f_zwt.subs({t_var: t_val})
        return RiemannSurface(f_zw, prec=prec)

    g = surface_at(t_vals[0]).genus
    M_total = identity_matrix(ZZ, 2*g)

    for k in range(len(t_vals) - 1):
        S0 = surface_at(t_vals[k])
        S1 = surface_at(t_vals[k+1])
        isos = S0.symplectic_isomorphisms(S1)
        if not isos:
            raise ValueError(f"No symplectic isomorphism at step {k}; "
                              "check for critical values between t_vals[{k}] and t_vals[{k+1}]")
        # Pick the one closest to identity (local parallel transport)
        M_k = min(isos, key=lambda M: (M - identity_matrix(ZZ, 2*g)).norm())
        M_total = M_k * M_total

    return M_total
```

**Example — Legendre family y² = x(x-1)(x-t)**:

```python
R.<z, w, t> = ZZ[]
f = w^2 - z*(z-1)*(z-t)
# Critical values of f: t=0, t=1. Loop around t=0 using QQ[i] square:
QQi.<I> = QuadraticField(-1)
t_loop = [QQi(v) for v in [1/2 + I/2, -1/2 + I/2, -1/2 - I/2, 1/2 - I/2, 1/2 + I/2]]
# (scale avoids t=0 and t=1 critical values; check Disc_z(f) = t^2(t-1)^2)
M = monodromy_curve_family(f, t_loop, prec=100)
# Expected: M = [[1,0],[-2,1]] or [[1,2],[0,1]] depending on orientation/basis
```

**Example — cuspidal degeneration y² = x³ - t**:

```python
R.<z, w, t> = ZZ[]
f = w^2 - z^3 + t
# Single critical value at t=0. Loop:
QQi.<I> = QuadraticField(-1)
t_loop = [QQi(v) for v in [1, -I, -1, I, 1]]  # unit square, avoids t=0
M = monodromy_curve_family(f, t_loop, prec=100)
# Expected: unipotent M = [[1,0],[1,1]], N = M-I, N^2 = 0 (Kodaira type I_1)
```

---

## Case 2: Families of surfaces — ore_algebra (Picard-Fuchs ODE)

**Setup**: f(x₁,...,xₙ, t) for n ≥ 3 (fibers are surfaces). The period integrals
  ω(t) = ∫_{γ(t)} Ω    (Ω = holomorphic (n-1)-form on F_t)
satisfy a Picard-Fuchs ODE L_t(ω) = 0, a linear ODE in t with rational function
coefficients. The monodromy of this ODE (analytic continuation of solutions around
the singular points) IS the monodromy of the family.

**Key tool**: `ore_algebra.analytic.monodromy.monodromy_matrices(dop, base)`.
- Input: a differential operator `dop` in `ore_algebra`'s `DifferentialOperators` ring,
  and a base point `base ∈ QQbar`.
- Output: one matrix per singular point, each an element of CBF (complex ball field),
  with certified precision. The matrices generate the monodromy group.
- Algorithm: analytic continuation via numerical_transition_matrix along carefully
  chosen Voronoi-like paths, using ball arithmetic for certified error bounds.
  Two modes: `algorithm='connect'` (default), `algorithm='binsplit'` (more robust).

**Note on availability**: `ore_algebra` is NOT a standard Sage package and is not
currently installed. It is available from https://github.com/mkauers/ore_algebra .
It requires a Cython build step.

**The hard step — computing the Picard-Fuchs ODE**:

Given f(x, y, z, t) = 0 (K3 surface family), the Picard-Fuchs ODE for ∫ Ω/(f^k) as a
function of t is obtained by Griffiths-Dwork reduction: repeatedly differentiate
∫ Ω/f^k with respect to t, and reduce the resulting rational differential forms modulo
the image of the Griffiths reduction map to express everything in terms of a basis of
H^n(F_t). This gives an ODE of order = dim H^n.

This computation is NOT available in Sage. It requires:
- Macaulay2's `PeriodIntegrals` package (Lian-Song-Yau, implemented by H. Lê Trung Nhân)
- or Singular's deformation module / `gaussman.lib`
- or an explicit tabulation (for standard families, the Picard-Fuchs ODE is in the
  literature — see Doran-Morgan [DM06] for K3 families, or AESZ database for CY3)

Once the ODE is known:
```python
# ore_algebra (once installed):
from ore_algebra import DifferentialOperators
from ore_algebra.analytic.monodromy import monodromy_matrices

Dops, t, Dt = DifferentialOperators()

# Example: Picard-Fuchs for the family y^2 = x(x-1)(x-t) (Legendre, genus 1)
# ODE: 4t(1-t)·y'' + 4(1-2t)·y' - y = 0
dop = 4*t*(1-t)*Dt^2 + 4*(1-2*t)*Dt - 1
mats = monodromy_matrices(dop, base=QQ(1,2))
# Returns one matrix per singularity (t=0, t=1, t=∞)
```

For K3 families (Picard number ρ, second cohomology H²), the monodromy group is a
subgroup of O(Λ) where Λ = H²(F, ZZ) with the intersection form. The Picard-Fuchs
ODE has order = 2 + (rank of primitive cohomology) for a one-parameter family.

**`ore_algebra.analytic.monodromy` code structure** (from source):
- `monodromy_matrices(dop, base, eps, sing)`: iterates `_monodromy_matrices`
- For regular singular points: computes `formal_monodromy` (purely from local exponents,
  no numerical work) if the point is regular and the formal monodromy is scalar.
  Otherwise uses `numerical_transition_matrix` along a polygon around the singularity.
- For irregular singular points: `_local_monodromy_loop` integrates numerically around
  a polygon.
- The base point can be QQbar (including QQ and QQ[i]). Singularities are roots of
  the leading coefficient of dop.

---

## Summary: what is directly feasible

| Family type | Method | Tools | Base ring | Status |
|---|---|---|---|---|
| Curves (f(z,w,t)=0) | RiemannSurface chain | Sage built-in | ZZ/QQ/QQ[i] | **Directly implementable** |
| Curves (known ODE) | ore_algebra | external package | QQ | Needs ore_algebra install |
| Surfaces (known Picard-Fuchs ODE) | ore_algebra | external package | QQ | Needs ore_algebra install |
| Surfaces (ODE not known) | Griffiths-Dwork reduction | Macaulay2 / Singular | QQ | Requires external CAS step |

For the primary use case (ZZ-coefficient families of curves): the `RiemannSurface` chain
approach is completely self-contained in Sage. Loop coordinates are always taken in
QQ[i] (vertices {1, -i, -1, i} scaled to avoid critical values).

---

## Explicit examples with expected monodromy

### Legendre family y² = x(x-1)(x-t)

Critical values: t=0, t=1. Fundamental group π₁(ℙ¹ \ {0,1,∞}) = ⟨γ₀, γ₁ | γ₀γ₁γ∞ = 1⟩.

Monodromy in standard symplectic basis {[α],[β]} of H₁(F_{1/2}, ZZ):
  M₀ = [[1, 0], [-2, 1]]   (around t=0; transvection by the vanishing cycle δ₀)
  M₁ = [[1, 2], [0, 1]]    (around t=1; transvection by the vanishing cycle δ₁)
  M∞ = (M₀·M₁)⁻¹ = [[-1,-2],[2,3]]

These generate Γ(2) ⊂ SL(2,ZZ) (principal congruence subgroup of level 2).

### Weierstrass/cuspidal family y² = x³ - t

Critical value: t=0 (Δ = -27t² = 0). Fiber F_0: cuspidal cubic (genus 0 with cusp).
Kodaira fiber type: I₁ (nodal after change of variables; the cusp is a rational
singularity). Monodromy:
  M = [[1, 0], [1, 1]]   (unipotent; N = M-I, N² = 0)
This is the standard Type II unipotent in Kulikov/Persson-Pinkham classification.

### Hesse pencil x³+y³+1 = 3t·xyz (elliptic surface)

Critical values: t = 1, ω, ω² (ω = e^{2πi/3}), t = ∞ (Hessian inflection). Each
gives an I₁ Kodaira fiber. The global monodromy group is commensurable with SL(2,ZZ).

---

## References

- Sage RiemannSurface: `sage.schemes.riemann_surfaces.riemann_surface` (4115 lines).
  Key methods: `period_matrix`, `riemann_matrix`, `homomorphism_basis`,
  `symplectic_isomorphisms`, `monodromy_group` (sheet permutations only).
  `integer_matrix_relations`: LLL-based Z-basis of Hom(Jac₁, Jac₂).
  Source: Bruin-Sijsling-Zotine [BSZ2019].
- ore_algebra: https://github.com/mkauers/ore_algebra — Kauers-Mezzarobba et al.
  `analytic/monodromy.py`: `monodromy_matrices`, `formal_monodromy`, `_monodromy_matrices`.
- Griffiths-Dwork: Dwork (1962); Griffiths (1969); Dimca "Singularities and Topology"§5.
- Picard-Lefschetz: SGA 7 Exp. XV (Katz); Lamotke (1981).
- Kulikov/Persson-Pinkham: classification of degenerate fibers, Kodaira types I_n/II/III/IV.
- Doran-Morgan [DM06]: classification of K3 families by Picard-Fuchs ODE.

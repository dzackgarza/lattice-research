# MAPPING.md — Lattices Subtree

Records the mathematical justification for how every Sage surface maps to our hierarchy.
For each Sage type: what Sage provides, the correct mathematical concept, placement
decision, and consequence for refinement and regression tests.

---

## Hierarchy Overview

```
Modules(R).WithForms()                          [axiomatic; stays in modules/]
└── .Bilinear()                                 [axiomatic; stays in modules/]
    └── .Symmetric()                            [axiomatic; stays in modules/]
        └── .Nondegenerate()                    [axiomatic; stays in modules/]
            └── .Indefinite()                   [axiomatic; stays in modules/]
            └── .Definite()                     [axiomatic; stays in modules/]

lattices/subcategories/
├── with_forms.py          _WithForms              (axiom class for modules/)
├── bilinear.py            _BilinearModules         (axiom class for modules/)
├── symmetric.py           _SymmetricBilinearModules
├── nondegenerate.py       _NondegenerateBilinearModules
├── indefinite.py          _IndefiniteBilinearModules
├── definite.py            _DefiniteBilinearModules
├── free_bilinear.py       _FreeBilinearModules     (Free + Bilinear)
├── over_dedekind.py       _LatticesOverDedekindDomain
├── over_pid.py            _LatticesOverPID
├── over_integers.py       _LatticesOverIntegers    (= Lattices(ZZ))
├── even.py                _EvenLattices
├── unimodular.py          _UnimodularLattices
└── constructions/
    ├── dual_lattices.py
    ├── overlattices.py
    ├── orthogonal_direct_sums.py
    └── discriminant_groups.py
```

---

## Method Placement Table

The table answers: at what tier is each method first universally well-defined?

| Method | Minimal tier | Justification |
|--------|-------------|---------------|
| `form()` | `WithForms` | definitional; every object in this category carries a form |
| `evaluate(v, *args)` | `WithForms` | form evaluation on elements; lifting from cartesian product |
| `form_degree() -> (p,q)` | `WithForms` | (1,1) for bilinear, (1,0) for linear, etc. |
| `b(v, w)` | `Bilinear` | bilinear evaluation; only defined once the form is bilinear |
| `self_product(v)` | `Bilinear` | `b(v,v)`; defined for any bilinear form |
| `is_isotropic(v)` | `Bilinear` | `b(v,v) = 0`; defined for any bilinear form |
| `perp(v)` (element) | `Bilinear` | `{w ∈ M : b(v,w)=0}` is a submodule for any bilinear form |
| `orthogonal_submodule_to(S)` | `Bilinear` | `S^⊥ = {w : b(s,w)=0 ∀s∈S}`; always a submodule |
| `q(v)` | `Quadratic` | quadratic form evaluation |
| `is_symmetric()` | `Symmetric` | witness predicate |
| `is_alternating()` | `Alternating` | witness predicate |
| `is_nondegenerate()` | `Nondegenerate` | witness predicate |
| `is_indefinite()` | `Indefinite` | witness predicate |
| `is_definite()` | `Definite` | witness predicate |
| `gram_matrix()` | `Free + Bilinear` | requires a basis; entries `b(e_i,e_j)` lie in R; see note (1) |
| `inner_product_matrix()` | `Free + Bilinear` | synonym / alternative presentation |
| `rank()` | `Free` | rank of free module; undefined for general modules |
| `determinant()` | `Free + Bilinear` | `det(gram_matrix)`; requires basis |
| `discriminant()` | `Free + Bilinear` | `(-1)^r * det`; requires basis |
| `is_positive_definite()` | `Free + Symmetric` | eigenvalue criterion needs free + symmetric |
| `is_negative_definite()` | `Free + Symmetric` | same |
| `signature_pair()` | `Free + Symmetric + OverIntegralDomain` | eigenvalues over Frac(R)⊗R; see note (2) |
| `signature()` | `Free + Symmetric + OverIntegralDomain` | derived: `p - q` |
| `dual_lattice()` | `Bilinear.Integral + OverIntegralDomain` | `L^*={v∈L_K:β(v,L)⊆R}` requires K=ff(R) and R-valued form; see note (3) |
| `discriminant_group()` | `Bilinear.Integral + OverIntegralDomain` | `L^*/L`; follows from dual_lattice; see note (3) |
| `inclusion_morphism()` | `Bilinear.Integral + OverIntegralDomain` | `ι: L → L^*`; same tier |
| `is_even()` | `Bilinear.Integral` | `b(e_i,e_i) ∈ 2R`; requires integrality but NOT freeness |
| `is_unimodular()` | `Bilinear.Symmetric.Nondegenerate.Integral + OverIntegralDomain` | `L=L^*`, i.e. `|det|=1` |
| `orthogonal_complement(S)` (parent) | `Bilinear.Symmetric` | `S^⊥` is a submodule for ANY symmetric bilinear module; see note (4) |
| `is_primitive(M)` | `Free + OverIntegralDomain` | quotient L/M is torsion-free |
| `direct_sum(other)` | `Free + Bilinear` | orthogonal direct sum with block-diagonal gram matrix |
| `tensor_product(other)` | `Free + Bilinear` | Kronecker product of gram matrices |
| `sublattice(basis)` | `Free + Bilinear + OverPID` | sublattice on a basis requires PID structure |
| `overlattice(gens)` | `Free + Symmetric + Nondegenerate + OverIntegralDomain` | L + span(gens) ∩ dual; requires dual |
| `maximal_overlattice(p)` | `OverZZ` | algorithm uses ZZ-specific arithmetic |
| `twist(s)` | `WithForms` | scale form by scalar; defined for any module with form |
| `genus()` | `OverZZ` | local-global genus theory; requires ZZ (or at least Dedekind) |
| `orthogonal_group()` | `Free + Symmetric + Nondegenerate + OverIntegralDomain` | O(L) ≤ GL_n(R); see note (5) |
| `special_orthogonal_group()` | same as above | SO(L) |
| `stable_orthogonal_group()` | same as above | O^+(L) |
| `nikulin_invariants()` | `OverZZ + Free + Symmetric + Nondegenerate` | discriminant group invariants (l, δ) |
| `is_isometric_to(other)` | `OverZZ + Free + Symmetric + Nondegenerate` | lattice isometry test |
| `minimum()` | `OverZZ + Free + Symmetric` | shortest vector (requires ZZ for finiteness) |
| `maximum()` | `OverZZ + Free + Symmetric` | longest nonzero vector in compact regions |
| `LLL()` | `OverZZ + Free + Symmetric` | LLL reduction; ZZ-specific |
| `short_vectors(n)` | `OverZZ + Free + Symmetric` | ZZ-specific enumeration |
| `quadratic_form()` | `Free + Symmetric` | convert to `QuadraticForm` object |
| `rational_span()` | `Free + OverIntegralDomain` | `L ⊗_R Frac(R)` |
| `base_change_to(ring)` | `Free + Bilinear` | change coefficient ring |
| `gram_matrix_bilinear()` | `Torsion + Bilinear` | Gram matrix in Q/mZ; see note (6) |
| `gram_matrix_quadratic()` | `Torsion + Quadratic` | quadratic Gram matrix |
| `brown_invariant()` | `Torsion + Bilinear + Symmetric` | global torsion QF invariant |
| `normal_form()` | `Torsion + Bilinear + Symmetric` | canonical form |
| `primary_part(m)` | `Torsion` | m-primary part |
| `value_module()` | `Torsion + Bilinear` | Q/mZ containing form values |
| `value_module_qf()` | `Torsion + Quadratic` | Q/nZ containing QF values |
| `additive_order(v)` | `Torsion` (element) | order in torsion group |
| `lift(v)` | `Torsion` (element) | lift to dual lattice |
| `divisibility(v)` | `Free` (element) | gcd{a ∈ R : v = a·w for w ∈ L} |
| `is_primitive(v)` | `Free` (element) | divisibility is a unit |
| `discriminant_class(v)` | `Free + Nondegenerate + OverIntegralDomain` (element) | image of v in L^*/L |
| `reflection(v)` | `Free + Symmetric + Nondegenerate` (element) | s_v(w) = w - 2b(v,w)/b(v,v) · v |
| `is_root(v)` | `Free + Symmetric + Integral` (element) | b(v,v) ∈ {-2, 2} |
| `norm(v)` | `Bilinear` (element) — see note (7) | b(v,v); defined for any bilinear form |

---

## Notes

**(1) `gram_matrix()` placement**: Sage places this at `FreeQuadraticModule_generic`
(free over commutative ring). We confirm: entries `b(e_i, e_j)` live in R only when the
form is R-valued and M is free (so the `e_i` are a basis). For a torsion module over a
PID, the analogous concept is `gram_matrix_bilinear()` in Q/mZ. These are distinct
methods at distinct tiers; do NOT merge them.

**(2) `signature_pair()` placement**: Sage places this at
`FreeQuadraticModule_integer_symmetric` (= ZZ). Mathematically it is meaningful for any
free symmetric bilinear module over an ordered integral domain via base-change to the
fraction field and then to ℝ. We place it at `Free + Symmetric + OverIntegralDomain`;
the `OverIntegers` tier provides the concrete algorithm. The abstract stub lives at the
Dedekind domain level.

**(3) `dual_lattice()` placement**: `L^* = {v ∈ L_K : β(v,L) ⊆ R}` where
`L_K = L ⊗_R K` and `K = ff(R)`. The definition makes almost no assumptions on `R`:
we only need a fraction field (OverIntegralDomain) and an R-valued form (Integral).
Nondegeneracy is NOT required by the definition — `L^*` is always a well-defined
sub-K-module of `L_K` containing `L`. Freeness is NOT required — the definition is
purely set-theoretic inside `L_K`. We therefore place the abstract stub at
`Bilinear.Integral + OverIntegralDomain`; Sage's ZZ-specific implementation is just
one concrete algorithm.

**(4) `orthogonal_complement(S)` placement**: `S^⊥ = {v ∈ M : b(v,s) = 0 ∀s ∈ S}`.
This is always a submodule. No assumptions needed beyond having a bilinear form.
For symmetric forms, left and right orthogonal complements coincide, so the symmetric
axiom is needed only to guarantee `(S^⊥)^⊥ = S`. Abstract stub belongs at
`Bilinear.Symmetric`. Computability (as a free module of explicit rank) requires
nondegeneracy + free; that is an algorithm concern, not a placement concern.

**(5) `orthogonal_group()` placement**: `O(L) = Aut_{isometry}(L)`. Requires: free (to
express as matrix group GL_n(R)), nondegenerate (to have a meaningful notion of
isometry), symmetric (orthogonal group is for symmetric forms; symplectic group is the
alternating analogue). Place at `Free + Symmetric + Nondegenerate + OverIntegralDomain`.
The finite-group computation for `OverZZ` uses Plesken-Souvignier; that's an algorithm
detail, not a placement issue.

**(6) Torsion `gram_matrix_bilinear()`**: For `TorsionQuadraticModule = V/W`, the form
takes values in `Q/mZ = (V^*/W^*) / (V/W)^*`. This is a *different type* from the
integral Gram matrix. Both are "gram matrices" but they live at different tiers with
different codomains. The torsion version is named `gram_matrix_bilinear()` (following
Sage) to avoid ambiguity with `gram_matrix()` at the free level.

**(7) `norm(v)` vs `self_product(v)`**: Both are `b(v,v)`. The name `norm` is Sage
lattice convention (appears in `Lattices.ElementMethods`). The name `self_product`
appears in our `BilinearModules.ElementMethods`. Both belong at `Bilinear` (element).
In the spec we use `self_product` at the generic bilinear level and provide `norm` as an
alias at the `Lattices(ZZ)` level (where "norm" is standard terminology).

---

## Sage Type → Spec Category Mapping

| Sage Type | Spec Category | Justification |
|-----------|--------------|---------------|
| `FreeQuadraticModule_generic` | `Modules(R).Free().Bilinear()` | free quadratic module over commutative ring |
| `FreeQuadraticModule_generic_pid` | `Modules(R).Free().Bilinear().OverPID()` | adds span/span_of_basis with PID structure |
| `FreeQuadraticModule_generic_field` | `Modules(K).Free().Bilinear().OverField()` | over a field (= vector space with form) |
| `FreeQuadraticModule_submodule_*_pid` | `Modules(R).Free().Bilinear().Subobjects().OverPID()` | submodule of free quadratic over PID |
| `FGP_Module_class` | `Modules(R).FinitelyPresented().OverPID()` | V/W presentation; no form |
| `TorsionQuadraticModule` | `Modules(R).FinitelyPresented().OverPID().Torsion().Bilinear()` | V/W with Q/mZ-valued bilinear form |
| `FreeQuadraticModule_integer_symmetric` | `Modules(ZZ).Free().Bilinear().Symmetric().Nondegenerate().Integral()` | the canonical integral lattice |
| `QuadraticForm` | `Modules(ZZ).Free().Bilinear().Symmetric().Nondegenerate().Integral()` | same category; different presentation (upper-triangular coefficients) |

**Note on `QuadraticForm` vs `FreeQuadraticModule_integer_symmetric`**: Both represent
the same mathematical object (an integral lattice). Sage keeps them as separate classes
for historical reasons. Our spec treats them as objects in the same category; the
constructor `Lattices(ZZ).Constructors().from_quadratic_form(qf)` converts between them.

---

## What Stays in `modules/` vs What Lives in `lattices/`

### Stays in `modules/subcategories/` (minimal attachment point only)

Most consumers of `Modules(R)` are not concerned with bilinear forms. The modules
subtree owns only the generic "module with some form" attachment:

- `_WithForms` — currently in `modules/subcategories/axiomatic.py`
- `_BilinearModules` — same
- `_QuadraticModules` — same

These three classes will eventually each live in their own file when `axiomatic.py` is
split, but that is a module-subtree cleanup task tracked in `modules/docs/TRIAGE.md`.
All further specialization of forms belongs in the lattices subtree.

### Lives in `lattices/subcategories/`

All form-specialization axiom classes live here, because these are lattice-theoretic
concerns:

- `symmetric.py` — `_SymmetricBilinearModules`
- `alternating.py` — `_AlternatingBilinearModules`
- `nondegenerate.py` — `_NondegenerateBilinearModules`
- `indefinite.py` — `_IndefiniteBilinearModules`
- `definite.py` — `_DefiniteBilinearModules`
- `integral.py` — `_IntegralBilinearModules`
- `rational.py` — `_RationalBilinearModules`
- `free_bilinear.py` — `_FreeBilinearModules` (`Free + Bilinear`; `gram_matrix()` lands here)
- `over_dedekind.py` — `_LatticesOverDedekindDomain`
- `over_pid.py` — `_LatticesOverPID`
- `over_integers.py` — `_LatticesOverIntegers` (canonical `Lattices(ZZ)`)
- `even.py` — `_EvenLattices`
- `unimodular.py` — `_UnimodularLattices`

These axiom classes set `_base_category_class_and_axiom` to point at `Modules` (or the
appropriate parent category) — they extend the module hierarchy from the lattice side.

### Discriminant groups live in `lattices/subcategories/constructions/discriminant_groups.py`

`DiscriminantGroups(ZZ)` = `TorsionBilinearModules(QQ/ZZ)`. The full discriminant group
method surface lives here.

---

## Key Gap: `axiomatic.py` Must Be Split

`plans/category_specs/modules/subcategories/axiomatic.py` currently aggregates ~18
axiom classes in one file. AGENTS.md §File Tree bans flat aggregators. The eventual
split (tracked in `modules/docs/TRIAGE.md`) produces one file per class:

```
modules/subcategories/
├── over_integral_domain.py    (_OverIntegralDomain)
├── over_dedekind_domain.py    (_OverDedekindDomain)
├── over_pid.py                (_OverPID)
├── over_commutative_ring.py   (_OverCommutativeRing)
├── over_field.py              (_OverField)
├── over_local_ring.py         (_OverLocalRing)
├── over_complete_ring.py      (_OverCompleteRing)
├── free.py                    (_Free, _FreeFiniteRank)
├── torsion.py                 (_Torsion)
├── torsionfree.py             (_Torsionfree)
├── projective.py              (_Projective)
├── generating_set.py          (_WithOrderedGeneratingSet)
├── finitely_generated.py      (_FinitelyGenerated)
├── finitely_presented.py      (_FinitelyPresented)
├── ideals.py                  (_RIdeals)
├── with_forms.py              (_WithForms)
├── bilinear.py                (_BilinearModules)
└── quadratic.py               (_QuadraticModules)
```

This is a future cleanup task; the forms-specialization files already exist in
`lattices/subcategories/` and do not require this split to be usable.

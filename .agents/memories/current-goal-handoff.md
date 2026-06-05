---
title: Current Goal Handoff
---
# Handoff

## Current Phase

Category-spec vocabulary. The purpose is to give later lattice and Coble work precise
mathematical objects, morphisms, constructions, invariants, category refinements, and
witness data grounded in Sage/source evidence.

## Next Work

Next mathematical obligation: state the smaller subgroup actually used in the Coble
quotient, if it is not full `O(T_Co)` or full `O^+(T_Co)`.  The Dolgachev-Kondo
standard target `N=<2>+E_10(2)` is sourced as `T_Co`, and `N=2B` with
`B=<1>+U+E_8(-1)`.  For this target, primitive vectors have divisibility `2`,
`Iso(A_N,q_N)` has `528` elements, and full `O(A_N,q_N)` has two isotropic orbits with
sizes `[1, 527]`.

The full primitive-isotropic lattice orbit claim is now sourced: `O(N)=O(B)`, `B` is
odd unimodular of signature `(2,9)`, Milnor/Nikulin identify the odd unimodular
isometry class, Dawes/Attwell-Duval give the split maximal condition in signature
`(2,n)` for `n>=5`, and Dawes Algorithm 4.4 gives one primitive-isotropic vector orbit
under `O^+(B)`, hence under `O^+(T_Co)` and `O(T_Co)`.

The next subgroup obligation is not an orbit computation yet.  The source-backed
Enriques-side candidate is now
`Gamma_Co^En(delta)=im(Stab_{Gamma_En,2}(Z delta)->O(delta^perp))`, where AEGS define
`Gamma_En,2` from K3-lattice isometries commuting with `I_En` and fixing the degree-2
polarization vector `h=e+f`, and `delta` is a `(-2)` Heegner vector in `T_En` with
`delta^perp ~= T_Co`.

Use the explicit representative supplied by the AEGS decomposition
`T_En = U + U(2) + E_8(2)`: for a standard basis `u,v` of the unimodular `U` summand,
`delta=u-v` has square `-2`, and `delta^perp = Z(u+v) + U(2) + E_8(2) ~= <2> +
E_10(2) = T_Co`.

Use the discriminant-gluing description of `Gamma_En,2` before attempting orbit
computation: `g_T in O(T_En)` belongs to `Gamma_En,2` exactly when its action on
`A_TEn` matches, via the anti-isometry `A_SEn ~= A_TEn`, the action of some
`g_S in O(S_En)` fixing `h`.  Thus the finite image to compute first is the image of
`Stab_{O(S_En)}(h)` on `A_SEn`, transported to `A_TEn`.

Finite container already computed:
`theory/computations/coble_enriques_degree2_discriminant_stabilizer.sage` gives
`|O(A_SEn,q)|=46998591897600`, `Q(h) mod 4=2`, and
`|Stab_{O(A_SEn,q)}(h/2)|=94755225600`.  Do not treat this as the actual
`Gamma_En,2` image until the lift/surjectivity of `Stab_{O(S_En)}(h)` onto that finite
stabilizer is proved or computed.

Next mathematical obligation: determine the `Gamma_En,2`-orbit of the chosen Heegner
line `Z delta`, compute or source the image of `Gamma_Co^En(delta)` in
`O(A_T,q_T)`, and then compare this Enriques-side subgroup with the project
stabilizer-centralizer notation
`Stab(typed Coble polarization data) ∩ Z(theta)`.  The comparison still requires
constructing `theta`, the transported polarization class, and the ambient-lattice
restriction maps.

Do not use the five AEGS 0-cusps as the answer to the Heegner-line question.  AEGS
Corollary 3.12 concerns `Gamma_En,2`-orbits of primitive isotropic lines in `T_En`; the
Coble Heegner datum is a negative line `Z delta` with `delta^2=-2`.

Dolgachev-Kondo source the full quotient `D(N)/O(N)` for the Coble target and the
birational quotient of the `(-2)` Heegner divisor by `O(U+E_10(2))`.  AEGS source the
degree-2 Enriques group `Gamma_En,2` and the `(-2)` discriminant divisor.  Together
these source `Gamma_Co^En(delta)` as an Enriques-side subgroup, not yet the project
`Gamma_Co` until the `theta` comparison is proved.  The local Sterk extraction symlink
is currently broken, so Sterk-specific subgroup-orbit claims need source restoration or
another inspected source before use.

If later code must build `T_Co` from geometric input rather than use the accepted
source-level target `N`, create that implementation-constructor obligation separately
instead of treating it as a blocker for the source-level target.

The cited Eichler criterion requiring a copy of `2U` is not available for
`T_Co ~= N=2(<1>+E_10)`, because every pairing in `N` is divisible by `2`; smaller
subgroup orbit claims still need their own theorem or backend.

Backend note: `theory/computations/coble_standard_target_discriminant_orbits.sage`
computes the full standard finite action by defining `O(A_N,q_N)` as the stabilizer of
the four fibers of `Q(v)=B(v,v) mod 4` inside `GL(B/2B)` and then using GAP finite-set
orbits on `Q^{-1}(0)`.  The naive Sage full `D.orthogonal_group()` call for this
rank-11 form did not return during the earlier session and remains non-evidence for
the orbit count.

Do not reopen the discriminant-form finite-action conversion as a mapping or
terminology task.  The finite-action conversion for Sage torsion quadratic modules now
lives in
`category_specs/lattices/subcategories/constructions/discriminant_form_actions.py`.

The finite formed-module side now has source-backed rows in
`[[SPEC-MAPPING-LATTICES]]` and `[[SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES]]`:

- `O(A,q)=Aut(A,q)` for Sage torsion quadratic modules is realized by
  `TorsionQuadraticModule.orthogonal_group()` and `FqfOrthogonalGroup`.
- Supplied generators define generated subgroups of `O(A,q)` after coercion to finite
  abelian-group automorphisms.
- The full Sage group is computed by `_isom_fqf(A)` as a slow brute-force finite
  search over form-compatible images of Smith generators.
- `ActionOnFqf` supplies the right action on `A` and invariant subquotients.
- `FqfOrthogonalGroup` does not expose public `orbit`, `orbits`, or `stabilizer`
  methods; the spec states the bounded construction from finite carrier, generated
  group, and certified action, and `discriminant_form_actions.py` is the implementation
  witness for that construction.
- `PermutationGroup.orbit`, `PermutationGroup.orbits`, and
  `PermutationGroup.stabilizer` are Sage/GAP implementation evidence only after the
  typed conversion to and from the finite permutation/action domain is specified.
- Oscar/Hecke is source-checked exact backend evidence for `TorQuadModule`, isometry
  tests, stable submodules, subgroup stabilizers, centralizers `O(T,f)`, and generic
  finite `GSet` actions; the checked versions do not expose a
  torsion-quadratic-module-specific operation for arbitrary finite subsets `X <= A`
  under `G <= O(A,q)`.

The lattice lifting statement has been separated from the finite formed-module orbit
claims.  The full-group statement is settled for the standard target, while smaller
subgroups still obey the conservative implication:

```text
For primitive v in L with div(v)=d, the class v/d + L lies in A_L; if v^2=0,
that class is isotropic.  O(L)-equivalence implies equivalence of these classes
under im(O(L)->O(A_L,q_L)).  The converse requires a checked Nikulin/Eichler theorem
or a named primitive-isotropic orbit backend.
```

Do not weaken the finite orbit object or promote lattice-level orbit lifting without
the subgroup choice, subgroup image when needed, checked theorem hypotheses, a
primitive-isotropic backend, or a theorem proving the required smaller-subgroup lifting
statement.

## Mapping Rule

Read Sage behavior before choosing the mathematical vocabulary. Do not accept a mapping
row until it contains both a behavior statement grounded in body/docs/examples and a
sentence a mathematician can read without knowing Sage.

Examples:

- In any category, morphisms have domains and codomains and compose.
- In a concrete category, morphisms can be evaluated on elements.
- In an additive category, each `Hom(X,Y)` is an abelian group and composition is
  bilinear.
- In an `R`-linear category, each `Hom(X,Y)` is an `R`-module and composition is
  `R`-bilinear.
- In an abelian category, kernels and cokernels exist, images and coimages are defined,
  and monomorphisms and epimorphisms are detected by the corresponding kernel and
  cokernel conditions.
- `End(X)=Hom(X,X)` contains the identity endomorphism.
- `Aut(X)` is the group of invertible endomorphisms in the ambient category. It lies in
  `Groups`; generator methods belong only to finite-generation or generated-subgroup
  refinements.
- A morphism has a matrix only after choosing finite free presentations or bases.

Only after the behavior record and mathematical sentence are present should the row
assign a project owner.

## Current Decisions

- `SPEC-MAPPING-LATTICES` is the routing source for lattice, module, torsion, Homset,
  and form-adjacent Sage names.
- `IntegralLattice`, `IntegralLatticeDirectSum`, and `IntegralLatticeGluing` are the
  admitted `Lattices(ZZ).Constructors()` names and have source-backed operation rows.
- `FreeQuadraticModule` is forms/module-owned, not a lattice constructor;
  `QuadraticSpace`/`InnerProductSpace` is the field-valued free bilinear wrapper, not a
  lattice constructor.
- `TorsionQuadraticForm` and generic `TorsionQuadraticModule` are forms-owned torsion
  quadratic constructors. They become lattice discriminant-group constructions only
  through explicit lattice metric-dual descent `A_L = coker(L -> L^#)`.
- `invariants()` and `invariant_factors()` belong to finitely presented modules over a
  PID. Lattices and discriminant/torsion objects inherit them only through that module
  structure.
- `BinaryQF`, `BQFClassGroup`, and `TernaryQF` belong to forms or binary/ternary
  quadratic-form vocabulary, not to `Lattices(ZZ)` constructors.
- Package exports such as `sage.modules.all`, `sage.quadratic_forms.genera.all`, and
  `sage.geometry.all` are import evidence. They do not create mathematical owners.
- `TASK-FORMED-COKERNEL-DESCENDED-FORM` stays closed unless new source contradicts its formed-cokernel construction.
- `stable_orthogonal_group()` denotes `~O(L)=ker(O(L)->O(A_L,q_L))`, not `O^+(L)`.
  `O^+(L)` is the real-spinor-kernel subgroup.
- `SO(L)`, `~O(L)`, `O^+(L)`, `SO^+(L)`, `~SO(L)`, and `~SO^+(L)` are distinct
  subgroup objects in the lattice Aut mapping; generator methods remain absent unless a
  stronger finite/generated/backend refinement supplies witnesses.

## Non-Goals

- Do not turn Sage implementation classes into method owners.
- Do not add lattice methods merely because lattice code uses them.
- Do not record progress as complete unless the relevant Sage behavior has a
  source-backed operation row, a one-line residue classification, or an unresolved
  mathematical question.
- Do not use this handoff as a changelog. The mapping spec and git history carry past
  work.

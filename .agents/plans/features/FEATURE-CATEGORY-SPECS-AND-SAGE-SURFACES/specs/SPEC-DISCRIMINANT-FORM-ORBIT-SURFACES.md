---
id: SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-MAPPING-LATTICES]]'
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
title: Define discriminant-form isotropic orbit objects
status: in-progress
priority: medium
requirement: 'The Coble cusp and discriminant-orbit arguments require finite
  discriminant-form objects, their automorphism groups, isotropic subsets, finite orbit
  sets, stabilizers, and the separate lattice-lifting theorem or algorithm that relates
  discriminant-form orbits to primitive isotropic lattice vectors.'
acceptanceCriteria:
- Each object or operation is stated as a mathematical claim with category/refinement,
  hypotheses, witnesses, codomain or return object, and source evidence.
- The finite formed-module objects are separated from lattice-level lifting and
  primitive-isotropic orbit theorems.
- The spec does not promise generators, presentations, or full lattice orbit algorithms
  unless the stronger group category or backend witness is named.
- Sage TorsionQuadraticModule, QuadraticForm, GAP, Oscar, Hecke, and stored Dawes or
  building evidence are used only as implementation witnesses for the stated
  mathematical operations.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Spec: Discriminant-Form Isotropic Orbit Objects

## Relationship to existing specs

Phase 4 (PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT) already specifies
discriminant-group methods: `b(x,y)`, `q(x)`, `invariants()`, `cardinality()`,
`isotropic_elements()`, `elements_of_norm(n)`, `is_isometric_to(other)`,
`isomorphic_as_groups(other)`, `is_p_elementary(p)`, `p_rank(p)`, `value_map()`.

These operations give the finite torsion module `A`, the quotient-valued quadratic
form `q: A -> Q/2Z`, and the subset of isotropic elements.  The remaining mathematical
objects needed for cusp and orbit computations are:

- the automorphism group `O(A,q) = Aut_{TorsionQuadraticModules}(A,q)`;
- the action of `O(A,q)` or a specified subgroup `G <= O(A,q)` on the finite set `A`;
- the finite subset `Iso(A,q) = {a in A : q(a) = 0}`;
- orbit sets such as `Iso(A,q)/G` and `{a in A : q(a)=n}/G`;
- stabilizers `Stab_G(a)` or `Stab_G(S)` for elements or subgroups;
- the separate lattice theorem or algorithm relating a discriminant class to primitive
  isotropic vectors in a lattice with discriminant form `(A,q)`.

## Mathematical Claims

### Discriminant Orthogonal Group

For a finite torsion quadratic module `(A,q)`, the orthogonal group

`O(A,q) = Aut_{Modules(ZZ).WithForms().Quadratic().Torsion()}(A,q)`

is the group of automorphisms of the underlying finite abelian group preserving `q`
and the associated bilinear form where present.

Weakest category:
`Modules(ZZ).WithForms().Quadratic().Torsion().AutCategory()`.

Witnesses:
finite torsion module presentation, quotient-valued quadratic form, and a certified
automorphism or stronger finite/generated group representation when generator methods
are claimed.

Computational consequence:
membership of a proposed automorphism is checkable by finite abelian group
automorphism data plus form preservation.  Methods such as `gens()`,
`presentation()`, or a concrete matrix-group return are valid only for a refinement
whose construction supplies generator or presentation witnesses.

### Isotropic Elements and Norm Fibers

For a finite torsion quadratic module `(A,q)`,

`Iso(A,q) = {a in A : q(a) = 0 in Q/2Z}`

is a finite subset of `A`.  More generally, for a value `n in Q/2Z`,

`A_n = {a in A : q(a) = n}`.

Weakest category:
finite torsion quadratic modules with an enumerable finite carrier.

Witnesses:
finite presentation of `A`, value codomain for `q`, exact equality in `Q/2Z`, and
enumeration of the finite carrier or a source-backed finite subset constructor.

### Orbit Sets and Stabilizers

For a subgroup `G <= O(A,q)` acting on a finite subset `X <= A` preserved by `G`, the
orbit set

`X/G`

is a finite quotient set.  For `x in X`, the stabilizer is

`Stab_G(x) = {g in G : g(x) = x}`.

When `G` is given by certified generators and the action on `A` is effective on the
finite set `X`, the representative-level constructions are:

- `orbit_G(x) = {x*g : g in G} <= X`;
- `orbits_G(X) = {orbit_G(x) : x in X}`;
- a representative set `R <= X` with one element in each orbit;
- `Stab_G(x)` as a subgroup of `G`, with generator witnesses only when the finite
  group-action backend returns them in the same group representation.

Weakest category:
finite group actions when `G` is finite with an enumerable or generated action; lazy
group-action objects when `G` is only defined by predicates and membership witnesses.

Witnesses:
the subgroup inclusion `G <= O(A,q)`, a certified action on `A`, proof or check that
`X` is `G`-stable, and finite enumeration or generator witnesses when orbit
representatives are requested.

Typed computation requirement:
a finite backend may enumerate orbits only after choosing a bijection between `X` and a
finite action domain and proving that every generator of `G` preserves `X`.  The backend
output must be converted back to elements of `A` and subgroups of the original
generated `G`.  Raw GAP points, tuples, permutation labels, or Smith-coordinate lists
are not public return objects for discriminant-form orbits.

For stabilizers, the conversion must preserve the acting group.  If the backend acts
directly with `G.gap()` on encoded elements of `X`, then a GAP stabilizer subgroup can
be converted back through the same `FqfOrthogonalGroup` subgroup constructor.  If the
backend first replaces the action by a permutation image `rho(G) <= Sym(X)`, then
`PermutationGroup.stabilizer(label(x))` returns `Stab_{rho(G)}(label(x))`, not
`Stab_G(x)`.  The public stabilizer is the preimage
`rho^{-1}(Stab_{rho(G)}(label(x)))`; returning only the image stabilizer is a different
object and must be named as such.

Public consequences:
`isotropic_orbits()` is shorthand for `Iso(A,q)/O(A,q)` only when the chosen
orthogonal-group realization supplies the finite action data needed to enumerate
orbits.  Otherwise the spec should expose the orbit object and membership/equality
claims without promising representatives.

### Lattice Lifting

Let `L` be an even nondegenerate integral lattice with discriminant form `(A_L,q_L)`.
The natural homomorphism

`O(L) -> O(A_L,q_L)`

is a group homomorphism induced by the action on `L^#/L`.  Its kernel is the stable
orthogonal group `\widetilde O(L)`.

For a primitive lattice vector `v in L`, let

`div(v) = <b(v,w) : w in L> = d Z`

in the scalar-valued integral case.  Then `v/d in L^#`, and the class

`\bar v = v/d + L in A_L`

is the discriminant class attached to `v`.  If `v` is isotropic, then
`q_L(\bar v) = v^2/d^2 = 0 in Q/2Z`, so `\bar v` lies in `Iso(A_L,q_L)`.

The implication from lattice orbits to discriminant-form orbits is formal: if
`g in O(L)` and `w=g(v)`, then `div(w)=div(v)` and
`\bar w = \bar g(\bar v)` under the induced action of `O(L)` on `A_L`.  Thus an
`O(L)`-orbit of primitive isotropic vectors maps to an orbit for the image subgroup
`im(O(L) -> O(A_L,q_L))`.

The converse is not a finite discriminant-form operation.  A claim that finite
`O(A_L,q_L)`-orbits classify primitive isotropic `O(L)`-orbits requires a theorem or
backend with hypotheses.  The source-backed theorem patterns currently available to
the spec are:

- Nikulin surjectivity for the actual indefinite lattice under checked rank, length,
  parity, and discriminant-form hypotheses; this identifies the image of
  `O(L) -> O(A_L,q_L)` only after those hypotheses are verified for `L`;
- Eichler-style criteria when the lattice contains the required hyperbolic summands,
  giving stable-plus equivalence of primitive vectors from the square and the
  discriminant class;
- a named primitive-isotropic orbit backend for isotropic line or plane orbit
  computation when the previous theorem hypotheses are not enough.

Surjectivity of `O(L) -> O(A_L,q_L)` does not by itself construct primitive vector
representatives, prove divisibility values, or compute stable-subgroup orbits.  Those
are separate lattice obligations.  Since `\widetilde O(L)` acts trivially on `A_L`,
stable orbit statements must be made with the actual discriminant class fixed and with
the additional theorem or backend that controls the kernel action.

For the Coble/K3 pipeline, the admissible statement is therefore: first compute the
actual Coble lattice `T`, its discriminant form `(A_T,q_T)`, the divisibility of the
primitive isotropic vectors under consideration, and the finite orbit structure in
`Iso(A_T,q_T)`; then apply a checked Nikulin, Eichler, stable-plus, or backend theorem
to convert that finite result into a lattice orbit claim.  The finite orbit
calculation alone is not a proof of the lattice statement.

Weakest category:
lattices with discriminant descent plus a specified orthogonal subgroup/refinement.

Witnesses:
the lattice `L`, the discriminant descent `L -> L^# -> A_L`, the subgroup of `O(L)`,
the image subgroup in `O(A_L,q_L)`, and the theorem or backend that identifies the
lattice orbit with the finite discriminant-form orbit.

Primitive totally isotropic planes are a further lattice-level object.  Their orbit
statements require a primitive plane `J <= L`, the quotient lattice `J^\perp/J`, and a
building or isotropic-subspace orbit theorem/backend.  They are not methods on a
single element of `A_L`.

## Source-Backed Implementation Evidence

`TorsionQuadraticModule.orthogonal_group(gens=None, check=False)` is Sage evidence for
the finite generated group refinement of `O(A,q)` for Sage torsion quadratic modules.
The source constructs the ambient automorphism group of the finite abelian group with
Smith invariants `A.invariants()`, then returns `FqfOrthogonalGroup(ambient, gens, A)`.
If `gens` is supplied, Sage coerces each supplied matrix, automorphism, or acting object
through the ambient abelian-group automorphism group; this realizes the subgroup of
`O(A,q)` generated by certified finite automorphisms.  If `gens is None`, Sage calls
`_isom_fqf(A)` and caches a small generating set for the full orthogonal group; the
source labels this a slow brute-force computation.

Source evidence:
`sage/modules/torsion_quadratic_module.py:816-887` and
`sage/groups/fqf_orthogonal.py:490-578`.

`FqfOrthogonalGroup._preserves_form(f)` is Sage evidence for the membership witness:
for Smith generators `g_i`, it checks `q(f(g_i)) = q(g_i)` and
`b(f(g_i), f(g_j)) = b(g_i,g_j)`.  This is the finite formed-module preservation
condition, not a lattice-level isometry computation.

Source evidence:
`sage/groups/fqf_orthogonal.py:282-297`.

`ActionOnFqf` is Sage evidence for the right action of the generated orthogonal group
on the torsion quadratic module and invariant subquotients.  Elements are acted on by
the matrix of a group element relative to Smith-form generators, then converted back to
the torsion module by `linear_combination_of_smith_form_gens`.

Source evidence:
`sage/groups/fqf_orthogonal.py:299-487`.

Sage's carrier enumeration and element data come from the finitely presented PID-module
parent inherited by `TorsionQuadraticModule`: `gens()` returns selected generators or
Smith-form generators, element evaluation uses `b` and `q`, and finite enumeration is
owned by the underlying finite FGP module.

Source evidence:
`sage/modules/torsion_quadratic_module.py:420-537` and `[[SPEC-MAPPING-LATTICES]]`.

Oscar/Hecke backend evidence:
the current Oscar/Hecke documentation gives exact `TorQuadModule` discriminant-group
objects, element lifts, `is_isometric_with_isometry(T,U)`, submodules,
`stable_submodules(T, G)`, torsion quadratic modules with a chosen isometry
`(T,f)`, and `automorphism_group_with_inclusion(T,f)`, where `O(T,f)` is the
centralizer of `f` in `O(T)` with an inclusion into `O(T)`.

Source evidence:
Oscar/Hecke discriminant-group docs, `https://docs.oscar-system.org/v1.4/Hecke/manual/quad_forms/discriminant_group/`;
Oscar/Hecke torsion-quadratic-module-with-isometry docs,
`https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/torquadmodwithisom/`;
`theory/backends/oscar-lattices`; `theory-backend-routing`.

Backend consequence:
Oscar/Hecke is a candidate exact backend for discriminant-form objects, isometry tests,
stable submodule enumeration, and centralizer subgroups attached to a specified
isometry.  It is not recorded here as a replacement for the typed finite
`G`-action orbit/stabilizer construction on arbitrary finite subsets `X <= A`, because
the checked docs do not exhibit a public operation that takes `G <= O(A,q)` and `X` and
returns typed orbit representatives and stabilizers in `G`.

Negative finding:

- Searched: Oscar/Hecke discriminant-group docs; Oscar/Hecke torsion-quadratic-module
  with isometry docs; local memories `theory/backends/oscar-lattices`,
  `theory/backends/gap-orbits`, and `theory-backend-routing`.
- Found: exact `TorQuadModule` construction and invariants, isometry and anti-isometry
  tests with maps, stable-submodule enumeration under supplied maps, and
  `automorphism_group_with_inclusion(T,f)` for centralizers in `O(T)`.
- Conclusion: based on the checked docs, Oscar/Hecke should be recorded as a candidate
  backend for formed-module objects, stable submodules, centralizers, primitive
  embeddings, and equivariant extension work, but not as a stronger already-specified
  backend for arbitrary finite subset orbit/stabilizer enumeration under
  `G <= O(A,q)`.
- Confidence: Medium.
- Gaps: source code or newer examples may still expose such a route; a later backend
  implementation card should check the exact Oscar/Hecke source before rejecting it for
  code work.

Stored theory to keep separate:
`theory-orbit-and-building-backends`, `theory-backend-routing`, and
`theory/foundations/reflective-two-elementary-lattices.md` distinguish finite
discriminant-form orbits from lattice-level stable/plus orbit algorithms.

Runtime witness:
for `D = TorsionQuadraticForm(matrix.identity(2)/2)`, Sage constructs
`G = D.orthogonal_group()` with `G.gens()`, `G.order()`, `G.subgroup(...)`, and a right
action `D.gen(0) * G.gen(0)`.  The same object has no public `orbit`, `orbits`, or
`stabilizer` methods.  The only source-backed orbit code found in this Sage family is
the private helper inside `_isom_fqf`, which calls GAP `Orbits(..., OnTuples)` while
searching for generators or isometries.

Source evidence:
`sage/groups/fqf_orthogonal.py:520-536`, `sage/groups/perm_gps/permgroup.py:1672-1948`,
and runtime probe of `FqfOrthogonalGroup_with_category`.

Sage's `PermutationGroup.orbit(point, action=...)`, `orbits()`, and
`stabilizer(point, action=...)` are implementation evidence for the finite-action
backend shape: GAP computes orbits and stabilizers on a finite permutation domain, and
Sage converts the result back to the permutation group's domain or subgroup
representation.  This is evidence for a project conversion layer from typed
discriminant-form elements to finite action labels and back, not evidence that
`FqfOrthogonalGroup` already owns public typed orbit methods.

Source evidence:
`sage/groups/perm_gps/permgroup.py:1672-1968`.

`FqfOrthogonalGroup._subgroup_constructor(libgap_subgroup)` is Sage evidence for the
direct-GAP stabilizer route: a subgroup produced inside the libgap representation of
`G` can be converted back to a generated `FqfOrthogonalGroup` subgroup by coercing GAP
generators through the parent group.

Source evidence:
`sage/groups/fqf_orthogonal.py:344-365`.

Consequence:
finite orbit and stabilizer enumeration for discriminant-form subsets is not inherited
as a public Sage method of `FqfOrthogonalGroup`.  The project should specify it as a
bounded local construction from the finite carrier `X`, the generated finite group
`G`, and the certified action `x * g`; a GAP-backed implementation may use
`libgap.Orbits` and `libgap.Stabilizer` only after the conversion between project
elements and GAP action points is stated.

## Non-Goals

- Do not re-specify the discriminant group's bilinear/quadratic form evaluation (Phase 4).
- Do not specify lattice-level isometry backends as methods on the finite discriminant
  object.
- Do not identify `O(A,q)` with a matrix group carrying generators unless the chosen
  realization actually supplies that stronger finite generated group data.
- Do not implement orbit enumeration from first principles before surveying existing
  finite-group orbit methods in GAP/Sage/Oscar.

## Current Missing Evidence

This card is not complete until the remaining implementation evidence above is
source-mined into ordinary mathematical operation rows.  The unresolved claims are:

- the concrete project implementation witness for the typed conversion
  `X <-> finite action labels` and for converting GAP/permutation orbit and stabilizer
  output back to elements of `A` and subgroups of the generated `G <= O(A,q)`;
- source-code verification for any future Oscar/Hecke implementation card that tries
  to use `TorQuadModule`, `TorQuadModuleWithIsom`, or `automorphism_group_with_inclusion`
  for finite discriminant-form orbit/stabilizer computation beyond the documented
  centralizer and stable-submodule cases;
- the actual Coble lattice data needed before finite discriminant-form orbit results
  can be lifted: Gram model, signature, discriminant form, divisibility of primitive
  isotropic vectors, Nikulin/Eichler hypotheses, and the subgroup of `O(T)` whose
  orbit is being asserted;
- a named backend or theorem for primitive isotropic plane or flag orbits whenever the
  statement involves `J <= L` rather than a primitive vector class.

# Lattice Interface Style Guide

Lattice-specific code conventions for the `src/lattices/` hierarchy.
For general code style rules, see `CONTRIBUTING.md` at repo root.
For the implementation plans, see `PHASE_0_SAGE_PATCHES.md` and
`PHASE_1_BILINEAR_MODULES.md` in this directory.

This guide consolidates lattice-specific conventions from the original
CONTRIBUTING.md and the normalized design directives from the user
corrections in `lattice_redesign_corrections_spec.md`.


## Public Mathematical Model

- A bilinear module is presented by canonical generators of `R^n` together
  with a Gram matrix.
- `BilinearModules(R)` is a genuine new Sage category of pairs `(M, beta)`,
  not merely an informal wrapper convention around existing module parents.
- This must be defined generally over a Sage ring `R`, not hard-coded to `ZZ`
  except where a class specifically models integral lattices.
- Public lattice/module nouns are not naturally embedded in ambient spaces.
- Public nouns must not carry `inclusion_matrix`, `projection_matrix`,
  `projection_lattice`, or similar ambient-embedding state.
- Specific embeddings and subobjects must be represented separately, not
  baked into the core noun.
- `gens()` is semantically well-defined throughout the hierarchy and should
  not be omitted.
- Membership is a parent check: coordinate vectors are not automatically
  elements of a lattice.
- `L.element_from(v)` is the semantic conversion from coordinates to an
  element.


## No Ambient Module Assumption

Sage assumes all lattices inject into some "ambient" module.
**We do not assume this.**

An arbitrary indefinite lattice $L$ does admit a natural map $L \to L
\otimes_{\mathbb{Z}} \mathbb{Q}$ given by $v \mapsto v \otimes 1$, and the
bilinear form extends by linearity. But this is just the general formula for
a tensor product in the category of pairs $(L, b)$.

**This is very different from Sage's assumption** that lattices have a
"basis" of vectors in $\mathbb{Z}^n$ or $\mathbb{Q}^n$. An arbitrary
indefinite lattice is defined abstractly, not as a collection of vectors and
their inner products.

**Rule:** This "everything is in an ambient space" artifact of existing Sage
code should not be used or even acknowledged in our code whatsoever.


## Do Not Leak Sage API

The Sage API should not be leaked through, because it is broken, fragmented,
and theoretically wrong in many places.

**Example:** An `inner_product_matrix` on a lattice makes no sense
mathematically -- an indefinite bilinear form never defines an inner product.
Only expose the API that is specifically requested:

- In the specs and tests
- By other internal code

**Interop with existing Sage code is not a requirement nor desired.** The
entire point is to replace and unify the existing lattice code. Sage's
lattice code was historically only for definite and cryptographic lattice
theory, which is not what we want at all.

No public object should require a Sage object as its constructor input.
Constructors build and store their internal Sage object themselves.
Separate class methods may accept Sage objects and convert them internally.


## Mathematical Syntax Sugar

Nouns should have basic syntax sugar expected in Sage, which are usually
category-level constructions:

| Operator | Meaning |
| --- | --- |
| `A + B` | Direct sum (do **not** follow the Sage-internal "span" interpretation) |
| `A^n` | Direct sum $A + A + \dots + A$ ($n$ times) |
| `n * A` | Usually `A.twist(n)` |
| `f + g` | Usually a map $A_1 \oplus A_2 \to B_1 \oplus B_2$ |
| `f * g` | Usually composition (when defined) |
| `n * f` | Usually `Hom(L_1, L_2).element_from_matrix(n * f.to_matrix())` |
| `x in L` | Validates that `x.parent() == L` -- a lattice does not "contain" a vector |
| `f in O(L)` | Checks isometry |
| `f in Hom(L_1, L_2)` | Checks isometry |

We do **not** automatically coerce when checking membership.

**Quotient notation:** `A / B` := `coker(f: A -> B)` for some specific map
`f`, where sometimes there is a "natural" map returned by something like
`Hom(A, B).natural_map()`.

**Generator assignment:** `L.<e1, e2> = {some lattice construction}` is
typical sugar for extracting and assigning generators, which requires
special methods to exist on `L` (see the Sage preparser code).

### The `__call__` Method for Polymorphic Coercion

The `__call__` method usually handles polymorphic coercion:

- `L.<e1, e2> = Lattice.U()` => `L([1, -2])` produces "$1 \cdot e_1 - 2
  \cdot e_2$"
- `A_L = L.discriminant_group()`, `A_L(e1) == A_L(0)` might also hold
- `H = Hom(L_1, L_2)`, `M = matrix(...)`, `f = H(M)` would convert the
  matrix to a homomorphism

These should ultimately be defined on `classmethod`s, e.g.
`H.element_from_matrix(...)`, and the `__call__` method should be a thin
localized "router".

The specs demonstrate this consistently for orthogonal groups:
```python
swap = matrix(ZZ, [[0, 1], [1, 0]])
assert swap not in O_U2             # A matrix is not a hom
assert O_U2(swap) in O_U2           # __call__ dispatches to element_from_matrix
assert O_U2.element_from_matrix(swap) in O_U2  # Explicit construction
```


## Morphisms, Not Matrices

We do not semantically work with matrices in the frontend layer.
We work with:
- Morphisms
- Gram matrices (as a special case)
- Collections of vectors
- Sublattices (with embedding morphisms)

**Bad example:**
```python
invariant_sublattice(self, involution_matrix)
```
Why? This encourages public users to bypass the correct hom layer entirely.

**Correct approach:** Construct a valid hom from a desired matrix, and only
in backend algorithms do you deconstruct and/or extract its matrix.

Morphisms of free modules are defined symbolically by sending generators to
linear combinations of generators. These are more properly defined in terms
of dicts or list of images, from which the matrices are automatically
constructed and extractible.


## Morphism Construction

Preferred construction is a **dict of generators and their images**.

Allowed classmethods:
- Take a domain and a sequence of images
- Take domain/codomain/matrix when applicable

**Do not** coerce matrices to morphisms. Force users to declare
domain/codomain and explicitly construct using element methods.


## Hom Spaces

`H := A.Hom(B)` is a **space of morphisms** $A \to B$, not a specific
morphism.

Create morphisms via:
- `H.element_from_dict(...)` (preferred)
- `H.element_from_matrix(...)`

Homs should have a reasonable method of infinite enumeration. Since every
$f \in \operatorname{Hom}(L_1, L_2)$ is a $\mathbb{Z}$-matrix, we can
bootstrap a centralized enumeration algorithm for $\mathbb{Z}^m$ to provide
an iterable generator for hom spaces.


## Morphisms and Categorical Semantics

- `hom()` constructs a hom-space, not a specific morphism requiring images.
- Elements of a hom-space are the morphisms.
- Bilinear-module objects need category-owned elements and morphisms, not
  plain Python wrappers carrying Sage objects on the side.
- The category should be hooked properly through Sage parent/category
  machinery, modeled on `sage.categories.modules`, with its own parent
  methods, element methods, and homset category.
- The actual Sage hook for custom homset construction is `_Hom_`; redefining
  `Hom` alone is not sufficient.
- Wrapped elements must be real Sage elements (`Element` /
  `ElementWrapper`-based), not plain Python wrappers carrying Sage objects on
  the side, or Sage morphisms will not compose through `Map.__call__`.
- Morphisms are not containers; no morphism class should define semantic
  containment for arbitrary values.
- `perp` / orthogonal-complement verbs do not belong on morphisms; those
  belong on the relevant subobject or ambient bilinear-module noun.
- General verbs should live as high in the hierarchy as their semantics
  allow: on `BilinearModule`, `BilinearModuleMorphism`,
  `BilinearModuleHomSpace`, and only specialize lower when extra structure
  genuinely appears.
- Cokernels must construct the correct mathematical object, which may be a
  lattice, torsion bilinear module, discriminant form, or another appropriate
  object depending on the context.
- `A_L := coker(L -> L^*)` must be modeled correctly.
- Dual lattices are rational lattices and may be quotiented by more than the
  original lattice.


## Subobjects as Morphisms

"Subobjects" are really morphisms, not objects themselves.

- A subobject needs some kind of mix-in that endows objects with an attached
  morphism and is where notions like "ambient" make sense
- Or one should have explicit `SubLattice` types which extend `Lattice` and
  add all of these notions

**Rule:** Regard a subobject as a morphism, or have explicit subobject
classes. Do not make "subobject" semantics optional notions on the object
itself.


## Subobjects and Division

**Subobject mixin:** Keep track of inclusion morphisms when constructing
subobjects.

- Every element $v$ in $L$ has an inclusion morphism
  $\iota_v: v.\text{span()} \to L$
- Every submodule is defined as a span
  $M := L.\text{span}([v_1, \dots, v_n])$ and a morphism $\iota_M: M \to L$

**Division (`/`):** `B / A` always means `B / im(f)` for some $f: A \to B$.
This requires the subobject mixin which keeps track of inclusion morphisms.

**General cokernel machinery:** Division is completely general and always
yields some bilinear module. Special case: $\iota_L: L \to L^*$ yields the
discriminant group $A_L$, which is a case of automatic promotion.


## Discriminant Groups and Duals

One needs to carefully handle the maps:
- $\iota_L: L \to L^* := \operatorname{Hom}_{\mathbb{Z}}(L, \mathbb{Z})$
- $\iota_L^\sharp: L \to \{v \in L_{\mathbb{Q}} \mid \beta(v, L) \subseteq
  \mathbb{Z}\}$

A dual lattice element is literally a morphism $f_v: L \to \mathbb{Z}$, and
$\iota_L(v) := \beta(v, \cdot)$.

We regard $\iota_L$ as a morphism of rational lattices, so that
$A_L := L^* / \iota(L)$ is actually computed as the cokernel of $\iota_L$.

This should NOT be abstractly constructed from invariants or SNF -- morphisms
like $\iota_L$ should be constructible from matrices and have well-defined
cokernel bilinear modules which are automatically promoted.

One should have a **working vocabulary** of bilinear modules, their morphisms,
cokernels, submodules, etc. One should **not short-circuit** this when
constructing discriminant groups.


## Stabilizers and Centralizers

Stabilizers, centralizers, etc. should be defined on Orthogonal group
objects:

```python
G = L.orthogonal_group()
f = ...
H = G.centralizer(f)
Hp = G.stabilizer(v)
Hp2 = G.stabilizer_of_flag([v1, v2, ...])
```

**Not** as indirected spaghetti methods like
`L.stabilizer_of_flag([v1, v2, ...])`.

Elements can have convenience methods:
- `v.stabilizer()`, `v.stabilizer(in_group=Gamma)`
- `f.centralizer()`, `f.centralizer(in_group=Gamma)`

**No restricted functions** like `centralizer_of_involution`. Instead, have a
generic centralizer function -- if you only support involutions right now,
assert:
```python
assert f.is_involution(), "Non-involutions are not yet supported"
```


## Set Operations

- Use `&` and `|` to mean **intersect** and **union**.
- For modules and lattices, always mean the **span** of such.
- For groups or subsets of lattices (e.g., centralizers, isotropic vectors),
  use **ConditionSets**, and simply use `&` or `|` on those.


## ConditionSets and Membership

Each object we use should truly have some kind of underlying Sage set. Wire
a **ConditionSet** that can be used to check abstract membership "lazily"
based on centralized predicates.


## Invariants and Theory Placement

- `delta` / `coparity` are invariants of lattices `L`, not of discriminant
  groups `A_L`.
- `outside_domain` should not be a separate ad hoc notion when the meaningful
  predicate is `is_p_elementary(2)`.
- Isometry verification belongs in the containment semantics of `O(L)`, not
  scattered matrix-equation assertions.


## API Hierarchy and File Organization

- The redesign must use a real hierarchy of files under a subdirectory
  structure, not a monolithic public file.
- The existing generated code should be migrated into the organized
  hierarchy, not discarded and restarted from scratch.
- Public API terminology should be semantic and stable; do not preserve stale
  names from older designs.


## Typing, Validation, and Dispatch

- Do not use `hasattr` or ad hoc runtime probing where proper typing and
  dispatch are intended.
- Add real type annotations throughout the hierarchy.
- Use Pydantic validation rather than loose assertions for public-object
  validation.
- Do not use `pass` where simple ABCs should be defined.
- Do not use `assert False` in places where mathematically meaningful objects
  must be constructed.


## Anti-Wrapper / Anti-Slop Rules

- Do not introduce helper functions that merely wrap obvious one-line Sage
  functionality.
- Do not create helpers like `zero_gram` when `zero_matrix()` already exists.
- Do not create helpers like identity-column builders when `identity_matrix()`
  already exists.
- Do not create row-oriented constructor helpers when the semantics are really
  about generators or standard objects already available in Sage.


## Terminology and Interop

- Do not expose `native` terminology on the public API.
- If Sage interop must exist, use explicit "sage-like" extraction, not leaked
  wrapper passthroughs.
- Constructors should build and store their internal Sage object themselves.
- Separate class methods may accept Sage objects and convert them internally.
- No public object should require a Sage object as its constructor input.


## Semantics Explicitly Rejected

- `signature_vector` on the public API.
- `merge_orbit_constraints` or parallel subgroup-constraint bookkeeping when
  `ConditionSet` should express subgroup restrictions directly.
- `scaled_element` as a semantic public operation on free-module elements.
- `submodule_from_rows`; submodules are defined by generators, not matrix
  rows as a public noun.
- `projection_lattice`; lattices do not canonically project onto sublattices.
- `lift_vector`; lifts in this context are elements of `L^*`, not bare
  vectors.
- `vec_to_list` style shims.
- old shim names like `has_isomorphic_group_structure_to`.
- ill-defined invariants or algorithms such as the cited `p-rank` method.


## Banned / Out-of-Scope Constructs

- LLL
- Short vectors/closest vectors
- min/max vectors
- `signature_pair` [the pair (p,q) is just called the signature]
- signature defined as p-q [this is the index, not the signature]
- `rescale`, or "scale" used as a verb instead of a noun [scale is an
  invariant, not an operation]
- `IntegralLattice`, `IntegralLatticeGluing`, etc [LatticeGlueData is its
  own class, and `from_glue_data` is a verb for construction]
- `IntegralLatticeDirectSum` [need a bilinear module native solution]
- bases, echelon forms, ambient modules [our lattices are not subsets of any
  "ambient" object]
- Regarding vectors as elements and matrices as morphisms [ill-defined:
  vectors must be EXTRACTED from semantically constructed lattice elements;
  morphisms must be CONSTRUCTED, possibly from a matrix]
- `basis()` [modules have generators, not bases -- "basis" means "generators
  of a K-module" where K is a field]
- `ambient_vector_space`, `vector_space`, etc [module machinery is more
  natural; `L.base_change(QQ)` HAS an associated vector space but is really
  a bilinear QQ-module]
- `basis_matrix` [doesn't make sense, always identity for us]
- `dimension` [free modules have ranks, not dimensions]
- `inner_product` [we do not special case positive definite forms; an
  arbitrary bilinear form is NOT an inner product]
- sparse/dense vectors, matrices [irrelevant numerical optimizations]
- pseudohoms [implement real `Der_R(L_1, L_2)` if needed]
- `complement` [only use `perp()` == orthogonal complement]
- intersections, subspaces, Sage's `A+B` span notation [use explicit
  `L.span([..])` semantics, reserve `+` for direct sum]
- top-level `span` function [not well-defined without specifying the ambient
  lattice; use `L.span([..])`]


## Vocabulary Reference

The following vocabulary is extracted from the authoritative `*.sage` spec
files in `tests/`. These are the behavioral contracts that every object in
the hierarchy must satisfy at the appropriate level.

Source files:
- `tests/sage_spec/misc.sage` (module theory)
- `tests/sage_spec/lattice_methods.sage` (lattice orthogonal groups, spans,
  perps, eigenlattices, roots, Weyl, Coxeter, enumeration)
- `tests/lattice_spec/interface_semantics.sage` (constructors, elements,
  discriminant, orbits, stabilizers)
- `tests/lattice_spec/interface_extensions.sage` (duals, embeddings,
  saturation, explicit groups, Eichler)
- `tests/lattice_spec/more_specs.sage` (dual functionals, twist vs
  multiplication, torsion bilinear modules)
- `tests/sage_spec/coxeter.sage` (root lattices, Coxeter diagrams, diagram
  automorphisms, folding)


### Operator Vocabulary (Expanded)

The syntax sugar table in this document gives short descriptions. The
following clarifies critical distinctions visible in the specs.

**`+` is external direct sum, `L.span([..])` is internal span:**
```python
e.span() + f.span() != L.span([e,f])
```
The left side is the external direct sum (forces off-diagonal gram entries
to zero). The right side is the internal span within `L` (preserves the
bilinear form of `L`). These are **not** interchangeable.

**`L.twist(n)` vs `n * L`:**
`L.twist(n)` scales the gram matrix by `n`. `n * L` scales the generators
by `n`, i.e. `n * L := {n*v | v in L}`. Generally `n * L` is isometric to
`L.twist(n^2)`, not `L.twist(n)`.

```python
assert U.twist(2).gram_matrix() == 2 * U.gram_matrix()
assert not (2*U).is_isometric(U.twist(2))
```

**`L^G` is the invariant sublattice:**
```python
assert L^G == G.invariant_sublattice()
```

**Canonical isomorphisms are equalities:**
When a canonical isomorphism exists, `==` should hold:
```python
assert M/(2*M) == M.tensor(Z2)
assert M.base_change(Z2) == M.tensor(Z2)
assert M.dual() == M.Hom(ZZ)
```

**`<=` for subgroup containment:**
```python
assert G <= L.O()  # G.is_subgroup_of(L.O())
```


### Construction Vocabulary

**Named lattice constructors** (class methods on `Lattice`):
- `Lattice.Z()` -- rank-1 lattice with gram `[[1]]`
- `Lattice.U()` -- hyperbolic plane
- `Lattice.A(n)`, `Lattice.D(n)`, `Lattice.E(n)` -- root lattices
- `Lattice.II(p, q)` -- unique even unimodular lattice of signature `(p,q)`
- `Lattice.I(p, q)` -- unique odd unimodular lattice of signature `(p,q)`
- `Lattice.k3()` -- K3 lattice
- `Lattice.coble_picard()` -- Coble Picard lattice
- `Lattice.from_gram(matrix)` -- construct from gram matrix
- `Lattice.from_string("U(2) + A_1")` -- parse LaTeX-like notation
- `Lattice.root_lattice("A4")` -- root lattice by Dynkin type

**Module constructor** (general bilinear modules):
- `FreeBilinearModule(R, gram_matrix)` -- over any PID `R`
- `BilinearModule(R, gram_matrix)` -- including torsion, e.g.
  `BilinearModule(ZZ/(2*ZZ), matrix(...))`

**Generator assignment syntax** (Sage preparser sugar):
```python
L.<e, f> = Lattice.U()
M.<x, y, z> = ZZ^3
R.<r1, r2, r3, r4> = L.root_system()
G.<n1, n2, n3, n4> = L.coxeter_diagram()
```


### Element Vocabulary

Every element of a bilinear module should support:

| Method | Returns | Semantics |
|--------|---------|-----------|
| `v * w` or `v.inner_product(w)` | scalar | `beta(v, w)` |
| `v^2` or `v * v` | scalar | `beta(v, v)` (norm) |
| `v.is_isotropic()` | bool | `v^2 == 0` |
| `v.is_primitive()` | bool | not `k*w` for any `k >= 2`, `w in L` |
| `v.divisibility()` | integer | `gcd{beta(v, w) : w in L}` |
| `v.discriminant_class()` | element of `A_L` | image in discriminant group |
| `v.span()` | subobject | `L.span([v])` |
| `v.perp()` | subobject | orthogonal complement in ambient |
| `v.inclusion()` | morphism | `v.span() -> L` |
| `v.isotropic_reduction()` | bilinear module | `v.perp() / v` (when `v` isotropic) |
| `v.reflection()` | isometry | `s_v(x) = x - (2*beta(v,x)/beta(v,v))*v` (non-isotropic `v`) |
| `v.is_root()` | bool | `s_v` is an integral isometry |
| `v.stabilizer()` | group | `{g in O(L) : g(v) = v}` |


### Morphism Vocabulary

Every morphism `f: A -> B` of bilinear modules should support:

| Method | Returns | Semantics |
|--------|---------|-----------|
| `f.domain()` | bilinear module | source |
| `f.codomain()` | bilinear module | target |
| `f(v)` | element | apply to element |
| `f.apply_to([v1, v2])` | list | apply to sequence |
| `f.to_matrix()` | matrix | matrix representation |
| `f.to_dict()` | dict | generator-image pairs |
| `f.is_injective()` | bool | trivial kernel |
| `f.is_surjective()` | bool | image equals codomain |
| `f.is_bijective()` | bool | injective and surjective |
| `f.is_isomorphism()` | bool | bijective (as bilinear modules) |
| `f.is_isometry()` | bool | preserves the bilinear form |
| `f.is_identity()` | bool | identity morphism |
| `f.is_involution()` | bool | `f^2 == id` |
| `f.is_primitive()` | bool | cokernel is torsion-free |
| `f.order()` | integer | smallest `n` with `f^n == id` |
| `f.kernel()` | bilinear module | kernel as explicit module |
| `f.cokernel()` | bilinear module | cokernel as explicit module |
| `f.image()` | subobject | image with inclusion |
| `f.lift(element)` | element | find some preimage |
| `f.inverse()` | morphism | inverse (when bijective) |
| `f.direct_sum(g)` | morphism | `f + g: A1+A2 -> B1+B2` |
| `f.base_change(S)` | morphism | extend scalars to `S` |
| `f.cyclic_subgroup()` | group | `<f>` (when `f` is an automorphism) |
| `f.as_word_in_reflections()` | list | decompose into reflections |


### Cokernel Contract

When `f: A -> B` has nontrivial cokernel, the cokernel object must carry:

```python
C = f.cokernel()        # Explicit bilinear module
pi = C.projection()     # The morphism pi: B -> C
assert pi.is_surjective()
assert pi.kernel() == f.image()

# Cokernel generators lift
c_bar = next(iter(C.gens()))
assert c_bar.lift() in B  # Lift back to B

# Cokernel has invariants (for FGP modules)
assert C.invariants() == [2, 3]  # Smith normal form invariants
```


### Hom Space Vocabulary

For `H = A.Hom(B)`:

| Method | Returns | Semantics |
|--------|---------|-----------|
| `H.element_from_dict({...})` | morphism | preferred construction |
| `H.element_from_images([...])` | morphism | images of generators |
| `H.element_from_matrix(M)` | morphism | from matrix representation |
| `H.element_from_function(f)` | morphism | from any callable |
| `H.natural_map()` | morphism | canonical map (when exists) |

**End/Aut:**
```python
assert M.End() == M.Hom(M)
assert M.End().identity() in M.Aut()
assert M.End() in Monoids
assert M.Aut() in Groups
```


### Orthogonal Group Vocabulary

For `G = L.orthogonal_group()` (abbreviated `L.O()`):

| Method | Returns | Semantics |
|--------|---------|-----------|
| `G.stabilizer(v)` | subgroup | `{g : g(v) = v}` |
| `G.stabilizer_of_isotropic_line(v)` | subgroup | `{g : g(<v>) = <v>}` |
| `G.centralizer(f)` | subgroup | `{g : gf = fg}` |
| `G.kernel_of_discriminant_action()` | subgroup | `ker(G -> O(A_L))` |
| `G.isotropic_line_orbits()` | set | orbits of isotropic lines |
| `G.isotropic_plane_orbits()` | set | orbits of isotropic planes |
| `G.isotropic_flag_orbits(dim)` | set | orbits of isotropic flags |
| `G.isotropic_lines_are_equivalent(e, f)` | bool | same orbit |
| `G.special_orthogonal_subgroup()` | subgroup | `SO(L)` |
| `G.inclusion()` | morphism | into `O(L)` (for subgroups) |
| `G.index()` | integer | `[O(L) : G]` |
| `G.identity()` | morphism | identity isometry |
| `G.element_from_matrix(M)` | isometry | validate and construct |
| `G.from_matrix(M)` | isometry | alias |
| `G.subgroup_from_gens([...])` | subgroup | subgroup by generators |
| `G.invariant_sublattice()` | sublattice | `L^G` |
| `G.coinvariant_sublattice()` | sublattice | `(L^G)^perp` |
| `G.invariant_coinvariant_sublattice_pair()` | pair | both at once |

**Convenience abbreviations:**
- `L.O()` = `L.orthogonal_group()`
- `L.W()` = `L.weyl_group()`
- `L.E()` = `L.eichler_group()`
- `L.O_plus()` = stable orthogonal group
- `L.Aut()` = `L.O()` (for lattices, automorphisms = isometries)
- `L.b(v, w)` = bilinear form evaluation


### Dual and Discriminant Vocabulary

**Dual lattice elements are functionals:**
```python
L_dual = L.dual()
e_star, f_star = L_dual.gens()
assert e_star in L.Hom(Lattice.Z())   # Each dual element is a morphism L -> ZZ
assert e_star(e) == 1 and e_star(f) == 0   # Dual basis
```

**The inclusion morphism `iota_L: L -> L*`:**
```python
iota = L.dual().inclusion_morphism()
assert iota(e) == L.Hom(Lattice.Z()).from_dict({e: L.b(e,e), f: L.b(e,f)})
```

**Discriminant group from cokernel:**
```python
assert L.discriminant_group() == L.dual() / L
```

**Discriminant class of elements:**
```python
assert e.discriminant_class() in A_L
assert e.discriminant_class().lift() in L.dual()
```

**Discriminant form methods:**
```python
A = L.discriminant_group()
assert A.b(g1, g2) == QQ(1, 2)          # Bilinear form (QQ/ZZ-valued)
assert A.q(g1) == 0                       # Quadratic form (QQ/2ZZ-valued)
assert A.isotropic_elements() == {...}    # {g : q(g) == 0}
assert A.elements_of_norm(k) == {...}     # {g : q(g) == k}
assert A.value_map() == {0: {...}, 1: {...}}  # norm -> elements
```


### Direct Sum Structure

When `L = L1 + L2`:

```python
L1p, L2p = L.summands
iota_1, iota_2 = L.embeddings

assert iota_1.domain().is_isometric_to(L1)
assert iota_1.image().perp() == iota_2.image()
assert iota_1.is_primitive()
assert iota_1.cokernel().is_isomorphic_to(L2)

# Direct sum of embeddings
iota = iota_1.direct_sum(iota_2)
assert iota.is_bijective() and iota.is_isomorphism()
```


### Span and Subobject Vocabulary

**Spans are constructed from an ambient lattice:**
```python
S = L.span([v1, v2, v3])    # Internal span within L
assert S.inclusion() in S.Hom(L)
assert S.perp() == ...       # Perp within L
```

**Perps are defined with respect to inclusion morphisms:**
```python
assert e.perp() == e.span().perp()
```

**Saturation:**
```python
assert S.is_saturated()      # Cokernel of inclusion is torsion-free
assert S.saturation() == L   # Smallest saturated overlattice
assert S.inclusion().index() == 2
```


### Root and Weyl Vocabulary

```python
L.roots()                    # ConditionSet of roots (v with v^2 = -2 and s_v integral)
L.root_sublattice()          # Sublattice spanned by roots
L.is_root_lattice()          # Root sublattice == L

v.reflection()               # s_v: the reflection isometry
s.is_reflection()            # True if s = s_v for some root v
s.reflection_decomposition() # Decompose into product of reflections

L.W()                        # Weyl group = group generated by reflections in roots
L.W().gens()                 # Set of generating reflections
L.W().coxeter_diagram()      # Weighted graph of root angles

eichler_transvection(e, r)   # Eichler transvection for isotropic e, root r in e.perp()
L.E()                        # Eichler group
```


### Coxeter Diagram Vocabulary

```python
G = L.coxeter_diagram()
G.subdiagram_poset()         # Poset of sub-diagrams
G.subdiagram({0, 1})         # Sub-diagram on node subset
G.adjacency_matrix()         # Weighted adjacency
G.is_connected()
G.Aut()                      # Weight-preserving graph automorphisms

# Diagram morphisms from root morphisms
fold = G.Hom(G).element_from_dict({n1: n4, n2: n3, ...})
root_fold.diagram_morphism()  # Convenience
```


### Category Promotion

Objects automatically promote to the richest category their invariants
support. This is not optional: quotients, subobjects, and constructions
must check and promote.

```python
# Degenerate bilinear module, not a lattice
assert e.span() in BilinearModules(ZZ)
assert e.span() not in Lattices(ZZ)

# Quotienting can produce a lattice
assert e.perp()/e in Lattices(ZZ)   # Isotropic reduction is nondegenerate

# Root sublattices promote
assert r.span() in RootLattices

# Hyperbolic lattices promote
assert L.is_hyperbolic()
assert L in HyperbolicLattices
```


### Enumeration Contract

All countable objects must support iteration. The iteration should "spiral"
outward from small elements:

```python
# ZZ^n has a canonical enumeration via diagonal argument
assert {zero_vector, e_1, -e_1, e_2, -e_2, ...} <= set(itertools.islice(ZZ^4, 20))

# Lattice enumeration delegates to ZZ^n enumeration via coordinates
assert {L.zero(), e, -e, f, -f} <= set(L.enumerate(5))

# Convenience for bounded slicing
L.enumerate(bound=20)  # == itertools.islice(L, 20)
```


### Witness Pattern

Methods that answer existence questions should optionally return witnesses:

```python
is_isom, witness = L1.is_isometric_to(L2, witness=True)
assert is_isom and witness.is_isometry()
assert witness in L1.Hom(L2)

is_isom, witness = G.is_isomorphic_to(H, witness=True)
assert is_isom and witness.is_isomorphism()
assert witness in G.Hom(H)
```

When `witness=False` (default), return only the boolean.


### Isometry Comparison Hierarchy

Lattice comparison has a strict hierarchy of conditions, from weakest to
strongest:

```python
L.is_rationally_isometric_to(M)       # Over QQ
L.is_locally_isometric_to(M, p)       # Over ZZ_p for prime p
L.is_in_same_genus_as(M)              # Locally isometric at all primes
L.is_isometric_to(M)                  # Over ZZ (strongest)
```

Each condition implies the ones above it. The discriminant group provides
obstructions:
```python
A_L.isomorphic_as_groups(A_M)         # Necessary for genus
A_L.is_isometric_to(A_M)             # Stronger: isometric as forms
```


## Spec Authority and Execution Discipline

- The lattice spec is authoritative.
  If a behavior appears in the normative spec files, it is required target
  behavior until the user explicitly revises that status.
- Do not describe unmet spec surface as "aspirational", "optional",
  "migration-only", or otherwise outside the redesign gate merely because the
  implementation does not satisfy it yet.
- Do not describe unfinished required implementation as a "blocker".
  It is remaining required work on the spec itself.
- Do not treat completion of a local redesign slice as completion of the task.
  The task ends only when the required spec surface is actually implemented.
- The redesign plan is a signoff artifact and must stay truthful.
  It must not claim architectural completion while required spec work remains.

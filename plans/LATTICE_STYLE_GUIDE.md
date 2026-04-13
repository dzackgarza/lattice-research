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


## Style Principles

The following principles are distilled from the authoritative `*.sage` spec
files in `tests/`. They generalize the style to any new code, including
objects and constructions not yet specced. For concrete method signatures
and behavioral contracts, read the spec files themselves:

- `tests/sage_spec/misc.sage` -- module theory
- `tests/sage_spec/lattice_methods.sage` -- orthogonal groups, spans, perps,
  eigenlattices, roots, Weyl, Coxeter, enumeration
- `tests/lattice_spec/interface_semantics.sage` -- constructors, elements,
  discriminant, orbits, stabilizers
- `tests/lattice_spec/interface_extensions.sage` -- duals, embeddings,
  saturation, explicit groups, Eichler
- `tests/lattice_spec/more_specs.sage` -- dual functionals, twist vs
  multiplication, torsion bilinear modules
- `tests/sage_spec/coxeter.sage` -- root lattices, Coxeter diagrams,
  folding


### Write Code That Reads as Mathematics

Prefer syntax that mirrors how a mathematician would write it on a
blackboard. Sage's preparser and operator overloading exist precisely for
this.

| Prefer | Avoid |
|--------|-------|
| `ZZ^n` | `FreeModule(ZZ, n)` |
| `ZZ/2` | `ZZ.quotient(ZZ.ideal(2))` |
| `2*ZZ` | `ZZ.ideal(2)` |
| `M + N` | `M.direct_sum(N)` |
| `M * N` | `M.tensor_product(N)` |
| `B / A` | `B.quotient_by(A)` |
| `L^G` | `G.invariant_sublattice()` |
| `G <= H` | `G.is_subgroup_of(H)` |
| `f^2 == id` | `f.is_involution()` (as a definition; ok as a convenience) |

The test for whether syntax is right: could you copy-paste it into a
textbook and have it be understood? `ZZ^3` reads as "$\mathbb{Z}^3$";
`FreeModule(ZZ, 3)` reads as a Java constructor.


### Containment Over Equations

The single most important principle. To verify a property of an object,
**check that it lives in the right set**, don't reproduce the defining
equations of that set.

**Bad:**
```python
assert all(m in ZZ for m in M.gram_matrix().list())
assert f.to_matrix().T * G * f.to_matrix() == G
```

**Good:**
```python
assert M.gram_matrix() in GL(n, ZZ)
assert f in L.O()
```

Why: `f in O(L)` asserts a *mathematical theorem* -- that `f` is an
isometry. The manual matrix equation asserts a *programming fact* that
happens to be equivalent. The set-membership version:

- Has one source of truth for the defining equation (inside `O(L).__contains__`)
- Prevents convention drift (left vs right action, transpose conventions)
- Reads like mathematics
- Generalizes: the same pattern works for `f in Hom(L_1, L_2)`,
  `v in ZZ^n`, `M in Modules(ZZ)`, `G in Groups`

**Corollary -- assert mathematical content, not implementation
tautologies:**

```python
# Rich mathematical fact: base change preserves module structure
assert L.base_change(ZZ/2) in Modules(ZZ) and L.base_change(ZZ/2) in Modules(ZZ/2)

# Tautology: reads back a constructor argument
assert L.base_ring() == ZZ
```

The first tells you something about the *category theory* of base change.
The second tells you nothing you didn't already know from constructing `L`.
Prefer assertions that would be nontrivial theorems.


### Canonical Isomorphisms Are Equalities

When a canonical isomorphism exists in mathematics, `==` should hold in
code:

```python
assert M/(2*M) == M.tensor(ZZ/2)
assert M.base_change(ZZ/2) == M.tensor(ZZ/2)
assert M.dual() == M.Hom(ZZ)
assert L.discriminant_group() == L.dual() / L
```

This is not just sugar. It enforces that the universal property is actually
implemented: the base change of `M` to `ZZ/2` must *be* the tensor product,
not merely be isomorphic to it.


### Verbs Live on the Right Noun

Every mathematical verb belongs on the object that *owns* that concept.
When in doubt, ask: "In a textbook, what object is the subject of this
sentence?"

- Stabilizers, centralizers, orbits -> methods on the group, not the lattice
- Perp, span -> methods on the element or subobject, not the ambient space
- Kernel, cokernel, image -> methods on the morphism
- Invariants (delta, coparity) -> methods on the lattice, not its
  discriminant group

**Bad:** `L.centralizer_of_involution(f)` -- the lattice is not computing
centralizers; the group is.

**Good:** `L.O().centralizer(f)` -- the orthogonal group owns the concept.

This generalizes: if you're adding a new verb and it feels awkward on the
noun you've chosen, you probably need a different noun.


### Constructions Return Objects, Not Data

Every categorical construction (kernel, cokernel, image, dual, span, perp,
etc.) must return a fully-formed object in the appropriate category, not
raw data.

- `f.kernel()` returns a bilinear module, not a matrix or a list of vectors
- `f.cokernel()` returns a bilinear module with `.projection()` and `.lift()`
- `v.span()` returns a subobject (with inclusion morphism), not a set
- `L.dual()` returns a bilinear module whose elements are functionals

The returned object must be complete: it must live in the right category,
support all the verbs that category provides, and have correct morphisms
connecting it back to its source. If `f.cokernel()` doesn't have a
projection morphism from `B`, it's not a cokernel -- it's a data leak.


### Automatic Category Promotion

Objects promote to the richest category their invariants support. This is
not optional; all constructions must check and promote.

```python
assert e.span() in BilinearModules(ZZ)         # Degenerate, not a lattice
assert e.span() not in Lattices(ZZ)
assert e.perp()/e in Lattices(ZZ)              # Quotient happens to be nondegenerate
```

The principle: **don't force the user to know in advance what category the
result will land in.** When a quotient of bilinear modules happens to be
nondegenerate, it should automatically be a `Lattice`, not a generic
`BilinearModule` that the user must manually cast. Similarly, a root
sublattice should automatically be in `RootLattices`, a hyperbolic lattice
in `HyperbolicLattices`, etc.


### Operators Mean One Thing

Each operator has exactly one mathematical meaning across the entire
hierarchy. Never overload an operator to mean different things in different
contexts.

| Operator | Universal meaning |
|----------|-------------------|
| `+` | Direct sum (external). Never "span" or "union" |
| `*` | Tensor product (of modules), or composition (of morphisms) |
| `/` | Cokernel of the natural inclusion |
| `^` | Power: `L^n` = n-fold direct sum, `f^n` = n-fold composition, `L^G` = invariant sublattice |
| `in` | Category or parent containment. Never automatic coercion |
| `&` | Intersection (of sets, groups, condition sets) |
| `|` | Union / join |
| `<=` | Subset / subgroup containment |

**Critical distinction -- `+` vs `span`:**
`e.span() + f.span()` is the *external* direct sum (zero off-diagonal
entries). `L.span([e, f])` is the *internal* span within `L` (inherits the
bilinear form of `L`). These are mathematically different and must not be
confused.

**Critical distinction -- `twist` vs scalar multiplication:**
`L.twist(n)` scales the *form* by `n`: the gram matrix becomes `n*G`.
`n*L` scales the *generators* by `n`: the sublattice `{n*v : v in L}`.
The resulting gram matrix of `n*L` is `n^2 * G`, not `n*G`.


### Witnesses for Existence Claims

Any method that answers an existence question ("is there an isometry?",
"is this isomorphic?") should optionally return a witness:

```python
is_isom, f = L1.is_isometric_to(L2, witness=True)
assert f in L1.Hom(L2)
```

The witness is itself a mathematical object (a morphism, an element, etc.)
that lives in the appropriate hom space or parent. It is not a matrix, a
dict, or a boolean -- it is a proof.


### Everything Iterates

All countable mathematical objects must support `__iter__`. Infinite objects
use lazy generators that "spiral" outward from small elements. The key
principle: **iteration follows the mathematical structure**, not an
implementation-convenient ordering.

For `ZZ^n`, this means a diagonal-argument enumeration that visits elements
of increasing norm. For a group, this means enumerating by word length in
generators. The user should be able to find any element by iterating long
enough, without needing to know the implementation strategy.


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

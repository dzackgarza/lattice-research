---
id: SPEC-HISTORICAL-LATTICE-CONSTRUCTORS-INVARIANTS-AND-COMPARISONS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS]]'
title: Recover lattice constructors, invariants, and comparison predicates
status: needs-review
priority: high
requirement: Standard constructors, invariants, and comparison predicates from historical
  lattice code must be recovered with source-grounded mathematical owners and theorem
  hypotheses.
acceptanceCriteria:
- Named standard-lattice constructors are admitted through the approved constructor
  layer and remain available for later research reuse.
- Coble-specific derived lattice constructors are not used as evidence in the feature
  that proves the Coble lattice presentation.
- Rank, determinant, signature, scale, evenness, genus, local genus, rational isometry,
  and integral isometry are methods on the appropriate lattice noun.
- Nikulin-style invariants are lattice invariants with explicit domain hypotheses
  and warnings or rejection outside those hypotheses.
- Comparison predicates either return exact booleans with sourced criteria or return
  witness-bearing morphisms when the claim is existential.
complexity: 75
tags:
- FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY
---
# Recover lattice constructors, invariants, and comparison predicates

## Source Provenance

- `src.bak/lattices/core/integral.py`: `Z`, `U`, `A`, `D`, `E`, `I`, `II`,
  `from_string`, `scale`, `is_even`, `genus`, `local_genus_symbol`,
  `is_rationally_isometric_to`, `is_locally_isometric_to`,
  `is_in_same_genus_as`, `is_isometric_to`, and `nikulin_invariants`.
- `src.bak/lattices/core/rational.py`: rational Gram construction, integral
  promotion, signature, and negative root Gram construction.
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`:
  backend routing for isometry/genus/local conditions, constructor naming, negative
  root-lattice convention, twist versus scalar multiplication, signature terminology,
  and Nikulin invariant ownership.
- `.agents/memories/bilinear-form-category-semantics.md`: named constructor placement,
  negative root convention, hyperbolic plane convention, and stable orthogonal group
  notation.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`:
  source-backed owner rows for constructors, direct sums, twist, signature, genus,
  isometry predicates, and deferred definite/indefinite algorithms.

## Contract

The constructor surface must recover common lattice families and operations only after
the current constructor admission layer says where they live. Examples include rank-one
lattices, hyperbolic planes, root lattices, odd and even unimodular lattices, K3
lattices, Mathieu-related lattices where source-grounded, twists, direct sums, and
parseable expression syntax if that syntax is approved as public.

The invariant surface must be method-owned by the lattice noun. Immediate invariants
such as rank, determinant, signature, scale, and evenness are computed directly from
the presentation. Genus, local equivalence, rational equivalence, and integral isometry
must route to mature exact backends or theorem-backed classification branches.

Nikulin-style data such as `(r, a, delta)` are invariants of the lattice under explicit
hypotheses. They must not be presented as discriminant-group-local facts and must not
be used outside their theorem-backed domain as if classification still applies.

## Recovered Constructor Surface

Named standard constructors are admitted as project vocabulary when they construct a
presented lattice object with selected generators and form data:

- `Lattice.Z()` constructs the rank-one lattice `<1>`.
- `Lattice.U()` constructs the hyperbolic plane with Gram `[[0,1],[1,0]]`.
- `Lattice.A(n)`, `B(n)`, `C(n)`, `D(n)`, `E(n)`, `F4()`, and `G2()` construct the
  repo's root-lattice convention. Roots are negative definite unless the constructor
  explicitly says otherwise; backend positive-definite conventions are sign-adjusted at
  the backend boundary.
- `Lattice.I(p, q)` constructs the odd unimodular lattice of signature `(p,q)`.
- `Lattice.II(p, q)` constructs the even unimodular indefinite lattice when the
  existence hypotheses hold, including `p-q == 0 mod 8` and positive rank.
- `Lattice.k3()` constructs the K3 lattice as a standard comparison object
  `II(3,19)`.
- `RationalLattice.from_gram(...)` owns Gram construction with promotion to the
  integral lattice meet when the Gram matrix is integral and the hypotheses hold.
- `Lattice.from_gram(...)` is the integral closed constructor after validation.
- `from_string(...)` is optional parser syntax for the same named constructors; it must
  remain a parser for approved constructor expressions, not an independent semantic
  surface.

`direct_sum(other)` or `L + M` is the orthogonal direct sum with block-diagonal form
data and selected generators. `L ** n` is repeated orthogonal direct sum when admitted
as notation. `twist(s)` scales the form by `s`; it is not scalar multiplication of the
carrier or selected generators. Scalar multiplication of submodules remains the module
operation `{s*x : x in M}`.

## Derived Research Constructor Boundary

The historical `coble_picard()` and `coble_transcendental()` methods are not admitted
as proof shortcuts. The Coble pipeline must first construct the geometric lattice from
the surface/cover data, then compare it with a standard target by a sourced isometry
test or witness.

After that derivation is accepted, a canonical project constructor such as a named
`T_Co` target may be added as downstream convenience. Its docstring must cite the
accepted proof artifact or decision authorizing the standard presentation, and it must
not replace the derivation in the feature that proves the Coble lattice presentation.

## Recovered Immediate Invariants

Immediate invariants are computed from the presented object and its form:

- `rank()` or `ngens()` is the finite rank of the selected free carrier.
- `gram_matrix()` is presentation data for the form in selected generators.
- `determinant()` or `discriminant()` is the determinant/discriminant of the presented
  form where that invariant is defined.
- `signature_pair()` is the pair `(n_+, n_-)` after scalar extension to a selected
  ordered real realization. Sage's scalar `signature() = n_+ - n_-` is display or
  interop data, not the owner of signature semantics.
- `scale()` is the ideal generated by all pairings `b(x,y)`; over `ZZ` this is a
  principal ideal generator after sign convention is fixed.
- `is_even()` means `b(x,x) in 2R` for every element under the integral form
  hypotheses; it is not a definite-lattice property.
- `is_unimodular()` means `L = L^#`, equivalently trivial discriminant group under the
  nondegenerate integral hypotheses.

## Recovered Theorem And Backend Invariants

The following methods are admitted only with explicit theorem or backend branch data:

- `genus()` returns the genus data for integral lattices through a sourced local-global
  theory or an exact backend such as Hecke/Oscar.
- `local_genus_symbol(p)` returns the local genus symbol at a prime and must record
  the local field/ring and backend/theorem used.
- `is_in_same_genus_as(other)` compares genus data only after both objects satisfy the
  same branch hypotheses.
- `is_rationally_isometric_to(other)` is a rational isometry predicate over `K` and
  must route through a mature exact quadratic/form backend or return a witness when
  requested.
- `is_locally_isometric_to(other, p)` compares local isometry at `p` under the local
  branch hypotheses.
- `is_isometric_to(other, witness=False)` is integral lattice isometry. With
  `witness=True`, it must return an isometry morphism or a structured failure, not only
  a boolean.

Backend failure is not proof of non-isometry. If the selected backend cannot decide a
case, the method must report an undecided/error state or route to a tracked backend-gap
task instead of silently weakening the claim.

## Recovered Nikulin-Style Invariant Surface

`nikulin_a()`, `coparity()`, `delta()`, and `nikulin_invariants()` are lattice theorem
context methods. They are admitted only under the explicitly recorded branch for even
indefinite 2-elementary lattices or another cited theorem with equivalent hypotheses:

- `r = rank(L)`;
- `a` is the length of the 2-elementary discriminant group;
- `delta`/`coparity` is determined by the parity of the discriminant quadratic form;
- the discriminant group may expose `is_p_elementary(p)`, but it does not own
  `delta`, `coparity`, or `(r,a,delta)`.

Outside the theorem-backed domain, implementations must either reject the method call
or emit the category diagnostic warning required by `SPEC-MAPPING-CAT` and return only
the explicitly meaningful components. They must not imply Nikulin classification or
genus uniqueness outside the stated hypotheses.

## Standard Library Versus Derived Research Objects

Standard lattice constructors are a desired library surface. They let later research
use canonical sourced objects instead of constructing ad hoc isometric presentations
such as `I_{1,10}(2)`, `\langle -2 \rangle \oplus U(2) \oplus E_8(2)`, or a
handwritten Gram matrix when the intended object is already canonical.

Derived project objects are separate. The feature that proves a Coble lattice is
isometric to a standard presentation must construct the object geometrically, then
verify the isometry. It may use standard constructors as comparison targets only after
the constructed lattice exists. Once accepted, a canonical sourced `T_Co` surface is
desirable for downstream research so later agents do not re-invent equivalent
presentations.

## Non-Preservation Boundaries

- Do not preserve `coble_picard` or `coble_transcendental` as proof shortcuts that
  bypass the Coble construction.
- Do not present a self-computed invariant match as an isometry without the theorem,
  hypotheses, or witness required for that branch.
- Do not hide backend failure by falling back to weaker sampled or bounded checks.
- Do not duplicate simple Sage or Oscar constructors behind trivial helper aliases
  unless the alias is the approved project vocabulary.

## Acceptance Criteria

- [x] Every recovered standard constructor has an owner category and source grounding.
- [x] Derived project constructors such as a future canonical `T_Co` record the proof
  artifact or decision that authorizes their downstream use.
- [x] Every recovered invariant records whether it is immediate, theorem-backed, or
  backend-computed.
- [x] Integral isometry and classification predicates state the exact branch used and
  the evidence needed to accept the result.
- [x] Coble derivation code is forced to construct the geometric input before invoking
  lattice comparisons.
- [x] Downstream post-derivation Coble research is directed to use the canonical
  sourced `T_Co` rather than ad hoc isometric presentations or raw Gram matrices.

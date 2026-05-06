---
id: SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY]]'
dependsOn:
- '[[FEATURE-MODULES-WITH-FORMS-AND-LATTICES]]'
title: Recover presented lattice object and element contracts from src.bak
status: needs-review
priority: high
requirement: The historical presented-lattice object model must be recovered as category-correct
  presented modules with forms, not as Sage ambient lattices.
acceptanceCriteria:
- Lattice objects distinguish selected generators, Gram presentation, equality of
  presentations, and isometry by a morphism witness.
- Coordinate vectors enter a lattice only through a semantic element constructor such
  as element_from; raw vectors are not public elements.
- Dual and rational lattice objects are actual formed-module objects with explicit
  maps, not matrices masquerading as objects.
- Subobjects, spans, and primitive checks are specified through generators and morphisms
  rather than rows, ambient spans, or ad hoc coordinate helpers.
complexity: 70
tags:
- FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY
---
# Recover presented lattice object and element contracts from src.bak

## Source Provenance

- `src.bak/lattices/core/rational.py`: `RationalLattice`, `from_gram`, `dual`,
  `signature_pair`, and root Gram construction.
- `src.bak/lattices/core/integral.py`: `Lattice`, `element_from`, `dual`,
  `overlattice`, `scale`, `is_even`, and conversion between raw backend matrices and
  column-action public matrices.
- `src.bak/lattices/core/elements.py`: element coordinate conversion and primitive
  coordinate ideal check.
- `.agents/skills/lattice-redesign/references/category-abc-spec.md`: presented object
  identity and morphism semantics.
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`:
  parent-owned element construction, subobject/morphism discipline, and lattice API
  audit rules.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`:
  Sage-source reconciliation for `dual_lattice`, `discriminant_group`, element
  divisibility, subobjects, and formed-module method ownership.

## Contract

A recovered lattice object is a presented free bilinear module. Its public identity
contains the carrier, form data, and chosen generators. Changing generators returns a
new presented object and, when appropriate, an explicit isometry or isomorphism witness.

Elements belong to a fixed parent. A coordinate vector is not an element until the
parent constructs it through a method such as `element_from`. Element methods may expose
coordinates relative to the selected generators, but public algorithms must consume
elements and morphisms rather than free-floating vectors.

The rational, dual, and integral specializations must be expressed as category objects:
codomain extension to `Frac(R)`, dual objects, and integral promotion are mathematical
constructions with maps. A matrix may represent one of these maps after generators are
chosen, but the matrix is not the public object.

## Recovered Presented-Object Surface

The historical `Lattice.from_gram(gram, generator_names=...)` and
`RationalLattice.from_gram(gram, generator_names=...)` paths recover a constructor
from a finite selected generating set and a symmetric Gram presentation. The admitted
surface is not "a matrix is a lattice"; it is:

- a free finitely generated carrier module `M` over `R`;
- selected generators `B = (b_i)` as presentation data;
- a bilinear form `beta: M tensor_R M -> S`, where `S = R` for integral lattices and
  `S = K = Frac(R)` for rational lattices;
- `gram_matrix()` as the matrix of `beta` in the selected generators;
- `gens()`, `gen(i)`, `ngens()`, and `rank()` as presentation-owned generator access;
- `base_ring()` for `R` and `form_codomain()` or `value_ring()` for `S`.

Changing `B`, reducing a basis, canonicalizing a backend presentation, or passing
through Sage's ambient lattice model returns a new presented object. If the new object
is meant to represent the same mathematical object up to isometry, the construction
must return or record an explicit isometry witness in the formed-module Hom/Aut
surface. Equality remains presentation-sensitive; isometry is witnessed.

## Recovered Element Surface

The historical `element_from` and element classes recover the following contract:

- `L.element_from(coordinates)` is the only public conversion from coordinates in the
  selected generators to an element of `L`.
- Raw Sage vectors, rows, coordinate lists, or ambient vectors are not elements until a
  parent constructs them.
- `x.parent()`, `x.coordinates()` or `x.to_coordinates()`, and `x.to_vector()` are
  presentation readback methods, not membership substitutes.
- Element addition, subtraction, negation, and scalar multiplication are parent-local
  module operations.
- `x.b(y)` or `x.bilinear_product_with(y)` is defined only for elements in the same
  formed parent, or through an explicitly declared pairing with a dual object.
- `x.span()` constructs the subobject generated by `x` together with its inclusion
  morphism.
- `x.perp()` is shorthand for the orthogonal subobject to `x` only in a symmetric
  formed-module context; morphisms do not have perpendiculars.
- `x.divisibility()` is the ideal or submodule generated by `{beta(x, m): m in M}` in
  the form codomain. Coordinate gcds are backend witnesses only under stated
  hypotheses.
- `x.is_primitive()` for a free integral presentation is a coordinate-ideal predicate
  relative to the selected generators; primitive subobject predicates are owned by the
  inclusion or quotient surface and must not be conflated with element divisibility.

## Recovered Dual And Discriminant Surface

The recovered spec must separate three constructions that old names and Sage examples
can blur:

- `M.dual()` for a plain module is the Hom dual `Hom_R(M, R)`, an evaluation-bearing
  object in `Modules(R).DualObjects()`.
- `L.dual_lattice()` is the metric dual
  `L^# = {x in L_K : beta(x, L) subset R}` inside scalar extension to `K = Frac(R)`.
  Elements of `L^#` are not functionals by definition.
- A nondegenerate form may transport `x in L^#` to a functional
  `beta(x, -) in Hom_R(L, R)`; this is a recorded map/isomorphism under hypotheses,
  not an identity of constructions.

The historical `DualLattice` class therefore recovers the metric-dual object and its
maps, not the category-theoretic `DualObjects()` contract. Its admissible public
surface is:

- `source_lattice()` or `primal_lattice()` as provenance for the construction;
- `inclusion_morphism(): L -> L^#`;
- `element_from_primal_coordinates(...)` and `element_from_dual_coordinates(...)` as
  presentation-aware constructors;
- `primal_coordinates_of(x)` as coordinate readback for the selected presentation;
- `discriminant_class(x)` as the cokernel projection `L^# -> L^#/L`.

`L.discriminant_group()` must be the cokernel object of `L -> L^#`, with descended
quotient-valued bilinear or quadratic form data when the hypotheses hold. It is not
only a Smith-normal-form invariant package. For ordinary `v in L`, the discriminant
class is zero after inclusion into `L^#`; nonzero discriminant classes come from the
metric-dual/rational side.

Any implementation docstring for `dual_lattice()`, lattice-side `dual()` compatibility
spellings, or `discriminant_class()` must mention the global disabled-by-default
category diagnostic flag from `SPEC-MAPPING-CAT` and state when to warn about Hom-dual
versus metric-dual confusion.

## Recovered Subobject And Morphism Surface

Subobjects are generated by elements and carry inclusion morphisms. Historical row,
ambient-span, and Sage escape-hatch code is implementation evidence only. The admitted
surface is:

- `L.span(elements)` or `L.subobject_generated_by(elements)` returning a subobject with
  an inclusion morphism into `L`;
- `i: A -> B` as a formed-module morphism whose containment check owns
  form-preservation;
- `i.kernel()`, `i.image()`, and `i.cokernel()` as actual categorical objects with
  projection/lift structure where applicable;
- `B / A` only as notation for the cokernel of a recorded inclusion `A -> B`;
- `is_primitive()` for a subobject/inclusion as quotient torsion-freeness, not as a
  coordinate heuristic.

Matrices may construct morphisms through Hom parents such as `L.Hom(M).from_matrix(A)`.
They do not become public morphisms until Hom containment validates domain, codomain,
and form compatibility.

## Non-Preservation Boundaries

- Do not preserve `inner_product_matrix` as a public semantic name for indefinite
  lattices; use form or Gram vocabulary approved by the lattice specs.
- Do not preserve row-based submodule constructors. Subobjects are generated by
  elements and represented with embedding morphisms.
- Do not preserve `_sage_like` or backend escape hatches as public API.
- Do not use ambient-module membership to decide lattice element membership.

## Acceptance Criteria

- [x] The spec surface states the presented-object identity data and equality/isometry
  distinction.
- [x] Element construction and coordinate extraction are parent-owned and presentation
  explicit.
- [x] Dual/rational/integral promotion has named maps and return objects.
- [x] Any backend canonicalization that changes presentation returns a witness.

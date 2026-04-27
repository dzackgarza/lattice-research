# Rings Triage

Source for the current documentation pass: `rings/docs/SAGE_INVENTORY.md`,
`rings/docs/MAPPING.md`, Sage written category docs, and local Sage category source.

This file records documentation blockers before runtime validation. Existing constructor
refinement failures remain below as runtime blockers, but they are not the source of
truth for the current organization pass.

## Current Alignment

- Constructor entry points are exposed as `Rings().Constructors()`.
- Construction categories are split under `subcategories/constructions/`.
- Homsets, endsets, and automorphism sets are now treated as required category
  surfaces, not incidental method names on ring parents.
- Subquotients and isomorphic objects are documented as parent construction categories
  for subobjects and quotients.
- `Rings().NamedRings()` is not part of the forward surface. The canonical constructor
  namespace is `Rings().Constructors()`.

## Audit Conclusions Before Runtime Validation

- Ring homsets are a required explicit project surface even though Sage constructs them
  through `Rings.ParentMethods._Hom_` and may categorize them through lower algebraic
  supercategories. The target is `rings/homsets.py` for ring-homomorphism vocabulary
  and top-level `homsets/` for generic hom/end/aut behavior.
- Ring endsets are homsets with identical domain and codomain. The project `Autsets`
  target is the invertible part of the ring endset, with ring automorphisms preserving
  addition, multiplication, zero, and one.
- `Rings().Subquotients()` and `Rings().IsomorphicObjects()` are inherited construction
  surfaces and must be explicit files alongside `subobjects.py` and `quotients.py`.
  Quotient rings refine the subquotient surface through ideals or congruences.
- Ring subobjects are subrings in the ring category. Ideals are separate ring-side
  vocabulary unless the ideal is being regarded as a ring object in a specific
  category.
- Ring Cartesian products are direct products with componentwise operations; constructor
  signatures should use a sequence of ring parents at constructor level and reserve
  variadic forms for Sage parent-method compatibility.
- Ring realization categories use the generic realization surface. The audited
  `Rings` category source does not add ring-only realization parent methods.
- Ring-family documentation targets are mathematical files or nested directories:
  fields, finite fields, number fields, local rings, valuation rings, complete rings,
  quotient rings, polynomial rings, power-series rings, and matrix rings/algebras.
- Product, quotient, homset, extension, and free-module-over-subring signatures need
  `types.py` vocabulary: `Ring`, `RingElement`, `RingIdeal`, `QuotientRing`,
  `Subring`, `RingHomset`, `RingEndset`, `RingAutset`, and module-return types for
  `free_module`.
- Ring-family category surfaces are split into one mathematical file per family under
  `rings/subcategories/`.
- Category navigation methods live on `Rings.SubcategoryMethods` or on the
  subcategory that introduces the further restriction.

## Source note: ring-specific realizations

- Searched: local Sage `sage/categories/rings.py`, local `sage/rings/` package via
  Probe for `WithRealizations`, `Realizations`, homset, quotient, subquotient, and
  isomorphic-object terms.
- Found: The searched `Rings` category source exposes ring homsets, quotient rings, and
  generic inherited construction surfaces; it did not expose ring-specific
  `WithRealizations` or `Realizations` parent methods.
- Conclusion: inference -- ring realization mapping should use generic construction
  files unless a concrete ring-family source later provides its own realization
  methods.
- Confidence: Medium.
- Gaps: full Sage develop-tree search and ring-family-by-ring-family realization audit
  were not completed in this pass.

## Missing `completion`

These constructors fail with `AssertionError: Not implemented method: completion`.

- `Rings().Constructors().RR()`
- `Rings().Constructors().CC()`
- `Rings().Constructors().RDF()`
- `Rings().Constructors().CDF()`
- `Rings().Constructors().RIF()`
- `Rings().Constructors().CIF()`
- `Rings().Constructors().RealField(100)`
- `Rings().Constructors().ComplexField(100)`
- `Rings().Constructors().RealBallField(100)`
- `Rings().Constructors().ComplexBallField(100)`
- `Rings().Constructors().Zp(5)`
- `Rings().Constructors().Qp(5)`
- `Rings().Constructors().Zq((5, 2), names='a')`
- `Rings().Constructors().Qq((5, 2), names='a')`

## Missing `gcd`

These constructors fail with `AssertionError: Not implemented method: gcd`.

- `Rings().Constructors().ZZ()`
- `Rings().Constructors().QQbar()`
- `Rings().Constructors().AA()`
- `Rings().Constructors().GF(5)`
- `Rings().Constructors().NumberField(x^3 - 2, 'a')`
- `Rings().Constructors().CyclotomicField(5)`

## Missing `S_class_group`

This constructor fails with `AssertionError: Not implemented method: S_class_group`.

- `Rings().Constructors().QQ()`

## Missing `is_algebraically_closed`

These constructors fail with `AssertionError: Not implemented method: is_algebraically_closed`.

- `Rings().Constructors().IntegerModRing(6)`
- `Rings().Constructors().PolynomialRing(ZZ, 't')`

## Missing `Aut`

This constructor fails with `AssertionError: Not implemented method: Aut`.

- `Rings().Constructors().QuadraticField(5, 'a')`

## Missing `extension`

These constructors fail with `AssertionError: Not implemented method: extension`.

- `Rings().Constructors().PowerSeriesRing(ZZ, 't')`
- `Rings().Constructors().LaurentSeriesRing(ZZ, 't')`
- `Rings().Constructors().PuiseuxSeriesRing(QQ, 't')`

## Missing `End`

This constructor now fails with `AssertionError: Not implemented method: End`.

- `Rings().Constructors().MatrixRing(ZZ, 2)`

This changed after removing module-theoretic redeclarations from the
matrix-algebra ring spec. The previous `annihilator` failure was a spec
placement error in the ring construction-category surface; once matrix algebras inherit
their module surface instead of redeclaring it locally, refinement reaches
the next real missing surface on the Sage object.

## Consequence

The ring subtree records the constructor-level missing-method inventory separately from
the structural layout. Structural files now use the forward AGENTS.md pattern:
constructor entry points are inner methods on `Rings.Constructors`, navigation is on
`Rings.SubcategoryMethods`, and ring-family specs live in mathematical subcategory
files.

## Outstanding Decisions Needed

- Decide which topological-ring methods should be inherited from `topological_spaces`
  and which methods are genuinely ring-specific.

## Constructor Identity Notes

`RealField`, `ComplexField`, `RealIntervalField`, `ComplexIntervalField`, `RealBallField`, and `ComplexBallField` are constructor families parameterized by precision (and related options). `RR`, `CC`, `RIF`, and `CIF` are fixed named objects at Sage's default precision choices for their respective families.

Use exact identity statements rather than informal "equals" language:

- `RR is RealField(53)` is `True`.
- `CC is ComplexField(53)` is `True`.
- `RIF is RealIntervalField(53)` is `True`.
- `CIF is ComplexIntervalField(53)` is `True`.
- `RDF is RealField(53)` is `False`.
- `CDF is ComplexField(53)` is `False`.
- `RR is RDF` is `False`.
- `CC is CDF` is `False`.

Interpretation for spec work:

- `RR` / `CC` can have one-object category refinements.
- `RealField(...)` / `ComplexField(...)` and related precision families remain multi-object parameterized subcategories.
- `RDF` / `CDF` remain distinct one-object targets from the MPFR-backed `RealField` / `ComplexField` families.

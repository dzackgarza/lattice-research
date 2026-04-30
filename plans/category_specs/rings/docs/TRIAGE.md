# Rings Triage

Source for the current documentation pass: `rings/docs/SAGE_INVENTORY.md`,
`rings/docs/MAPPING.md`, Sage written category docs, and local Sage category source.

This file records the current `rings/smoketest.sage` frontier. The smoke is expected
to fail until the listed missing surfaces and structural blockers are implemented.

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

## Category Base-Class Mismatch

These constructors currently fail while refining through nested axiom categories.
The error reports matching class names with nonmatching class identity, so this is a
category-construction/cache boundary issue, not a missing ring method.

- `_IntegralDomains` over `_CommutativeRings`:
  `Rings().Constructors().ZZ()`
- `_Fields` over `_CommutativeRings`:
  `Rings().Constructors().QQ()`, `QQbar()`, `AA()`, `RR()`, `CC()`, `RDF()`,
  `CDF()`, `RIF()`, `CIF()`, `RealField(100)`, `ComplexField(100)`,
  `RealBallField(100)`, `ComplexBallField(100)`, `GF(5)`,
  `NumberField(x^3 - 2, 'a')`, `QuadraticField(5, 'a')`, and
  `CyclotomicField(5)`.
- `_CompleteRings` over `_TopologicalRings`:
  `Rings().Constructors().Zp(5)`, `Qp(5)`, `Zq((5, 2), names='a')`, and
  `Qq((5, 2), names='a')`.

## Missing `_sympy_`

These constructors refine far enough to expose the next missing Sage/project method:

- `Rings().Constructors().IntegerModRing(6)`
- `Rings().Constructors().PolynomialRing(ZZ, name='t')`
- `Rings().Constructors().PowerSeriesRing(ZZ, 't')`
- `Rings().Constructors().LaurentSeriesRing(ZZ, 't')`
- `Rings().Constructors().PuiseuxSeriesRing(QQ, 't')`
- `Rings().Constructors().MatrixRing(ZZ, 2)`

## Consequence

The current ring smoke failures are implementer-facing: the next work is either fixing
the category-base identity mismatch in the axiom construction path or implementing the
listed missing `_sympy_` surface on the relevant refined parents. Matrix algebra
ownership remains a separate design decision; do not hide it by moving or weakening the
matrix smoke.

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

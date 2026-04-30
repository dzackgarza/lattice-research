# Sets Triage

Source for this pass: `sets/docs/SAGE_INVENTORY.md` and `sets/docs/MAPPING.md`.

This triage records the current `sets/smoketest.sage` frontier. Mathematical mapping
decisions live in `sets/docs/MAPPING.md`.

## Current Smoke Frontier

- `sets/smoketest.sage` now exercises `RealSet` with an actual Sage real-interval
  object, matching the admitted `Sets().Constructors().RealSet(intervals=...)` shape.
- `sets/smoketest.sage` documents the `Set(ZZ)` replacement by checking `ZZ in Sets()`
  and documents the `Set([1, 2, 3])` replacement through
  `Sets().Constructors().from_iterable([1, 2, 3])`.
- The smoke still fails on existing abstract-method sentinels, not on tuple/list
  interval data, constructor call-shape mismatches, or arbitrary `Set(X)` wrapping.
- Missing `_element_constructor_`: `RealSet([RealSet.open(0, 1).get_interval(0)])`.
- Missing `_an_element_from_iterator`: `FiniteEnumeratedSet`, `IntegerRange`,
  `RecursivelyEnumeratedSet`, `DisjointUnionEnumeratedSets`, `CartesianProduct`,
  `ImageSubobject`, `TotallyOrderedFiniteSet`, `FiniteSetMaps`, `Family`, and
  categorical `cartesian_product`.
- Missing `__len__`: `NonNegativeIntegers`, `PositiveIntegers`, and
  `EnumeratedSetFromIterator`.
- Missing `__iter__`: `Primes`.
- Missing `algebra`: `Sets().Subobjects().Of(ZZ, predicates=(even predicate,))`.

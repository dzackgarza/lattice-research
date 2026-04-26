# Sets: Sage Category → Spec Hierarchy Mapping

This file records, for each Sage category relevant to `Sets()`, the mathematical
justification for how it maps to our hierarchy.

## Sage `EnumeratedSets` → our `Sets().Countable()`

Sage's `EnumeratedSets` axiom captures: "there exists an explicit enumeration
(iteration) of the set's elements." Countability is equivalent: a set is countable
iff there exists an injection f: X → ℕ, which is precisely an enumeration.
Every Sage enumerated set is countable, and every countable set in our hierarchy
must supply an iterator (via `__iter__`).

Consequence: objects that lie in `SageEnumeratedSets()` are refined to
`Sets().Countable()`. The spec class `_CountableSets` therefore declares
`super_categories = [Sets(), SageEnumeratedSets()]`.

## Sage `FiniteEnumeratedSets` → our `Sets().Countable().Finite()`

Finite enumerated sets are both finite and countable.

## Sage `InfiniteEnumeratedSets` → our `Sets().Countable().Infinite()`

Infinite enumerated sets are countably infinite.

## Sage `FacadeSets` → our `Sets().Facade()`

Facade sets represent their elements as elements of another parent.
Mapping is direct: `SageFacadeSets()` ↔ `Sets().Facade()`.

## Sage `TopologicalSpaces` → our `Sets().Topological()`

Sage's `TopologicalSpaces()` captures topological structure. `RealSet` lives here.

## Sage `FiniteSets` → our `Sets().Finite()`

Direct: `SageFiniteSets()` ↔ `Sets().Finite()`.

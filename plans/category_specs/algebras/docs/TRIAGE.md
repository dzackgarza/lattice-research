# Algebras Triage

## Current Alignment

- `Algebras(R)` exists as a top-level category over a base ring.
- Algebra-specific parent methods are centralized in `algebras/__init__.py`.
- The first shared-axiom subcategories are split into one file each:
  `Commutative`, `WithBasis`, `FiniteDimensional`, `FiniteDimensional().WithBasis()`,
  and `Semisimple`.
- These subcategories reuse the global axiom names from `axioms.py` and add only the
  algebra-specific method surfaces forced by those restrictions.
- Algebra construction categories are split under `subcategories/constructions/` for
  subobjects, quotients, Cartesian products, tensor products, and dual objects.

## Outstanding Decisions Needed

- Decide the first concrete constructor entries for `Algebras(R).Constructors()`.
- Decide how matrix algebras should be split between `rings`, `modules`, and `algebras`
  without duplicating inherited method surfaces.

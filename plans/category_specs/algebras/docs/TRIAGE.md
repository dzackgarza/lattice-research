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

## Current Smoke Frontier

`algebras/smoketest.sage` currently fails in two expected places:

- `Algebras(ZZ).DualObjects()` fails while Sage/project axiom inference tries to build
  the nested `category_specs.modules.homsets._Forms` class of `RModuleHomsets`.
  This is a module-homset/form-axiom blocker, not an algebra constructor issue.
- `Algebras(ZZ).Constructors() has admitted constructor cases` is the deliberate
  sentinel for the unresolved algebra constructor inventory.

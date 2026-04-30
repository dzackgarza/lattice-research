# Algebras Triage

## Current Smoke Frontier

`algebras/smoketest.sage` currently fails in two expected places:

- `Algebras(ZZ).DualObjects()` fails while Sage/project axiom inference tries to build
  the nested `category_specs.modules.homsets._Forms` class of `RModuleHomCategory`.
  This is a module hom-category/form-axiom blocker, not an algebra constructor issue.
- `Algebras(ZZ).Constructors() has admitted constructor cases` is the deliberate
  sentinel for the unresolved algebra constructor inventory.

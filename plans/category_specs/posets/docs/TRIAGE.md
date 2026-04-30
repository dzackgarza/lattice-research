# Posets Triage

The promoted subtree now exists and owns the order-theoretic method surface.
Remaining audit work is to expand constructor inventories for concrete Sage poset
constructors under a later constructor pass, not to model posets as ordinary set
subcategories.

## Current Smoke Frontier

`posets/smoketest.sage` currently fails in one expected constructor-frontier place:

- `Posets().Constructors() has admitted constructor cases` is the deliberate sentinel
  for the unresolved poset constructor inventory in the root `NEEDS_DECISIONS.md`.

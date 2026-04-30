# Homsets Triage

Source for this pass: Sage `sage/categories/homsets.py`, the project subtree
homset files, and the user directive to create a root homsets subtree.

Runtime smoke validation now instantiates `Homsets()`, `Homsets().Endset()`,
`Homsets().Endset().Autset()` through the `Homsets().Autset()` convenience selector,
and the `Cat` functor hom/end/aut layers.

## Current Smoke Frontier

No additional homsets-specific missing obligation is recorded in this file. Mapping
and ownership decisions live in `homsets/docs/MAPPING.md`.

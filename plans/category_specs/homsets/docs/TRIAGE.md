# Homsets Triage

Source for this pass: Sage `sage/categories/homsets.py`, the project subtree
homset files, and the user directive to create a root homsets subtree.

Runtime smoke validation has not been run in this pass.

## Audit Conclusions

- The project needs a root `homsets` subtree, not a flat `homsets.py`, because homsets,
  endsets, autsets, and their element surfaces are shared across every mathematical
  category subtree.
- Sage already supplies `HomsetsCategory`, `Homsets`, and `Homsets.Endset`; the project
  extends these constructions rather than replacing them.
- Generic autset construction belongs in `homsets/utils.py`. Subtrees should call
  `refine_automorphism_set_from_endset` instead of recreating `ConditionSet` logic.
- Set, ring, module, and algebra homset files remain responsible only for
  category-specific morphism laws.

## Integration Results

- `rings/homsets.py` now delegates autset construction to the root helper.
- `sets/homsets.py` now delegates autset construction to the root helper.
- `modules/homsets.py` now exposes autset refinement through the root helper.
- `types.py` now exposes generic hom/end/aut vocabulary from `homsets`.

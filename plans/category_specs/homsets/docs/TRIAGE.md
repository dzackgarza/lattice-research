# Homsets Triage

Source for this pass: Sage `sage/categories/homsets.py`, the project subtree
homset files, and the user directive to create a root homsets subtree.

Runtime smoke validation now instantiates `Homsets()`, `Homsets().Endset()`,
`Homsets().Autset()`, and the `Cat` functor hom/end/aut layers.

## Audit Conclusions

- The project needs a root `homsets` subtree, not a flat `homsets.py`, because homsets,
  endsets, autsets, and their element surfaces are shared across every mathematical
  category subtree.
- Sage already supplies `HomsetsCategory`, `Homsets`, and `Homsets.Endset`; the project
  extends these constructions rather than replacing them.
- Sage's `Homsets().Endset()` is a valid category. Sage models it as an axiom of
  `Homsets`, not as an independent functorial construction, so the project adds
  `EndsetsCategory` and the visible constructor `Endsets().Of(C)`.
- Generic autset construction belongs in `homsets/utils.py` and is exposed through
  `GenericAutsets`. Subtrees inherit it instead of calling the helper directly.
- Set, ring, module, algebra, and topological-space homset files remain responsible
  only for category-specific morphism laws and genuinely additional structure.

## Integration Results

- `rings/homsets.py` now inherits generic autset construction through
  `GenericAutsets`.
- `sets/homsets.py` now inherits generic autset construction through
  `GenericAutsets`.
- `modules/homsets.py` now establishes the extra-structure pattern: `Hom_R(M, N)` is
  an `R`-module and `End_R(M)` is an `R`-algebra, while Autset construction remains
  generic.
- `algebras/homsets.py` and `topological_spaces/homsets.py` now declare their
  hom/end/aut categories as extension points for algebra homomorphisms, continuous
  maps, and homeomorphisms.
- `types.py` now exposes generic hom/end/aut vocabulary from `homsets`.

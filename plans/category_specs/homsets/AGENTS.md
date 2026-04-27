# homsets subtree

This subtree owns the generic homset, endset, and autset category specs.

Rules:

- Extend Sage's `sage.categories.homsets.HomsetsCategory`, `Homsets`, and
  `Homsets.Endset` through the registered re-exports in `category_specs.cat`; do not
  inherit raw Sage category bases directly or create a parallel model of homsets.
- Keep the three root spec categories in separate files:
  - `homsets.py` owns `Homsets`, whose `ParentMethods` are homset specs and whose
    `ElementMethods` are morphism specs.
  - `endsets.py` owns `Endsets`, defining only genuinely new endset methods.
  - `autsets.py` owns `Autsets`, defining only genuinely new autset methods.
- Use the root category constructors `Homsets().Of(C)`, `Endsets().Of(C)`, and
  `Autsets().Of(C)` for the generic hierarchy internal to an arbitrary base category
  `C`.
- `HomsetsOf`, `EndsetsOf`, and `AutsetsOf` are construction implementation classes.
  The visible constructor form is `Homsets().Of(C)`, `Endsets().Of(C)`, and
  `Autsets().Of(C)`. These construction classes set supercategories so Sage mixes in
  the root specs; they do not define `ParentMethods` or `ElementMethods`.
- Private method-surface classes are local indentation devices. Never export them and
  never import them into another file; refer to public category attributes such as
  `Homsets.ParentMethods` in `types.py`.
- Keep generic `Aut(X)` construction here. Subtrees must not recreate
  `ConditionSet`-based autset wiring.
- Subtree homset files inherit from `HomsetsOf`, `GenericEndsets`, and
  `GenericAutsets`. They declare additional structure; they do not repeat generic
  identity, endset, inverse, or invertibility plumbing.
- Subtree-specific files may add mathematical laws for their morphisms, such as set
  maps, ring homomorphisms, module homomorphisms, or algebra homomorphisms.
- A homset object has a domain and codomain. An endset is `Hom(X, X)`. An autset is
  the invertible part of an endset.
- Element surfaces distinguish morphisms, endomorphisms, and automorphisms.

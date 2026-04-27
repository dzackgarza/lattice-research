# homsets subtree

This subtree owns the generic homset, endset, and autset category specs.

Rules:

- Extend Sage's `sage.categories.homsets.HomsetsCategory`, `Homsets`, and
  `Homsets.Endset`; do not create a parallel model of homsets.
- Keep generic `Aut(X)` construction here. Subtrees must not recreate
  `ConditionSet`-based autset wiring.
- Subtree-specific files may add mathematical laws for their morphisms, such as set
  maps, ring homomorphisms, module homomorphisms, or algebra homomorphisms.
- A homset object has a domain and codomain. An endset is `Hom(X, X)`. An autset is
  the invertible part of an endset.
- Element surfaces distinguish morphisms, endomorphisms, and automorphisms.

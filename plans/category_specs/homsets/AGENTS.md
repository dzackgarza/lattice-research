# homsets subtree

This subtree owns the generic homset, endset, and autset category specs.

Rules:

- Extend Sage's `sage.categories.homsets.HomsetsCategory`, `Homsets`, and
  `Homsets.Endset` through the registered re-exports in `category_specs.cat`; do not
  inherit raw Sage category bases directly or create a parallel model of homsets.
- If a hom/end/aut failure suggests new local plumbing, first ask whether the object is
  using a raw Sage construction or the wrong base category. The intended solution is a
  Cat-native construction hierarchy that lets Sage mix in the declared method surfaces,
  not an additional dispatcher that imitates Sage's homset machinery.
- Domain, codomain, call, identity, composition, inverse, and invertibility are
  universal morphism/homset concerns. If they appear first or repeatedly in module,
  ring, set, or algebra homset subtrees, treat that as evidence that the generic
  `homsets/`, `endsets/`, or `autsets/` surface is missing the abstraction.
- Subtree homset specs own only the structure that first appears there. Set homsets may
  declare that functions between sets are sets; module homsets should focus on
  `R`-linearity, enrichment over `R-Mod`, algebra/ring structure on endsets, and
  representability of automorphism groups. They must not restate generic morphism
  mechanics.
- This is a mathematical separation, not a DRY rule. If a fact is true for every
  morphism, put it on the generic morphism/homset surface because that is where it is
  true. If a fact first becomes true for `R`-linear maps, ring maps, or continuous
  maps, put it in that subtree even if the implementation is inconvenient.
- Do not let set, module, ring, or algebra homset specs own the bare facts that
  `End(X)` is a monoid or `Aut(X)` is a group. Those are generic end/aut facts.
  Specialized subtrees may state the additional structure, such as `End_R(M)` as an
  `R`-algebra or `Aut_R(M)` as a representable matrix group when appropriate.
- Keep the three root spec categories in separate files:
  - `homsets.py` owns `Homsets`, whose `ParentMethods` are homset specs and whose
    `ElementMethods` are morphism specs.
  - `endsets.py` owns `Endsets`, defining only genuinely new endset methods.
  - `autsets.py` owns `Autsets`, defining only genuinely new autset methods.
- Use the root category constructors `Homsets().Of(C)`, `Endsets().Of(C)`, and
  `Autsets().Of(C)` for the generic hierarchy internal to an arbitrary base category
  `C`. `Autsets().Of(C)` routes through the endset category:
  `C.Homsets().Endset().Autset()`.
- `HomsetsOf`, `EndsetsOf`, and `AutsetsOf` are construction implementation classes.
  The visible constructor form is `Homsets().Of(C)`, `Endsets().Of(C)`, and
  `Autsets().Of(C)`. These construction classes set supercategories so Sage mixes in
  the root specs; they do not define `ParentMethods` or `ElementMethods`.
- The generic method surfaces are public universal classes:
  `UniversalHomsetObjectMethods`, `UniversalHomsetElementMethods`,
  `UniversalEndsetObjectMethods`, `UniversalEndsetElementMethods`,
  `UniversalAutsetObjectMethods`, and `UniversalAutsetElementMethods`. Subtrees may
  extend these surfaces through category inheritance, but must not re-declare the same
  abstract method lower in an end/aut chain.
- Keep generic `Aut(X)` construction here. Subtrees must not recreate
  `ConditionSet`-based autset wiring.
- Subtree homset files inherit from `HomsetsOf`, `GenericEndsets`, and
  `GenericAutsets`. They declare additional structure; they do not repeat generic
  identity, endset, inverse, or invertibility plumbing.
- `Autset` is an axiom on an endset category, not directly on a homset category.
  Homset-level `Autset()` methods are convenience selectors and must return
  `self.Endset().Autset()`. Concrete homset classes declare `Endset = ...`; concrete
  endset classes declare `Autset = ...`.
- Audit `Autset` wiring by ontology: an automorphism set is the invertible predicate
  subset of an endomorphism set. If a proposed change attaches an autset class directly
  to a homset class, first justify why the mathematical object is not an endset
  subcategory. In this hierarchy, that justification should almost never exist.
- Subtree-specific files may add mathematical laws for their morphisms, such as set
  maps, ring homomorphisms, module homomorphisms, or algebra homomorphisms.
- A homset object has a domain and codomain. An endset is `Hom(X, X)`. An autset is
  the invertible part of an endset.
- Element surfaces distinguish morphisms, endomorphisms, and automorphisms.

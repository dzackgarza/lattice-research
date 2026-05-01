# Category Spec Todo

This list tracks live category-spec work. It is not a decision log; concrete human
choices live in `NEEDS_DECISIONS.md`.

## Delegated Research Pass

- [x] Encode orthogonal groups as automorphism groups in modules with forms.
  `OrthogonalGroup(M, b)` means automorphisms of the module-with-form object preserving
  the form. Lattice orthogonal groups specialize this aut surface inside the lattice
  category.
- [x] Repair the `algebras/` scaffold with source-backed inventory and mapping docs.
  Plain-set Sage `S.algebra(R)` is routed to the module constructor surface; true
  set-to-algebra construction is routed separately through Sage `FreeAlgebra`.
- [x] Repair the `topological_spaces/` scaffold with pure topological-space inventory,
  ambient-relative method mapping, and `Connected`, `Compact`, and metric `Complete`
  subcategory stubs.
- [x] Build the initial poset subtree from Sage's documented finite poset, semilattice,
  and lattice surfaces, including finite meet- and join-semilattice subcategories.

## Remaining Implementation Todo

- [x] Add the concrete formed-module `orthogonal_group()` parent method returning the
  appropriate aut object, and add standard Hom/End/Aut names for discriminant groups
  before exporting a `DiscriminantGroupAut` alias.
- [x] Implement Sage-backed `free_algebra_from_set` through Sage `FreeAlgebra`, and
  implement `S.free_module(R)` by routing directly through
  `Modules(R).Constructors().CombinatorialFreeModule(basis_keys=S)`. Keep Sage's
  plain-set `S.algebra(R)` path as inventory and migration evidence only.
- [ ] Admit pure topological constructors after the real-line and real-subset ownership
  choices in `NEEDS_DECISIONS.md` are settled.
- [ ] Admit poset, meet-semilattice, join-semilattice, and lattice constructors through
  named closed overloads for the documented Sage input cases.

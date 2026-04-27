# Sage Poset Inventory

Sage exposes order-theoretic posets through `sage.categories.posets.Posets`,
`sage.categories.lattice_posets.LatticePosets`, and
`sage.categories.finite_lattice_posets.FiniteLatticePosets`.

`Posets.ParentMethods` requires `le` and exposes derived order comparisons,
covers, ideals, filters, chains, antichains, and order-ideal toggles.
`LatticePosets.ParentMethods` requires `meet` and `join`.
`FiniteLatticePosets.ParentMethods` exposes irreducible-element posets and
finite lattice morphism checks.

# Posets Mapping

Sage `Posets()` maps to the promoted `category_specs.posets.Posets()` category.
It remains a set-structured category, but its method surface is order-theoretic
and therefore not buried under `sets/subcategories/`.

Sage `LatticePosets()` maps to `Posets().Lattice()`. Here "lattice" means an
order-theoretic meet/join lattice. It does not mean a free module with a
bilinear form.

Sage `FiniteLatticePosets()` maps to `Posets().Lattice().Finite()`.

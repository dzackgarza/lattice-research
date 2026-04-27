# Posets Subtree

This subtree specifies order-theoretic categories promoted out of `sets/`.
Here, a lattice is a poset in which every pair of elements has a meet and a join.
It is unrelated to module lattices or quadratic-form lattices.

Homsets, endsets, and autsets live in `homsets.py`. Their elements are
order-preserving maps, poset endomorphisms, and poset automorphisms; the generic
Autset construction is inherited from the root `homsets/` subtree.

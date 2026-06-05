# Dawes 2022 Orbits In Lattices Source Notes

Source:

- Matthew Dawes, *Orbits in Lattices*, arXiv:2205.10601.
- The local markdown symlink `theory/references/literature/dawes2022orbits.md` currently
  points to a missing extracted PDF artifact.  The statements below were checked against
  the arXiv TeX source `orbits_in_lattices.tex` acquired from
  `https://arxiv.org/e-print/2205.10601`.

## Lattice conventions

Dawes works with lattices equipped with an integral symmetric bilinear form.  The
signature is denoted `(t_+,t_-)`; `U` is the hyperbolic plane with Gram matrix
`[[0,1],[1,0]]`; `mL` is the orthogonal direct sum of `m` copies of `L`; and `L(m)`
means the same underlying group with the form multiplied by `m`.

A vector is isotropic when its square is zero, and primitive when its generated rank-one
sublattice is primitive.  Dawes defines the dual lattice, discriminant group
`D(L)=L^vee/L`, and discriminant form `q_L` in the usual way.

## Isotropic vectors and Tits buildings

In the section titled "Algorithms for Tits' buildings and isotropic vectors," Dawes
works with lattices of signature `(2,n)` and groups contained in `O^+(L tensor Q)`.
The Tits-building definition uses orbits of totally isotropic subspaces of dimensions
one and two in `L tensor Q`, and Dawes notes that this is equivalently formulated using
primitive totally isotropic sublattices of `L`.

Algorithm 4.1 computes the Tits building of a finite-index subgroup from a known
building for a larger group by refining the larger group's isotropic line and plane
orbits.  The following remark states that the same node-refinement part computes
orbits of isotropic vectors.

## Maximal and split maximal lattices

Dawes defines a maximal lattice `L'` by the condition that its discriminant group has no
nontrivial totally isotropic subgroup.  Every lattice has a maximal overlattice, using
Nikulin's correspondence between overlattices and isotropic subgroups of the
discriminant group.

A maximal lattice of signature `(2,n)` is called split when it is isomorphic to
`2U + L_0'`.  Dawes records the Attwell-Duval result that a maximal lattice of
signature `(2,n)` is split for `n>=5`.

For a maximal lattice `L'` of signature `(2,n)`, Algorithm 4.2 computes the
`O^+(L')` Tits building.  Its line-node set is initialized with a single primitive
isotropic vector `e`; hence `O^+(L')` has one orbit of primitive isotropic lines.

## Primitive isotropic vector transport

Algorithm 4.4 applies to a split maximal lattice

```text
L = U + L_1,  L_1 = U + L_0.
```

For primitive isotropic vectors `x,y in L`, it constructs an element
`tau(x,y) in O^+(L)` such that

```text
tau(x,y) x = y.
```

The proof uses the standard `SL(2,Z) x SL(2,Z)` action on the `2U` summand and Eichler
transvections.  For the Coble target reduction, the important consequence is that a
split maximal lattice of signature `(2,n)` has one `O^+(L)` orbit of primitive
isotropic vectors, not merely one orbit of isotropic lines.

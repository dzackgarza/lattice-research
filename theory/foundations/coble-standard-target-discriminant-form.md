# Coble Standard Target Discriminant Form

For the Dolgachev-Kondo Coble target

```text
N = <2> + E_10(2)
```

use the project convention `E_10 = U + E_8(-1)`.  Thus

```text
N = 2B,  where  B = <1> + U + E_8(-1).
```

The lattice `B` is unimodular.  Hence

```text
A_N = N^#/N = (1/2)B / 2B ~= B/2B ~= (Z/2Z)^11.
```

For a residue class represented by `a in B`, the discriminant quadratic form is

```text
q_N(a/2 + N) = B(a,a)/2 mod 2Z.
```

Therefore `a/2 + N` is isotropic exactly when

```text
B(a,a) = 0 mod 4.
```

Using the Gram model `<1> + U + E_8(-1)`, exact enumeration of the `2^11` classes in
`B/2B` gives:

```text
|{x in A_N : q_N(x)=0}| = 528.
```

The zero class is one of these classes, so the standard target has `527` nonzero
isotropic discriminant-form classes.

The full finite orthogonal-group orbit decomposition is also determined.  Let

```text
Q(a mod 2B) = B(a,a) mod 4.
```

Then

```text
O(A_N,q_N) = {g in GL(B/2B) : Q(gx)=Q(x) for every x in B/2B}.
```

Equivalently, `O(A_N,q_N)` is the stabilizer in `GL(B/2B)` of the four fibers
`Q^{-1}(0)`, `Q^{-1}(1)`, `Q^{-1}(2)`, and `Q^{-1}(3)`.  Exact GAP/Sage computation of
that stabilizer gives:

```text
|Q^{-1}(0)| = 528, |Q^{-1}(1)| = 528, |Q^{-1}(2)| = 496, |Q^{-1}(3)| = 496,
|O(A_N,q_N)| = 46998591897600,
Iso(A_N,q_N)/O(A_N,q_N) has orbit sizes [1, 527].
```

Thus the full finite discriminant orthogonal group has exactly two orbits on
`Iso(A_N,q_N)`: the zero class and one orbit containing every nonzero isotropic class.

This is a finite discriminant-form count for the Dolgachev-Kondo target.  It is not, by
itself, a primitive-isotropic lattice-orbit statement.  Lifting it to a statement about
primitive isotropic vectors in the project lattice `T_Co` still requires the
construction or accepted isometry witness identifying `T_Co=(f^*Pic(S))^\perp` with
`N`, the chosen subgroup of `O(T_Co)`, and the relevant Nikulin, Eichler, or backend
orbit theorem.

Source basis:

- `theory/references/literature/dolgachev_kondo_2013.md:97-101` identifies the Coble
  K3 orthogonal complement as `N=<2>+E(2)`.
- `.agents/plans/features/FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION/decisions/DECISION-TCO-DEFINITION-AND-SIGNATURE.md:40-43`
  records the project convention `E_10=U+E_8(-1)`.
- `theory/computations/coble_standard_target_discriminant_orbits.sage` computes the
  exact full-group orbit decomposition by stabilizing the four `Q`-fibers in
  `GL(B/2B)` and using GAP orbit computation on the finite `Q=0` fiber.

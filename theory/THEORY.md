# Theory: Reflective Two-Elementary Lattices

All definitions and results are sourced from:

- **V. Alexeev**, "Reflective Hyperbolic 2-Elementary Lattices, K3 Surfaces and Hyperkahler Manifolds" [@alexeev2024reflective]
- **V. Alexeev, P. Engel, D. Zack Garza, and L. Schaffler**, "Compact Moduli of Enriques Surfaces with a Numerical Polarization of Degree 2" [@aegs2023compact]

Section references are given for each entry.

* * *

## Conventions

### Orthogonal complement and radical

For a lattice $(L, b)$ and sublattice $S \subset L$, the **orthogonal complement** is $S^\perp = \{x \in L \mid b(x, S) = 0\}$. The **radical** is $\mathrm{rad}(b) = L^\perp$.

**Key properties (Lemma 1.3.1):** For nondegenerate $L$ with primitive nondegenerate sublattice $S$ and $T = S^\perp$:
- $\mathrm{rank}(S) + \mathrm{rank}(T) = \mathrm{rank}(L)$
- $S \oplus T$ has finite index $e = [L : S \oplus T]$ in $L$
- $\mathrm{disc}(S) = e \cdot c_S$, $\mathrm{disc}(T) = e \cdot c_T$, $\mathrm{disc}(L) = c_S c_T$
- $L$ is unimodular iff $|\mathrm{disc}(S)| = |\mathrm{disc}(T)| = e$

**Unimodular splitting (Corollary 1.3.4):** If $S \subset L$ is a unimodular sublattice of a nondegenerate lattice, then $L = S \oplus S^\perp$. If $L$ is also unimodular, then $S^\perp$ is unimodular.

**Decomposability:** $L$ is **decomposable** if $L = S \oplus S^\perp$ for some nonzero $S$; otherwise **indecomposable**.

> **Source**: [@peters_sterk2024, §1.3, Lemma 1.3.1, Corollary 1.3.4].

### Overlattice

An **overlattice** of a nondegenerate lattice $(N, b)$ is an integral lattice $L$ containing $N$ as a finite-index sublattice. One has $N \subset L \subset L^* \subset N^*$, giving $L/N \subset \mathrm{dg}_N$. The subgroup $L/N$ is isotropic with respect to the discriminant form of $N$.

Conversely, every isotropic subgroup $H \subset \mathrm{dg}_N$ determines an overlattice $L = \{x \in N^* \mid x \bmod N \in H\}$.

> **Source**: [@peters_sterk2024, §1.7].

### Two-elementary lattice type I/II

A 2-elementary even lattice is **type I** if its discriminant quadratic form is $\frac{1}{2}\mathbb{Z}/\mathbb{Z}$-valued (equivalently, the polar form is nondegenerate mod 2 and $\dim W_L$ is even). It is **type II** if the discriminant quadratic form takes at least one value in $\frac{1}{4}\mathbb{Z}/\mathbb{Z} \setminus \frac{1}{2}\mathbb{Z}/\mathbb{Z}$.

Examples: $U(2)$ is type I; $\langle 2 \rangle$ is type II (discriminant form takes value $\frac{1}{4}$).

> **Source**: [@peters_sterk2024, §1.7, Definition 1.7.2].

### Stable equivalence

Two nondegenerate symmetric lattices $L_1$ and $L_2$ are **stably equivalent** if there exist unimodular lattices $U_1, U_2$ such that $L_1 \oplus U_1 \simeq L_2 \oplus U_2$. If $L_1, L_2$ are even and $U_1, U_2$ can be taken even, they are **evenly stably equivalent**.

> **Source**: [@peters_sterk2024, §12.2, Definition 12.2.1].

### Index mod 8 (of a discriminant form)

The **index mod 8** of a nondegenerate quadratic torsion group $(G, q)$, denoted $\tau_8(q)$, is $\tau(L) \bmod 8$ for any nondegenerate quadratic lattice $L$ with discriminant form $q$. This is well-defined by Milgram's formula.

> **Source**: [@peters_sterk2024, §12.2, Definition 12.2.3].

### Spinor genus

Two sublattices $L', L''$ of $(V, q)$ are **spinor-equivalent** (belong to the same **spinor genus**) if there exist $\gamma' \in \mathrm{SO}(V, q)$ and $g_p \in \mathrm{SO}^+(V_p, q_p)$ for all primes $p$ such that $L'' = \gamma' g_p L'$ locally at each $p$.

The spinor genus is a refinement of the genus: lattices in the same spinor genus are locally equivalent at all places including the spinor norm condition.

> **Source**: [@peters_sterk2024, §14.2, Definition 14.2.1].

### Sign conventions

- **Root lattices** ($A_n$, $D_n$, $E_n$, etc.)
  are **negative definite** unless otherwise stated.
  Their Gram matrices have negative eigenvalues.
- **Hyperbolic lattices** have signature $(1, r - 1)$ (one positive, $r-1$ negative
  eigenvalues), where $r$ is the rank.
- **Elliptic lattices** are negative definite.
- The **hyperbolic plane** $U = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has
  signature $(1, 1)$.

### Dual lattice

For a nondegenerate integral lattice $(L, b)$, the **dual lattice** is
$$L^* = \{x \in L \otimes \mathbb{Q} \mid b(x, y) \in \mathbb{Z} \text{ for all } y \in L\} = \mathrm{Hom}_\mathbb{Z}(L, \mathbb{Z}).$$
It is a free $\mathbb{Z}$-module of the same rank as $L$. The **correlation morphism** $b_L: L \to L^*$, $x \mapsto b(x, -)$, is injective iff $L$ is nondegenerate, and an isomorphism iff $L$ is unimodular. If $A$ is the Gram matrix of $b$ in basis $\mathcal{E}$, then $A^{-1}$ is the Gram matrix of $b_\mathbb{Q}$ in the dual basis $\mathcal{E}^*$.

> **Source**: [@peters_sterk2024, §1.6, Lemma 1.6.1, 1.6.3].

### Discriminant group and form

For a nondegenerate integral lattice $(L, b)$, the **discriminant group** is the finite abelian group
$$\mathrm{dg}_L := L^*/L, \quad |\mathrm{dg}_L| = |{\rm disc}(L)|.$$

The **discriminant bilinear form** is the $\mathbb{Q}/\mathbb{Z}$-valued form:
$$b_L^\#: \mathrm{dg}_L \times \mathrm{dg}_L \to \mathbb{Q}/\mathbb{Z}, \quad (\bar{x}, \bar{y}) \mapsto b_\mathbb{Q}(x,y) \bmod \mathbb{Z}.$$

For an even lattice $(L, b)$ with associated quadratic form $q(x) = \frac{1}{2}b(x,x)$, the **discriminant quadratic form** is:
$$q_L^\#: \mathrm{dg}_L \to \mathbb{Q}/\mathbb{Z}, \quad \bar{x} \mapsto q_\mathbb{Q}(x) \bmod \mathbb{Z}.$$

**Convention note:** Some sources (e.g. Nikulin) use $q_L^\#(x) = b_\mathbb{Q}(x,x) \bmod 2\mathbb{Z}$, giving a $\mathbb{Q}/2\mathbb{Z}$-valued form. The two are equivalent via the isomorphism $\mathbb{Q}/\mathbb{Z} \xrightarrow{\times 2} \mathbb{Q}/2\mathbb{Z}$.

For two-elementary lattices, $\mathrm{dg}_L \simeq \mathbb{Z}_2^a$ for some $a \geq 0$.

> **Source**: [@peters_sterk2024, §1.6, Definitions 1.6.4, 1.6.5, Remark 1.6.6].

### Orthogonal groups

- $O(L)$: the full isometry group of a lattice $L$.
- $O^+(L)$: the subgroup preserving the light cone (index 2 in $O(L)$ for hyperbolic $L$).
- $O^*(L)$: the stable orthogonal group, acting trivially on the discriminant group $A_L$. Also written $\widetilde{\mathrm{O}}(L)$ (Dawes' notation). Defined as the kernel of the natural map $\mathrm{O}(L) \to \mathrm{O}(D(L))$. Has the property that $\widetilde{\mathrm{O}}(S) \subset \widetilde{\mathrm{O}}(L)$ for any sublattice $S \subset L$, where elements of $\widetilde{\mathrm{O}}(S)$ act as the identity on $S^\perp$.

**Key inclusion for orbit computations:** In Sterk's setup, $O^*(L_-) \subset \Gamma$ (the arithmetic group of the moduli space). This means $O^*$-equivalence of vectors implies $\Gamma$-equivalence, making the Eichler criterion directly applicable. However, $O(L_-)$-orbits can strictly contain multiple $\Gamma$-orbits: e.g., the $O(L_-)$-orbit of $e'-f'$ splits into four $\Gamma$-orbits (Sterk, Proposition 3.7).
- $W(L)$: the reflection subgroup (generated by reflections in roots).
- $W_2(L)$: generated by reflections in $(-2)$-roots only.
- $W_r(L)$: generated by reflections in all roots ($(-2)$- and $(-4)$-roots).

### Genus

The **genus** $\mathfrak{g}(L)$ of a nondegenerate integral quadratic lattice $(L, q)$ is the set of isometry classes of lattices $L'$ such that $L'_v \simeq L_v$ for all places $v$ (i.e., isomorphic over $\mathbb{R}$ and over $\mathbb{Z}_p$ for all primes $p$). Lattices in the same genus are called **genus-equivalent**.

The **genus invariant** is the triple $\mathsf{g}(L) := (r_+, r_-, [q_L^\#])$, where $(r_+, r_-)$ is the signature and $[q_L^\#]$ is the isometry class of the discriminant quadratic form. For indefinite even lattices with $\mathrm{rank}(L) > \ell(\mathrm{dg}_L)$ (where $\ell$ is the minimal number of generators), the genus contains a unique isometry class.

> **Source**: [@peters_sterk2024, §1.9, Definition 1.9.1; §11.3].

### Notation

- $S$: Typically denotes an even two-elementary hyperbolic lattice (e.g., the Picard
  lattice $S_X$ of a K3 surface $X$).
- $(r, a, \delta)$: Nikulin invariants for two-elementary lattices: $r$ is the rank,
  $a$ is the $\mathbb{Z}_2$-rank of the discriminant group, and $\delta \in \{0, 1\}$ is the coparity.
- $L(n)$: the lattice $L$ with bilinear form scaled by $n$.
- $L_1 \oplus L_2$: orthogonal direct sum.
- $\langle n \rangle$: rank-1 lattice with generator squaring to $n$.
- $I_{p,q}$: diagonal lattice with $p$ entries of $+1$ and $q$ entries of $-1$.
- $\Gamma_r, \Gamma_2$: Coxeter diagrams for the reflection groups $W_r(S)$ and $W_2(S)$
  respectively.
- $\Gamma_4$: The subdiagram of $\Gamma_r$ consisting of vertices corresponding to
  $(-4)$-roots (represented as black vertices).
- $W(\Gamma)$: The Coxeter group generated by reflections in the roots encoded by the
  diagram $\Gamma$.

* * *

## Definitions

### ABCDE surfaces

**ADE surfaces** are the irreducible components of KSBA stable degenerations of K3 surfaces with a nonsymplectic involution.
Type III surfaces correspond to ADE Dynkin diagrams $A_n$, $D_n$, $E_n$; Type II surfaces correspond to affine diagrams $\widetilde{A}_n$, $\widetilde{D}_n$, $\widetilde{E}_n$.
Each ADE surface $(X, D + \epsilon R)$ comes with a double cover $\pi \colon X \to Y$ to a del Pezzo ADE surface $(Y, C + \frac{1+\epsilon}{2}B)$ of index 2.

**BCDE surfaces** arise as quotients of ADE surfaces by involutions, corresponding to folding of ADE Dynkin diagrams:
- **B-type surfaces**: Quotients of ADE surfaces by involutions $\iota_{\mathrm{En}}$ of type $(x,y,z) \to (x^{-1}, -y, -z)$.
- **C-type surfaces**: Quotients corresponding to symplectic involutions $\iota_{\mathrm{Nik}}$.

The notation $\alpha:2 = {}_2\beta \subset \gamma$ indicates: $\alpha$ is the ADE type of $X \to Y$, $\gamma$ is the ADE type of $Z' \to W$ (symplectic quotient), and ${}_2\beta$ is the ABCDE type of the index-2 cover $Z \to W$ (nonsymplectic quotient).

> **Source**: [@aegs2023compact, §6, Proposition 6.1, Lemma 6.2]

### ADE root lattices

The **ADE root lattices** are the indecomposable negative definite even lattices spanned by $(-2)$-roots. All are even. Standard Gram matrices (negative definite convention):

**$A_n(-1)$** (rank $n$, $n \geq 1$): tridiagonal matrix with $-2$ on diagonal, $1$ on off-diagonals.
$$\mathrm{disc}(A_n(-1)) = (-1)^n(n+1), \quad \mathrm{dg}_{A_n(-1)} \simeq \mathbb{Z}/(n+1)\mathbb{Z}, \quad q^\#_{A_n(-1)} = \left\langle\tfrac{-n}{n+1}\right\rangle$$

**$D_n(-1)$** (rank $n$, $n \geq 3$): $D_n(-1) = \widetilde{T}_{2,2,n-2}$; concretely, vectors in $\mathbb{Z}^n(-1)$ with even coordinate sum.
$$\mathrm{disc}(D_n(-1)) = (-1)^n \cdot 4$$
Discriminant group $\simeq \mathbb{Z}/4\mathbb{Z}$ ($n$ odd) or $\mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$ ($n$ even).

**$E_6(-1), E_7(-1), E_8(-1)$**: $E_n(-1) = \widetilde{T}_{2,3,n-3}$ for $n = 6,7,8$.
$$\mathrm{disc}(E_n(-1)) = (-1)^{n+1}(n-9)$$
So $E_8(-1)$ is unimodular ($\mathrm{disc} = 1$), $E_7(-1)$ has $|\mathrm{disc}| = 2$, $E_6(-1)$ has $|\mathrm{disc}| = 3$.

**Affine (extended) Dynkin diagrams** $\widetilde{A}_n, \widetilde{D}_n, \widetilde{E}_6, \widetilde{E}_7, \widetilde{E}_8$: negative semidefinite with 1-dimensional null-space. Obtained by adding one vertex (white) to the Dynkin diagram.

**Key isometries:**
- $E_{10}(-1) = \widetilde{T}_{2,3,7} \simeq E_8(-1) \oplus U$ (Enriques lattice)
- $E_8(-1) \oplus E_8(-1) \simeq \bigoplus^8 U$ (from classification of indefinite unimodular lattices)
- $E_n(-1) = (-3,1,\ldots,1)^\perp \subset \mathbb{Z}^{1,n}$ (Lorentz lattice description)

**Weyl group:** All $(-2)$-roots in each indecomposable ADE lattice are conjugate under the Weyl group.

> **Source**: [@peters_sterk2024, §4.1, Proposition 4.1.4, Table 4.1.1].

### Ample cone

The **ample cone** $A(X)$ of a projective K3 surface $X$ is the set of all ample classes
in $S_X \otimes \mathbb{R}$, where $S_X$ is the Picard lattice of $X$.
It is one of the connected components of the set $\{x \in S_X \otimes \mathbb{R} : x^2 > 0, x \cdot d > 0 \text{ for all } d \in \text{Roots}(S_X)\}$.

> **Source**: [@alexeev2024reflective, §9.4]

### Arithmetic group $\Gamma_{\mathrm{En},2}$

Let $L = U^3 \oplus E_8^2$ be the K3 lattice with involutions $I_{\mathrm{dP}}$, $I_{\mathrm{En}}$, $I_{\mathrm{Nik}}$ as defined in [@aegs2023compact, Definition 2.3].
Let $T_{\mathrm{En}}$ and $T_{\mathrm{dP}}$ be the $(-1)$-eigenspaces of $I_{\mathrm{En}}$ and $I_{\mathrm{dP}}$ respectively.
The **arithmetic group** $\Gamma_{\mathrm{En},2}$ is the image in $O(T_{\mathrm{En}})$ of
$$\{g \in O(L) \mid g \circ I_{\mathrm{En}} = I_{\mathrm{En}} \circ g \text{ and } g(h) = h\},$$
where $h = e + f \in U(2)$ is a fixed polarization vector.
Additionally, $\Gamma_{\mathrm{En}} = O(T_{\mathrm{En}})$ and $\Gamma_{\mathrm{dP}} = O(T_{\mathrm{dP}})$.

> **Source**: [@aegs2023compact, Definition 2.6]

### Baily-Borel compactification

Let $L$ be a lattice of signature $(2,n)$, $\Gamma \subset \mathrm{O}^+(L\otimes\mathbb{R})$ an arithmetic subgroup, and $\mathcal{F}_L(\Gamma) = \mathcal{D}_L/\Gamma$ the associated orthogonal modular variety. The **Baily-Borel compactification** $\mathcal{F}_L(\Gamma)^*$ is the irreducible normal complex projective variety defined by $\mathrm{Proj}\, M_*(\Gamma, \mathds{1})$, where $M_*(\Gamma, \mathds{1})$ is the graded ring of modular forms with trivial character for $\Gamma$. It contains $\mathcal{F}_L(\Gamma)$ as a Zariski-open dense subset.

**Boundary decomposition (Theorem 1.1 of Dawes 2021):**
$$\mathcal{F}_L(\Gamma)^* = \mathcal{F}_L(\Gamma) \sqcup \bigsqcup_{E \in \mathcal{E}} \mathcal{C}_E \sqcup \bigsqcup_{l \in \ell} P_l$$
where $\ell$ (resp. $\mathcal{E}$) indexes the finitely many $\Gamma$-orbits of primitive totally isotropic sublattices of rank 1 (resp. rank 2) in $L$. Each $\mathcal{C}_E \cong \mathbb{H}^+/G(E)$ is a modular curve (1-cusp) and each $P_l$ is a point (0-cusp). The point $P_l$ lies in the closure of $\mathcal{C}_E$ if and only if $l \subset E$ (for suitable representatives).

> **Source**: [@dawes2021baily, §1.6, Theorem 1.1]; original construction in [@bailyborel1966].

### Branch divisor

The **branch divisor** $B$ of a double cover $\pi: X \to Y$ is the locus in $Y$ over
which the map is not local-isomorphic.
For Coble surfaces (K3 surfaces with a nonsymplectic involution), $B$ is the rational plane sextic on the quotient surface $Y = X/\iota$.

> **Source**: [@alexeev2024reflective, §9.4]

### Built on top of (a graph)

Let $L$ be an even two-elementary lattice. A Coxeter diagram $\Gamma$ is **built on top of** a simple graph $H$ if it contains a
subdiagram of the main roots isomorphic to $H$, and the additional roots are defined in
terms of the main roots by specified rules.
For the two-elementary lattices treated by Alexeev, the main roots are the
$(-2)$-roots $\alpha$ of divisibility 1 (i.e., satisfying $\alpha \cdot L = \mathbb{Z}$), and if a main root $\alpha$ and an additional root $\beta$ are connected, then $\alpha \cdot \beta = 2$.

> **Source**: [@alexeev2024reflective, Definition 9.1.3]

### Characteristic element

Let $L$ be an integral lattice with odd discriminant. A vector $u \in L$ is a **characteristic element** if $u \cdot x \equiv x \cdot x \pmod{2}$ for every $x \in L$. Every such lattice has a characteristic element, and the **$\sigma$-invariant** $\sigma(L) := u \cdot u \bmod 8$ is independent of the choice of $u$. For even lattices, $u = 0$ is characteristic and $\sigma(L) = 0$.

> **Source**: [@peters_sterk2024, §2.1, Definition 2.1.4, Lemma 2.1.6].

### Class number

The **class number** of a genus is the number of isometry classes in that genus.

**Criterion for class number 1 (Corollary 14.4.3):** Let $L$ be an even nondegenerate indefinite lattice of rank $r \geq 3$. If $\ell(\mathrm{dg}_L) \leq r - 2$ (where $\ell$ is the minimal number of generators of the discriminant group), then $L$ has class number 1 — i.e., the isometry class of $L$ is determined by its rank, index, and discriminant quadratic form $q_L^\#$.

**Spinor equivalence = proper equivalence (Theorem 14.4.1):** For an indefinite quadratic inner product space $(V, q)$ over $\mathbb{Q}$ of dimension $\geq 3$, spinor equivalence for integer-valued lattices coincides with proper equivalence (isometry by an element of $\mathrm{SO}(V,q)$).

> **Source**: [@peters_sterk2024, §14.4, Theorem 14.4.1, Corollary 14.4.3].

### Classification of indefinite unimodular lattices

**Odd case (Theorem 2.3.1):** Every odd indefinite unimodular lattice is diagonalizable, i.e., isometric to $\bigoplus^p \langle 1 \rangle \oplus \bigoplus^q \langle -1 \rangle$. Such lattices are classified by rank and index.

**Even case (Corollary 2.4.3):** Every even indefinite unimodular lattice of rank $r$ and index $\tau = 8a\varepsilon$ ($\varepsilon = \pm 1$) is isometric to:
$$\underbrace{E_8 \oplus \cdots \oplus E_8}_{a} (\varepsilon) \oplus \underbrace{U \oplus \cdots \oplus U}_{b}, \quad b = \tfrac{1}{2}(r - |\tau|).$$
In particular, even indefinite unimodular lattices are classified by rank and index, and the index must be divisible by 8.

**Consequence:** $E_8 \oplus E_8(-1) \simeq \bigoplus^8 U$.

> **Source**: [@peters_sterk2024, §2.3, §2.4, Theorems 2.3.1, 2.4.1, 2.4.2, Corollary 2.4.3].

### Coeven lattice

A two-elementary lattice $S$ is **coeven** ($\delta = 0$) if the doubled dual $S^\dagger := S^*(2)$ is even, where $S^*(2)$ denotes the dual lattice with the bilinear form multiplied by 2.

> **Source**: [@alexeev2024reflective, §9.2]

### Coodd lattice

A two-elementary lattice $S$ is **coodd** ($\delta = 1$) if the doubled dual $S^\dagger := S^*(2)$ is odd.

> **Source**: [@alexeev2024reflective, §9.2]

### Coparity

The **coparity** is the invariant $\delta \in \{0, 1\}$ in the Nikulin classification $(r, a, \delta)$ of a two-elementary lattice.
It distinguishes coeven ($\delta = 0$) from coodd ($\delta = 1$) lattices.
A direct sum of two-elementary lattices is coeven if and only if every summand is coeven.

> **Source**: [@alexeev2024reflective, §9.2; @nikulin1979integral]

### Coxeter diagram

For an even hyperbolic lattice $S$, the **Coxeter diagram** $\Gamma_r$ encodes the
angles between the roots orthogonal to the facets of the fundamental polyhedron $P_r$ of
the full reflection group $W_r(S)$. The diagram $\Gamma_2$ is defined analogously for
the $(-2)$-reflection group $W_2(S)$.

Vertices denote roots. Edge types specify the angle $\theta$ between roots $\alpha_i, \alpha_j$:

| Edge type | Angle $\theta$ | Intersection $\alpha_i \cdot \alpha_j$ (for $(-2)$-roots) |
|-----------|----------------|----------------------------------------------------------|
| Single line | $\pi/3$ | 1 |
| Double line | $\pi/4$ | (for mixed $(-2)$,$(-4)$ pairs) 2 |
| No line | $\pi/2$ | 0 |
| Bold line | hyperplanes meet at infinity | 2 |
| Broken line | hyperplanes are skew | $>2$ |

For two-elementary lattices, short $(-2)$-roots are white vertices and long $(-4)$-roots
are black vertices.

> **Source**: [@alexeev2024reflective, §9.2; @vinberg1972units]

### Cusp (0-cusp, 1-cusp)

In the Baily-Borel compactification of a type IV arithmetic quotient $\mathcal{F}_L(\Gamma) = \mathcal{D}_L/\Gamma$ for $L$ of signature $(2,n)$:

- A **0-cusp** (Type III boundary point) corresponds to a $\Gamma$-orbit of a primitive isotropic rank-1 sublattice $I = \mathbb{Z}\delta \subset L$ (i.e., $\delta^2 = 0$, $\delta$ primitive). It is a point $P_I$ in $\overline{\mathcal{F}_L(\Gamma)}^\mathrm{BB}$.
- A **1-cusp** (Type II boundary curve) corresponds to a $\Gamma$-orbit of a primitive isotropic rank-2 sublattice $J \subset L$. It is a modular curve $\mathcal{C}_J \cong \mathbb{H}^+/G(J)$.

**Incidence:** $P_I$ lies in the closure of $\mathcal{C}_J$ if and only if $I \subset J$.

**Full correspondence table:**

| Boundary object | Isotropic sublattice | Degeneration type | Coxeter fan object |
|---|---|---|---|
| 0-cusp (point) | rank-1 primitive isotropic $I \subset L$ | Type III | — |
| 1-cusp (modular curve) | rank-2 primitive isotropic $J \subset L$ | Type II | maximal parabolic subdiagram of $G_\mathrm{cox}$ |
| Interior stratum of dim $d$ | — | — | elliptic subdiagram of rank $n-1-d$ |

**Quotient lattice at a 0-cusp:** For $I = \mathbb{Z}\delta$, the lattice $\Lambda_I := I^\perp/I$ has signature $(1, n-2)$. The stabilizer $\Gamma_I := \mathrm{Stab}_\Gamma(I)/U_I$ (where $U_I$ is the unipotent subgroup) acts on $\Lambda_I$, and the fan for the toroidal compactification at this cusp lives in the positive cone of $\Lambda_I \otimes \mathbb{R}$.

**Quotient lattice at a 1-cusp:** For $J$, the stabilizer $\mathrm{Stab}_\Gamma(J)$ acts on $J \cong \mathbb{Z}^2$ via a finite-index subgroup $\Gamma_J \subset \mathrm{SL}_2(\mathbb{Z})$, and $\mathcal{C}_J \cong \Gamma_J \backslash \mathbb{H}^+$ maps finitely to the $j$-line $\mathbb{A}^1_j$.

**Correspondence with vectors in the positive cone:**

For a hyperbolic lattice $N$ of signature $(1, r-1)$ with positive cone $\mathcal{C} \subset N \otimes \mathbb{R}$, the **rational closure** is:
$$\overline{\mathcal{C}} := \mathcal{C} \cup \{\text{rational null rays } \mathbb{R}_{\geq 0} v : v \in N_\mathbb{Q},\, v^2 = 0\}.$$

Points in $\mathcal{C}$ correspond to **interior points** of the associated hyperbolic space $\mathbb{H}^{r-1} = \mathbb{P}(\mathcal{C})$ (non-ideal). Rational null rays $\mathbb{R}_{\geq 0} v \subset \partial \overline{\mathcal{C}}$ with $v^2 = 0$ correspond to **ideal points** (cusps) of $\mathbb{H}^{r-1}$. The projectivization $\mathbb{P}(\mathfrak{K})$ of the fundamental chamber $\mathfrak{K}$ is a hyperbolic polytope with cusps at the null rays $v \in \mathfrak{K}$ with $v^2 = 0$ — these are the infinite vertices of the polytope, corresponding to 1-cusps of the modular variety.

Thus:
- **Non-isotropic $v \in \mathcal{C}$** ($v^2 > 0$): interior point of $\mathbb{H}^{r-1}$, corresponds to a point of the modular variety $\mathcal{F}_L(\Gamma)$
- **Primitive isotropic $v \in \partial\overline{\mathcal{C}}$** ($v^2 = 0$): ideal point (cusp) of $\mathbb{H}^{r-1}$, corresponds to a 1-cusp boundary component after passing to the modular variety

> **Source**: [@alexeev_engel_thompson2019, §3, p.15–16; §4A, p.21]: "The projectivization $P = \mathbb{P}(\mathfrak{K})$ is a hyperbolic polytope with cusps: it has infinite vertices corresponding to null rays $v \in \mathfrak{K}$ with $v^2 = 0$."; [@dawes2021baily, Theorem 1.1]; [@aegs2023compact, Definition 2.9].

### Cyclic torsion forms

Non-degenerate torsion forms on the cyclic group $C_m = \mathbb{Z}/m\mathbb{Z}$ (Proposition 6.1.8):

- **Symmetric forms:** classified by $\mathsf{D}(\mathbb{Z}/m\mathbb{Z})$. Every non-degenerate form is $\langle a \cdot m^{-1} \rangle$ with $(a,m)=1$, i.e., $(x,y) \mapsto am^{-1}xy \in \mathbb{Q}/\mathbb{Z}$.
- **Quadratic forms:** classified by $\mathsf{D}(\mathbb{Z}/2m\mathbb{Z})$. Every non-degenerate form is $[\frac{1}{2}am^{-1}]$, i.e., $x \mapsto a(2m)^{-1}x^2$ with $am$ even and $(a,m)=1$.

Two quadratic forms $[\frac{1}{2}am^{-1}]$ and $[\frac{1}{2}a'm^{-1}]$ are isometric iff $a' \equiv au^2 \pmod{2m}$ for some $u$ with $(u,2m)=1$.

**Key distinction:** Two quadratic forms on $C_m$ can have the same polar form but be non-isometric (this happens for $m$ even, e.g., $[\frac{1}{2} \cdot 2^{-1}]$ and $[\frac{1}{2} \cdot 3 \cdot 2^{-1}]$ on $C_2$).

> **Source**: [@peters_sterk2024, §6.1.D, Proposition 6.1.8, Table 6.1.1].

### Divisibility

Let $L$ be a lattice. The **divisibility** $\mathrm{div}(\alpha)$ of a vector $\alpha \in L$ is the positive integer $d$ such that $\alpha \cdot L = d\mathbb{Z}$, i.e., the greatest common divisor of all values $\alpha \cdot y$ for $y \in L$.

> **Source**: [@alexeev2024reflective, §9.2]

### Dlt model

Let $(\mathcal{X}, \mathcal{R}) \to (C,0)$ be a divisor model of Enriques K3 surfaces for which the Enriques involution $\iota_{\mathrm{En}}$ is a regular involution preserving $\mathcal{R}$.
The **dlt model** (divisorially log terminal model) is the quotient $\mathcal{Z} := \mathcal{X}/\iota_{\mathrm{En}}$.
Similarly, the **half-divisor model** is $(\mathcal{Z}, \mathcal{R}_{\mathcal{Z}}) := (\mathcal{X}, \mathcal{R})/\iota_{\mathrm{En}}$.
The central fiber $\mathcal{Z}_0$ has slc singularities and $K_{\mathcal{Z}} + \epsilon\mathcal{R}_{\mathcal{Z}}$ is relatively big and nef over $C$.

> **Source**: [@aegs2023compact, Definition 4.7]

### Edge $n$-fold graph

Let $G$ be a graph and $n \geq 2$ an integer. The **edge $n$-fold graph** $G^{(n)}$ is obtained by
subdividing each edge of $G$ into $n$ edges and inserting $n-1$ intermediate vertices.
Thus $G^{(n)}$ has $n|E_G|$ edges and $|V_G| + (n-1)|E_G|$ vertices, where $|E_G|$ and $|V_G|$ denote the number of edges and vertices of $G$.
The vertices of $G^{(2)}$ are in natural bijection with the set of vertices and edges of $G$.

> **Source**: [@alexeev2024reflective, Definition 9.1.2]

### Eichler criterion

Let $L$ be a lattice containing a copy of $2U$, and let $v_1, v_2 \in L$ be primitive vectors. The **Eichler criterion** states that there exists $g \in \widetilde{\mathrm{SO}}^+(L)$ with $gv_1 = v_2$ if and only if:
1. $v_1^2 = v_2^2$, and
2. $v_1^* \equiv v_2^* \bmod L$ in $D(L)$, where $v_i^* := v_i/\mathrm{div}(v_i) \in L^\vee$.

**Application:** Reduces the problem of determining $\Gamma$-orbits of primitive vectors to a finite computation in the discriminant group $D(L)$.

**Sterk's version (Corollary 3.3):** Let $N = \Lambda \oplus P$ where $\Lambda = \mathbf{H} \oplus \mathbf{H}(2)$ and $P$ is even nondegenerate. If $v, w \in N$ are primitive with:
1. $(v,v) = (w,w)$
2. $(v,N) = (w,N) =: p\mathbb{Z}$
3. $v \equiv w \pmod{pN}$

then $v \sim_{O^*(N)} w$.

**Proof sketch:** Two steps using Siegel-Eichler transformations $E_{e,y}(x) = x + (x,y)e - \frac{1}{2}(y,y)(x,e)e - (x,e)y$:
- Step 1: Find $j \in O^*(N)$ with $(j(v), f) = p$ (using Corollary 3.2 to move $v$ into $\mathbf{H}(2) \oplus P$ or $\mathbf{H} \oplus P$, then apply $E_{e,y}$)
- Step 2: With $(v,f) = (w,f) = p$, write $v - w = pu$ and apply $E_{f,u}$ to conclude $v = w$

**Crucial subtlety:** $O^*(L_-) \subset \Gamma$ (the arithmetic group), so $O^*$-equivalence implies $\Gamma$-equivalence. But $O(L_-)$-orbits can split into multiple $\Gamma$-orbits (e.g., the $O(L_-)$-orbit of $e'-f'$ splits into four $\Gamma$-orbits, Proposition 3.7).

> **Source**: [@dawes2021baily, §1.4]; [@sterk1991, Corollary 3.3]; original in [@eichler1952quadratische].

### Eichler transvection

Let $L$ be a lattice, $e \in L$ an isotropic vector, and $a \in e^\perp \subset L$. The **Eichler transvection** (Siegel-Eichler transformation) $E_{e,a} \in O(L)$ is defined by:
$$E_{e,a}(x) = x + (x,a)e - \tfrac{1}{2}(a,a)(x,e)e - (x,e)a.$$

**Properties:**
- $E_{e,a} \in O^*(L)$ (acts trivially on $\mathrm{dg}_L$)
- $E_{e,a} \in O^+(L)$ (spinor norm 1)
- Inverse: $E_{e,-a}$
- The map $a + \mathbb{Z}e \mapsto E_{e,a}$ is an injective group homomorphism $L_e = e^\perp/\mathbb{Z}e \to O(L)$
- $E_e(L_e)$ is a normal abelian subgroup of the stabilizer $O_e(L)$

Eichler transvections generate $O^*(L)$ and are the key tool in proving the Eichler criterion.

**Orbit theorem for $\Lambda = \mathbf{H} \oplus \mathbf{H}(2)$ (Proposition 3.1, Sterk):** For primitive $v \in \Lambda$:
$$v \sim_{O(\Lambda)} \begin{cases} e + kf & \text{if } (v,v) = 2k \text{ and } v \notin 2\Lambda^* \\ e' + kf' & \text{if } (v,v) = 4k \text{ and } v \in 2\Lambda^* \end{cases}$$

**$O^*$ vs $O$ splitting (Corollary 3.2):** The same holds with $O^*(\Lambda)$ replacing $O(\Lambda)$, except the $v \in 2\Lambda^*$ case splits: $v \sim_{O^*(\Lambda)} e' + kf'$ or $ke' + f'$. The involution $e' \leftrightarrow f'$ generates $O(\Lambda)/O^*(\Lambda)$.

> **Source**: [@peters_sterk2024, §17.3, Definition 17.3.1, Lemma 17.3.3]; [@sterk1991, Proposition 3.1, Corollary 3.2]; [@dawes2021baily, §2].

### Eichler-Siegel transformation

Let $(V, b)$ be a rational inner product space with quadratic form $q$. Given a primitive isotropic vector $f \in L$ and $y \in L$ with $b(f,y) = 0$ and $b(y,y)$ even, the **Eichler-Siegel transformation** is:
$$\psi_{f,y}: x \mapsto x + b(x,y)f - b(x,f)y - b(x,f)q(y)f.$$

This is a lattice isometry with:
1. $\psi_{f,y} \in \mathrm{O}^+(L)$ (spinor norm 1)
2. $\psi_{f,y}$ acts as the identity on $\mathrm{dg}_L$
3. The map $y + \mathbb{Z}f \mapsto \psi_{f,y}$ is an injective group homomorphism $L_f = f^\perp/\mathbb{Z}f \to \mathrm{O}(L)$
4. $\psi_f(L_f)$ is a normal abelian subgroup of the stabilizer $\mathrm{O}_f(L)$

> **Source**: [@peters_sterk2024, §17.3, Definition 17.3.1, Lemma 17.3.3].

### Elementary hyperbolic summands

The three indecomposable even hyperbolic two-elementary lattices that appear as direct
summands in any even hyperbolic two-elementary lattice:

- $\langle 2 \rangle$: rank-1 lattice with generator squaring to 2; $(r,a,\delta) = (1,1,1)$.
- $U$: the hyperbolic plane with Gram matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$; $(r,a,\delta) = (2,0,0)$.
- $U(2)$: the hyperbolic plane with form scaled by 2; $(r,a,\delta) = (2,2,0)$.

> **Source**: [@alexeev2024reflective, §9.2]

### Elliptic diagram (subdiagram)

Let $G_\mathrm{cox}$ be a Coxeter diagram for a hyperbolic lattice $N$, with nodes corresponding to roots $\{r_i\}$. A subdiagram $G \subset G_\mathrm{cox}$ is **elliptic** if the restriction of the quadratic form of $N$ to $\mathbb{R}V_G$ (where $V_G$ is the span of the roots in $G$) is **negative definite**.

Equivalently, $G$ is a disjoint union of finite ADE Dynkin diagrams $G_k$ (types $A_n, D_n, E_6, E_7, E_8$). The rank of $G$ is $\sum |G_k|$.

**Correspondence with Coxeter fan:** Elliptic subdiagrams of rank $r$ correspond to Type III cones of dimension $19 - r$ in the Coxeter fan (cones meeting the interior $\mathcal{C}$). The empty diagram $G = \emptyset$ corresponds to the fundamental chamber itself.

> **Source**: [@alexeev_engel_thompson2019, §4, p.21]: "A subdiagram is called elliptic if the restriction of the quadratic form of $N$ to $\mathbb{R}V$ is negative definite."

### Elliptic fibration

An **elliptic fibration** on a K3 surface $X$ is a surjective morphism $\pi: X \to \mathbb{P}^1$ whose generic fiber is a smooth curve of genus 1 (an elliptic curve). Such fibrations are in bijection with primitive isotropic vectors $\nu \in S_X$ with $\nu^2 = 0$ in the Picard lattice.

> **Source**: [@huybrechts2016lectures, §11.1]. The correspondence with isotropic vectors is [@alexeev2024reflective, §9.1].

### Enriques lattice

The **Enriques lattice** is $\Lambda_\mathrm{Enr} := U \oplus E_8(-1)$, an even unimodular lattice of signature $(1,9)$ and rank 10. It is the intersection lattice of an Enriques surface $Y$: $H^2(Y)/\mathrm{tors} \simeq \Lambda_\mathrm{Enr}$.

The **lattice Enriques involution** on $\Lambda = U \oplus W \oplus W'$ (where $W, W'$ are copies of $\Lambda_\mathrm{Enr}$) is:
$$\iota_\mathrm{Enr}(u, v, v') = (-u, v', v)$$
with invariant lattice $\Lambda^G \simeq \Lambda_\mathrm{Enr}(2)$ (discriminant quadratic form $\bigoplus^5 u_1$).

Every Enriques surface $Y = X/\langle j \rangle$ admits a marking $\varphi: H^2(X,\mathbb{Z}) \to \Lambda$ making $j^*$ correspond to $\iota_\mathrm{Enr}$.

> **Source**: [@peters_sterk2024, §21.1]; also [@peters_sterk2024, §4.1, Lemma 4.1.5] for $\Lambda_\mathrm{Enr} \simeq E_{10}(-1)$.

### Enriques surface

An **Enriques surface** $Z$ is a quotient $Z = X/\iota_{\mathrm{En}}$ of a K3 surface $X$ by a fixed-point-free involution $\iota_{\mathrm{En}}$.
Enriques surfaces satisfy $2K_Z \sim 0$ (the canonical divisor is 2-torsion) and $q = 0$ (irregularity zero).
The K3 cover $X$ has a nonsymplectic Enriques involution acting as $-1$ on the holomorphic 2-form.
Equivalently, $X$ is an Enriques K3 surface with transcendental lattice $T_X \simeq U \oplus U(2) \oplus E_8(2) = (12,10,0)_2$ and Picard lattice $S_X \simeq U(2) \oplus E_8(2) = (10,10,0)_1$.

> **Source**: [@aegs2023compact, §1, Definition 2.3]

### Even lattice

A lattice $(L, b)$ is **even** if $b(x,x) \in 2\mathbb{Z}$ for all $x \in L$, equivalently if the associated quadratic form $q(x) = \frac{1}{2}b(x,x)$ is integral. Otherwise $L$ is **odd**.

> **Source**: [@peters_sterk2024, §1.2].

### Folded diagram

Let $\Lambda$ be an elliptic, parabolic, or hyperbolic lattice with an involution $J$, and let $G$ be its Coxeter diagram.
The **folded diagram** $G^J$ is the diagram with the vectors $\alpha_J$ for the roots $\alpha$ in $G$ for which the folded vectors $\alpha_J$ are roots of $\Lambda^{J=1}$.
For the moduli space $F_{\mathrm{En},2}$, the folded diagrams are obtained from the Coxeter diagrams of $(18,0,0)_1$ and $(18,2,0)_1$ by folding with respect to five involutions, giving the Coxeter diagrams for the reflection groups at the five 0-cusps.

> **Source**: [@aegs2023compact, Definition 3.7]

### Folded vector

Let $\Lambda$ be a lattice with an involution $I$ and let $\alpha \in \Lambda$ be a vector.
The **folded vector** $\alpha_I \in \Lambda^{I=1}$ is defined by:
$$\alpha_I = \begin{cases} \alpha & \text{if } I(\alpha) = \alpha \\ \alpha + I(\alpha) & \text{if } I(\alpha) \neq \alpha \end{cases}$$

For roots in the K3 lattice with involutions $I_{\mathrm{dP}}$, $I_{\mathrm{En}}$, $I_{\mathrm{Nik}}$, the folded vectors satisfy:
(1) If $\alpha^2 = -2$ and $\alpha \in T_{\mathrm{En}}$, then $\alpha_I$ is a root of both $T_{\mathrm{dP}}$ and $T_{\mathrm{En}}$.
(2) If $\alpha^2 = -4$ and $\alpha \in T_{\mathrm{En}}$, then $\alpha_I$ is a root of both $T_{\mathrm{dP}}$ and $T_{\mathrm{En}}$.
(3) If $\alpha^2 = -2$, $\alpha \cdot I(\alpha) = 0$, then $\alpha_I^2 = -4$ is a root of $T_{\mathrm{En}}$ but not of $T_{\mathrm{dP}}$.

> **Source**: [@aegs2023compact, Definition 3.3, Lemma 3.4]

### Fundamental polyhedron

The **fundamental polyhedron** $P_r$ of a reflection group acting on hyperbolic space is
a convex set whose images under the group tile the space.
Its facets are defined by the orthogonal hyperplanes to the roots.

> **Source**: [@alexeev2024reflective, §9.2, §9.3]

### Generalised Kummer variety

Let $A$ be an abelian surface and $A^{[n+1]}$ the Hilbert scheme of $(n+1)$ points on $A$. The natural summation map $p: A^{[n+1]} \to A$ has fiber $X := p^{-1}(0)$, called a **generalised Kummer variety**. It is a compact hyperkähler manifold of dimension $2n$. The Beauville-Bogomolov-Fujiki form on $H^2(X,\mathbb{Z})$ gives it the structure of a lattice:
$$M \cong 3U \oplus \langle -2(n+1) \rangle.$$
Deformations of $X$ are called **deformation generalised Kummer varieties**.

> **Source**: [@dawes2021baily, §1.8]; lattice structure from [@rapagnetta2008beauville].

### Hasse invariant

For a nondegenerate quadratic form $q = \sum a_j x_j^2$ over $\mathbb{Q}_p$ (or $\mathbb{Q}$), the **Hasse invariant** at a place $v$ is:
$$\varepsilon_v(q) := \prod_{i < j} (a_i, a_j)_v \in \{\pm 1\}$$
where $(a, b)_v$ is the Hilbert symbol at $v$. This is independent of the choice of diagonalization.

**Local classification over $\mathbb{Q}_p$:** Two nondegenerate forms $q, q'$ are isometric over $\mathbb{Q}_p$ iff they have the same rank, discriminant (mod squares), and Hasse invariant $\varepsilon_p$.

**Global classification (Hasse principle):** Two nondegenerate forms over $\mathbb{Q}$ are isometric iff they are isometric over $\mathbb{R}$ and over $\mathbb{Q}_p$ for all primes $p$. Explicitly: same rank, same index $\tau$, same discriminant (mod squares), and $\varepsilon_p(q) = \varepsilon_p(q')$ for all primes $p$.

> **Source**: [@peters_sterk2024, §3, Introduction, Proposition 3.1.3].

### Hyperbolic lattice

A lattice of signature $(1, r - 1)$ is called **hyperbolic**, where $r$ is the rank.
(This convention follows the algebraic geometry direction, where the positive direction corresponds to the ample cone.)

> **Source**: [@alexeev2024reflective, §9.2]

### Hyperkähler manifold

A **hyperkähler manifold** (also called irreducible holomorphic symplectic manifold) is a simply-connected compact Kähler manifold $X$ such that $H^0(X, \Omega_X^2)$ is spanned by a nowhere-degenerate holomorphic 2-form. The second cohomology $H^2(X, \mathbb{Z})$ carries the Beauville–Bogomolov–Fujiki form. Examples include Hilbert schemes of $n$ points on K3 surfaces, denoted $\mathrm{K3}^{[n]}$-type.

> **Source**: [@huybrechts2016lectures, §4.3; @beauville1983varietes]

### IAS² (Integral-affine sphere)

An **integral-affine sphere** (IAS²) is a collection of local embeddings of $S^2$ minus a finite set into the flat plane, which differ on overlaps by transformations in $\mathrm{SL}_2(\mathbb{Z}) \ltimes \mathbb{Z}^2$.
For Kulikov degenerations of K3 surfaces $\mathcal{X} \to (C,0)$, the dual complex $\Gamma(\mathcal{X}_0)$ of the central fiber carries a natural integral-affine structure with singularities.
Complete triangulations of IAS² with vertices in $\mathbb{Z}^2$ describe the dual complexes of Kulikov degenerations.
A **polarized IAS²** $(B(\ell), R_{\mathrm{IA}})$ encodes both the dual complex and the integral-affine polarization corresponding to a divisor model.

> **Source**: [@aegs2023compact, §1, §4.1, Theorem 4.4]

### Irrelevant root

Let $W$ be a reflection group with fundamental chamber $\mathfrak{K}$ and Coxeter diagram $G$. The **generalized Coxeter semifan** construction (Definition 4.16 of AET) takes as input a partition $K = I \sqcup J$ of the mirrors into **active** ($I$) and **inactive** ($J$) subsets, and produces a coarser tiling of $\overline{\mathcal{C}}$.

The inactive mirrors $J$ generate a subgroup $W_J \subset W$. The **generalized chamber** $\mathfrak{L} = \bigcup_{h \in W_J} h(\mathfrak{K})$ is a larger fundamental domain, and $W$ tiles $\overline{\mathcal{C}}$ by $\mathfrak{L}$ with stabilizer $W_J$ (Proposition 4.17(2)). This is a **different, coarser tiling** of hyperbolic space — the reflection group for this tiling is $W$ acting on chambers of size $\mathfrak{L}$, with $W_J$ as the stabilizer of each chamber.

A face of $\mathfrak{K}$ is **irrelevant** if it is an interior wall of $\mathfrak{L}$ — i.e., it is shared between two copies $h(\mathfrak{K})$ and $h'(\mathfrak{K})$ within the same generalized chamber, so it disappears in the coarser tiling. Precisely: a face $F = \mathfrak{K} \cap \bigcap_{i \in V} r_i^\perp$ is irrelevant iff $V \subset J$, because then $W_V \subset W_J$ and the $W_J$-images of $\mathfrak{K}$ cover a neighborhood of $F$, making $F$ interior to $\mathfrak{L}$.

**Wythoff construction (Remark 4.19):** The Coxeter fan $\mathfrak{F}^\mathrm{cox}$ is the normal fan of $\mathrm{Conv}(W \cdot p)$ for $p$ in the interior of $\mathfrak{K}$. The semifan $\mathfrak{F}^\mathrm{semi}$ is the normal fan of $\mathrm{Conv}(W \cdot q)$ for $q$ on the face of $\mathfrak{K}$ corresponding to $J$ — a different point, giving a different (coarser) polytope and thus a different tiling.

> **Source**: [@alexeev_engel_thompson2019, Definition 4.16, Proposition 4.17, Remark 4.19].

### Isometry (of lattices)

Two integral lattices $(L, b)$ and $(L', b')$ are **isometric** (written $L \simeq L'$) if there exists an isomorphism of free $\mathbb{Z}$-modules $f: L \to L'$ such that $b'(f(x), f(y)) = b(x,y)$ for all $x, y \in L$. In matrix terms: $F^\top B_{\mathcal{E}'} F = B_\mathcal{E}$ where $F$ is the matrix of $f$.

An **isometric embedding** $f: S \hookrightarrow L$ satisfies $F^\top B_\mathcal{E} F = B_\mathcal{F}$.

The **isometry group** (orthogonal group) of $(L,b)$ is $\mathrm{O}(b) = \mathrm{O}(L) = \{\varphi \in \mathrm{Aut}_\mathbb{Z}(L) \mid b(\varphi x, \varphi y) = b(x,y)\}$.

**Isometry invariants:** discriminant, index (signature), and parity (even/odd) are all isometry invariants.

> **Source**: [@peters_sterk2024, §1.5].

### Isospectral non-isometric tori

The flat tori $\mathbb{R}^{16}/\Gamma_{16}$ and $\mathbb{R}^{16}/(E_8 \oplus E_8)$ are isospectral (same Laplace spectrum) but not isometric as Riemannian manifolds. Their theta functions both equal the unique cusp form $E_4$ of weight 8.

> **Source**: [@peters_sterk2024, §1.12, Theorem 1.12.2].

### Isotropic subgroup

A non-zero subgroup $H$ of a torsion group $(G, b^\#)$ (or $(G, q^\#)$) is **isotropic** if the bilinear form (resp. quadratic form) is identically zero on $H$.

> **Source**: [@peters_sterk2024, §1.6, Definition 1.6.7].

### Isotropic vector

A vector $x \in L$ (or $x \in V$) is **isotropic** if $b(x,x) = 0$ (equivalently $q(x) = 0$ for the associated quadratic form). A subspace or sublattice is **totally isotropic** if every vector in it is isotropic and any two vectors are orthogonal.

The **Witt index** $\mathsf{W}_\tau(L_\mathbb{R})$ is $\min(r_+, r_-)$ where $(r_+, r_-)$ is the signature — it equals half the dimension of the maximal totally isotropic subspace in $L \otimes \mathbb{R}$.

> **Source**: [@peters_sterk2024, §1.5, §7.2].

### Isotropic vector (primitive)

Let $L$ be a lattice. A vector $\nu \in L$ is **primitive isotropic** if $\nu^2 = 0$ and $\nu$ is not a
multiple of another lattice vector (i.e., $\nu = k\nu'$ for $k \in \mathbb{Z}$ implies $k = \pm 1$).

> **Source**: [@alexeev2024reflective, §9.2]

### K3 lattice

The **K3 lattice** is the unique even unimodular lattice of signature $(3,19)$:
$$\Lambda_\mathrm{K3} := U^{\oplus 3} \oplus E_8(-1)^{\oplus 2}.$$
For any K3 surface $X$, $H^2(X,\mathbb{Z}) \simeq \Lambda_\mathrm{K3}$.

> **Source**: [@peters_sterk2024, §1.13, Example 1.13.1.2].

### K3 surface

A **K3 surface** over a field $k$ is a complete non-singular variety $X$ of dimension two such that $\omega_X \simeq \mathcal{O}_X$ and $H^1(X, \mathcal{O}_X) = 0$. Over $\mathbb{C}$, a K3 surface is simply connected and has $H^2(X, \mathbb{Z}) \cong U^3 \oplus E_8(-1)^2$ (the K3 lattice). The Picard lattice $S_X \subset H^2(X, \mathbb{Z})$ is the subgroup of algebraic classes with the intersection form.

> **Source**: [@huybrechts2016lectures, Definition 1.1]

### KSBA compactification

A **KSBA stable pair** $(X, B = \sum_{i=1}^n b_i B_i)$ consists of a projective variety $X$ which is deminormal (seminormal with only double crossings in codimension 1), effective Weil divisors $B_i$ not containing any components of the double locus, coefficients $0 < b_i \leq 1$ rational, satisfying:
(1) The pair $(X, B)$ has semi log canonical (slc) singularities.
(2) The divisor $K_X + B$ is an ample $\mathbb{Q}$-Cartier divisor.

For $K$-trivial pairs $(Z, \epsilon R_Z)$ with $R_Z$ ample Cartier and $0 < \epsilon \ll 1$, the **KSBA compactification** $\overline{F}_{\mathrm{En},2}$ is the closure in the moduli space of KSBA stable pairs. The normalization of $\overline{F}_{\mathrm{En},2}$ is a semitoroidal compactification.

> **Source**: [@aegs2023compact, Definition 2.10, §5.3]

### Kummer lattice

The **Kummer lattice** $\Lambda_\mathrm{Kum} = \Gamma_{D_5}(-1)$ is the rank-8 even negative definite lattice associated to the $D_5$ code. It is the primitive closure of the 16 nodal curves on a Kummer surface. Its discriminant quadratic form is $\bigoplus^3 u_1$ on $(\mathbb{Z}/2\mathbb{Z})^6$, and $\Lambda_\mathrm{Kum}^\perp \simeq \bigoplus^3 U(2)$ in the K3 lattice.

A K3 surface $Y$ is a Kummer surface iff $\Lambda_\mathrm{Kum}$ embeds primitively in $\mathrm{NS}(Y)$ and $\mathrm{Trs}(Y)$ embeds primitively in $\bigoplus^3 U(2)$.

> **Source**: [@peters_sterk2024, §20.6, Proposition 20.6.1, 20.6.4].

### Lagrangian fibration

A **Lagrangian fibration** on a hyperkähler manifold $X$ of dimension $2n$ is a surjective morphism $X \to B$ onto a base $B$ of dimension $n$ whose fibers are Lagrangian with respect to the holomorphic symplectic form (i.e., the symplectic form restricts to zero on each fiber). For hyperkähler manifolds of $\mathrm{K3}^{[n]}$-type, Lagrangian fibrations correspond to primitive isotropic vectors in the Picard lattice.

> **Source**: Standard notion; see [@huybrechts2016lectures, §4.3] for hyperkähler manifolds. Alexeev uses the correspondence with isotropic vectors without defining Lagrangian fibrations.

### Lannér subdiagram

A subdiagram $G \subset G_\mathrm{cox}$ is **Lannér** (or **hyperbolic**) if the restriction of the quadratic form of $N$ to $\mathbb{R}V_G$ is **negative definite on no proper subspace** — equivalently, the form has signature $(1, |G|-1)$ (one positive eigenvalue). Lannér diagrams are the minimal subdiagrams that are neither elliptic nor parabolic.

The finitely many connected Lannér diagrams (of rank 2 through 5) were classified by Lannér (1950). They correspond to compact hyperbolic Coxeter simplices.

**Role in Vinberg's algorithm:** A Coxeter diagram is complete (i.e., the corresponding reflection group has finite covolume in hyperbolic space) if and only if every connected subdiagram is elliptic, parabolic, or Lannér, and every Lannér subdiagram is contained in a maximal parabolic subdiagram. The absence of Lannér subdiagrams is a sufficient condition for completeness (for diagrams without broken edges).

> **Source**: [@alexeev2024reflective, §9.3] (usage); [@vinberg1972units] (classification). Definition by exclusion: a subdiagram that is neither elliptic (negative definite) nor parabolic (negative semidefinite).

### Lattice

An **integral (symmetric) lattice** is a pair $(L, b)$ consisting of a free $\mathbb{Z}$-module $L$ of finite rank and a symmetric bilinear form $b: L \times L \to \mathbb{Z}$. The **Gram matrix** with respect to a basis $\mathcal{E} = \{e_1,\ldots,e_n\}$ is $B_\mathcal{E} = (b(e_i,e_j)) \in \mathbb{Z}^{n\times n}$. The **discriminant** $\mathrm{disc}(b) = \det B_\mathcal{E}$ is independent of the choice of basis.

$L$ is **nondegenerate** if $\mathrm{disc}(b) \neq 0$; **unimodular** if $\mathrm{disc}(b) = \pm 1$.

An **integral quadratic lattice** is a pair $(L, q)$ where $q: L \to \mathbb{Z}$ satisfies $q(\alpha x) = \alpha^2 q(x)$ and the polar form $b_q(x,y) := q(x+y) - q(x) - q(y)$ is a symmetric bilinear form. The polar form is always even: $b_q(x,x) = 2q(x)$. Conversely, every even lattice $(L,b)$ is the polar form of $q(x) = \frac{1}{2}b(x,x)$.

> **Source**: [@peters_sterk2024, §1.2].

### Main roots

Let $L$ be an even two-elementary lattice. The **main roots** in $L$ are the
$(-2)$-roots $\alpha$ of divisibility 1, i.e., satisfying $\alpha \cdot L = \mathbb{Z}$.

> **Source**: [@alexeev2024reflective, Definition 9.1.3]

### Mass formula (Siegel-Minkowski)

For even unimodular positive definite lattices of rank $n = 8k$, the **mass** of the genus is:
$$m_n = \frac{B_{2k}}{8k} \prod_{j=1}^{4k-1} \frac{B_j}{4j}$$
where $B_k$ are Bernoulli numbers. This is a weighted count $\sum_\Gamma 1/|\mathrm{O}(\Gamma)|$ over isometry classes in the genus.

> **Source**: [@peters_sterk2024, §1.12].

### Maximal parabolic subdiagram

Let $S$ be a hyperbolic lattice with Coxeter diagram $\Gamma_r$. A **maximal parabolic subdiagram** of $\Gamma_r$ corresponds to an
$O(S)$-orbit of primitive isotropic vectors in $S$.
If a parabolic subdiagram $\Gamma \subset \Gamma_r$ corresponds to a vector $\nu \in S$
with $\nu^2 = 0$, then its image in $\nu^\perp/\nu$ spans an elliptic root system.

> **Source**: [@alexeev2024reflective, §9.2]

### Moduli quotients $F_{\mathrm{En},2}$, $F_{(10,10,0)}$, $F_{(2,2,0)}$

For the period domains $\mathbb{D}(T_{\mathrm{En}})$ and $\mathbb{D}(T_{\mathrm{dP}})$ with arithmetic groups $\Gamma_{\mathrm{En},2}$, $\Gamma_{\mathrm{En}}$, $\Gamma_{\mathrm{dP}}$:
- $F_{\mathrm{En},2} = \mathbb{D}(T_{\mathrm{En}})/\Gamma_{\mathrm{En},2}$ is the moduli space of Enriques surfaces with numerical polarization of degree 2.
- $F_{(10,10,0)} = \mathbb{D}(T_{\mathrm{En}})/\Gamma_{\mathrm{En}}$ is the moduli space of unpolarized Enriques surfaces.
- $F_{(2,2,0)} = \mathbb{D}(T_{\mathrm{dP}})/\Gamma_{\mathrm{dP}}$ is the moduli space of K3 surfaces with ADE singularities and a nonsymplectic involution with $(+1)$-eigenspace $(2,2,0)_1$.

One has $F_{\mathrm{En},2} \subset F_{(2,2,0)}$ and the morphism $F_{\mathrm{En},2} \to F_{(10,10,0)}$ has degree $2^7 \cdot 17 \cdot 31$.

> **Source**: [@aegs2023compact, Definition 2.7, Lemma 2.8]

### Monodromy invariant

Let $\lambda \in \mathfrak{C}$ be in the fundamental chamber for one of the two 0-cusps of $F_{(2,2,0)}$.
The **monodromy invariant** $\lambda$ encodes the Picard-Lefschetz transformation of a degeneration.
Associated to $\lambda$ is the tuple $\ell = (\ell_i)_{i \in G} = (\lambda \cdot \alpha_i)_{i \in G}$ where $\alpha_i$ are the roots of the Coxeter diagram.
For the cusp $(18,2,0)_1$, one has $\ell \in (\mathbb{Z}_{\geq 0})^{22}$; for $(18,0,0)_1$, one has $\ell \in (\mathbb{Z}_{\geq 0})^{19}$.
For $F_{\mathrm{En},2}$, the monodromy invariant lies in $\mathfrak{C}^J$ for one of the five folding involutions.

> **Source**: [@aegs2023compact, Definition 4.1, §4.3]

### Niemeier lattice

A **Niemeier lattice** is an even unimodular positive definite lattice of rank 24. There are exactly 24 isometry classes, classified by their root sublattice (the sublattice spanned by $(-2)$-roots): either the root sublattice is 0 (the **Leech lattice** $\Lambda_{24}$, the unique Niemeier lattice without roots) or it has rank 24. Examples: $\bigoplus^3 E_8$, $\Gamma_{16} \oplus E_8$, $\Gamma_{24}$.

> **Source**: [@peters_sterk2024, §1.12, Theorem 1.12.1].

### Nikulin classification

An indefinite even two-elementary lattice is uniquely determined by its signature and a
triple of integers $(r, a, \delta)$, where:

- $r$ is the rank of the lattice,
- $a$ is the $\mathbb{Z}_2$-rank of the discriminant group $A_L = L^*/L$, and
- $\delta \in \{0, 1\}$ is the coparity invariant.

> **Source**: [@alexeev2024reflective, §9.2; @nikulin1979integral, Theorem 1.14.2]

### Nikulin involution

A **Nikulin involution** is a symplectic involution $\iota$ on a K3 surface $X$ (i.e., $\iota^*\omega_X = \omega_X$). It has exactly 8 fixed points. The **Nikulin lattice** $\Lambda_\mathrm{Nik}$ is the primitive closure of the 8 exceptional curves in the minimal resolution $\widetilde{X/\langle\iota\rangle}$; it has discriminant group $\oplus^6 \mathbb{Z}/2\mathbb{Z}$.

The **lattice Nikulin involution** on $\Lambda_\mathrm{K3} = \bigoplus^3 U \oplus E_8(-1)^2$ is:
$$(v, e, e') \mapsto (v, e', e)$$
with invariant part $\bigoplus^3 U \oplus E_8(-2)$ and anti-invariant part $E_8(-2)$.

Every K3 surface with a Nikulin involution admits a marking turning it into the lattice Nikulin involution.

> **Source**: [@peters_sterk2024, §20.7, Proposition 20.7.1].

### Nonsymplectic involution

An involution $\iota$ on a K3 surface $X$ is **nonsymplectic** if it acts as $-1$ on the
holomorphic 2-form $\omega_X$. It acts as $+1$ on the Picard lattice $S_X$ and $-1$ on
the transcendental lattice $T_X = S_X^\perp \subset H^2(X, \mathbb{Z})$.

> **Source**: [@alexeev2024reflective, §9.4]

### Normal form (p-adic lattice)

For an odd prime $p$, a nondegenerate $p$-adic symmetric lattice is in **normal form** if it is an orthogonal direct sum of **homogeneous normal forms** $L_{r,u}(p^k) = (\langle u \rangle \oplus \bigoplus^{r-1}\langle 1\rangle)(p^k)$ where $u \in \mathbb{Z}_p^\times$.

**Uniqueness (Proposition 11.1.3):** For odd $p$, the discriminant form map from isometry classes of $p$-adic symmetric lattices of rank $r$ to isometry classes of $p$-primary torsion symmetric forms of length $r$ is bijective. Every $p$-primary torsion form is the discriminant form of a unique $p$-adic lattice of minimal rank.

**Genus invariant:** The **genus invariant** of a nondegenerate integral quadratic lattice $(L,q)$ is the triple $\mathsf{g}(L) := (r_+, r_-, [q_L^\#])$ where $(r_+, r_-)$ is the signature and $[q_L^\#]$ is the isometry class of the discriminant quadratic form.

**Genus characterization (Theorem 11.3.1, Nikulin):** The genus of a nondegenerate quadratic lattice $(L,q)$ is completely determined by its genus invariant $\mathsf{g}(L)$. In other words: two nondegenerate quadratic lattices are in the same genus iff they have the same signature and isometric discriminant quadratic forms.

**Existence (Theorem 12.1.1):** Every nondegenerate quadratic torsion form is the discriminant quadratic form of some nondegenerate quadratic lattice.

> **Source**: [@peters_sterk2024, §11.1–11.3, Proposition 11.1.3, Theorem 11.3.1; §12.1, Theorem 12.1.1].

### Orthogonal modular variety

Let $L$ be a lattice of signature $(2,n)$ and $\Gamma \subset \mathrm{O}^+(L\otimes\mathbb{R})$ an arithmetic subgroup. Let $\mathcal{D}_L$ be the connected component of
$$\Omega_L := \{[x] \in \mathbb{P}(L\otimes\mathbb{C}) \mid (x,x) = 0,\, (x,\bar{x}) > 0\}$$
preserved by $\mathrm{O}^+(L\otimes\mathbb{R})$. The quotient
$$\mathcal{F}_L(\Gamma) := \mathcal{D}_L / \Gamma$$
is a **orthogonal modular variety** — a quasi-projective complex analytic space (locally symmetric variety of type IV).

> **Source**: [@dawes2021baily, §1.5].

### Parabolic diagram (subdiagram)

Let $G_\mathrm{cox}$ be a Coxeter diagram for a hyperbolic lattice $N$. A subdiagram $G \subset G_\mathrm{cox}$ is **parabolic** if the restriction of the quadratic form of $N$ to $\mathbb{R}V_G$ is **negative semidefinite** (but not negative definite).

Equivalently, $G$ is a disjoint union of affine ADE Dynkin diagrams $\widetilde{G}_k$ (types $\widetilde{A}_n, \widetilde{D}_n, \widetilde{E}_6, \widetilde{E}_7, \widetilde{E}_8$). A **maximal parabolic** subdiagram is one that is maximal by inclusion among all parabolic subdiagrams.

**Correspondence with Coxeter fan:** Maximal parabolic subdiagrams correspond to Type II rays $\mathbb{R}_{\geq 0} v$ with $v^2 = 0$ in the Coxeter fan. They are disjoint unions of affine Dynkin diagrams $\widetilde{G}_i$ with $\sum |G_i| = \mathrm{rank}(N) - 2$.

**Square-zero vectors:** For each maximal parabolic subdiagram, the square-zero vectors of its connected components coincide — this common vector is the isotropic ray representative.

For two-elementary lattices, long-root versions are denoted with a $(2)$ suffix, e.g., $\widetilde{A}_n(2)$.

> **Source**: [@alexeev_engel_thompson2019, §4, p.21]: "It is called parabolic if it [is] negative semi-definite. Maximal parabolic means maximal by inclusion among the parabolic diagrams."

### Period domain

For a lattice $\Lambda$ of signature $(2,n)$, the **period domain** $\mathbb{D}(\Lambda)$ is a connected component of
$$\{[x] \in \mathbb{P}(\Lambda \otimes \mathbb{C}) \mid x \cdot x = 0, x \cdot \bar{x} > 0\}.$$
For K3 surfaces, $\Lambda$ is typically a transcendental lattice $T_X \subset H^2(X, \mathbb{Z})$.
The period domains satisfy $\mathbb{D}(T_{\mathrm{En}}) \subset \mathbb{D}(T_{\mathrm{dP}})$ since $T_{\mathrm{En}} \subset T_{\mathrm{dP}}$.

> **Source**: [@aegs2023compact, Definition 2.5]

### Picard lattice

The **Picard lattice** $S_X$ of a surface $X$ is the lattice of divisor classes modulo
algebraic (or numerical) equivalence, equipped with the intersection form.
For K3 surfaces, $S_X \subset H^2(X, \mathbb{Z})$ is an even primitive sublattice of the
K3 lattice $\Lambda_{\mathrm{K3}} \cong U^3 \oplus E_8(-1)^2$, which has signature $(3, 19)$ and rank 22.

> **Source**: [@alexeev2024reflective, §9.1]

### Positive definite, negative definite, semidefinite

Let $(V, B)$ be a quadratic vector space with associated quadratic form $Q(x) = B(x,x)$.

- $Q$ (or $B$, or the matrix $A$ with $Q(x) = x^\top A x$) is **positive definite** if $Q(x) > 0$ for all $x \neq 0$.
- $Q$ is **negative definite** if $Q(x) < 0$ for all $x \neq 0$.
- $Q$ is **positive semidefinite** if $Q(x) \geq 0$ for all $x$.
- $Q$ is **negative semidefinite** if $Q(x) \leq 0$ for all $x$.
- $Q$ is **indefinite** if it takes both positive and negative values.

**Theorem (eigenvalue criterion):** For a real symmetric matrix $A$:
- $A$ is positive definite $\iff$ all eigenvalues of $A$ are $> 0$
- $A$ is negative definite $\iff$ all eigenvalues of $A$ are $< 0$
- $A$ is positive semidefinite $\iff$ all eigenvalues of $A$ are $\geq 0$
- $A$ is negative semidefinite $\iff$ all eigenvalues of $A$ are $\leq 0$

Note: the eigenvalue criterion is a *theorem*, not a definition. The definition is the sign condition on $x^\top A x$.

**For lattices:** An even lattice $L$ is positive (resp. negative) definite if its Gram matrix is positive (resp. negative) definite. Root lattices $A_n, D_n, E_n$ are negative definite by convention in this document.

> **Source**: Standard linear algebra. Lattice convention from [@alexeev2024reflective, §9.2].

### Primitive embedding

A **primitive embedding** of a lattice $S$ into a lattice $L$ is an isometric embedding $i: S \hookrightarrow L$ such that $i(S)$ is a primitive sublattice of $L$.

**Gluing construction (Proposition 15.1.3):** Given nondegenerate lattices $S$ and $T$ with an injective homomorphism $\psi_{S,T}: H_S \hookrightarrow \mathrm{dg}_T$ satisfying the **gluing criterion** $q_T^\#(\psi_{S,T}(-)) + q_S^\# = 0$ on $H_S \subset \mathrm{dg}_S$, the lattice $L = \{y \in (S \oplus T)^* \mid y \bmod (S \oplus T) \in \mathrm{graph}(\psi_{S,T})\}$ is an overlattice of $S \oplus T$ in which $S$ and $T$ embed primitively with $T = S^\perp$. If $H_S = \mathrm{dg}_S$ and $\psi_{S,T}$ is an isomorphism, then $L$ is unimodular.

**Nikulin's existence theorem (Proposition 15.2.1):** Let $S$ be a nondegenerate even lattice of signature $(s_+, s_-)$ with $\ell(\mathrm{dg}_S) \leq (r_+ + r_-) - \mathrm{rank}(S)$. Then $S$ can be primitively embedded in some even unimodular lattice of signature $(r_+, r_-)$ (with $r_+ - r_- \equiv 0 \pmod 8$, $s_\pm \leq r_\pm$) if and only if a nondegenerate even lattice $T$ of signature $(r_+ - s_+, r_- - s_-)$ with discriminant quadratic form $-q_S^\#$ exists.

> **Source**: [@peters_sterk2024, §15.1, §15.2, Propositions 15.1.1, 15.1.3, 15.2.1].

### Primitive sublattice

A submodule $S \subset L$ is **primitive** if any of the following equivalent conditions hold:
1. For $x \in L$, if $nx \in S$ for some nonzero $n \in \mathbb{Z}$, then $x \in S$
2. $L/S$ is torsion-free
3. Any basis for $S$ extends to a basis for $L$
4. $L = S \oplus S'$ for some submodule $S' \subset L$

A nonzero vector $x \in L$ is **primitive** if $\mathbb{Z}x \subset L$ is a primitive sublattice, i.e., $x = ny$ for $y \in L$ implies $n = \pm 1$.

The **primitive closure** of any submodule $S \subset L$ is $S_\mathbb{Q} \cap L = \{x \in L \mid nx \in S \text{ for some } n \in \mathbb{Z}\}$.

> **Source**: [@peters_sterk2024, §1.2, Definition 1.2.4].

### Reflection

**General definition (quadratic vector spaces):** An orthogonal transformation $R \in \mathrm{O}(V)$ of a quadratic vector space $(V, B)$ is a **reflection** if its fixed-point set $\ker(R - I)$ has codimension 1, equivalently if $\mathrm{ran}(R - I) = \ker(R - I)^\perp$ is 1-dimensional.

**Key lemma (Lemma 4.1):** For any $A \in \mathrm{O}(V)$:
$$\mathrm{ran}(A - I) = \ker(A - I)^\perp.$$
*Proof:* For any $L \in \mathrm{End}(V)$, $\mathrm{ran}(L) = \ker(L^\top)^\perp$. Apply to $L = A - I$ and note $\ker(A^\top - I) = \ker(A - I)$ since $A^\top = A^{-1}$.

**Explicit formula:** For any non-isotropic $v \in V$ (i.e., $B(v,v) \neq 0$), the map
$$R_v(w) = w - 2\frac{B(v,w)}{B(v,v)}v$$
is a reflection with $\mathrm{ran}(R_v - I) = \mathrm{span}(v)$.

**Uniqueness (Proposition 4.3):** Any reflection $R$ is of the form $R_v$ where the non-isotropic vector $v$ is unique up to a non-zero scalar. Specifically, $v$ spans $F = \mathrm{ran}(R - I)$, which is necessarily a non-isotropic (quadratic) subspace. Then $R_v$ acts as $-1$ on $F$ and $+1$ on $F^\perp$.

*Proof sketch:* If $F$ were isotropic, one reduces to the case $\dim V = 2$ with $F$ maximal isotropic, where $\mathrm{O}(V)_F$ is identified with skew-symmetric maps $F^* \to F$, which is trivial for $\dim F = 1$ — contradicting $\dim\,\mathrm{ran}(R-I) = 1$.

**Properties:**
1. $\det(R) = -1$
2. $R^2 = I$
3. $AR_vA^{-1} = R_{Av}$ for all $A \in \mathrm{O}(V)$
4. Distinct reflections $R_1 \neq R_2$ commute if and only if $\mathrm{ran}(R_1 - I) \perp \mathrm{ran}(R_2 - I)$

**Lattice case:** For a lattice $L$ with $\alpha \in L$ and $\alpha^2 \neq 0$, the reflection $w_\alpha = R_\alpha$ preserves $L$ when $\alpha$ is a root (i.e., $2(v \cdot \alpha)/\alpha^2 \in \mathbb{Z}$ for all $v \in L$).

> **Source**: General definition and properties from [@dawes2021baily, §4, Definition 4.2, Lemma 4.1, Proposition 4.3]; lattice case from [@alexeev2024reflective, §9.2].


### Reflection group

Let $S$ be a lattice.

- $W_2(S)$: the group generated by reflections in $(-2)$-vectors.
- $W_r(S)$: the group generated by reflections in all roots (both $(-2)$- and $(-4)$-roots).

Both are normal subgroups of $O(S)$ and of its index-2 subgroup $O^+(S)$ preserving the
light cone.

> **Source**: [@alexeev2024reflective, §9.2]

### Reflective lattice

A lattice $L$ is called **$k$-reflective** if the group generated by reflections in $k$-roots has finite index in $\mathrm{O}(L)$. It is called **reflective** if the group generated by reflections in all roots (for all $k$) has finite index in $\mathrm{O}(L)$.

> **Source**: [@peters_sterk2024, §17.2, Definition 17.2.1].

### Relevant root

In the context of generalized Coxeter semifans, the roots of a Coxeter diagram are divided into **relevant** and irrelevant roots $I \sqcup J$.
The relevant roots are those used to define the walls of the generalized chamber.
For the ramification semifan $\mathfrak{F}_{\mathrm{ram}}$ of $F_{(2,2,0)}$, the relevant roots are those lying on the boundary of the square or triangle polytope.

> **Source**: [@aegs2023compact, §5.2]

### Root

Let $(L, b)$ be an integral lattice. A vector $r \in L$ is a **$k$-root** if $r^2 = b(r,r) = k < 0$ and the reflection $\sigma_r(x) = x - \frac{2b(x,r)}{b(r,r)}r$ preserves $L$ (i.e., $\frac{2b(x,r)}{b(r,r)} \in \mathbb{Z}$ for all $x \in L$). A **root** is a $k$-root for some $k < 0$.

For even lattices, the roots are the $(-2)$-vectors (2-roots) and the $(-4)$-vectors of divisibility 2 (4-roots). For a root lattice spanned by its roots, the Weyl group $W(L)$ generated by all reflections in roots acts on $L$.

> **Source**: [@peters_sterk2024, §17.2]; [@alexeev2024reflective, §9.2] for the two-elementary case.

### Root lattice notation

- $A_n$, $D_n$, $E_n$: standard negative-definite root lattices generated by $(-2)$-roots.
- $U = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$: the hyperbolic plane.
- $H(n)$: the lattice $H$ with bilinear form scaled by $n$.
- $B_n(2)$, $C_n$, $F_4$: root lattices for $(-2)$-roots; as $(-2)$-root lattices these are $A_1^n$, $D_n$, and $D_4$ respectively.

> **Source**: [@alexeev2024reflective, §9.2]

### Semifan (Coxeter semifan, generalized Coxeter semifan)

Let $W$ be a reflection group acting on a hyperbolic lattice with fundamental chamber $\mathfrak{C}$ and Coxeter diagram $G = \{\alpha_i\}$.
Divide the vertices of $G$ into relevant and irrelevant sets $I \sqcup J$.
Let $W_{\mathrm{irr}}$ be the subgroup generated by irrelevant roots and let $\mathfrak{C}_{\mathrm{gen}} = \cup_{h \in W_{\mathrm{irr}}} h \cdot \mathfrak{C}$.

The **generalized Coxeter semifan** $\mathfrak{F}_{\mathrm{gen}}$ has support $\overline{\mathcal{C}}_{\mathbb{Q}}$ with maximal dimensional cones being $\mathfrak{C}_{\mathrm{gen}}$ and its $W$-images.
The **Coxeter semifan** $\mathfrak{F}_{\mathrm{cox}}$ is the case where all roots are relevant (so $W_{\mathrm{irr}} = \{1\}$).
A semifan differs from a fan in that there may be infinitely many generators and infinite stabilizer groups.

> **Source**: [@aegs2023compact, Definition 5.1, §5.2]

### Semitoroidal compactification

A **semitoroidal compactification** of a type IV arithmetic quotient $F = \mathbb{D}(\Lambda)/\Gamma$ is a normal compactification dominating the Baily-Borel compactification and dominated by some toroidal compactification.
It is defined by a collection of compatible semifans, one for each Baily-Borel 0-cusp.
For $F_{\mathrm{En},2}$, the KSBA compactification has normalization given by a semitoroidal compactification with semifans $\mathfrak{F}^k$ for $k = 1, 2, 3, 4, 5$.

> **Source**: [@aegs2023compact, §5.2, Theorem 5.9]

### Sign structure and $\mathrm{O}^{+,\#}(L)$

For an indefinite quadratic space $(V, q)$ with signature $(n_+, n_-)$, the **$q^+$-orientation** is a coherent choice of orientation on all maximal positive-definite subspaces (which form a connected Grassmannian). Similarly for **$q^-$-orientation**.

The four components of $\mathrm{O}(n_+, n_-)$ are distinguished by $(\mathrm{Nm}_\mathrm{spin}, \det)$:
- $\mathrm{SO}^+(V)$: preserves both $q^+$ and $q^-$ orientations (connected component of identity)
- $\mathrm{O}^+(V)$: spinor norm 1, preserves $q^-$-orientation (components I and II)
- $\ker(\mathrm{Nm}_\mathrm{spin}^-)$: preserves $q^+$-orientation (components I and III)

For a hyperbolic lattice $L$ of signature $(1, n)$, $\mathrm{O}^-(L)$ is the subgroup preserving the positive cone $\mathcal{C}_L$.

**$\mathrm{O}^{+,\#}(L)$:** The subgroup of $\mathrm{O}^+(L)$ acting trivially on the discriminant group $\mathrm{dg}_L$. This is the intersection $\mathrm{O}^+(L) \cap \widetilde{\mathrm{O}}(L)$.

> **Source**: [@peters_sterk2024, §16.1, Lemma 16.1.2, 16.1.3].

### Spinor norm

For a quadratic space $(V, q)$ over a field $k$ with $\mathrm{char}(k) \neq 2$, the **spinor norm** is the homomorphism
$$\mathrm{Nm}_\mathrm{spin}: \mathrm{Clif}(q) \to k^\times, \quad u \mapsto u \cdot \alpha(u^*)$$
where $\alpha$ is the canonical involution of the Clifford algebra. For non-isotropic $v \in V$, $\mathrm{Nm}_\mathrm{spin}(v) = -q(v)$.

Every $u \in \mathrm{Clif}(q)$ can be written as a product $u = v_1 \cdots v_r$ of non-isotropic vectors, and then:
$$\mathrm{Nm}_\mathrm{spin}(u) = (-1)^r q(v_1) \cdots q(v_r) \in k^\times.$$

**$\mathrm{O}^+(L \otimes \mathbb{R})$** is the kernel of the spinor norm on $\mathrm{O}(L \otimes \mathbb{R})$, i.e., elements with spinor norm $1 \in \mathbb{R}^\times / (\mathbb{R}^\times)^2$. For a hyperbolic lattice, this coincides with the index-2 subgroup preserving the positive cone.

For $\Gamma \subset \mathrm{O}(L \otimes \mathbb{R})$, write $\Gamma^+ := \Gamma \cap \mathrm{O}^+(L \otimes \mathbb{R})$.

> **Source**: [@peters_sterk2024, §13.3, Definition 13.3.4, Corollary 13.3.3]; [@dawes2021baily, §1.2] for the lattice convention.

### Split polarisation

The **stable orthogonal group** $O^*(L)$ is the kernel of the natural map $O(L) \to O(A_L, q_L)$ to the isometry group of the discriminant form. Equivalently, it is the subgroup of $O(L)$ acting trivially on the discriminant group $A_L$.

> **Source**: [@alexeev2024reflective, §9.4]

### Symmetric $R$-module (general)

For a commutative ring $R$ and $R$-module $F$, an **$F$-valued symmetric $R$-module** is a pair $(V, b)$ of an $R$-module $V$ and a symmetric bilinear form $b: V \times V \to F$. An **$F$-valued quadratic $R$-module** is $(V, q)$ where $q: V \to F$ satisfies $q(rx) = r^2 q(x)$ and the polar form $b_q(x,y) = q(x+y) - q(x) - q(y)$ is symmetric bilinear.

**Isotropic/totally isotropic (Definition 6.1.5):**
- A submodule $W \subset V$ is **isotropic** if $b(x,y) = 0$ for all $x,y \in W$ (i.e., $W \subset W^\perp$)
- $W$ is **totally isotropic** if $W = W^\perp$
- $W$ is **totally anisotropic** if $b(x,x) = 0$ has only the trivial solution in $W$
- The **radical** of $b$ is $\mathrm{rad}(b) = V^\perp$; for a quadratic form, $\mathrm{rad}(q) = \{x \in \mathrm{rad}(b_q) \mid q(x) = 0\}$

**Key lemma (6.1.6):** $\mathrm{rad}(q) \subset \mathrm{rad}(b_q)$ with equality iff 2 is invertible in $R$.

**Unimodular submodules split off (Lemma 6.2.1):** If $W \subset V$ is a unimodular submodule, then $V = W \oplus W^\perp$.

**Splitting off units (Proposition 6.3.10):** If $v \in L$ with $b(v,v) = u \in R^\times$, then $L = Rv \oplus (Rv)^\perp \simeq \langle u \rangle \oplus (Rv)^\perp$.

**Splitting over local rings (Proposition 6.3.11):** If $R$ is a local ring with 2 a unit and $(L,b)$ is unimodular, then $b$ is diagonalizable.

**Semi-discriminant (Definition 6.3.3):** For a quadratic $R$-module of odd rank, $\mathrm{sdisc}(q) \in R/(R^\times)^2$ is the semi-discriminant. The module is **semi-unimodular** if $\mathrm{sdisc}(q) \in R^\times$.

**Reduction homomorphism (§6.5):** An isometry $\varphi \in \mathrm{O}(L)$ induces an isometry $\bar\varphi$ of $L^*/L$ preserving $b_L^\#$, giving:
$$r_L^b: \mathrm{O}(L,b) \to \mathrm{O}(b_L^\#), \quad r_L^q: \mathrm{O}(L,b_q) \to \mathrm{O}(q_L^\#).$$
These are in general neither injective nor surjective.

**Special cases:**
- $R = F = \mathbb{Z}$: integral lattices
- $R = F = \mathbb{Z}_p$: $p$-adic lattices
- $R = \mathbb{Z}$, $F = \mathbb{Q}/\mathbb{Z}$: symmetric/quadratic torsion forms (discriminant forms)

> **Source**: [@peters_sterk2024, §6.1–6.5, Definitions 6.1.1–6.5.2, Lemmas 6.1.6, 6.2.1, Propositions 6.3.10, 6.3.11].

### Tits building (of an orthogonal group)

Let $L$ be a lattice of signature $(2,n)$ and $G \subset \mathrm{O}^+(L\otimes\mathbb{Q})$ a group. Let $\mathcal{P}$ and $\mathcal{C}$ denote the $G$-orbits of totally isotropic subspaces of dimension 1 and 2 in $L\otimes\mathbb{Q}$, respectively. The **Tits building** $\mathcal{B}(G) = (\mathcal{N}, \mathcal{E})$ is the bipartite graph with:
- **Node set** $\mathcal{N} := \mathcal{P} \sqcup \mathcal{C}$ (black nodes = isotropic lines $[\ell] \in \mathcal{P}$, white nodes = isotropic planes $[\Pi] \in \mathcal{C}$)
- **Edge set** $\mathcal{E}$: an edge connects $[\Pi] \in \mathcal{C}$ and $[\ell] \in \mathcal{P}$ if and only if $g\ell \subset \Pi$ for some $g \in G$

Equivalently (replacing subspaces by lattices): an edge connects $[\Pi]$ and $[\ell]$ iff some $G$-translate of the primitive isotropic line $\ell \cap L$ is contained in the primitive isotropic plane $\Pi \cap L$.

**Interpretation under the cusp correspondence:**

For $G = \Gamma$ the arithmetic group of a modular variety $\mathcal{F}_L(\Gamma)$:
- Black nodes $[\ell] \in \mathcal{P}$ = **0-cusps** (Type III boundary points) of $\overline{\mathcal{F}_L(\Gamma)}^\mathrm{BB}$
- White nodes $[\Pi] \in \mathcal{C}$ = **1-cusps** (Type II boundary curves) of $\overline{\mathcal{F}_L(\Gamma)}^\mathrm{BB}$
- An edge between $[\Pi]$ and $[\ell]$ means: **the 0-cusp $P_\ell$ lies in the closure of the 1-cusp curve $\mathcal{C}_\Pi$**

In terms of hyperbolic geometry: a 0-cusp (ideal point of $\mathbb{H}^n$) is connected to a 1-cusp (ideal boundary curve) when the isotropic line is contained in the isotropic plane — i.e., the ideal point lies "at the end" of the horocycle/boundary component parametrized by the 1-cusp.

In terms of the Coxeter fan: an edge in the building corresponds to a face relation — the ray (maximal parabolic) is a face of a higher-dimensional cone, or equivalently, the isotropic line $\ell$ is in the boundary of the isotropic plane $\Pi$ as a degeneration.

> **Source**: [@dawes2022orbits, Definition 3.1, §3]: "an edge is drawn between $[\Pi] \in \mathcal{C}$ and $[\ell] \in \mathcal{P}$ if and only if $g\ell \in \Pi$ for some $g \in G$."

### Torelli theorem

For K3 surfaces, the **Torelli theorem** states that the isomorphism class of $X$ is
uniquely determined by the Hodge structure on its transcendental lattice $T_X$.
The automorphism group $\operatorname{Aut}(X)$ is commensurable to $O(S_X)/W_2(S_X)$.

> **Source**: [@alexeev2024reflective, §9.1, §9.4; @friedman1984new]

### Torelli theorem (K3 surfaces)

**Theorem 19.2.1:** Two K3 surfaces are isomorphic if and only if there exist markings giving the same period point in $D(\Lambda)$ (injectivity). Every point of $D(\Lambda)$ is a period point (surjectivity).

**Automorphism group description (Theorem 19.2.2, Lemma 19.2.4):**
$$\mathrm{Aut}(X) \hookrightarrow \mathrm{O}(H^2(X,\mathbb{Z}))$$
is injective, and:
$$\mathrm{Aut}(X) \simeq \{\gamma \in \mathrm{O}(H^2(X,\mathbb{Z})) \mid \gamma_\mathbb{C}(H^{2,0}(X)) = H^{2,0}(X)\} / \{\pm\mathrm{id}\} \times W^-(X).$$

An isometry $\gamma$ is induced by an automorphism iff $\gamma_\mathbb{C}$ preserves the Hodge decomposition and $\gamma_\mathbb{R}$ preserves the Kähler cone.

> **Source**: [@peters_sterk2024, §19.2, Theorems 19.2.1, 19.2.2, Lemma 19.2.4].

### Toroidal compactification

A **toroidal compactification** of a type IV arithmetic quotient is defined by a collection of fans, one for each 0-cusp.
For the moduli space $F_{(2,2,0)}$, the toroidal compactification $\overline{F}_{(2,2,0)}^{\mathrm{cox}}$ is defined by the Coxeter fans $\mathfrak{F}_{\mathrm{cox}}^{\mathrm{dP}} = \{\mathfrak{F}_r(18,0,0), \mathfrak{F}_r(18,2,0)\}$ for the full reflection groups.
The faces of the fundamental chamber correspond to:
- Type II rays (generated by vectors with $v^2 = 0$), in bijection with maximal parabolic subdiagrams.
- Type III cones, in bijection with elliptic subdiagrams.

> **Source**: [@aegs2023compact, Definition 5.1]

### Torsion form (discriminant form invariants)

**Jordan splitting (Proposition 9.3.7, Theorem 9.3.12):** Every nondegenerate $p$-primary symmetric (resp. quadratic) torsion group $(G, b)$ (resp. $(G,q)$) admits a **Jordan splitting** $G = \bigoplus_{k=1}^s H_k$ where each $H_k$ is homogeneous of exponent $k$ with nondegenerate restriction. The splitting is not unique but the ranks $\ell_k = \mathrm{rank}(\rho_k(G))$ are invariants.

**Classification for odd $p$ (Proposition 9.4.1):** A nondegenerate homogeneous $p$-primary symmetric torsion form of exponent $k$ and length $r$ is isometric to:
$$\bigoplus^{r-1}\langle p^{-k}\rangle \oplus \langle \epsilon p^{-k}\rangle$$
where $\epsilon = 1$ if $\mathrm{disc}(\rho_k(b)) = 1$ (square mod $p$) and $\epsilon$ is a non-square otherwise. Two isometry classes per $(k, r)$.

**Classification for $p=2$ (Proposition 9.4.2):** Building blocks for homogeneous 2-primary forms of exponent $k \geq 2$:
- Symmetric: $\bigoplus^a \langle u^{(j)} 2^{-k}\rangle \oplus^b u_k \oplus^c v_k$ with $a + 2(b+c) = r$
- Quadratic: $\bigoplus^a [u^{(j)} 2^{-k-1}] \oplus^b u_k \oplus^c v_k$

For exponent 1, quadratic forms have additional type II building blocks $[u \cdot 2^{-2}]$ with $u \in \{1,3\}$.

**Basic invariants (Definition 9.3.8):** For each $k$: the rank $\ell_k$ of $\rho_k(G)$; for odd $p$, also $\mathrm{disc}(\rho_k(b)) \in \mathsf{D}(\mathbb{F}_p)$.

> **Source**: [@peters_sterk2024, §9.3–9.4, Proposition 9.3.7, Theorem 9.3.12, Propositions 9.4.1–9.4.2].

### Totally isotropic sublattice

A sublattice $S \subset L$ is **totally isotropic** if the restriction of the quadratic form of $L$ to $S$ is identically zero, i.e., $(x,y) = 0$ for all $x, y \in S$. In particular, every element of $S$ is isotropic.

In the Baily-Borel compactification of $\mathcal{F}_L(\Gamma)$:
- Rank-1 primitive totally isotropic sublattices $\langle v \rangle$ correspond to **0-cusps** (boundary points).
- Rank-2 primitive totally isotropic sublattices $E$ correspond to **1-cusps** (boundary curves).

> **Source**: [@dawes2021baily, §1.1, Theorem 1.1].

### Transcendental lattice

The **transcendental lattice** $T_X$ is the orthogonal complement of the Picard lattice
$S_X$ in the full cohomology $H^2(X, \mathbb{Z})$, i.e., $T_X = S_X^\perp \cap H^2(X, \mathbb{Z})$.

> **Source**: [@alexeev2024reflective, §9.4]

### Two-elementary lattice

A lattice $S$ is **two-elementary** if its discriminant group $A_S := S^*/S \simeq \mathbb{Z}_2^a$ for some $a \geq 0$, where $S^* \subset S \otimes \mathbb{Q}$ is the dual lattice.

> **Source**: [@alexeev2024reflective, §9.2]

### Two-reflective lattice

A lattice $S$ is **two-reflective** if the $(-2)$-reflection group $W_2(S)$ has finite index in $O(S)$.

> **Source**: [@alexeev2024reflective, §9.2]

### Type II degeneration

A **Type II degeneration** of K3 surfaces $\mathcal{X} \to (C,0)$ has dual complex $\Gamma(\mathcal{X}_0)$ a segment.
The central fiber is a chain of surfaces glued along elliptic curves.
Type II boundary components correspond to maximal parabolic subdiagrams of the Coxeter diagram.
For Enriques surfaces, in Type II the action of $\iota_{\mathrm{En},0}$ on $\Gamma(\mathcal{X}_0)$ either flips the segment (double rectangle cusps) or fixes it (single rectangle cusps).

> **Source**: [@aegs2023compact, §3.2, §7.2, Proposition 4.8]

### Type III degeneration

A **Type III degeneration** of K3 surfaces $\mathcal{X} \to (C,0)$ has dual complex $\Gamma(\mathcal{X}_0)$ a 2-sphere $S^2$.
The central fiber is a union of rational surfaces forming a "pumpkin" or "smashed pumpkin" configuration.
Type III boundary components correspond to elliptic subdiagrams of the Coxeter diagram.
For Enriques surfaces, the quotient $\Gamma(\mathcal{Z}_0) = \Gamma(\mathcal{X}_0)/\iota_{\mathrm{En,IA}}$ is either $\mathbb{RP}^2$ (Cusp 1, antipodal involution) or $\mathbb{D}^2$ (Cusps 2–5, hemispherical involution).

> **Source**: [@aegs2023compact, §4.1, §7.1, Proposition 4.8]

### Unique splitting (definite lattices)

Every positive definite lattice decomposes uniquely as an orthogonal sum of indecomposable lattices.

> **Source**: [@peters_sterk2024, §1.12, Theorem 1.12.3].

### Vanishing lattice

A **vanishing lattice** is a pair $(L, \Delta)$ where $L$ is a lattice and $\Delta$ is a set of roots spanning $L$ that forms a single orbit under the Weyl group $W^-(\Delta) = \langle \sigma_r \rangle_{r \in \Delta}$, i.e., $\Delta = W^-(\Delta)\Delta$.

A vanishing lattice $(L, \Delta)$ is **complete** if it contains a copy of the minimal vanishing lattice $(L_\mathrm{min}, \Gamma_\mathrm{min})$ where $L_\mathrm{min} = U \oplus U' \oplus A_2(-1)$.

**Application:** The primitive cohomology $H^n_\mathrm{prim}(X_*)$ of a smooth hypersurface $X_*$ in $\mathbb{P}^{n+1}$ carries a vanishing lattice structure, with vanishing cycles as the roots. The monodromy group equals $\mathrm{O}^{-,\#}(\Lambda_{d,n})$ for $d \geq 4$ or $d=3, n \neq 2$.

> **Source**: [@peters_sterk2024, §18.1, Definitions 18.1.2, 18.1.4].

### Vinberg's algorithm

Let $(M, b)$ be a nondegenerate lattice of signature $(1, n)$ with positive cone $\mathcal{C}_M$. Let $\mathrm{O}^-(M)$ be the index-2 subgroup fixing $\mathcal{C}_M$. If the subgroup generated by reflections $\sigma_v$ (for $b(v,v) < 0$) has finite index in $\mathrm{O}^-(M)$, it has a polyhedral fundamental domain $P$ of finite volume in the Lobachevskii space $\mathcal{C}_M/\mathbb{R}_+$.

**Algorithm:** Starting from $x \in \mathcal{C}_M \cap M$, successively find bounding hyperplanes $v_1, v_2, \ldots$ by minimizing the Lobachevskii distance function $\frac{b(x,z)^2}{|b(z,z)|}$ subject to $b(v_k, v_j) \geq 0$ for all previous $v_j$.

**Termination criterion:** Stop when the Coxeter diagram satisfies:
1. No Lannér subdiagrams
2. Every parabolic subdiagram extends to a parabolic subdiagram of rank $n-1$
3. A condition on pairs of non-meeting bounding hyperplanes (dashed rank-2 subdiagrams)

The **vertices at infinity** of $P$ (isotropic rank-1 sublattices up to reflection equivalence) are read off from the diagram. The step to full isometry equivalence uses symmetries of the Coxeter diagram.

> **Source**: [@peters_sterk2024, §19.4, citing Vinberg]; [@vinberg1972units]; [@belolipetsky_kapovich2022] for effective bounds.

* * *

### Witt cancellation

If $L_1 \perp M \simeq L_2 \perp M$ for nondegenerate lattices, then $L_1 \simeq L_2$ (over $\mathbb{Q}$ or over $\mathbb{Z}$ under appropriate conditions).

> **Source**: [@peters_sterk2024, §7.2].

### Witt decomposition

Let $(V, b)$ be a nondegenerate inner product space over a field $k$ with $\mathrm{char}(k) \neq 2$. The **Witt decomposition** is an orthogonal decomposition
$$V = \hat{U} \perp S$$
where $\hat{U}$ is an even-dimensional subspace containing all isotropic vectors (a direct sum of hyperbolic planes) and $S$ contains no isotropic vectors (anisotropic). This decomposition is unique up to isometry.

The **Witt index** $\mathsf{W}_\tau(V) = \frac{1}{2}\dim \hat{U}$ is an isometry invariant. For $V = L \otimes \mathbb{R}$ with signature $(r_+, r_-)$: $\mathsf{W}_\tau(L_\mathbb{R}) = \min(r_+, r_-)$.

> **Source**: [@peters_sterk2024, §1.5, §7.2].

## WARNING: Commonly Misapplied Invariants

The following invariants are sometimes incorrectly invoked in the context of lattice classification. **They are not relevant to the isometry classification of integral lattices.**

### Arf invariant

> **WARNING: NOT relevant to lattice theory.**

The **Arf invariant** is an invariant of quadratic forms over the field $\mathbb{F}_2$. For a quadratic form $q: V \to \mathbb{F}_2$ on an $\mathbb{F}_2$-vector space $V$, the Arf invariant is defined as $\mathrm{Arf}(q) = \sum_{i=1}^{n} q(e_i)q(f_i)$ where $\{e_i, f_i\}$ is a symplectic basis.

**Why it is irrelevant to lattice theory:**

- The Arf invariant is a **weakening** of the discriminant form of a lattice.
- It is **only well-defined for $\mathbb{F}_2$-valued forms**, not for $\mathbb{Z}$-valued bilinear forms.
- It is **extremely ill-defined** for arbitrary quadratic forms over $\mathbb{Z}$.
- Two lattices with the same Arf invariant need not be isometric.
- The discriminant form $q_L: A_L \to \mathbb{Q}/2\mathbb{Z}$ contains strictly more information than any $\mathbb{F}_2$-valued reduction.

> **Source**: Standard notion in quadratic form theory. For the correct discriminant-form approach to lattice classification, see [@nikulin1979integral].

### Brown invariant (Brown-Kervaire invariant)

> **WARNING: NOT relevant to lattice isometry classification.**

The **Brown invariant** (also called the Brown-Kervaire invariant) of a non-degenerate quadratic form $q: V \to \mathbb{F}_2$ on an $\mathbb{F}_2$-vector space of even dimension is an element of $\mathbb{Z}/8\mathbb{Z}$. For a symmetric bilinear form over $\mathbb{Z}$ with signature $(p, q)$, one sometimes sees $\mathrm{Brown}(L) = (p - q) \bmod 8$.

**Why it is irrelevant to lattice theory:**

- The Brown invariant is a **weakening** of the signature $\tau = p - q \in \mathbb{Z}$.
- It is **NOT an invariant of $\mathbb{Z}$-valued forms** up to isometry.
- It is a **bordism invariant**, not a lattice invariant—it classifies manifolds up to bordism, not lattices up to isometry.
- Two lattices with the same Brown invariant can have completely different isometry classes.
- The actual signature $(p, q) \in \mathbb{Z}^2$ (or equivalently $\tau \in \mathbb{Z}$) is the correct invariant for indefinite lattices.

> **Source**: The Brown invariant originates in bordism theory. For the lattice-theoretic classification, use the signature $(p, q) \in \mathbb{Z}^2$ or discriminant form.

### Milgram's formula

> **WARNING: NOT a lattice invariant.**

A **discriminant form** is a finite abelian group $A$ together with a $\mathbb{Q}/\mathbb{Z}$-valued non-degenerate quadratic form $q: A \to \mathbb{Q}/2\mathbb{Z}$ given by $x \mapsto \frac{1}{2}x^2$ for $x \in A$. If $L$ is a non-degenerate even lattice, then $L^*/L$ is a discriminant form where the quadratic form is given by the mod 1 reduction of the quadratic form on $L^*$. Conversely, every discriminant form can be obtained in this way.

**Milgram's formula** (also called the Gauss sum formula) states that the quadratic form on $L^*/L$ determines the signature of $L$ modulo 8:
$$\sum_{\lambda \in L^*/L} e(\lambda^2/2) = \sqrt{|L^*/L|} \cdot e(\mathrm{sig}(L)/8)$$
where $e(z) = e^{2\pi i z}$ and $\mathrm{sig}(L) = p - q \in \mathbb{Z}$ is the signature.

One can define the **signature of a discriminant form** $A$ to be $\mathrm{sig}(A) \in \mathbb{Z}/8\mathbb{Z}$, i.e., the signature of any even lattice with that discriminant form. This is well-defined by Milgram's formula.

**Why it is irrelevant to distinguishing lattices:**

- Milgram's formula is a **constraint**, not a distinguishing invariant.
- It is an invariant of the **discriminant form**, not of the lattice itself.
- It is NOT an invariant of the lattice $L$; rather, it is an invariant of **some even lattice that has the same discriminant form as $L$**.
- Two different even lattices with the same discriminant form have the same value in Milgram's formula—but they may not be isometric.
- The formula only determines the signature **modulo 8** from the discriminant form; the actual signature $\tau \in \mathbb{Z}$ contains strictly more information.
- For classification of even lattices, one needs the full discriminant form together with the signature (not just mod 8).

> **Source**: [@nikulin1979integral] for discriminant forms; [@milnor1973symmetric, Appendix 4] for the formula; [@bruinier2002borcherds, §2] and [@boylan2015hecke] for modern treatments.

* * *

## Results

### Automorphism group finiteness

The automorphism group $\operatorname{Aut}(X)$ of a complex projective K3 surface $X$ is finite if and only if $\mathrm{O}^-(S)/W^-(S)$ is finite, where $S = \mathrm{NS}(X)$ — i.e., the Weyl group $W^-(S)$ has finite index in the isometry group of the Néron-Severi lattice.

**Exact sequence (Theorem 20.1.1):** There is an exact sequence
$$1 \to \mathrm{Aut}_s(X) \to \mathrm{Aut}(X) \xrightarrow{\rho_T} \mu_m \to 1$$
where $\mu_m$ is the group of $m$-th roots of unity and $\mathrm{Aut}_s(X)$ is the symplectic automorphism group. The group $\mathrm{Aut}_s(X) \simeq \mathrm{O}^{-,\#}(S)/W^-(S)$.

**Finite generation (Proposition 20.1.5):** $\mathrm{Aut}(X)$ is finitely generated for any projective K3 surface.

> **Source**: [@peters_sterk2024, §20.1, Theorem 20.1.1, Criterion 20.1.3, Proposition 20.1.5].

### Classification of isotropic vectors

Let $S$ be an even hyperbolic two-elementary lattice with invariants $(r, a, \delta)$.
Primitive isotropic vectors $\nu \in S$ with $\nu^2 = 0$ fall into three types.
Denoting $\overline{S} = \nu^\perp/\nu$:

1. **Odd**: $S = U \oplus \overline{S}$, $a_{\overline{S}} = a_S$, $\delta_{\overline{S}} = \delta_S$.
2. **Even ordinary**: $S = U(2) \oplus \overline{S}$, $a_{\overline{S}} = a_S - 2$, $\delta_{\overline{S}} = \delta_S$.
3. **Even characteristic**: $S = I_{1,1}(2) \oplus \overline{S}$, $a_{\overline{S}} = a_S - 2$, $\delta_S = 1$, and $\delta_{\overline{S}} = 0$.

> **Source**: [@alexeev2024reflective, §9.2; @aegs2023compact, Proposition 5.5]

### Coxeter diagrams built on $K_n^{(2)}$

For $n = 3, 4, 5, 6$, the Coxeter diagram $\Gamma_r$ of the even two-elementary lattice
$(10+n, 12-n, 1)$ is built on top of $K_n^{(2)}$, where $K_n$ is the complete graph on $n$ vertices.
The diagram for $(18,4,0)$ is built on top of $K_{4,4}^{(2)}$. The diagram for $(14,8,0)$ is built on
top of $D_4^{(2)}$. In all cases, $\operatorname{Aut}\Gamma_r = \operatorname{Aut}G$ and $O^+(S) = \operatorname{Aut}G \ltimes W_r$.

> **Source**: [@alexeev2024reflective, Theorem 9.1.4]

### Duality for coeven lattices

If $S = (r, a, 0)$ is coeven, then $S^\dagger = S^*(2) = (r, r - a, 0)$ is also coeven.
Their Coxeter diagrams are dual, with $(-2)$ and $(-4)$ roots interchanged, and there is
a bijection between their maximal parabolic subdiagrams.

> **Source**: [@alexeev2024reflective, §9.3]

### Elliptic and Lagrangian fibrations

Let $X$ be a K3 surface with Picard lattice $S_X$. Primitive isotropic vectors $\nu \in S_X$ correspond bijectively to elliptic fibrations on $X$. For hyperkähler manifolds, primitive isotropic vectors in the Picard lattice correspond to Lagrangian fibrations.

> **Source**: [@alexeev2024reflective, §9.1]

### K3 automorphism exact sequence

For a two-elementary K3 lattice $S \neq (10,10,0)$, with Coxeter diagram $\Gamma_r$ and
K3 surface $X$ with $S_X = S$:
$$0 \to \langle \iota \rangle \times \operatorname{Aut}'(Y, B) \to \operatorname{Aut}X \to \operatorname{Sym}\Gamma_r \ltimes W(\Gamma_4) \to 0,$$
where $\iota$ is the canonical nonsymplectic involution, $Y = X/\iota$, $B$ is the branch divisor, and $\Gamma_4 \subset \Gamma_r$ is the subdiagram of $(-4)$-roots.

> **Source**: [@alexeev2024reflective, Lemma 9.4.1]

### Nonreflective lattices on the $r + a = 22$ line

The two-elementary lattices $(17,5,1)$, $(18,4,1)$, and $(19,3,1)$ are not reflective.
All other even two-elementary lattices on the line $r + a = 22$ are reflective.

> **Source**: [@alexeev2024reflective, Theorem 9.1.1]

### Reflection group quotient

The quotient group $W_r(S)/W_2(S)$ is isomorphic to $W(\Gamma_4)$, where $W(\Gamma_4)$
is the Coxeter group generated by reflections in the $(-4)$-roots.

> **Source**: [@alexeev2024reflective, §9.4; citing @vinberg1983two, Proposition, page 2]

### $(-4)$-subdiagrams for $r + a = 22$

| Lattice | $\operatorname{Aut}\Gamma_r$ | $\Gamma_4$ |
| --- | --- | --- |
| $(11,11,1)$ | 1 | $T_{2,3,7}$ |
| $(12,10,1)$ | 1 | $T_{2,4,6} \sqcup A_1$ |
| $(13,9,1)$ | $S_3$ | $T_{4,4,4}$ |
| $(14,8,1)$ | $S_4$ | 10-vertex trivalent tree with 6 ends |
| $(15,7,1)$ | $S_5$ | Petersen graph |
| $(16,6,1)$ | $S_6$ | Diagram with $10 + 15$ vertices |
| $(18,4,0)$ | $S_2 \ltimes (S_4 \times S_4)$ | Diagram with 24 vertices |
| $(20,2,1)$ | $S_5$ | $K_5$ with bold edges |

Here $T_{p,q,r}$ denotes a tree with legs of lengths $p, q, r$.

> **Source**: [@alexeev2024reflective, Table 9.1]

### Maximal parabolic subdiagram counts

| Lattice | Total parabolics | Modulo $\operatorname{Aut}\Gamma_r$ |
| --- | --- | --- |
| $(11,11,1)$ | 2 | 2 |
| $(12,10,1)$ | 5 | 5 |
| $(13,9,1)$ | 22 | 7 |
| $(14,8,0)$ | 11 | 5 |
| $(14,8,1)$ | 127 | 15 |
| $(15,7,1)$ | 1027 | 20 |
| $(16,6,1)$ | 8917 | 28 |
| $(18,4,0)$ | 5244 | 17 |
| $(20,2,1)$ | 581 | 13 |
| $(13,11,1)$ | 9 | 5 |
| $(14,10,1)$ | 69 | 12 |
| $(15,9,1)$ | 2114 | 20 |
| $(18,6,0)$ | 90,897,634 | 28 |
| $(22,2,0)$ | 1,095,990 | 18 |
| $(14,12,1)$ | 16 | 9 |
| $(15,11,1)$ | 522 | 16 |
| $(15,13,1)$ | 46 | 10 |
| $(16,14,1)$ | 115 | 14 |

> **Source**: [@alexeev2024reflective, §9.3]

### Surjectivity of $O(H) \to O(A_H, q_H)$

For an indefinite two-elementary lattice $H$, the natural homomorphism $O(H) \to O(A_H, q_H)$ to the isometry group of its discriminant form is surjective.

> **Source**: [@alexeev2024reflective, §9.4; @nikulin1979integral]

### KSBA compactification of $F_{\mathrm{En},2}$

The normalization of the KSBA compactification $\overline{F}_{\mathrm{En},2}$ is a semitoroidal compactification $\overline{F}_{\mathrm{En},2}^{\mathfrak{F}}$ corresponding to a collection $\mathfrak{F} = \{\mathfrak{F}^k\}_{k=1,2,3,4,5}$ of explicit semifans, one for each 0-cusp of $F_{\mathrm{En},2}$.
It is dominated by a toroidal compactification $\overline{F}_{\mathrm{En},2}^{\mathrm{cox}}$ for a collection of Coxeter fans.
The compactification is toroidal over the 0-cusps 2 and 4, the 1-cusps adjacent to them, and over 1-cusp 35; it is strictly semitoroidal over the remaining cusps.

> **Source**: [@aegs2023compact, Theorem 1.1, Theorem 5.9]

* * *

## Bibliography

Local markdown extractions should be symlinked in `refs/` directory. Run:

```bash
cd /home/dzack/research/theory
mkdir -p refs
ln -sf ../../pdfs/other/nsf_10653059/content.md refs/alexeev2024reflective.md
# Find and link others: aegs, huybrechts, nikulin
```

- **[@sterk1991]**: H. Sterk, *Compactifications of the period space of Enriques surfaces. I*, Math. Z. 207(1):1–36, 1991.  
  Extraction: `/home/dzack/pdfs/other/sterk_1991_period_enriques_I/content.md`

- **[@sterk1995thesis]**: H. Sterk, *Compactifications of the period space of Enriques surfaces: arithmetic and geometric aspects*, PhD thesis, Radboud University Nijmegen, 1995.  
  Extraction: `/home/dzack/pdfs/other/sterk_1995_period_enriques_II/content.md`

- **[@peters_sterk2024]**: C. Peters and J. Sterk, *Symmetric and Quadratic Forms, with Applications to Coding Theory, Algebraic Geometry and Topology*, 2024.  
  Extraction: `/home/dzack/pdfs/Peters-Sterk_2024_Symmetric-and-Quadratic-Forms/Peters-Sterk_2024_Symmetric-and-Quadratic-Forms.md`

- **[@dawes2021baily]**: M. Dawes, *The Baily-Borel compactification of a family of orthogonal modular varieties*, arXiv:2108.06236, 2021.  
  Extraction: `/home/dzack/pdfs/arxiv/2108.06236/paper.md`

- **[@dawes2022orbits]**: M. Dawes, *Orbits in lattices*, arXiv:2205.10601, 2022.  
  Extraction: `/home/dzack/pdfs/arxiv/2205.10601/paper.md`

- **[@alexeev_engel_thompson2019]**: V. Alexeev, P. Engel, and A. Thompson, *Stable pair compactification of moduli of K3 surfaces of degree 2*, J. Reine Angew. Math. 799 (2023), 1–56, arXiv:1903.09742.  
  Extraction: `/home/dzack/pdfs/arxiv/1903.09742/paper.md`

- **[@alexeev2024reflective]**: V. Alexeev, *Reflective Hyperbolic 2-Elementary Lattices, K3 Surfaces and Hyperkahler Manifolds*, in: Advances in Geometry and Lattice Theory, NSF Public Access Repository, PURL 10653059, 2024.  
  Extraction: `/home/dzack/pdfs/other/nsf_10653059/content.md`

- **[@aegs2023compact]**: V. Alexeev, P. Engel, D. Zack Garza, and M. Schaffler, *Compact Moduli of Enriques Surfaces with a Numerical Polarization of Degree 2*, arXiv:2208.10383, 2023.  
  Extraction: locate via `find /home/dzack -name "*aegs*" -o -name "*enriques*"`

- **[@beauville1983varietes]**: A. Beauville, *Variétés Kähleriennes dont la première classe de Chern est nulle*, J. Diff. Geom. 18 (1983), 755–782.

- **[@boylan2015hecke]**: H. Boylan, *A Quick Proof of Reciprocity for Hecke Gauss Sums*, available at http://www.hboylan.de/static/documents/hecke-reciprocity.pdf.

- **[@bruinier2002borcherds]**: J. H. Bruinier, *Borcherds Products on O(2,l) and Chern Classes of Heegner Divisors*, Springer Lecture Notes in Mathematics 1780, 2002. Available at https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/bruinier/publikationen/weil5.pdf.

- **[@friedman1984new]**: R. Friedman, *A New Proof of the Global Torelli Theorem for K3 Surfaces*, Ann. of Math. 120 (1984), no. 2, 237–269.

- **[@huybrechts2016lectures]**: D. Huybrechts, *Lectures on K3 Surfaces*, Cambridge Studies in Advanced Mathematics 158, Cambridge University Press, 2016.  
  Extraction: locate via `find /home/dzack -name "*huybrechts*"`

- **[@milnor1973symmetric]**: J. Milnor and D. Husemoller, *Symmetric Bilinear Forms*, Springer, 1973. (Milgram's formula appears in Appendix 4; cited as [MH] in Bruinier.)

- **[@nikulin1979integral]**: V. V. Nikulin, *Integer Symmetric Bilinear Forms and Some of Their Geometric Applications*, Izv. Akad. Nauk SSSR Ser. Mat. 43 (1979), no. 1, 111–177.  
  Extraction: locate via `find /home/dzack -name "*nikulin*"`

- **[@vinberg1972units]**: É. B. Vinberg, *The Groups of Units of Certain Quadratic Forms*, Mat. Sb. (N.S.) 87 (1972), no. 129, 18–36.

- **[@vinberg1975arithmetical]**: É. B. Vinberg, *Some Arithmetical Discrete Groups in Lobachevskiĭ Spaces*, in: Discrete Subgroups of Lie Groups and Applications to Moduli, Oxford University Press, 1975, 323–348.

- **[@vinberg1983two]**: É. B. Vinberg, *The Two Most Algebraic K3 Surfaces*, Math. Ann. 265 (1983), no. 1, 1–21.

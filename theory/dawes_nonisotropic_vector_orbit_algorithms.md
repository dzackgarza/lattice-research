# Dawes: Algorithms for Orbits of Non-Isotropic Vectors

**Source**
- Matthew Dawes, *Orbits in lattices*, §2.1, Algorithms 2.1-2.3, Theorem 2.3, Lemmas 2.4-2.5.

## Scope

This sidecar records only the explicit general algorithms and supporting criteria in
Dawes's paper for deciding whether two non-isotropic vectors lie in the same orbit.

Notation is Dawes's:

- $L$ is a lattice of rank $n$.
- $\Gamma \subset O(L)$ is a subgroup.
- $v_1, v_2 \in L \otimes \mathbb{Q}$ are the vectors to compare.

## Algorithmic Hierarchy

Dawes presents the following hierarchy.

### Algorithm 2.1

This is the broadest algorithm in §2.1.

Hypotheses:

- $L$ is any lattice of rank $n$.
- $\Gamma \subset O(L)$ is any subgroup.
- $v_1$ is non-isotropic.
- $v_1^\perp$ is definite.

No discriminant-form description of $\Gamma$ is required.
No surjectivity hypothesis on $O(L) \to O(D(L))$ is required.

### Algorithm 2.2

This is a stricter specialization for the indefinite-complement case.

Hypotheses:

- $L$ is a lattice of rank $n$.
- $\Gamma = O_{\mathcal A}(L)$ for some subgroup
  $$
  \mathcal A \subset O(D(L)).
  $$
- $v_1$ is non-isotropic.
- $v_1^\perp$ is indefinite.
- The natural map
  $$
  O(L) \to O(D(L))
  $$
  is surjective.

Algorithm 2.2 replaces direct lattice-isometry testing by discriminant-form and gluing
data.

### Algorithm 2.3

This is Dawes's coordinate rephrasing of Algorithm 2.2.

It uses Smith normal forms, explicit generators for discriminant groups, and explicit
formulas for the gluing subgroups and induced maps on discriminant groups.

## Common Preliminary Invariants

All three algorithms begin by normalizing the rational vectors.

For $i \in \{1,2\}$:

1. Let $c_i \in \mathbb{Q}_{>0}$ be minimal such that
   $$
   w_i := c_i v_i \in L.
   $$
2. Reject immediately if either invariant differs:
   - $v_1^2 \neq v_2^2$,
   - $c_1 \neq c_2$.

These are orbit invariants under every subgroup of $O(L)$.

## Algorithm 2.1

Assume $v_1$ is non-isotropic and $v_1^\perp$ is definite.

### Procedure

1. Normalize to integral vectors $w_1, w_2$.
2. Reject if $v_1^2 \neq v_2^2$ or $c_1 \neq c_2$.
3. For each $i \in \{1,2\}$:
   - compute $w_i$,
   - compute $(q_1|\cdots|q_n) := Q(\hat w_i)$,
   - define
     $$
     K_i := \langle k_{ij} \mid j = 1,\dots,n-1 \rangle
     \quad\text{with}\quad
     k_{ij} = q_{j+1},
     $$
   - define the embedding
     $$
     \iota_i := (w_i|k_{i1}|\cdots|k_{i(n-1)}).
     $$
4. Let $\varphi$ be the map $w_1 \mapsto w_2$.
5. Search over
   $$
   \psi \in \operatorname{Iso}(K_1, K_2).
   $$
6. For each such $\psi$, form
   $$
   \theta := \iota_2 \circ (\varphi \oplus \psi) \circ \iota_1^{-1}.
   $$
7. If some $\theta$ lies in $\Gamma$, return $v_1 \sim_\Gamma v_2$.
8. Otherwise return $v_1 \not\sim_\Gamma v_2$.

### Dawes's explanation

- The Smith normal form shows that each $K_i$ is the primitive orthogonal complement
  $w_i^\perp \subset L$.
- By Lemma 2.1, $w_1 \sim_\Gamma w_2$ if and only if the fixed map on
  $\langle w_1 \rangle$ and some isometry $K_1 \to K_2$ extend simultaneously to an
  element of $\Gamma$.
- Because $K_1$ is definite, $\operatorname{Iso}(K_1,K_2)$ can be computed with
  standard definite-lattice isometry algorithms.

### Membership remarks

Dawes makes the following subgroup-specific remarks:

- If $\Gamma = SO_{\mathcal A}(L)$ or $O_{\mathcal A}(L)$, one can check membership by
  verifying that $\theta$ is integral and that $\overline{\theta} \in \mathcal A$.
- If $\Gamma = SO_{\mathcal A}^+(L)$ or $O_{\mathcal A}^+(L)$, one must also check the
  relevant spinor-norm or positive-cone condition.

## Algorithm 2.2

Assume simultaneously:

- $v_1$ is non-isotropic,
- $v_1^\perp$ is indefinite,
- $\Gamma = O_{\mathcal A}(L)$ for some $\mathcal A \subset O(D(L))$,
- the natural map $O(L) \to O(D(L))$ is surjective.

### Procedure

1. For each $i \in \{1,2\}$:
   - normalize to $w_i := c_i v_i \in L$,
   - reject if $c_1 \neq c_2$ or $v_1^2 \neq v_2^2$,
   - define
     $$
     K_i := w_i^\perp \subset L,
     $$
   - for the natural inclusion
     $$
     \langle w_i \rangle \oplus K_i \subset L \subset L^\vee
     \subset \langle w_i \rangle^\vee \oplus K_i^\vee,
     $$
     define
     $$
     H_i := L / (\langle w_i \rangle \oplus K_i)
     \subset D(\langle w_i \rangle) \oplus D(K_i),
     $$
   - define
     $$
     \iota_i :
     D(L) \xrightarrow{\sim}
     \bigl(D(\langle w_i \rangle) \oplus D(K_i)\bigr) \bmod H_i.
     $$
2. If $K_1 \not\cong K_2$, return $v_1 \not\sim_\Gamma v_2$.
3. Search over
   $$
   \overline{\varphi} \oplus \overline{\psi}
   \in \{\pm 1\} \oplus \operatorname{Iso}(q_{K_1}, q_{K_2}).
   $$
4. If
   $$
   (\overline{\varphi} \oplus \overline{\psi})(H_1) = H_2
   $$
   and
   $$
   \iota_2^{-1} \circ (\overline{\varphi} \oplus \overline{\psi}) \circ \iota_1
   \in \mathcal A,
   $$
   return $v_1 \sim_\Gamma v_2$.
5. Otherwise return $v_1 \not\sim_\Gamma v_2$.

### What changed from Algorithm 2.1

Algorithm 2.1 searches over actual lattice isometries
$$
\psi : K_1 \to K_2.
$$

Algorithm 2.2 replaces that search by finite data:

- the discriminant forms $q_{K_i}$,
- the gluing subgroups $H_i$,
- the allowed image $\mathcal A \subset O(D(L))$.

## Algorithm 2.3

Algorithm 2.3 is Dawes's coordinate form of Algorithm 2.2.

Assume the same hypotheses as Algorithm 2.2.

### Procedure

1. For each $i \in \{1,2\}$:
   - let $c_i \in \mathbb{Q}_{>0}$ be minimal such that $w_i := c_i v_i \in L$,
   - let
     $$
     \alpha_i := \frac{w_i^2}{|w_i^2|}.
     $$
2. Reject if $v_1^2 \neq v_2^2$ or $c_1 \neq c_2$.
3. For each $i \in \{1,2\}$:
   - compute $(q_1|\cdots|q_n) := Q(\hat w_i)$,
   - define
     $$
     K_i := \langle k_{ij} \mid j = 1,\dots,n-1 \rangle
     \quad\text{with}\quad
     k_{ij} = q_{j+1},
     $$
   - compute the Smith normal form
     $$
     [d_1,\dots,d_n]_{n,n} := P(G(K_i))\,G(K_i)\,Q(G(K_i)),
     $$
     and identify
     $$
     D(K_i) \cong \bigoplus_j C_{d_j},
     $$
   - define explicit dual representatives
     $$
     f_{il} := \frac{1}{d_k}\sum_{j=1}^n q_{jl}k_{il},
     $$
   - define
     $$
     \theta_{i1} := (w_i|k_{i1}|\dots|k_{in}), \quad
     \theta_{i2} := (w_i^2)\oplus G(K_i),
     $$
     $$
     \theta_{i3} := (\alpha_i \underline e_1|f_{i1}|\dots|f_{i(n-1)}),
     \quad
     \lambda_i := \theta_{i3}\circ\theta_{i2}\circ\theta_{i1}^{-1}.
     $$
4. If $K_1 \not\cong K_2$, return $v_1 \not\sim_\Gamma v_2$.
5. For each $i \in \{1,2\}$:
   - let $H_i$ be the subgroup of
     $D(\langle w_i\rangle)\oplus D(K_i)$ generated by the columns of $\lambda_i$,
   - let
     $$
     \iota_i := \lambda_i \circ G(L)^{-1}.
     $$
6. Search over
   $$
   \overline{\varphi} \oplus \overline{\psi}
   \in \{\pm 1\} \oplus \operatorname{Iso}(q_{K_1}, q_{K_2}).
   $$
7. If
   $$
   (\overline{\varphi} \oplus \overline{\psi})(H_1) = H_2
   $$
   and
   $$
   \theta := \iota_2^{-1} \circ
   (\overline{\varphi} \oplus \overline{\psi}) \circ \iota_1 \bmod L
   \in \mathcal A,
   $$
   return $v_1 \sim_\Gamma v_2$.
8. Otherwise return $v_1 \not\sim_\Gamma v_2$.

### Role of Algorithm 2.3

Algorithm 2.3 is the implementation-ready form of Algorithm 2.2.
Its purpose is to replace the abstract gluing and discriminant-form constructions of
Algorithm 2.2 by explicit coordinate formulas.

## Supporting Results Used by Algorithms 2.2-2.3

### Theorem 2.3

If a discriminant form $q$ satisfies:

1. $t_+ \ge 1$, $t_- \ge 1$, and $t_+ + t_- \ge 3$;
2. $t_+ + t_- \ge 2 + l(q)$,

then there exists a lattice $L$ of signature $(t_+, t_-)$ with $q_L = q$.
Moreover:

- the natural map $O(L) \to O(D(L))$ is surjective;
- the genus of $L$ contains a single class.

This is the criterion Dawes uses to identify indefinite lattices from signature plus
discriminant form and to justify the surjectivity hypothesis in many examples.

### Lemma 2.4

In the notation of Algorithm 2.3, if $K_1$ represents both $\pm 2$, then
$$
v_1 \sim_{O_{\mathcal A}(L)} v_2
\quad\Longleftrightarrow\quad
v_1 \sim_{SO_{\mathcal A}^+(L)} v_2.
$$

This is the mechanism Dawes uses to pass from $O_{\mathcal A}(L)$-equivalence to
$SO_{\mathcal A}^+(L)$-equivalence without a separate spinor-norm computation.

### Lemma 2.5

Let $K$ be an indefinite lattice with discriminant form $q_K$ and signature
$(t_+, t_-)$.
If $S := \langle \pm 2 \rangle$ and $\delta$ is one of:

1. $\delta = q_S \oplus (-q_K)$;
2. $\delta = ((q_S \oplus (-q_K)) \mid \Gamma_\gamma^\perp)/\Gamma_\gamma$,

and if:

- $K$ is unique in its genus,
- there exists a lattice of signature $(t_+, t_-)$ with discriminant form $-\delta$,

then $S \subset K$.

Dawes uses this together with Theorem 2.3 to prove that $K$ represents $\pm 2$, which is
the input needed for Lemma 2.4.

## Bottom Line

Dawes gives one general algorithm and then two stricter specializations:

- **Algorithm 2.1** handles the definite-complement case for arbitrary
  $\Gamma \subset O(L)$.
- **Algorithm 2.2** handles a narrower indefinite-complement case under explicit
  discriminant-form and surjectivity hypotheses.
- **Algorithm 2.3** is the coordinate implementation of Algorithm 2.2.

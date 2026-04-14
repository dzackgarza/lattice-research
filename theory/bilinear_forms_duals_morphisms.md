# Bilinear Forms, Duals, and Morphisms

## Dual Basis and Adjoint Map

Assume $L$ is finite free over $R$, with basis $(e_1,\dots,e_n)$. Then $L^* =
\operatorname{Hom}_R(L,R)$ has the dual basis $(e_1^*,\dots,e_n^*)$, characterized by

$$ e_i^*(e_j) = \delta_{ij}. $$

Also $L_K = L \otimes_R K$ has basis $(e_1 \otimes 1,\dots,e_n \otimes 1)$.

Now define the adjoint map

$$ \operatorname{ad}_\beta: L \to L^*, \qquad v \mapsto \beta(v,-). $$

This requires no nondegeneracy.

For any $v \in L$, since $(e_i^*)$ is a basis of $L^*$, we can expand the functional
$\beta(v,-)$ uniquely as

$$ \beta(v,-) = \sum_{i=1}^n c_i(v) e_i^*. $$

The coefficients are determined by evaluation on the basis vectors $e_j$. But here it is
even more direct: because $e_i^*(e_j) = \delta_{ij}$, the coefficient of $e_i^*$ is
exactly the value of the functional on $e_i$. So

$$ c_i(v) = \beta(v,e_i). $$

Hence the actual abstract identity is

$$ \operatorname{ad}*\beta(v) = \sum*{i=1}^n \beta(v,e_i) e_i^*. $$

That is the clean formula, with no matrix language yet.

Now write

$$ v = \sum_{j=1}^n a_j e_j. $$

Then bilinearity gives

$$ \beta(v,e_i) = \sum_{j=1}^n a_j \beta(e_j,e_i), $$

so

$$ \operatorname{ad}*\beta(v) = \sum*{i=1}^n \left( \sum_{j=1}^n a_j \beta(e_j,e_i)
\right) e_i^*. $$

Only at this point do you extract a matrix.

If you define the Gram coefficients by

$$ G_{ij} := \beta(e_j,e_i), $$

then the matrix of $\operatorname{ad}_\beta: L \to L^*$ in the basis $e_j$ of $L$ and
$e_i^*$ of $L^*$ is exactly $G$.

If instead you use the more common convention

$$ \widetilde G_{ij} := \beta(e_i,e_j), $$

then the matrix of $\operatorname{ad}_\beta$ is $\widetilde G^{\,t}$.

So the "transpose issue" is purely a convention about how you index the Gram matrix.
The underlying morphism is always

$$ v \longmapsto \sum_i \beta(v,e_i) e_i^*. $$

That is the correct abstract statement.

## Dual Lattice Map

The same style applies to the map

$$ \lambda: L^\# \to L^*, \qquad x \mapsto \bigl( w \mapsto \beta_K(x,w \otimes 1)
\bigr). $$

Namely, for $x \in L^\#$,

$$ \lambda(x) = \sum_{i=1}^n \beta_K(x, e_i \otimes 1) e_i^*. $$

Again: first the abstract expansion in the dual basis, then matrix language only
afterward.

## Summary

The correct formulation is: $G$ represents the map $L \to L^*$, and the reason its
entries are the $\beta(e_j,e_i)$ is exactly that

$$ \operatorname{ad}_\beta(e_j) = \sum_i \beta(e_j,e_i) e_i^*. $$

That is the whole coordinate computation, done correctly.

## The Complete Diagram

The right way to express everything is with the single diagram:

$$ \begin{array}{ccccc} && L && \\
& \swarrow_{\operatorname{ad}_\beta} & \downarrow_i & \searrow^{j} & \\
L^* & \xleftarrow{\ \lambda\ } & L^\# & \xrightarrow{\ \iota\ } & L_K \end{array} $$

with

$$ j = \iota \circ i, \qquad \operatorname{ad}_\beta = \lambda \circ i. $$

Everything here is abstract.

## Choosing Bases and Defining the Matrix $G$

Now choose a basis $(e_1,\dots,e_n)$ of $L$, and let $(e_1^*,\dots,e_n^*)$ be the dual
basis of $L^*$. Do **not** define $G$ as a matrix of numbers first.
Define it as:

$$ G := [\operatorname{ad}*\beta]*{(e_j) \to (e_i^*)}. $$

So $G$ is the matrix representing the morphism $\operatorname{ad}_\beta: L \to L^*$.

If $\lambda: L^\# \to L^*$ is an isomorphism, for example in the usual nondegenerate
finite free situation, define elements $(f_1,\dots,f_n \in L^\#)$ by

$$ \lambda(f_i) = e_i^*. $$

This gives a basis of $L^\#$.

Also $L_K$ has the basis $(e_1 \otimes 1,\dots,e_n \otimes 1)$.

Now the matrices of the five arrows are:

- $[j]_{(e_j) \to (e_j \otimes 1)} = I$
- $[\lambda]_{(f_j) \to (e_i^*)} = I$
- $[\operatorname{ad}*\beta]*{(e_j) \to (e_i^*)} = G$
- $[i]_{(e_j) \to (f_i)} = G$
- $[\iota]_{(f_j) \to (e_i \otimes 1)} = G^{-1}$

And these are forced by the commutative diagram:

From $\operatorname{ad}_\beta = \lambda \circ i$, we get $G = I \cdot [i]$, so $[i] =
G$.

From $j = \iota \circ i$, we get $I = [\iota] \cdot G$, so $[\iota] = G^{-1}$.

That is the clean abstract meaning of "$G$" and "$G^{-1}$" in this picture:

- **$G$** is the matrix of the morphism $L \to L^*$, and equally of $L \to L^\#$ once
  $L^\#$ is based via $\lambda$.
- **$G^{-1}$** is the matrix of the inclusion $L^\# \hookrightarrow L_K$ in those chosen
  bases.
- **$G^{-1}$** is **not** defining $L^\#$; it is only the matrix of that inclusion after
  the basis of $L^\#$ has been chosen through $\lambda^{-1}(e_i^*)$.

One should not write things like $G^t x \in R^n$ unless one has already fixed
identifications with free coordinate modules.
The invariant content is in the morphisms; the matrices come only afterward.

## The Non-Isomorphic Case

The one caveat is that none of the $G^{-1}$ language exists unless $\lambda$ is an
isomorphism. Without that, the diagram still exists, but there is no basis of $L^\#$
induced from $L^*$, and no inverse matrix to discuss.

## Categorical Formulation: Fibered Categories over $R$-Alg

The mistake in naive formulations is treating everything as though it already lived in
one ambient module category.
It does not.
The objects live over varying coefficient rings, so the right framework is a
category fibered over $R$-Alg, or equivalently a pseudofunctor

$$ S \longmapsto \mathrm{BilForm}(S), $$

where $\mathrm{BilForm}(S)$ is the category of $S$-modules equipped with $S$-valued
$S$-bilinear forms.

### Definition for a Fixed Base Ring

Concretely, for a fixed $R$-algebra $S$, an object is $(L, b)$ with $L \in S$-Mod and
$b: L \otimes_S L \to S$ an $S$-module morphism.

### Base Change and Morphisms

Now let $g: S_1 \to S_2$ be a morphism in $R$-Alg.
As usual, $g$ gives a base-change functor

$$ G = g_* := S_2 \otimes_{S_1}(-): S_1\text{-Mod} \to S_2\text{-Mod}. $$

So the right notion of morphism $(L_1, b_1) \to (L_2, b_2)$ lying over $g$ is not
directly a square between $L_1 \otimes_{S_1} L_1$ and $L_2 \otimes_{S_2} L_2$, because
those live in different categories.
The correct datum is an $S_2$-module morphism

$$ \varphi: S_2 \otimes_{S_1} L_1 \to L_2 $$

such that the following diagram in the single category $S_2$-Mod commutes:

$$ \begin{array}{ccc} (S_2 \otimes_{S_1} L_1) \otimes_{S_2} (S_2 \otimes_{S_1} L_1) &
\xrightarrow{\ \varphi\otimes\varphi\ } & L_2\otimes_{S_2}L_2\\
\downarrow & & \downarrow b_2\\
S_2\otimes_{S_1}(L_1\otimes_{S_1}L_1) & \xrightarrow{\ S_2\otimes b_1\ } &
S_2\otimes_{S_1}S_1\cong S_2 \end{array} $$

where the left vertical arrow is the canonical associativity/base-change isomorphism.

That is the honest one-category statement.

### Unpacking to Semilinear Maps

Now, if you unpack $\varphi$, it is equivalent by adjunction to an $R$-linear map $f:
L_1 \to L_2$ satisfying

$$ f(sx) = g(s)f(x) \qquad (s\in S_1, x\in L_1), $$

so $f$ is $g$-semilinear.
In those terms, the commutative diagram above becomes exactly

$$ b_2(fx,fy) = g\!\left(b_1(x,y)\right).
$$

### Summary: Clean Categorical Definition

The correction is right in two ways:

1. One should not say "restrict scalars and draw a square" unless one has explicitly
   chosen to work in $R$-Mod.
   The more natural formulation is to work in the target category $S_2$-Mod after
   applying the base-change functor determined by $g$.

2. The object really is not just an $R$-module with an $R$-bilinear map.
   It is an $R$-module together with an $S$-module structure and an $S$-bilinear form
   $b\in\operatorname{Hom}_S(L\otimes_SL,S)$.

**Clean definition:**

- **Objects over $S$**: pairs $(L,b)$ with $L\in S$-Mod and $b:L\otimes_SL\to S$ in
  $S$-Mod;
- **Morphisms over $g:S_1\to S_2$**: maps $\varphi:S_2\otimes_{S_1}L_1\to L_2$ in
  $S_2$-Mod making the base-changed form diagram commute.

That is the precise categorical version of what was described above.

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

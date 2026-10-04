---
tags: [convex-optimization, topic, ml-notebook, background]
source: ML notebook "Graphs"; Boyd & Vandenberghe §2.2.5, App. A.5
---
# Positive Semidefinite Matrices
Back to [Index](../Index.md) · ML notebook

## Spectral theorem
If $A = A^{\top}$ is real, its eigenvalues are real and
$$
A = Q\Lambda Q^{\top}, \qquad Q \text{ orthonormal (a rotation)},\ \Lambda \text{ diagonal of eigenvalues.}
$$

## Equivalent conditions for $A \succeq 0$
From the notebook:
1. $x^{\top}Ax \ge 0$ for all $x \in \R^n$.
2. All eigenvalues are nonnegative.
3. $A = B^{\top}B$ for some matrix $B$.
4. All principal minors of $A$ are nonnegative.

For $A \succ 0$ (positive definite), make each inequality strict and $B$ nonsingular.

## Where it shows up
- **Convexity test:** $f$ is convex iff $\nabla^2 f \succeq 0$.
- **Covariance** $\Sigma = \E[(x - \bar x)(x - \bar x)^{\top}] \succeq 0$, so $x^{\top}\Sigma x$ in Markowitz is convex.
- **Graph Laplacian:** $L_G = B^{\top}B \succeq 0$ (see [Laplacian of a Graph](../../graph-theory/Theory/Laplacian%20of%20a%20Graph.md)).
- **Regularized Laplacian:** $L_G + \tau\big(I - \tfrac1n J\big) \succeq 0$, and $D + \tau I \succ 0$, so $(D + \tau I)^{-1/2}$ exists even with isolated vertices (see [Regularized Spectral Clustering](../../graph-theory/Theory/Regularized%20Spectral%20Clustering.md)).
- $\Spsd{n}$ is a convex cone.

See also: [Second-Order Conditions](Second-Order%20Conditions.md), [Important Convex Sets](Important%20Convex%20Sets.md), [Sparsest Cut as a Spectral Relaxation](Sparsest%20Cut%20as%20a%20Spectral%20Relaxation.md)

---
tags: [convex-optimization, topic, ml-notebook, background]
source: ML notebook "Graphs"; Boyd & Vandenberghe §2.2.5, App. A.5
---
# Positive Semidefinite Matrices
Back to [[self-study/convex-optimization/Index|Index]] · ML notebook

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
- **Graph Laplacian:** $L_G \succeq 0$.
- $\Spsd{n}$ is a convex cone.

See also: [[Second-Order Conditions]], [[Important Convex Sets]], [[Graph Laplacian]]

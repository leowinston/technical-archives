---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, Ch. 3 introduction and §3.1
---
# Line Search Methods
Back to [Index](../Index.md) · Nocedal & Wright Ch. 3

Choose a direction, then decide how far to go along it.
$$
x_{k+1} = x_k + \alpha_k\,p_k
$$
$p_k$ is the **search direction** and $\alpha_k > 0$ the **step length**.

## Descent directions
$p_k$ is a descent direction if $p_k^{\top}\nabla f_k < 0$. Then $f$ decreases for small enough steps along it.

Most methods use
$$
\boxed{\,p_k = -B_k^{-1}\,\nabla f_k\,}
$$
with $B_k$ symmetric. If $B_k$ is [positive definite](../ml-notebook/Positive%20Semidefinite%20Matrices.md) then $p_k^{\top}\nabla f_k = -\nabla f_k^{\top}B_k^{-1}\nabla f_k < 0$, so $p_k$ is a descent direction.

| $B_k$ | Method | Rate |
|---|---|---|
| $I$ | steepest descent | [linear](Convergence%20Rate%20of%20Steepest%20Descent.md) |
| approximation to $\nabla^2 f_k$, updated by a low-rank formula | [quasi-Newton](Quasi-Newton%20Methods%20and%20Superlinear%20Convergence.md) | superlinear |
| $\nabla^2 f_k$ | [Newton](Newton's%20Method%20for%20Optimization.md) | quadratic |

## The step length is a 1-D problem
$$
\phi(\alpha) = f(x_k + \alpha\,p_k), \qquad \alpha > 0
$$
The ideal $\alpha_k$ minimizes $\phi$, which is exactly [univariate minimization](../../../academic/math-315/Topics%204/Univariate%20Minimization.md). But finding that minimizer accurately costs too many evaluations of $f$ and $\nabla f$ at every single iteration.

So practical methods do an **inexact line search**: accept any $\alpha$ that reduces $f$ enough, as defined by the [Wolfe Conditions](Wolfe%20Conditions.md), found by the procedure in [Step-Length Selection](Step-Length%20Selection.md).

## The alternative
[Trust-Region Methods](Trust-Region%20Methods.md) choose the size of the step first and the direction second.

See also: [Zoutendijk's Theorem](Zoutendijk's%20Theorem.md) for why this converges, [Least Squares by Gradient Descent](../ml-notebook/Least%20Squares%20by%20Gradient%20Descent.md)

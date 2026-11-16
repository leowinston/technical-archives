---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §10.3, Theorem 10.1
---
# Gauss-Newton Method
Back to [Index](../Index.md) · Nocedal & Wright §10.3

[Newton's method](Newton's%20Method%20for%20Optimization.md) for nonlinear least squares, with the expensive part of the Hessian thrown away.

## Problem
$$
\min_x\; f(x) = \tfrac12\sum_{j=1}^{m}r_j(x)^2 = \tfrac12\lVert r(x)\rVert_2^2
$$
With the Jacobian $J(x) = [\partial r_j/\partial x_i]$:
$$
\nabla f = J^{\top}r, \qquad \nabla^2 f = J^{\top}J + \sum_{j}r_j\,\nabla^2 r_j
$$
The first term of the Hessian comes for free once $J$ is known.

## The step
Drop the second term:
$$
\boxed{\,J_k^{\top}J_k\;p_k^{GN} = -J_k^{\top}r_k\,}
$$
These are the [normal equations](../../../academic/math-315/Topics%202/Normal%20Equations.md) of the **linear** least-squares problem
$$
\min_p\; \tfrac12\lVert J_k\,p + r_k\rVert_2^2
$$
so each iteration linearizes the residual and solves a linear fit. Solve it by [QR](../../../academic/math-315/Topics%202/Least%20Squares%20via%20QR.md) rather than forming $J^{\top}J$, which [squares the condition number](../../../academic/math-315/Topics%202/Conditioning%20of%20the%20Normal%20Equations.md).

## Why it works
- No second derivatives of the $r_j$ are needed.
- If $J_k$ has full rank and $\nabla f_k \neq 0$, then $p_k^{GN}$ is a [descent direction](Line%20Search%20Methods.md): $(p^{GN})^{\top}\nabla f = -\lVert J\,p^{GN}\rVert^2 < 0$.
- With a Wolfe line search and singular values of $J$ bounded away from zero, $J_k^{\top}r_k \to 0$.

## Rate
The dropped term is $\sum r_j\nabla^2 r_j$.
- **Zero residual** at the solution, $r(x^*) = 0$: the dropped term vanishes and convergence is quadratic, like Newton.
- **Small residuals** or nearly linear $r_j$: fast linear convergence.
- **Large residuals:** the approximation is poor and convergence can be slow.

## Weakness
If $J_k$ is rank deficient, $J^{\top}J$ is singular and the step is not well defined. [Levenberg-Marquardt](Levenberg-Marquardt%20Method.md) repairs this.

See also: [Least-Squares and Linear Programming](../1-introduction/Least-Squares%20and%20Linear%20Programming.md), [Maximum Likelihood Estimation](../ml-notebook/Maximum%20Likelihood%20Estimation.md)

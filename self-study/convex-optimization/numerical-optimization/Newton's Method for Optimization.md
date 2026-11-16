---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §3.3, Theorem 3.5
---
# Newton's Method for Optimization
Back to [Index](../Index.md) · Nocedal & Wright §3.3

[Newton's method for roots](../../../academic/math-315/Topics%204/Newton's%20Method.md) applied to the equation $\nabla f(x) = 0$.

## The step
$$
\boxed{\,\nabla^2 f_k\;p_k^{N} = -\nabla f_k\,}, \qquad x_{k+1} = x_k + p_k^{N}
$$
In one dimension this is $x_{k+1} = x_k - f'(x_k)/f''(x_k)$. The [Hessian](../ml-notebook/Gradient,%20Jacobian,%20and%20Hessian.md) plays the role of the derivative, and a linear solve replaces the division.

Equivalently, $p_k^{N}$ minimizes the quadratic model
$$
m_k(p) = f_k + \nabla f_k^{\top}p + \tfrac12p^{\top}\nabla^2 f_k\,p
$$

## Local convergence
**Theorem.** Suppose $\nabla^2 f$ is Lipschitz continuous near $x^*$, where $\nabla f(x^*) = 0$ and $\nabla^2 f(x^*)$ is positive definite. If $x_0$ is close enough to $x^*$:
1. $x_k \to x^*$;
2. the convergence is **quadratic**, $\lVert x_{k+1} - x^*\rVert \le C\,\lVert x_k - x^*\rVert^2$;
3. $\lVert\nabla f_k\rVert \to 0$ quadratically.

Near the solution the unit step $\alpha = 1$ satisfies the [Wolfe Conditions](Wolfe%20Conditions.md), so a line search does not get in the way.

## Why it beats steepest descent
The step is invariant under linear changes of variables, so the [condition number](Convergence%20Rate%20of%20Steepest%20Descent.md) of the Hessian does not slow it down. On a strictly convex quadratic it lands on $x^*$ in one step.

## Costs
- Forming $\nabla^2 f_k$ and solving an $n \times n$ system each iteration, usually by [Cholesky](../../../academic/math-315/Topics%201/Cholesky%20Factorization.md): $O(n^3)$.
- **Local only.** Far from $x^*$ the Hessian may not be positive definite, and then $p_k^{N}$ may not be a descent direction or may not exist. See [Newton's Method with Hessian Modification](Newton's%20Method%20with%20Hessian%20Modification.md) and [Trust-Region Methods](Trust-Region%20Methods.md).

See also: [Second-Order Conditions](../3-convex-functions/Second-Order%20Conditions.md), [Quasi-Newton Methods and Superlinear Convergence](Quasi-Newton%20Methods%20and%20Superlinear%20Convergence.md), [Gauss-Newton Method](Gauss-Newton%20Method.md)

---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, Ch. 4 introduction, Algorithm 4.1, Theorem 4.1
---
# Trust-Region Methods
Back to [Index](../Index.md) · Nocedal & Wright Ch. 4

[Line search](Line%20Search%20Methods.md) picks a direction, then a length. A trust-region method picks a maximum length, then the best step within it.

## Subproblem
$$
\min_{p}\; m_k(p) = f_k + g_k^{\top}p + \tfrac12p^{\top}B_k\,p \qquad \text{subject to}\qquad \lVert p\rVert \le \Delta_k
$$
$g_k = \nabla f_k$, and $B_k$ is the Hessian or an approximation. $\Delta_k$ is the radius within which the model is trusted. $B_k$ does not need to be positive definite, because the constraint keeps the problem bounded.

## Is the model any good?
$$
\rho_k = \frac{f(x_k) - f(x_k + p_k)}{m_k(0) - m_k(p_k)} = \frac{\text{actual reduction}}{\text{predicted reduction}}
$$

| $\rho_k$ | Meaning | Radius |
|---|---|---|
| $< \tfrac14$ | poor prediction | shrink: $\Delta_{k+1} = \tfrac14\Delta_k$ |
| $> \tfrac34$ and $\lVert p_k\rVert = \Delta_k$ | good, and the boundary was limiting | expand: $\Delta_{k+1} = \min(2\Delta_k, \hat\Delta)$ |
| otherwise | acceptable | keep |

Accept the step, $x_{k+1} = x_k + p_k$, only if $\rho_k > \eta$ for a fixed $\eta \in [0, \tfrac14)$. Otherwise stay put and retry with the smaller radius.

## The exact solution
$p^*$ solves the subproblem if and only if there is $\lambda \ge 0$ with
$$
\boxed{\,(B + \lambda I)\,p^* = -g, \qquad \lambda\,(\Delta - \lVert p^*\rVert) = 0, \qquad B + \lambda I \succeq 0\,}
$$
- Inside the region, $\lambda = 0$ and $p^*$ is the [Newton step](Newton's%20Method%20for%20Optimization.md).
- On the boundary, $\lambda > 0$ and the step is a Newton step for a [shifted Hessian](Newton's%20Method%20with%20Hessian%20Modification.md).

As $\Delta$ shrinks, the step turns from the Newton direction toward steepest descent, so the direction changes with the radius.

## Solving it approximately
Exactness is not needed. Any step that reduces the model at least as much as [The Cauchy Point](The%20Cauchy%20Point.md) gives global convergence.

See also: [Levenberg-Marquardt Method](Levenberg-Marquardt%20Method.md), the trust-region method for least squares

---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §3.2, Theorem 3.2
---
# Zoutendijk's Theorem
Back to [Index](../Index.md) · Nocedal & Wright §3.2

The global convergence result for [line search methods](Line%20Search%20Methods.md). It says how far a direction may stray from steepest descent.

## The angle
$$
\cos\theta_k = \frac{-\nabla f_k^{\top}p_k}{\lVert\nabla f_k\rVert\,\lVert p_k\rVert}
$$
$\theta_k$ is the angle between $p_k$ and the steepest descent direction $-\nabla f_k$.

## Theorem
Suppose $f$ is bounded below, $\nabla f$ is Lipschitz continuous on the region containing the level set of $x_0$, every $p_k$ is a descent direction, and every $\alpha_k$ satisfies the [Wolfe Conditions](Wolfe%20Conditions.md). Then
$$
\boxed{\,\sum_{k \ge 0}\cos^2\theta_k\,\lVert\nabla f_k\rVert^2 < \infty\,}
$$

## Why
The curvature condition plus Lipschitz continuity bound the step from below: $\alpha_k \ge \dfrac{c_2 - 1}{L}\dfrac{\nabla f_k^{\top}p_k}{\lVert p_k\rVert^2}$. Put that into the Armijo condition to get $f_{k+1} \le f_k - c\,\cos^2\theta_k\,\lVert\nabla f_k\rVert^2$. Sum over $k$: the left side is bounded below, so the sum on the right is finite.

## Consequence
If the directions stay bounded away from orthogonal to the gradient, $\cos\theta_k \ge \delta > 0$, then
$$
\lim_{k\to\infty}\lVert\nabla f_k\rVert = 0
$$
from **any** starting point.
- **Steepest descent:** $\cos\theta_k = 1$.
- **Newton-like**, $p_k = -B_k^{-1}\nabla f_k$ with $B_k$ positive definite and [condition number](../../../academic/math-315/Topics%201/Condition%20Number.md) $\kappa(B_k) \le M$: $\cos\theta_k \ge 1/M$.

## What it does not say
Convergence is to a stationary point, not necessarily a minimizer, and it says nothing about speed. For convex $f$ a stationary point is a [global minimizer](../4-convex-problems/Local%20and%20Global%20Optima.md).

See also: [Convergence Rate of Steepest Descent](Convergence%20Rate%20of%20Steepest%20Descent.md), [Newton's Method with Hessian Modification](Newton's%20Method%20with%20Hessian%20Modification.md)

---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §4.1, Algorithm 4.2
---
# The Cauchy Point
Back to [Index](../Index.md) · Nocedal & Wright §4.1

The cheapest acceptable solution of the [trust-region](Trust-Region%20Methods.md) subproblem: go downhill along the gradient until the model stops decreasing or the boundary is reached.

## Definition
1. Minimize the linear model within the region: $p_k^{s} = -\dfrac{\Delta_k}{\lVert g_k\rVert}\,g_k$.
2. Minimize the quadratic model $m_k(\tau p_k^{s})$ over $\tau \in [0, 1]$.

## Closed form
$$
\boxed{\,p_k^{C} = -\tau_k\,\frac{\Delta_k}{\lVert g_k\rVert}\,g_k, \qquad
\tau_k = \begin{cases} 1, & g_k^{\top}B_k\,g_k \le 0 \\[4pt] \min\!\left(\dfrac{\lVert g_k\rVert^{3}}{\Delta_k\,g_k^{\top}B_k\,g_k},\ 1\right), & \text{otherwise} \end{cases}\,}
$$
- Negative curvature along $-g_k$: the model keeps falling, so go to the boundary.
- Positive curvature: the model is a convex parabola in $\tau$. Take its minimizer, or the boundary if that comes first.

## Why it matters
It costs one matrix-vector product and no linear solve, and it is the benchmark: a step $p_k$ gives global convergence if it reduces the model by at least a fixed fraction of what the Cauchy point achieves,
$$
m_k(0) - m_k(p_k) \ge c_1\,\lVert g_k\rVert\,\min\!\left(\Delta_k,\ \frac{\lVert g_k\rVert}{\lVert B_k\rVert}\right)
$$

## Why it is not enough
Always taking the Cauchy point is steepest descent with a particular step length, so it inherits the [slow linear rate](Convergence%20Rate%20of%20Steepest%20Descent.md). Better methods start from it and move toward the Newton step:
- **Dogleg:** follow the path from the steepest descent minimizer to the Newton point until it leaves the region.
- **Two-dimensional subspace minimization:** minimize the model over the span of $g_k$ and $B_k^{-1}g_k$.
- **Steihaug's conjugate gradient:** its first iterate is the Cauchy point.

See also: [Line Search Methods](Line%20Search%20Methods.md), [Newton's Method for Optimization](Newton's%20Method%20for%20Optimization.md)

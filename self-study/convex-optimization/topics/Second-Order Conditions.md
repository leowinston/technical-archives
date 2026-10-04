---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.1.4 (p. 71)
---
# Second-Order Conditions
Back to [Index](../Index.md) · Section 3.1.4

> [!important] ✎ Highlighted section heading

For twice differentiable $f$ with convex open $\dom f$:
$$
\boxed{\,f \text{ convex} \iff \nabla^{2} f(x) \succeq 0 \ \ \forall x \in \dom f\,}
$$
On $\R$ this is $f''(x) \ge 0$: the derivative is nondecreasing, the graph curves up.

- $\nabla^2 f \succ 0$ everywhere $\Rightarrow$ strictly convex. The converse fails: $f(x) = x^4$ is strictly convex but $f''(0) = 0$.
- $\dom f$ **must** be convex. $f(x) = 1/x^2$ on $x \ne 0$ has $f'' > 0$ but is not convex.

## Quadratic example
$f(x) = \tfrac12 x^{\top}Px + q^{\top}x + r$ has $\nabla^2 f = P$, so it is convex iff $P \succeq 0$.

## Explorations
- [EX02 - Checking Convexity with the Hessian](../explorations/EX02%20-%20Checking%20Convexity%20with%20the%20Hessian.md)

See also: [Gradient, Jacobian, and Hessian](Gradient%2C%20Jacobian%2C%20and%20Hessian.md), [Positive Semidefinite Matrices](Positive%20Semidefinite%20Matrices.md)

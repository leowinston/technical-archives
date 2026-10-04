---
tags: [convex-optimization, topic, ch-4]
source: Boyd & Vandenberghe §4.2.3 (pp. 139–142)
---
# Optimality Criterion for Differentiable Objectives
Back to [Index](../Index.md) · Section 4.2.3

For convex, differentiable $f_0$ and feasible set $X$:
$$
\boxed{\,x \text{ optimal} \iff x \in X \ \text{and}\ \nabla f_0(x)^{\top}(y - x) \ge 0 \ \ \forall y \in X\,}
$$
If $\nabla f_0(x) \ne 0$, then $-\nabla f_0(x)$ is the normal of a supporting hyperplane to $X$ at $x$.

## Special cases
| Problem | Condition |
|---|---|
| unconstrained | $\nabla f_0(x) = 0$ |
| $Ax = b$ only | $\nabla f_0(x) + A^{\top}\nu = 0$ for some $\nu$ |
| $x \succeq 0$ | $x \succeq 0$, $\nabla f_0(x) \succeq 0$, $x_i\,(\nabla f_0(x))_i = 0$ |

The last row is a first look at **complementary slackness**.

## Example
Unconstrained QP $f_0 = \tfrac12 x^{\top}Px + q^{\top}x$, $P \succeq 0$: optimal iff $Px^\star + q = 0$.

## Explorations
- [EX07 - Markowitz Three-Asset Portfolio](../explorations/EX07%20-%20Markowitz%20Three-Asset%20Portfolio.md)

See also: [First-Order Condition](First-Order%20Condition.md), [Local and Global Optima](Local%20and%20Global%20Optima.md)

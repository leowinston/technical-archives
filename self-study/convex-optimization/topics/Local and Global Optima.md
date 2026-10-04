---
tags: [convex-optimization, topic, ch-4]
source: Boyd & Vandenberghe §4.2.2 (p. 138)
---
# Local and Global Optima
Back to [Index](../Index.md) · Section 4.2.2

> [!important] ✎ Highlighted
> A fundamental property of convex optimization problems is that **any locally optimal point is also (globally) optimal.**

## Proof (by contradiction)
Suppose $x$ is locally optimal on a ball of radius $R$, but some feasible $y$ has $f_0(y) < f_0(x)$. Then $\lVert y - x\rVert_2 > R$. Step toward $y$:
$$
z = (1 - \theta)x + \theta y, \qquad \theta = \frac{R}{2\lVert y - x\rVert_2}.
$$
- $z$ is feasible (the feasible set is convex) and $\lVert z - x\rVert_2 = R/2$.
- By convexity, $f_0(z) \le (1-\theta)f_0(x) + \theta f_0(y) < f_0(x)$.

This contradicts local optimality.

## Why it matters
Any descent method that stops at a local minimum has found the global one. Nonconvex problems give no such guarantee.

## Explorations
- [EX06 - Local Versus Global Minima](../explorations/EX06%20-%20Local%20Versus%20Global%20Minima.md)

See also: [Convex Optimization Problems](Convex%20Optimization%20Problems.md), [First-Order Condition](First-Order%20Condition.md)

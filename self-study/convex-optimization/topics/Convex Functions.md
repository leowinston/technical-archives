---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.1.1–3.1.2 (pp. 67–68)
---
# Convex Functions
Back to [Index](../Index.md) · Section 3.1.1

## Definition
$f : \R^n \to \R$ is convex if $\dom f$ is a ✎ **convex** set and for all $x, y \in \dom f$, $0 \le \theta \le 1$:
$$
\boxed{\,f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta) f(y)\,}
$$
The chord from $(x, f(x))$ to $(y, f(y))$ lies above the graph.

- **Strictly convex:** strict $<$ for $x \ne y$, $0 < \theta < 1$.
- ✎ **Concave:** $-f$ is convex. Affine functions are both convex and concave.

## Restriction to a line
$f$ is convex iff $g(t) = f(x + tv)$ is convex on $\{t \mid x + tv \in \dom f\}$ for every $x, v$. This reduces many checks to one variable.

## Extended-value extension
Set $\tilde f(x) = \infty$ off $\dom f$. Then convexity is just the inequality above on all of $\R^n$, and $\min_C f$ equals $\min \big(f + I_C\big)$ with the indicator $I_C$.

See also: [First-Order Condition](First-Order%20Condition.md), [Second-Order Conditions](Second-Order%20Conditions.md), [Examples of Convex Functions](Examples%20of%20Convex%20Functions.md)

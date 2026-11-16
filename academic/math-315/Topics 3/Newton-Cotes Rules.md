---
tags: [math-315, topic, chapter-5]
---
# Newton-Cotes Rules
Back to [Index](../Index.md) · Section 5.2.2 (textbook)

Newton-Cotes rules are [interpolatory rules](Quadrature%20Rules.md) on **equally spaced** points $x_i = a + ih$, $h = \tfrac{b-a}{N}$.

## Closed and open
- **Closed** $(N+1)$-point: uses $x_0, \dots, x_N$, including both endpoints.
- **Open** $(N-1)$-point: uses $x_1, \dots, x_{N-1}$, excluding the endpoints.

| Rule | Type | Weights on $[-1, 1]$ | DOP |
|---|---|---|---|
| Midpoint | open, 1 point | $2$ | 1 |
| Trapezoidal | closed, 2 points | $1, 1$ | 1 |
| [Simpson](Simpson%27s%20Rule.md) | closed, 3 points | $\tfrac13, \tfrac43, \tfrac13$ | 3 |
| Weddle ($\tfrac38$ rule) | closed, 4 points | $\tfrac14, \tfrac34, \tfrac34, \tfrac14$ | 3 |

## Superconvergence
A rule with an **odd** number of points is exact for one degree more than its interpolant: midpoint integrates lines, Simpson integrates cubics. The extra degree comes from symmetry. $f - q$ is not zero, but it integrates to zero.

## Why not many points
- $I(f) - R(f) = I(f - q)$, and equally spaced high-degree interpolants can be wild ([Runge](../Topics%202/Interpolation%20Error.md)).
- For large $N$ the weights **oscillate in sign**, which causes [cancellation](../Topics%201/Cancellation%20Error.md).

Use low-order rules in [composite](Midpoint%20and%20Trapezoidal%20Rules.md) or [adaptive](Adaptive%20Integration.md) form, or use [Gauss rules](Gauss%20Rules.md).

## Explorations
- [EX44 - Weddle's Three-Eighths Rule and the Two-Point Open Rule](../Explorations%203/EX44%20-%20Weddle%27s%20Three-Eighths%20Rule%20and%20the%20Two-Point%20Open%20Rule.md)

See also: [Degree of Precision](Degree%20of%20Precision.md), [Simpson's Rule](Simpson%27s%20Rule.md)

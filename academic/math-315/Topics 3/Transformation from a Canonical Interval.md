---
tags: [math-315, topic, chapter-5]
---
# Transformation from a Canonical Interval
Back to [Index](../Index.md) · Section 5.2.5 (textbook)

Rules are derived on $[-1, 1]$. To use one on $[a, b]$, map $[-1, 1]$ to $[a, b]$ by the line through $(-1, a)$ and $(1, b)$.

## The map
$$
x = g(t) = \frac{b - a}{2}t + \frac{a + b}{2}, \qquad g'(t) = \frac{b - a}{2}
$$
$$
\int_a^bf(x)\,dx = \frac{b - a}{2}\int_{-1}^{1}f\big(g(t)\big)\,dt
$$

## Transformed rule
If $\int_{-1}^1h \approx \sum w_i^*h(t_i^*)$, then
$$
\boxed{\,w_i = \frac{b - a}{2}w_i^*, \qquad x_i = \frac{b - a}{2}t_i^* + \frac{a + b}{2}\,}
$$

## Properties
- The DOP does not change, since $g$ is linear and maps polynomials to polynomials of the same degree.
- The Peano constant scales by $\big(\tfrac{b-a}{2}\big)^{m+2}$, or find it directly with [Peano's theorem](Peano%27s%20Theorem.md).

## Example
Gauss 2-point on $[a, b]$: points $\tfrac{a+b}{2} \pm \tfrac{b-a}{2\sqrt3}$, both weights $\tfrac{b-a}{2}$.

## Explorations
- [EX47 - Gauss Two-Point Rule on a General Interval](../Explorations%203/EX47%20-%20Gauss%20Two-Point%20Rule%20on%20a%20General%20Interval.md)

See also: [Gauss Rules](Gauss%20Rules.md), [Adaptive Integration](Adaptive%20Integration.md)

---
tags: [math-315, topic, chapter-7]
---
# Quadratic Interpolation Search
Back to [Index](../Index.md) · Section 7.2.2 (textbook)

[Golden section](Golden%20Section%20Search.md) ignores how big the function values are. Quadratic search uses them: fit a parabola and jump to its minimum.

## Setup
Start with a [bracket](Univariate%20Minimization.md) $[a, b]$ and an interior point $c$ with $f(c) < \min\{f(a), f(b)\}$.

## The step
Interpolate $(c, f(c))$, $(a, f(a))$, $(b, f(b))$ in [Newton form](../Topics%202/Newton%20Form.md):
$$
P_2(x) = g_0 + (x - c)\,g_1 + (x - c)(x - a)\,g_2
$$
$$
g_0 = f(c), \qquad g_1 = \frac{f(c) - f(a)}{c - a}, \qquad g_2 = \frac{\dfrac{f(b) - f(c)}{b - c} - g_1}{b - a}
$$
These are [divided differences](../Topics%202/Divided%20Differences.md). Setting $P_2'(d) = 0$:
$$
\boxed{\,d = \frac{a + c}{2} - \frac{g_1}{2g_2}\,}
$$
Since $g_2 > 0$ the parabola opens upward and $d$ is its minimum.

## Refining the bracket
Of $c$ and $d$, the one with the larger $f$ becomes an endpoint and the other becomes the new $c$. If $d = c$ the bracket cannot be shortened and an error is reported.

## Guarantee
$d$ always lies between the midpoints of $[a, c]$ and $[c, b]$, so it stays inside the bracket.

## Convergence
Superlinear near a minimum where $f''(x^*) > 0$, compared with the fixed factor $0.618$ of golden section. Production codes (Brent's method) take the parabolic step when it behaves and fall back to a golden section step when it does not.

The same parabola fit chooses step lengths in a line search: [Step-Length Selection](../../../self-study/convex-optimization/numerical-optimization/Step-Length%20Selection.md).

See also: [Cubic Interpolation Search](Cubic%20Interpolation%20Search.md), [Inverse Quadratic Interpolation](Inverse%20Quadratic%20Interpolation.md)

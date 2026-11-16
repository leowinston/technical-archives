---
tags: [math-315, topic, chapter-7]
---
# Cubic Interpolation Search
Back to [Index](../Index.md) · Section 7.3.1 (textbook)

When $f'$ is available, use it. Two points with values and slopes determine a cubic.

## Setup
$f$ is U-shaped on $[a, b]$ with $f'(a) < 0$ and $f'(b) > 0$. The sign change of $f'$ is itself a [bracket](Roots%20and%20Fixed%20Points.md) for a root of $f'$.

## The step
Build the cubic **Hermite** polynomial with
$$
P_3(a) = f(a), \quad P_3'(a) = f'(a), \quad P_3(b) = f(b), \quad P_3'(b) = f'(b)
$$
Centered at the midpoint $m = \tfrac{a+b}{2}$ with half-width $h = \tfrac{b-a}{2}$, write $P_3(x) = A(x-m)^3 + B(x-m)^2 + C(x-m) + D$:
$$
A = \frac{h\,[f'(b) + f'(a)] - [f(b) - f(a)]}{4h^3}, \quad B = \frac{f'(b) - f'(a)}{4h}, \quad C = \frac{3[f(b) - f(a)] - h\,[f'(b) + f'(a)]}{4h}
$$
$P_3'(x) = 0$ is a quadratic. Because $P_3'(a) < 0 < P_3'(b)$, exactly one root $c$ lies in $(a, b)$, and it is the minimum of the cubic:
$$
\boxed{\,c = m + \frac{-B + \sqrt{B^2 - 3AC}}{3A}\,}
$$

## Refining the bracket
- $f'(c) \approx 0$: stop, $c$ is the minimizer.
- $f'(c) < 0$: move $a$ to $c$.
- $f'(c) > 0$: move $b$ to $c$.

One new point per step is enough, because the sign of $f'(c)$ says which side the minimum is on. That is the information [two interior points](Univariate%20Minimization.md) were needed for without derivatives.

## Convergence
Fast: on the textbook example $f = -e^{-x}\sin x$ on $[0, 1.5]$, the derivative at the iterate drops from $10^{-3}$ to $10^{-10}$ in two steps.

Cubic interpolation with function and gradient values is the standard step-length refinement inside a line search: [Step-Length Selection](../../../self-study/convex-optimization/numerical-optimization/Step-Length%20Selection.md).

See also: [Quadratic Interpolation Search](Quadratic%20Interpolation%20Search.md), [Cubic Splines](../Topics%202/Cubic%20Splines.md)

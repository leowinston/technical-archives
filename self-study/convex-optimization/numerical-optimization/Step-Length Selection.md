---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §3.5, Algorithms 3.5 and 3.6
---
# Step-Length Selection
Back to [Index](../Index.md) · Nocedal & Wright §3.5

How a line search actually finds an $\alpha$ that satisfies the [Wolfe Conditions](Wolfe%20Conditions.md). It is [univariate minimization](../../../academic/math-315/Topics%204/Univariate%20Minimization.md) of $\phi(\alpha) = f(x_k + \alpha p_k)$, stopped early.

## Interpolation
Known for free: $\phi(0)$ and $\phi'(0) < 0$. Try $\alpha_0$. If it fails sufficient decrease, fit a quadratic to $\phi(0)$, $\phi'(0)$, $\phi(\alpha_0)$ and take its minimizer:
$$
\boxed{\,\alpha_1 = -\frac{\phi'(0)\,\alpha_0^2}{2\,[\phi(\alpha_0) - \phi(0) - \phi'(0)\,\alpha_0]}\,}
$$
If $\alpha_1$ fails too, fit a **cubic** to $\phi(0)$, $\phi'(0)$, $\phi(\alpha_0)$, $\phi(\alpha_1)$ and minimize that. If a trial is too close to the previous one or much smaller, reset it to half the previous value (safeguarding).

This is [Quadratic Interpolation Search](../../../academic/math-315/Topics%204/Quadratic%20Interpolation%20Search.md) and [Cubic Interpolation Search](../../../academic/math-315/Topics%204/Cubic%20Interpolation%20Search.md) with derivative information at one end.

## Initial step
- Newton and quasi-Newton: always try $\alpha_0 = 1$ first. It is eventually accepted, which is what preserves the fast rate.
- Steepest descent and conjugate gradient have no natural scale. Assume the first-order change will match the previous iteration: $\alpha_0 = \alpha_{k-1}\dfrac{\nabla f_{k-1}^{\top}p_{k-1}}{\nabla f_k^{\top}p_k}$.

## A line search for the strong Wolfe conditions
Two phases, mirroring bracketing and refining in [root finding](../../../academic/math-315/Topics%204/Roots%20and%20Fixed%20Points.md):
1. **Bracketing.** Increase the trial step until an interval is found that must contain acceptable steps. This happens when the trial violates sufficient decrease, or $\phi$ stopped decreasing, or $\phi' \ge 0$.
2. **Zoom.** Shrink that interval by interpolation until a point satisfies the strong Wolfe conditions.

The interval $(\alpha_{lo}, \alpha_{hi})$ kept by zoom always contains acceptable steps, in the same way a sign change keeps a root inside a [bisection](../../../academic/math-315/Topics%204/Bisection%20Method.md) bracket.

See also: [Line Search Methods](Line%20Search%20Methods.md), [Golden Section Search](../../../academic/math-315/Topics%204/Golden%20Section%20Search.md)

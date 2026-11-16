---
tags: [math-315, topic, chapter-5]
---
# Differentiating a Cubic Spline
Back to [Index](../Index.md) · Section 5.1 (textbook)

Raising the degree of a local interpolant to get a better derivative fails for the same reason high-degree interpolation fails ([Runge](Interpolation%20Error.md)), and differentiating makes it worse. Instead, fit a [cubic spline](Cubic%20Splines.md) to all the data and differentiate it.

## Error
For the not-a-knot spline $S_{3,N}$ with mesh widths $h_i$:
$$
\boxed{\,\max|f - S_{3,N}| = O\big(\max_i h_i^4\big), \qquad \max|f' - S_{3,N}'| = O\big(\max_i h_i^3\big)\,}
$$
Each derivative costs one power of $h$, so $S'$ is third order, one order better than central differences.

## Global, not local
$S'(x)$ depends on **all** the data, because the spline coefficients come from one linear system. It also gives $f'$ at any $x$, not only at the nodes.

## In Python
```python
from scipy.interpolate import CubicSpline
S = CubicSpline(x, f)           # not-a-knot by default
fp = S.derivative()(x)          # or S(x, 1)
```

## Example
For $\sin x$ on $[0, \tfrac\pi2]$ with $h = \pi/20$, `np.gradient` has errors around $4\times10^{-3}$ and $8\times10^{-2}$ at the right end. The spline derivative has errors from about $10^{-6}$ inside to $7\times10^{-4}$ at the right end.

## Explorations
- [EX39 - np.gradient Versus a Cubic Spline Derivative of sin x](../Explorations%202/EX39%20-%20np.gradient%20Versus%20a%20Cubic%20Spline%20Derivative%20of%20sin%20x.md)

See also: [Differentiating Tabulated Data](Differentiating%20Tabulated%20Data.md), [Cubic B-Splines](Cubic%20B-Splines.md)

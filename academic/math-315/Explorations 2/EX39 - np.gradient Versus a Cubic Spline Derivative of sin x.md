---
tags:
  - math-315
  - exploration
  - chapter-5
source: Textbook Section 5.3.1, Examples 5.3.1–5.3.2 and Tables 5.2–5.3, redone in Python
topics:
  - "[[../Topics 2/Differentiating Tabulated Data]]"
  - "[[../Topics 2/Differentiating a Cubic Spline]]"
---
# EX39 — np.gradient Versus a Cubic Spline Derivative of sin x
Back to [Index](../Index.md)

> [!question] Problem
> Tabulate $f = \sin x$ on $[0, \tfrac\pi2]$ with $h = \pi/20$ ($N = 10$).
> (a) Approximate $f'$ at the nodes with `np.gradient` and tabulate the errors against $\cos x$.
> (b) Repeat with the derivative of a not-a-knot cubic spline.
> (c) Explain the size and location of the largest errors.

## Setup
- $11$ nodes $x_i = ih$, $h = \pi/20 \approx 0.157$
- $h^2 \approx 0.025$, $h^3 \approx 0.0039$

## Strategy
1. Build the table, then compute both derivatives.
2. Compare the interior and endpoint errors with the predicted orders.

```python
import numpy as np
from scipy.interpolate import CubicSpline
x = np.linspace(0, np.pi/2, 11); h = x[1] - x[0]
f = np.sin(x)
g = np.gradient(f, h)               # central inside, one-sided ends
s = CubicSpline(x, f).derivative()(x)
```

## Solution
**(a) and (b) The table**

| $x$ | `gradient` | error | spline $S'$ | error |
|---|---|---|---|---|
| 0.0000 | 0.995893 | $-4.1\times10^{-3}$ | 1.000105 | $1.1\times10^{-4}$ |
| 0.1571 | 0.983632 | $-4.1\times10^{-3}$ | 0.987656 | $-3.3\times10^{-5}$ |
| 0.3142 | 0.947150 | $-3.9\times10^{-3}$ | 0.951061 | $4.6\times10^{-6}$ |
| 0.4712 | 0.887347 | $-3.7\times10^{-3}$ | 0.891002 | $-5.0\times10^{-6}$ |
| 0.6283 | 0.805694 | $-3.3\times10^{-3}$ | 0.809015 | $-2.4\times10^{-6}$ |
| 0.7854 | 0.704203 | $-2.9\times10^{-3}$ | 0.707105 | $-1.6\times10^{-6}$ |
| 0.9425 | 0.585371 | $-2.4\times10^{-3}$ | 0.587780 | $-5.5\times10^{-6}$ |
| 1.0996 | 0.452126 | $-1.9\times10^{-3}$ | 0.454002 | $1.2\times10^{-5}$ |
| 1.2566 | 0.307748 | $-1.3\times10^{-3}$ | 0.308967 | $-5.0\times10^{-5}$ |
| 1.4137 | 0.155792 | $-6.4\times10^{-4}$ | 0.156618 | $1.8\times10^{-4}$ |
| 1.5708 | 0.078378 | $\mathbf{7.8\times10^{-2}}$ | $-0.000687$ | $-6.9\times10^{-4}$ |

These match the textbook tables digit for digit.

**(c) Explaining the errors**

*Gradient, interior.* The central difference error is $\tfrac{h^2}{6}f''' = -\tfrac{h^2}{6}\cos x$, so it should be negative and shrink like $\cos x$:
$$
-\frac{(0.157)^2}{6}\cos(0.785) = -0.00411 \times 0.707 \approx -2.9\times10^{-3} \ \checkmark
$$

*Gradient, right end.* The one-sided difference has error $\approx -\tfrac h2f''(x_N) = \tfrac h2\sin\tfrac\pi2 \approx 0.0785$, so the end point is first order. $\checkmark$ At the left end $f''(0) = 0$, which is why that end looks fine. `edge_order=2` cuts the right-end error to $1\times10^{-3}$.

*Spline.* Inside, the errors are $10^{-6}$ to $10^{-5}$, about $1000$ times smaller than the central difference. Near the ends they grow to $10^{-4}$, because the not-a-knot conditions are weaker there. The order is still $O(h^3)$.

## Result
- `np.gradient`: interior error $\approx 3\times10^{-3}$ ($O(h^2)$), end error $8\times10^{-2}$ ($O(h)$)
- Spline derivative: error $10^{-6}$ to $7\times10^{-4}$ ($O(h^3)$), worst at the ends

## Takeaways
- On the same data, the spline derivative beats finite differences by two to three digits.
- Always check the endpoints. That is where both methods are weakest.

## Related topics
- [Differentiating a Cubic Spline](../Topics%202/Differentiating%20a%20Cubic%20Spline.md)
- [Differentiating Tabulated Data](../Topics%202/Differentiating%20Tabulated%20Data.md)
- [Cubic Splines](../Topics%202/Cubic%20Splines.md)

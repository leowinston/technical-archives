---
tags:
  - math-315
  - exploration
  - chapter-5
source: Textbook Section 5.3.2, Example 5.3.7 and Problem 5.3.8, redone in Python
topics:
  - "[[../Topics 3/Integrating Tabulated Data]]"
  - "[[../Topics 3/Midpoint and Trapezoidal Rules]]"
---
# EX49 — Cardiac Output from Dye Concentration Data
Back to [Index](../Index.md)

> [!question] Problem
> A $5$ mg bolus of dye is injected into the right atrium. The concentration in the aorta is measured each second:
>
> | $t$ (s) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
> |---|---|---|---|---|---|---|---|---|---|---|---|
> | $c$ (mg/L) | 0 | 0.4 | 2.8 | 6.5 | 9.8 | 8.9 | 6.1 | 4.0 | 2.3 | 1.1 | 0 |
>
> The cardiac output is $F = A\big/\int_0^{10}c(t)\,dt$ with $A = 5$ mg.
> (a) Estimate $F$ with the trapezoidal rule.
> (b) Estimate it with a cubic spline, and with a PCHIP interpolant.
> (c) How many digits can you trust?

## Setup
- $c(t)$ is known only at the 11 data points, so this is [tabulated data](../Topics%203/Integrating%20Tabulated%20Data.md)
- Data has two significant digits

## Strategy
1. Integrate a linear spline (trapezoid), a cubic spline and PCHIP.
2. Let their agreement serve as the error estimate.

```python
t = np.arange(11.0)
c = np.array([0, 0.4, 2.8, 6.5, 9.8, 8.9, 6.1, 4.0, 2.3, 1.1, 0])
T  = scipy.integrate.trapezoid(c, t)
S3 = CubicSpline(t, c).integrate(0, 10)
P  = PchipInterpolator(t, c).integrate(0, 10)
```

## Solution
**(a) Trapezoidal rule**

With $h = 1$ and $c_0 = c_{10} = 0$, the rule is just the sum of the interior values:
$$
\int_0^{10}c\,dt \approx 0.4 + 2.8 + 6.5 + 9.8 + 8.9 + 6.1 + 4.0 + 2.3 + 1.1 = 41.9
$$
$$
F_1 = \frac{5}{41.9} = 0.1193\ \text{L/s}
$$

**(b) Spline integrals**

| Method | $\int c\,dt$ (mg·s/L) | $F$ (L/s) |
|---|---|---|
| Trapezoidal (linear spline) | $41.900$ | $0.11933$ |
| Cubic spline (not-a-knot) | $41.935$ | $0.11923$ |
| PCHIP | $41.988$ | $0.11908$ |

The cubic spline value is what you get from Simpson on every piece of the spline, since Simpson is exact for cubics.

**(c) Trustworthy digits**

The three values of $F$ agree to $0.119$ and differ in the fourth digit. The data has only two or three significant digits, so $F \approx 0.119$ L/s is all the data supports.

## Result
$$
\boxed{\,F \approx 0.119\ \text{L/s}\,}
$$

## Takeaways
- `trapezoid` gives no error estimate. Comparing two interpolants is a cheap substitute.
- Do not report more digits than the data has, however accurate the rule is.

## Related topics
- [Integrating Tabulated Data](../Topics%203/Integrating%20Tabulated%20Data.md)
- [Midpoint and Trapezoidal Rules](../Topics%203/Midpoint%20and%20Trapezoidal%20Rules.md)
- [Cubic Splines](../Topics%202/Cubic%20Splines.md)

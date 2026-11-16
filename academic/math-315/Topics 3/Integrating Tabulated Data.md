---
tags: [math-315, topic, chapter-5]
---
# Integrating Tabulated Data
Back to [Index](../Index.md) · Section 5.3.2 (textbook)

When only data $(x_i, f_i)$ is known, interpolate it with a spline and integrate the spline exactly.

## Linear spline = trapezoidal rule
Integrating the [linear spline](../Topics%202/Linear%20Splines.md) piece by piece gives the composite trapezoidal rule, on any mesh:
$$
\int_{x_0}^{x_N}S_1(x)\,dx = \sum_{i=1}^{N}\frac{x_i - x_{i-1}}{2}(f_{i-1} + f_i)
$$

## Cubic spline + Simpson
Each piece of a [cubic spline](../Topics%202/Cubic%20Splines.md) is a cubic, and Simpson has DOP $3$, so Simpson on each piece is **exact** for the spline:
$$
\int_{x_{i-1}}^{x_i}S_3 = \frac{h_i}{6}\Big[f_{i-1} + 4S_3\big(x_{i-\frac12}\big) + f_i\Big]
$$
This avoids extracting the polynomial coefficients.

## In Python
```python
T  = scipy.integrate.trapezoid(f, x)              # linear spline
S3 = CubicSpline(x, f).integrate(x[0], x[-1])     # cubic spline
P  = PchipInterpolator(x, f).integrate(x[0], x[-1])
```

## Error estimates
`trapezoid` gives no error estimate. Compare two methods (trapezoid versus cubic spline, or spline versus PCHIP) and trust only the digits they share, and no more digits than the data has.

## Explorations
- [EX49 - Cardiac Output from Dye Concentration Data](../Explorations%203/EX49%20-%20Cardiac%20Output%20from%20Dye%20Concentration%20Data.md)

See also: [Midpoint and Trapezoidal Rules](Midpoint%20and%20Trapezoidal%20Rules.md), [Simpson's Rule](Simpson%27s%20Rule.md)

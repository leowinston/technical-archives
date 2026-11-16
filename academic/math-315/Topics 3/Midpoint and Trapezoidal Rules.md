---
tags: [math-315, topic, chapter-5]
---
# Midpoint and Trapezoidal Rules
Back to [Index](../Index.md) · Section 5.2.1 (textbook)

Split $[a, b]$ into $N$ pieces, $x_i = a + ih$ with $h = \tfrac{b-a}{N}$, and integrate a simple approximation on each piece.

## Basic rules on $[c, d]$
| Rule | Approximation of $f$ | Rule |
|---|---|---|
| Midpoint | constant $f\big(\tfrac{c+d}{2}\big)$ | $R_M = (d - c)\,f\big(\tfrac{c+d}{2}\big)$ |
| Trapezoidal | line through both ends | $R_T = \tfrac{d-c}{2}\big[f(c) + f(d)\big]$ |

Midpoint is a rectangle's area. Trapezoidal is width times average height.

## Composite rules
With $x_s = a + sh$ for any real $s$:
$$
\boxed{\,R_{CM}(f, h) = h\sum_{i=1}^{N}f\big(x_{i-\frac12}\big), \qquad
R_{CT}(f, h) = h\Big[\tfrac12f(x_0) + f(x_1) + \cdots + f(x_{N-1}) + \tfrac12f(x_N)\Big]\,}
$$
For unequal pieces, use $(x_i - x_{i-1})$ in place of $h$ in each term.

## Accuracy
Both are exact for straight lines and both are $O(h^2)$, with midpoint about half the trapezoidal error and of opposite sign ([details](Error%20in%20the%20Midpoint%20and%20Trapezoidal%20Rules.md)).

## In Python
```python
xs = np.linspace(a, b, N + 1)
T = scipy.integrate.trapezoid(f(xs), xs)
M = h * f(xs[:-1] + h/2).sum()
```

## Explorations
- [EX41 - Trapezoidal Rule Error for x^2 + x - 1](../Explorations%203/EX41%20-%20Trapezoidal%20Rule%20Error%20for%20x%5E2%20%2B%20x%20-%201.md)
- [EX48 - Composite Rule Convergence for e^x on 0 to 1](../Explorations%203/EX48%20-%20Composite%20Rule%20Convergence%20for%20e%5Ex%20on%200%20to%201.md)

See also: [Quadrature Rules](Quadrature%20Rules.md), [Linear Splines](../Topics%202/Linear%20Splines.md)

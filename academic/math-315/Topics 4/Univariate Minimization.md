---
tags: [math-315, topic, chapter-7]
---
# Univariate Minimization
Back to [Index](../Index.md) · Section 7.1 (textbook)

Find a local minimum of $f$ on $[a, b]$. To maximize, minimize $-f$.

## From calculus
Find the critical points $f'(x) = 0$ and compare $f$ there and at the endpoints. Numerically that is root finding on $f'$, for example [Newton's method](Newton's%20Method.md):
$$
x_{i+1} = x_i - \frac{f'(x_i)}{f''(x_i)}
$$
This needs two derivatives and can land on a maximum. The search methods below need only values of $f$.

## U-shaped functions and brackets
$f$ is **U-shaped** on $[a, b]$ if it strictly decreases to a single minimum and then strictly increases. Then $[a, b]$ is a **bracket for the minimum**.

## Why two interior points
For a root, one interior point refines the bracket. For a minimum, one point $c$ is not enough: two U-shaped functions can agree at $a$, $c$, $b$ and have their minima on opposite sides of $c$. With two points $c < d$:
$$
f(c) \le f(d) \;\Rightarrow\; \text{minimum in } [a, d], \qquad f(c) \ge f(d) \;\Rightarrow\; \text{minimum in } [c, b]
$$

## Methods
| Method | Uses | Analogue in root finding |
|---|---|---|
| [Golden Section Search](Golden%20Section%20Search.md) | comparisons of $f$ | [Bisection Method](Bisection%20Method.md) |
| [Quadratic Interpolation Search](Quadratic%20Interpolation%20Search.md) | values of $f$ | [Inverse Quadratic Interpolation](Inverse%20Quadratic%20Interpolation.md) |
| [Cubic Interpolation Search](Cubic%20Interpolation%20Search.md) | $f$ and $f'$ | [Newton's Method](Newton's%20Method.md) |

## In Python
```python
from scipy.optimize import minimize_scalar
minimize_scalar(lambda x: -np.exp(-x) * np.sin(x), bounds=(0, 1.5), method='bounded')
```
This is Brent's method, golden section combined with parabolic interpolation. It returns $x = \pi/4$, $f = -0.3224$.

## Where this goes
A one-dimensional minimization is the inner step of every line search method in $n$ dimensions: [Line Search Methods](../../../self-study/convex-optimization/numerical-optimization/Line%20Search%20Methods.md), [Step-Length Selection](../../../self-study/convex-optimization/numerical-optimization/Step-Length%20Selection.md).

## Explorations
- [EX54 - Golden Section Search for -e^-x sin x](../Explorations%204/EX54%20-%20Golden%20Section%20Search%20for%20-e^-x%20sin%20x.md)

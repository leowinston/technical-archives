---
tags: [math-315, topic, lecture-4]
---
# Least Squares Fitting
Back to [Index](../Index.md) · Section 4.4

## Problem
With $N + 1$ points and degree $M \le N$ (usually $M \ll N$), exact interpolation is impossible, so minimize the sum of squared misfits:
$$
\min_{a_0, \dots, a_M}\ \sum_{i=0}^{N}\big(p_M(x_i) - f_i\big)^2
= \min_{\mathbf{a}}\ \|V\mathbf{a} - \mathbf{f}\|_2^2
$$
Here $V$ is the $(N+1)\times(M+1)$ Vandermonde matrix, which is **tall**.

## General basis
For $g(x) = \sum_j a_j\phi_j(x)$, use $W_{ij} = \phi_j(x_i)$ and minimize $\|W\mathbf{a} - \mathbf{f}\|_2^2$.

## Solving
1. Calculus: set every $\partial/\partial a_j$ to $0$. This gives the [Normal Equations](Normal%20Equations.md).
2. Orthogonal factorization: [Least Squares via QR](Least%20Squares%20via%20QR.md), which is more stable.

## Example
For $x = 1, 2, 3, 4$ and $y = 1, 0, -1, 0$:
$$
p_1(x) = 1 - \tfrac25x
$$

## In Python
```python
c = np.polyfit(x, y, M)   # only the degree changes vs interpolation
```

![L4-least-squares-fits.png](../Assets/L4-least-squares-fits.png)

## Explorations
- [EX33 - Least Squares Line and Quadratic for Four Points](../Explorations%202/EX33%20-%20Least%20Squares%20Line%20and%20Quadratic%20for%20Four%20Points.md)
- [EX34 - Least Squares Line by QR](../Explorations%202/EX34%20-%20Least%20Squares%20Line%20by%20QR.md)

See also: [Least Squares with a General Basis](Least%20Squares%20with%20a%20General%20Basis.md), [Power Series Form and the Vandermonde Matrix](Power%20Series%20Form%20and%20the%20Vandermonde%20Matrix.md)

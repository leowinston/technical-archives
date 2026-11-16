---
tags: [math-315, topic, lecture-4]
---
# Polynomial Interpolation
Back to [Index](../Index.md) · Section 4.1

## Definition
$p(x)$ **interpolates** the data $\{(x_i, f_i)\}_{i=0}^{N}$ if
$$
p(x_i) = f_i, \qquad i = 0, 1, \dots, N
$$

## Degree
$p_K(x) = c_0 + c_1x + \cdots + c_Kx^K$ has **degree** $K$. It has **exact degree** $K$ if also $c_K \neq 0$.
For example, $1 + x - 4x^3$ has exact degree $3$, and it also has degree $4, 5, 6, \dots$.

## Existence and uniqueness
> [!important] Theorem
> If the nodes $\{x_i\}_{i=0}^{N}$ are distinct, exactly one polynomial $p_N$ of degree $N$ interpolates the data.

The interpolant can have a lower exact degree when the data lie on a lower-degree polynomial.

## Same polynomial test
Two polynomials of degree $N$ are equal if they agree at $N+1$ distinct points. Use this to check that two forms (power, Newton, Lagrange) are the same polynomial.

## Three bases for the same $p_N$
| Basis | Functions |
|---|---|
| Power series | $1, x, x^2, \dots, x^N$ |
| Newton | $1, (x - x_0), (x - x_0)(x - x_1), \dots$ |
| Lagrange | $\ell_0(x), \dots, \ell_N(x)$ |

## In Python
```python
c = np.polyfit(x, y, len(x) - 1)  # degree N through N+1 points
p = np.polyval(c, z)
```

## Explorations
- [EX24 - Interpolating sin(x) at Three Collinear Points](../Explorations%202/EX24%20-%20Interpolating%20sin%28x%29%20at%20Three%20Collinear%20Points.md)
- [EX27 - Lagrange Form for Collinear Data](../Explorations%202/EX27%20-%20Lagrange%20Form%20for%20Collinear%20Data.md)

See also: [Power Series Form and the Vandermonde Matrix](Power%20Series%20Form%20and%20the%20Vandermonde%20Matrix.md), [Newton Form](Newton%20Form.md), [Lagrange Form](Lagrange%20Form.md)

---
tags: [math-315, topic, lecture-4]
---
# Cubic B-Splines
Back to [Index](../Index.md) · Section 4.3.2

## The basis function
Use equally spaced knots with spacing $h$. $B_p$ is centered at $x_p$, zero outside $[x_p - 2h, x_p + 2h]$, and normalized so that $B_p(x_p) = 1$. On the left half,
$$
B_p(x) = \begin{cases}
A\,(x - [x_p - 2h])^3 & [x_p - 2h,\ x_p - h] \\
A\,(x - [x_p - 2h])^3 + B\,(x - [x_p - h])^3 & [x_p - h,\ x_p]
\end{cases}
$$
The right half is the mirror image. Normalization gives $8A + B = 1/h^3$, and $C^1$ at $x_p$ gives $B = -4A$:
$$
\boxed{\,A = \frac{1}{4h^3}, \qquad B = -\frac{1}{h^3}\,}
$$

## Values at the knots
| $x$ | $x_p \mp 2h$ | $x_p \mp h$ | $x_p$ |
|---|---|---|---|
| $B_p$ | $0$ | $\tfrac14$ | $1$ |
| $B_p'$ | $0$ | $\pm\tfrac{3}{4h}$ | $0$ |
| $B_p''$ | $0$ | $\tfrac{3}{2h^2}$ | $-\tfrac{3}{h^2}$ |

## Interpolating with B-splines
$S(x) = \sum_{i=-1}^{n+1}a_iB_i(x)$, so each node gives one equation:
$$
\tfrac14a_{j-1} + a_j + \tfrac14a_{j+1} = f_j, \qquad j = 0, \dots, n
$$
The **natural** conditions $a_{-1} - 2a_0 + a_1 = 0$ (and the same at $n$) give
$$
a_0 = \tfrac23f_0, \qquad a_n = \tfrac23f_n
$$
The rest is a tridiagonal system with diagonal $1$ and off-diagonals $\tfrac14$. It is SPD, so elimination is simple and stable.

![L4-cubic-b-spline.png](../Assets/L4-cubic-b-spline.png)

## Explorations
- [EX31 - Deriving the Cubic B-Spline](../Explorations%202/EX31%20-%20Deriving%20the%20Cubic%20B-Spline.md)
- [EX32 - Natural Cubic Spline from B-Splines](../Explorations%202/EX32%20-%20Natural%20Cubic%20Spline%20from%20B-Splines.md)

See also: [Cubic Splines](Cubic%20Splines.md), [Symmetric Positive Definite Matrices](../Topics%201/Symmetric%20Positive%20Definite%20Matrices.md)

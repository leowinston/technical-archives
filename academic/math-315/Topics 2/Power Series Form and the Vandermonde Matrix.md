---
tags: [math-315, topic, lecture-4]
---
# Power Series Form and the Vandermonde Matrix
Back to [Index](../Index.md) · Section 4.1.1

## The linear system
Write $p_M(x) = a_0 + a_1x + \cdots + a_Mx^M$ and impose $p_M(x_i) = f_i$:
$$
V\mathbf{a} = \mathbf{f}, \qquad
V = \begin{bmatrix}
1 & x_0 & x_0^2 & \cdots & x_0^M \\
\vdots & \vdots & \vdots & & \vdots \\
1 & x_N & x_N^2 & \cdots & x_N^M
\end{bmatrix}
$$
This gives $N+1$ equations in $M+1$ unknowns.

## Square case
$$
\det V_N = \prod_{i>j}(x_i - x_j) \neq 0 \iff \text{the nodes are distinct}
$$
So $M = N$ with distinct nodes always gives a unique solution.

## Non-square cases
- $M < N$: some data have **no** solution. This leads to [Least Squares Fitting](Least%20Squares%20Fitting.md).
- $M > N$: a solution, if one exists, is **not unique**.

## Two points
$$
a_1 = \frac{f_1 - f_0}{x_1 - x_0}, \qquad a_0 = f_0 - a_1x_0, \qquad x_0 \neq x_1
$$

## Example
Through $(-1, 0)$, $(0, 1)$, $(1, 3)$:
$$
p_2(x) = 1 + \tfrac32x + \tfrac12x^2
$$

## Explorations
- [EX25 - Power Series Form Through Three Points](../Explorations%202/EX25%20-%20Power%20Series%20Form%20Through%20Three%20Points.md)
- [EX24 - Interpolating sin(x) at Three Collinear Points](../Explorations%202/EX24%20-%20Interpolating%20sin%28x%29%20at%20Three%20Collinear%20Points.md)

See also: [Polynomial Interpolation](Polynomial%20Interpolation.md), [Newton Form](Newton%20Form.md)

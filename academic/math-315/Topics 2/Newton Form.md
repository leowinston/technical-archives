---
tags: [math-315, topic, lecture-4]
---
# Newton Form
Back to [Index](../Index.md) · Section 4.1.2

## Basis
$$
\mathcal{N}_0(x) = 1, \qquad \mathcal{N}_j(x) = \prod_{k=0}^{j-1}(x - x_k), \qquad p_n(x) = \sum_{j=0}^{n} c_j \mathcal{N}_j(x)
$$
The nodes $x_0, \dots, x_{n-1}$ are the **centers**. $\mathcal{N}_j$ vanishes at $x_0, \dots, x_{j-1}$.

## Lower triangular system
For $n = 2$, $p_2 = b_0 + b_1(x - x_0) + b_2(x - x_0)(x - x_1)$:
$$
\begin{bmatrix}
1 & 0 & 0 \\
1 & x_1 - x_0 & 0 \\
1 & x_2 - x_0 & (x_2 - x_0)(x_2 - x_1)
\end{bmatrix}
\begin{bmatrix} b_0 \\ b_1 \\ b_2 \end{bmatrix}
= \begin{bmatrix} f_0 \\ f_1 \\ f_2 \end{bmatrix}
$$
Distinct nodes give a nonzero diagonal, so **forward substitution** gives the unique solution.

## Example
Through $(-1, 0)$, $(0, 1)$, $(1, 3)$, $b = (0, 1, \tfrac12)$:
$$
p_2(x) = (x + 1) + \tfrac12(x + 1)x = 1 + \tfrac32x + \tfrac12x^2
$$
This is the same polynomial as the power series form.

## Why use it
- The coefficients are easy to get, from [Divided Differences](Divided%20Differences.md).
- It evaluates cheaply by nested multiplication.
- A new node adds one term and leaves the old $c_j$ unchanged.

## Explorations
- [EX26 - Newton Form and Divided Differences Through Three Points](../Explorations%202/EX26%20-%20Newton%20Form%20and%20Divided%20Differences%20Through%20Three%20Points.md)
- [EX24 - Interpolating sin(x) at Three Collinear Points](../Explorations%202/EX24%20-%20Interpolating%20sin%28x%29%20at%20Three%20Collinear%20Points.md)

See also: [Divided Differences](Divided%20Differences.md), [Lagrange Form](Lagrange%20Form.md), [Triangular Systems](../Topics%201/Triangular%20Systems.md)

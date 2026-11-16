---
tags: [math-315, topic, lecture-4]
---
# Normal Equations
Back to [Index](../Index.md) · Section 4.4

## Derivation
Let $\sigma_M = \sum_{r=0}^{N}\big(p_M(x_r) - f_r\big)^2$. Then
$$
\frac{\partial\sigma_M}{\partial a_j} = 2\sum_{r=0}^{N}x_r^j\big(p_M(x_r) - f_r\big) = 0, \qquad j = 0, \dots, M
$$

## Matrix form
$$
\boxed{\,V^{\top}V\,\mathbf{a} = V^{\top}\mathbf{f}\,}
\qquad
V^{\top}V = \begin{bmatrix}
\sum 1 & \sum x_r & \cdots & \sum x_r^M \\
\sum x_r & \sum x_r^2 & \cdots & \sum x_r^{M+1} \\
\vdots & & \ddots & \vdots \\
\sum x_r^M & \sum x_r^{M+1} & \cdots & \sum x_r^{2M}
\end{bmatrix}
$$
The right side is $V^{\top}\mathbf{f} = \big(\sum f_r,\ \sum f_rx_r,\ \dots,\ \sum f_rx_r^M\big)^{\top}$.

## Properties
- $V^{\top}V$ is square and of size $(M+1)\times(M+1)$.
- If $V$ has full column rank, $V^{\top}V$ is **SPD** and the solution is unique.
- Solve it with [Cholesky](../Topics%201/Cholesky%20Factorization.md). Pivoting is not needed.

## Caveat
Forming $V^{\top}V$ is convenient, but it squares the condition number ([details](Conditioning%20of%20the%20Normal%20Equations.md)), so it is a poor choice when $V$ is ill-conditioned. Prefer [Least Squares via QR](Least%20Squares%20via%20QR.md).

## Example
For $x = 1, 2, 3, 4$ and $y = 1, 0, -1, 0$:
$$
\begin{bmatrix} 4 & 10 \\ 10 & 30 \end{bmatrix}\mathbf{a} = \begin{bmatrix} 0 \\ -2 \end{bmatrix}
\implies \mathbf{a} = \big(1,\ -\tfrac25\big)
$$

## Explorations
- [EX33 - Least Squares Line and Quadratic for Four Points](../Explorations%202/EX33%20-%20Least%20Squares%20Line%20and%20Quadratic%20for%20Four%20Points.md)
- [EX34 - Least Squares Line by QR](../Explorations%202/EX34%20-%20Least%20Squares%20Line%20by%20QR.md)

See also: [Least Squares Fitting](Least%20Squares%20Fitting.md), [Symmetric Positive Definite Matrices](../Topics%201/Symmetric%20Positive%20Definite%20Matrices.md)

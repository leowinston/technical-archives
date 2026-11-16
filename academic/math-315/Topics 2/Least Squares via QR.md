---
tags: [math-315, topic, lecture-4]
---
# Least Squares via QR
Back to [Index](../Index.md) · Section 4.5.2

## Idea
$Q^{\top}$ preserves the 2-norm, $\|Q^{\top}\mathbf{r}\|_2 = \|\mathbf{r}\|_2$. So factor $V = QR$, with $V$ of size $n\times m$ and $n > m$:
$$
\|V\mathbf{a} - \mathbf{f}\|_2^2
= \|R\mathbf{a} - Q^{\top}\mathbf{f}\|_2^2
= \left\|\begin{bmatrix} R_m \\ 0 \end{bmatrix}\mathbf{a} - \begin{bmatrix} \mathbf{b} \\ \mathbf{c} \end{bmatrix}\right\|_2^2
= \|R_m\mathbf{a} - \mathbf{b}\|_2^2 + \|\mathbf{c}\|_2^2
$$
Here $R_m$ is $m\times m$ upper triangular, $\mathbf{b}$ is the top $m$ entries of $Q^{\top}\mathbf{f}$, and $\mathbf{c}$ is the bottom $n - m$ entries.

## Solution
$$
\boxed{\,R_m\mathbf{a} = \mathbf{b}\,} \quad\text{(back substitution)}, \qquad
\min\|V\mathbf{a} - \mathbf{f}\|_2 = \|\mathbf{c}\|_2
$$
No choice of $\mathbf{a}$ can reduce the $\|\mathbf{c}\|$ term, so it is the leftover residual.

## Why QR
The normal equations work with $V^{\top}V$, which squares the conditioning. QR works with $V$ directly, so it is the stable choice. The SVD gives the same kind of solution at a higher cost.

## Example
For $x = 1, 2, 3, 4$, $R_m = \begin{bmatrix} 2 & 5 \\ 0 & \sqrt5 \end{bmatrix}$ and $\mathbf{b} = \big(0, -\tfrac{2}{\sqrt5}\big)$. This gives $\mathbf{a} = \big(1, -\tfrac25\big)$ and $\|\mathbf{c}\|_2^2 = \tfrac65$.

## Explorations
- [EX34 - Least Squares Line by QR](../Explorations%202/EX34%20-%20Least%20Squares%20Line%20by%20QR.md)

See also: [QR Factorization](../Topics%201/QR%20Factorization.md), [Normal Equations](Normal%20Equations.md), [Condition Number](../Topics%201/Condition%20Number.md)

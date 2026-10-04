---
tags: [math-315, topic, lecture-3]
---
# Singular Value Decomposition
Back to [Index](../Index.md) · Section 3.3 (SVD)

## Statement
**Every** $A \in \mathbb{R}^{m\times n}$ can be factored as
$$
A = U\Sigma V^{\top}
$$
with $U$ and $V$ orthogonal, $\Sigma = \operatorname{diag}(\sigma_1, \dots, \sigma_n)$, and $\sigma_1 \ge \cdots \ge \sigma_n \ge 0$.

## Computing it by hand
$A^{\top}A = V\big(\Sigma^{\top}\Sigma\big)V^{\top}$, so
$$
\sigma_i = \sqrt{\lambda_i\big(A^{\top}A\big)}, \qquad \mathbf{v}_i = \text{eigenvectors of } A^{\top}A, \qquad \mathbf{u}_i = \frac{A\mathbf{v}_i}{\sigma_i}
$$

## What it gives
$$
\|A\|_2 = \sigma_1, \qquad \|A^{-1}\|_2 = \frac{1}{\sigma_n}, \qquad \kappa_2(A) = \frac{\sigma_1}{\sigma_n}
$$
A square $A$ is singular exactly when $\sigma_n = 0$.

## Cost
It costs about $12n^3$ flops, roughly $18\times$ LU.

## Example
$$
A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}: \quad
\lambda\big(A^{\top}A\big) = 45,\ 5 \implies \sigma = 3\sqrt5,\ \sqrt5, \quad \kappa_2 = 3
$$

## Explorations
- [EX10 - SVD and Condition Number of a 2x2 Matrix](../Explorations/EX10%20-%20SVD%20and%20Condition%20Number%20of%20a%202x2%20Matrix.md)
- [EX12 - Four Norms of a 3x3 Matrix](../Explorations/EX12%20-%20Four%20Norms%20of%20a%203x3%20Matrix.md)

See also: [Matrix Norms](Matrix%20Norms.md), [Condition Number](Condition%20Number.md)

---
tags: [math-315, topic, lecture-3]
---
# Symmetric Positive Definite Matrices
Back to [Index](../Index.md) · Section 3.3.3

## Definition
$A$ is **SPD** if $A = A^{\top}$ and
$$
\mathbf{x}^{\top}A\mathbf{x} > 0 \quad \text{for all } \mathbf{x} \neq \mathbf{0}
$$

## Properties
Each one follows by choosing a particular $\mathbf{x}$:
| Property | Choice of $\mathbf{x}$ |
|---|---|
| $a_{ii} > 0$ | $\mathbf{x} = \mathbf{e}_i$ |
| $\lambda_i > 0$ | eigenvector: $\mathbf{v}^{\top}A\mathbf{v} = \lambda\lVert\mathbf{v}\rVert_2^2$ |
| $\det A = \prod\lambda_i > 0$ | follows from the eigenvalues |
| $\lvert a_{ij}\rvert < \tfrac12(a_{ii} + a_{jj})$ | $\mathbf{x} = \mathbf{e}_i \pm \mathbf{e}_j$ |
| pivots $d_{ii} > 0$ | $\mathbf{x} = L^{-\top}\mathbf{e}_i$ |

The fourth row means the largest entry lies on the diagonal. The last row means **no pivoting is needed**.

## Example
$$
\begin{bmatrix} 4 & -1 & 1 \\ -1 & 4.25 & 2.75 \\ 1 & 2.75 & 3.5 \end{bmatrix}
$$
It is symmetric with pivots $4, 4, 1$, all positive, so it is SPD.

## Explorations
- [EX08 - Cholesky Factorization of a 3x3 SPD Matrix](../Explorations/EX08%20-%20Cholesky%20Factorization%20of%20a%203x3%20SPD%20Matrix.md)

See also: [Cholesky Factorization](Cholesky%20Factorization.md), [LDLT Factorization](LDLT%20Factorization.md)

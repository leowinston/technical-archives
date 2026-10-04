---
tags: [math-315, topic, lecture-3]
---
# LU Decomposition
Back to [Index](../Index.md) · Section 3.2

## Idea
Factor $A = LU$ with $L$ **unit** lower triangular and $U$ upper triangular. Then solve in two triangular steps:
$$
L\mathbf{y} = \mathbf{b}, \qquad U\mathbf{x} = \mathbf{y}
$$

## Elementary row matrices
$R_i \leftarrow R_i - m_{ij}R_j$ is left multiplication by $M_{ij} = I - m_{ij}\mathbf{e}_i\mathbf{e}_j^{\top}$. For $i > j$, $\mathbf{e}_j^{\top}\mathbf{e}_i = 0$, so the inverse just flips the sign:
$$
M_{ij}^{-1} = I + m_{ij}\mathbf{e}_i\mathbf{e}_j^{\top}
$$

## Derivation
Let $M^{(j)} = I - \boldsymbol{\ell}_j\mathbf{e}_j^{\top}$ hold the multipliers for column $j$ in $\boldsymbol{\ell}_j$. Then
$$
M^{(n-1)}\cdots M^{(1)}A = U \implies A = \big(M^{(1)}\big)^{-1}\cdots\big(M^{(n-1)}\big)^{-1}U = LU
$$
The cross terms vanish because $\mathbf{e}_j^{\top}\boldsymbol{\ell}_k = 0$ for $j < k$. So $L = I + \sum_j \boldsymbol{\ell}_j\mathbf{e}_j^{\top}$: **$L$ is just the multipliers**, $l_{ij} = m_{ij}$.

## Existence
Without row swaps, $A = LU$ exists **iff every pivot is nonzero**, which is the same as every leading principal minor being nonzero. A zero pivot rules it out, even when $A$ is invertible.

## Cost
Factoring costs $O(n^3)$, and each solve costs $O(n^2)$. The factorization doesn't depend on $\mathbf{b}$, so it can be reused for every new right-hand side.

## Example
$$
\begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}
= \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{bmatrix}
\begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{bmatrix}
$$

## Explorations
- [EX03 - Gaussian Elimination and LU of a 3x3 Matrix](../Explorations/EX03%20-%20Gaussian%20Elimination%20and%20LU%20of%20a%203x3%20Matrix.md)
- [EX04 - Exploration 3.2.12 - A Matrix with No LU Decomposition](../Explorations/EX04%20-%20Exploration%203.2.12%20-%20A%20Matrix%20with%20No%20LU%20Decomposition.md)
- [EX06 - PA = LU for a Matrix with a Zero Pivot](../Explorations/EX06%20-%20PA%20%3D%20LU%20for%20a%20Matrix%20with%20a%20Zero%20Pivot.md)

See also: [Partial Pivoting](Partial%20Pivoting.md), [Determinants via LU](Determinants%20via%20LU.md), [LDLT Factorization](LDLT%20Factorization.md)

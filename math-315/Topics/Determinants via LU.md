---
tags: [math-315, topic, lecture-3]
---
# Determinants via LU
Back to [[Index]] · Sections 3.2.4, 3.2.5.4

## Why not the definition
Cofactor expansion costs $O(n!)$ flops.

## Without pivoting
Row replacements don't change $\det$, and $\det(L) = 1$ for a unit triangular $L$:
$$
\det(A) = \det(L)\det(U) = \prod_{i=1}^{n} u_{ii}
$$

## With pivoting
A single swap has $\det = -1$, so $p$ swaps give $\det(P) = (-1)^p$. From $PA = LU$:
$$
\det(A) = (-1)^p \prod_{i=1}^{n} u_{ii}
$$
The total cost is $O(n^3)$ for the factorization plus $n - 1$ multiplications.

> [!warning]
> A small $\det(A)$ does **not** mean $A$ is nearly singular. See [[Condition Number]].

## Example
$$
\det\begin{bmatrix} 1 & 4 & 7 \\ 2 & 8 & 5 \\ 3 & 6 & 9 \end{bmatrix} = (-1)^1(1)(-6)(-9) = -54
$$

## Explorations
- [[EX03 - Gaussian Elimination and LU of a 3x3 Matrix]]
- [[EX06 - PA = LU for a Matrix with a Zero Pivot]]
- [[EX14 - Determinant Versus Condition Number]]

See also: [[LU Decomposition]], [[Partial Pivoting]]

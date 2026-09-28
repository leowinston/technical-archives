---
tags: [math-315, topic, lecture-3]
---
# Partial Pivoting
Back to [[Index]] · Section 3.2.5

## Why pivot
In $a_{ik} \leftarrow a_{ik} - m_{ij}a_{jk}$, the multiplier $m_{ij}$ scales any rounding error in $a_{jk}$. A tiny pivot makes $|m_{ij}|$ huge. In 4-digit arithmetic, the pivot $0.003$ leads to a **200 %** error ([[EX05 - Four-Digit Arithmetic With and Without Pivoting]]).

## Strategy
Before eliminating column $j$, swap in the row with the largest entry on or below the diagonal:
$$
\big|a_{pj}\big| = \max_{j \le i \le n}|a_{ij}|, \qquad R_p \leftrightarrow R_j \implies |m_{ij}| \le 1
$$
This adds $O(n^2)$ comparisons, which is negligible next to $O(n^3)$.

## $PA = LU$
Each swap is a permutation matrix, and $P^{\top}P = I$. That lets every swap move up front ([[Permutation and Multiplier Matrices]]):
$$
PA = LU, \qquad P = P^{(n-1)}\cdots P^{(1)}
$$

## Solving
$$
LU\mathbf{x} = P\mathbf{b}: \qquad L\mathbf{y} = P\mathbf{b}, \qquad U\mathbf{x} = \mathbf{y}
$$
A new $\mathbf{b}$ doesn't need a new factorization.

## Explorations
- [[EX05 - Four-Digit Arithmetic With and Without Pivoting]]
- [[EX06 - PA = LU for a Matrix with a Zero Pivot]]

See also: [[Permutation and Multiplier Matrices]], [[LU Decomposition]], [[Determinants via LU]]

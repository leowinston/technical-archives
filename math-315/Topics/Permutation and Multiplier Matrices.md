---
tags: [math-315, topic, lecture-3]
source: Math_315_Lecture_3_Partial_Pivoting.pdf
---
# Permutation and Multiplier Matrices
Back to [[Index]] · Section 3.2.5 (supplement)

**Question:** how do we gather the swaps $P_j$ from elimination into one $P$ so that $PA = LU$?

## Derivation
Start from $M_{n-1}P_{n-1}\cdots M_2P_2M_1P_1A = U$ and insert $P_k^{\top}P_k = I$ to move each $P_k$ right:
$$
\begin{align*}
&\cdots P_3M_2\,\big(P_2M_1P_2^{\top}\big)\,P_2P_1A = U \\
&\cdots \big(P_3M_2P_3^{\top}\big)\big(P_3P_2M_1P_2^{\top}P_3^{\top}\big)\,P_3P_2P_1A = U \\
&\underbrace{\tilde M_{n-1}\cdots\tilde M_1}_{L^{-1}}\;\underbrace{P_{n-1}\cdots P_1}_{P}\;A = U
\end{align*}
$$
$$
\tilde M_j = P_{n-1}\cdots P_{j+1}\,M_j\,P_{j+1}^{\top}\cdots P_{n-1}^{\top}
$$
There are only $n-1$ steps because $a_{nn}$ has nothing below it.

> [!note] From lecture
> ![[IMG_1784.jpg]]

## Shortcut
Conjugating by a later swap only exchanges two multipliers in column $j$. So store the multipliers in $A$'s lower triangle and **swap whole rows, multipliers included**.

## Example
$$
\tilde M^{(1)} = P^{(2)}\begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ -3 & 0 & 1 \end{bmatrix}\big[P^{(2)}\big]^{\top} = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ -2 & 0 & 1 \end{bmatrix}
$$

## Explorations
- [[EX06 - PA = LU for a Matrix with a Zero Pivot]]

See also: [[Partial Pivoting]], [[LU Decomposition]]

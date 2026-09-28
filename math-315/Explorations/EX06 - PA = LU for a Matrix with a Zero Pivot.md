---
tags: [math-315, exploration, lecture-3]
source: Lecture 3 handout, pp. 9–10 (Section 3.2.5 Example); Partial Pivoting supplement
topics: ["[[Partial Pivoting]]", "[[Permutation and Multiplier Matrices]]", "[[Determinants via LU]]"]
---
# EX06 — PA = LU for a Matrix with a Zero Pivot
Back to [[Index]]

> [!question] Problem
> Let
> $$
> A = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 8 & 5 \\ 3 & 6 & 9 \end{bmatrix}
> $$
> (a) Eliminate column 1, detect the zero pivot, and swap rows to reach $U$.
> (b) Write the steps as $P^{(2)}M^{(1)}A = U$ and rearrange to $PA = LU$ using $\tilde M^{(1)} = P^{(2)}M^{(1)}\big[P^{(2)}\big]^{\top}$.
> (c) Solve $A\mathbf{x} = \mathbf{b}$ for $\mathbf{b} = (12, 15, 18)^{\top}$ and compute $\det(A)$.
> (d) Redo the factorization with **true** partial pivoting (largest pivot in each column).

## Setup
- **Matrix type:** general $3 \times 3$
- **Obstacle:** after step 1, the $(2, 2)$ entry is $0$
- **Tools:** permutation matrices ($P^{\top}P = I$), elementary matrices, $\det P = (-1)^p$

## Strategy
1. Eliminate column 1 and find that the pivot is $0$.
2. Swap rows 2 and 3, recording $P^{(2)}$.
3. Slide $P^{(2)}$ past $M^{(1)}$ by conjugating. This swaps two multipliers.
4. Solve $L\mathbf{y} = P\mathbf{b}$, then $U\mathbf{x} = \mathbf{y}$.

## Solution
**(a) Elimination**

The pivot is $a_{11} = 1$, so $m_{21} = 2$ and $m_{31} = 3$:
$$
\begin{align*}
R_2 - 2R_1 &= (2, 8, 5) - (2, 8, 14) = (0, 0, -9) \\
R_3 - 3R_1 &= (3, 6, 9) - (3, 12, 21) = (0, -6, -12)
\end{align*}
$$
$$
A^{(2)} = M^{(1)}A = \begin{bmatrix} 1 & 4 & 7 \\ 0 & \boxed{0} & -9 \\ 0 & -6 & -12 \end{bmatrix}, \qquad
M^{(1)} = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ -3 & 0 & 1 \end{bmatrix}
$$
The pivot at $(2, 2)$ is zero. **Swap rows 2 and 3:**
$$
P^{(2)} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \qquad
U = P^{(2)}M^{(1)}A = \begin{bmatrix} 1 & 4 & 7 \\ 0 & -6 & -12 \\ 0 & 0 & -9 \end{bmatrix}
$$
The matrix is already upper triangular, so $m_{32} = 0/(-6) = 0$ and $M^{(2)} = I$.

**(b) Rearranging to $PA = LU$**

Start from $P^{(2)}M^{(1)}A = U$. We want the permutation next to $A$. Insert $I = \big[P^{(2)}\big]^{\top}P^{(2)}$:
$$
P^{(2)}M^{(1)}\underbrace{\big[P^{(2)}\big]^{\top}P^{(2)}}_{I}A = U
\implies
\underbrace{P^{(2)}M^{(1)}\big[P^{(2)}\big]^{\top}}_{\tilde M^{(1)}}\;P^{(2)}A = U
$$
Compute $\tilde M^{(1)}$ in two moves. Left-multiplying by $P^{(2)}$ swaps rows 2 and 3, and right-multiplying by $\big[P^{(2)}\big]^{\top}$ swaps columns 2 and 3:
$$
M^{(1)} = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ -3 & 0 & 1 \end{bmatrix}
\xrightarrow{\text{rows } 2\leftrightarrow3}
\begin{bmatrix} 1 & 0 & 0 \\ -3 & 0 & 1 \\ -2 & 1 & 0 \end{bmatrix}
\xrightarrow{\text{cols } 2\leftrightarrow3}
\begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ -2 & 0 & 1 \end{bmatrix} = \tilde M^{(1)}
$$
The column swap restored the identity block, so $\tilde M^{(1)}$ is still unit lower triangular. The only change is that **the multipliers $2$ and $3$ traded rows**. That is why, in practice, you swap whole rows including the stored multipliers.

So, with $P = P^{(2)}$:
$$
L = \big[\tilde M^{(1)}\big]^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 2 & 0 & 1 \end{bmatrix}, \qquad
PA = \begin{bmatrix} 1 & 4 & 7 \\ 3 & 6 & 9 \\ 2 & 8 & 5 \end{bmatrix} = LU
$$
Verify row by row:
$$
\begin{align*}
\text{row 2 of } LU &= 3(1, 4, 7) + (0, -6, -12) = (3, 6, 9) \quad\checkmark \\
\text{row 3 of } LU &= 2(1, 4, 7) + (0, 0, -9) = (2, 8, 5) \quad\checkmark
\end{align*}
$$

**Storage view.** This is what the algorithm actually keeps in memory, with multipliers shown in brackets:
$$
\begin{bmatrix} 1 & 4 & 7 \\ [2] & 0 & -9 \\ [3] & -6 & -12 \end{bmatrix}
\xrightarrow{\text{swap full rows } 2\leftrightarrow3}
\begin{bmatrix} 1 & 4 & 7 \\ [3] & -6 & -12 \\ [2] & 0 & -9 \end{bmatrix}
$$
Here $L$ can be read directly from the bracketed entries.

**(c) Solve and determinant**

Permute $\mathbf{b}$ first:
$$
P\mathbf{b} = (12, 18, 15)^{\top}
$$
Forward, $L\mathbf{y} = P\mathbf{b}$:
$$
y_1 = 12, \qquad y_2 = 18 - 3(12) = -18, \qquad y_3 = 15 - 2(12) - 0 = -9
$$
Back, $U\mathbf{x} = \mathbf{y}$:
$$
x_3 = \frac{-9}{-9} = 1, \qquad x_2 = \frac{-18 - (-12)(1)}{-6} = 1, \qquad x_1 = \frac{12 - 4(1) - 7(1)}{1} = 1
$$
$$
\boxed{\,\mathbf{x} = (1, 1, 1)^{\top}\,}
$$
Check: each row sum of $A$ is $12, 15, 18$. $\checkmark$

Determinant, with $p = 1$ swap:
$$
\det(A) = (-1)^1 \cdot (1)(-6)(-9) = \boxed{\,-54\,}
$$
Cofactor check:
$$
1(72 - 30) - 4(18 - 15) + 7(12 - 24) = 42 - 12 - 84 = -54 \quad\checkmark
$$

**(d) True partial pivoting**

The handout only swapped because the pivot was $0$. Real partial pivoting picks the largest $|a_{ij}|$ at every step.

*Column 1:* $\max(|1|, |2|, |3|) = 3$ in row 3. Swap $R_1 \leftrightarrow R_3$:
$$
\begin{bmatrix} 3 & 6 & 9 \\ 2 & 8 & 5 \\ 1 & 4 & 7 \end{bmatrix}, \qquad m_{21} = \tfrac23,\quad m_{31} = \tfrac13
$$
$$
\begin{align*}
R_2 - \tfrac23R_1 &= (2, 8, 5) - (2, 4, 6) = (0, 4, -1) \\
R_3 - \tfrac13R_1 &= (1, 4, 7) - (1, 2, 3) = (0, 2, 4)
\end{align*}
$$
*Column 2:* $\max(|4|, |2|) = 4$, already in row 2, so no swap. $m_{32} = \tfrac24 = \tfrac12$:
$$
R_3 - \tfrac12R_2 = (0, 2, 4) - (0, 2, -\tfrac12) = (0, 0, \tfrac92)
$$
$$
P = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}, \quad
L = \begin{bmatrix} 1 & 0 & 0 \\ \tfrac23 & 1 & 0 \\ \tfrac13 & \tfrac12 & 1 \end{bmatrix}, \quad
U = \begin{bmatrix} 3 & 6 & 9 \\ 0 & 4 & -1 \\ 0 & 0 & \tfrac92 \end{bmatrix}
$$
Every $|l_{ij}| \le 1$. $\checkmark$

Determinant:
$$
\det A = (-1)^1(3)(4)(4.5) = -54 \quad\checkmark
$$
Both factorizations are valid. **$PA = LU$ is not unique**: it depends on which swaps you choose.

## Takeaways
- A zero pivot is fixed by one swap. The bookkeeping works out because $P^{\top}P = I$.
- $\tilde M^{(j)}$ is just $M^{(j)}$ with its multipliers permuted by the later swaps.
- $\det A = (-1)^p\prod u_{ii}$, where $p$ counts the swaps.

## Related topics
- [[Partial Pivoting]]
- [[Permutation and Multiplier Matrices]]
- [[Determinants via LU]]

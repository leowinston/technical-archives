---
tags: [math-315, exploration, lecture-3]
source: Constructed example for Sections 3.1.2 and 3.2
topics: ["[[Gaussian Elimination]]", "[[LU Decomposition]]", "[[Determinants via LU]]"]
---
# EX03 — Gaussian Elimination and LU of a 3×3 Matrix
Back to [[academic/math-315/Index|Index]]

> [!question] Problem
> Let
> $$
> A = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}
> $$
> (a) Reduce $A$ to upper triangular $U$ by Gaussian elimination, recording each multiplier.
> (b) Write each step as an elementary row matrix and derive $A = LU$.
> (c) Use the factorization to solve $A\mathbf{x} = \mathbf{b}$ for $\mathbf{b}_1 = (4, 10, 24)^{\top}$ and $\mathbf{b}_2 = (1, 1, -1)^{\top}$.
> (d) Compute $\det(A)$.

## Setup
- **Matrix type:** general square, $n = 3$
- **Pivoting needed?** Only if a pivot is $0$. We'll see that none are.
- **Method:** Gaussian elimination, then $L\mathbf{y} = \mathbf{b}$ and $U\mathbf{x} = \mathbf{y}$

## Strategy
1. Column 1: pivot $a_{11} = 2$. Compute $m_{21}$ and $m_{31}$ and eliminate.
2. Column 2: pivot $a_{22}^{(2)}$. Compute $m_{32}$ and eliminate.
3. Write $M^{(1)}$ and $M^{(2)}$, invert them by flipping signs, and multiply to get $L$.
4. Solve twice, reusing $L$ and $U$.

## Solution
**(a) Elimination**

*Step $j = 1$.* The pivot is $a_{11} = 2$.
$$
m_{21} = \frac{a_{21}}{a_{11}} = \frac{4}{2} = 2, \qquad m_{31} = \frac{a_{31}}{a_{11}} = \frac{8}{2} = 4
$$
$$
\begin{align*}
R_2 - 2R_1 &= \begin{bmatrix} 4 & 3 & 3 \end{bmatrix} - 2\begin{bmatrix} 2 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 & 1 \end{bmatrix} \\
R_3 - 4R_1 &= \begin{bmatrix} 8 & 7 & 9 \end{bmatrix} - 4\begin{bmatrix} 2 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 3 & 5 \end{bmatrix}
\end{align*}
$$
$$
A^{(2)} = \begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 3 & 5 \end{bmatrix}
$$

*Step $j = 2$.* The pivot is $a_{22}^{(2)} = 1 \neq 0$.
$$
m_{32} = \frac{a_{32}^{(2)}}{a_{22}^{(2)}} = \frac{3}{1} = 3, \qquad
R_3 - 3R_2 = \begin{bmatrix} 0 & 3 & 5 \end{bmatrix} - 3\begin{bmatrix} 0 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 2 \end{bmatrix}
$$
$$
U = \begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{bmatrix}
$$
The pivots are $2, 1, 2$, all nonzero, so no swaps were needed.

**(b) Elementary row matrices**

Each column's eliminations form one matrix. Put $-m_{ij}$ in position $(i, j)$ of $I$:
$$
M^{(1)} = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix}, \qquad
M^{(2)} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -3 & 1 \end{bmatrix}, \qquad
M^{(2)}M^{(1)}A = U
$$
Check the first step: row 2 of $M^{(1)}A$ is $-2(2, 1, 1) + (4, 3, 3) = (0, 1, 1)$. $\checkmark$

**Inverses.** $M^{(j)} = I - \boldsymbol{\ell}_j\mathbf{e}_j^{\top}$ and $\mathbf{e}_j^{\top}\boldsymbol{\ell}_j = 0$, so
$$
\big(I - \boldsymbol{\ell}_j\mathbf{e}_j^{\top}\big)\big(I + \boldsymbol{\ell}_j\mathbf{e}_j^{\top}\big) = I - \boldsymbol{\ell}_j\big(\mathbf{e}_j^{\top}\boldsymbol{\ell}_j\big)\mathbf{e}_j^{\top} = I
$$
$$
\big(M^{(1)}\big)^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 0 & 1 \end{bmatrix}, \qquad
\big(M^{(2)}\big)^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 3 & 1 \end{bmatrix}
$$

**Build $L$.** From $M^{(2)}M^{(1)}A = U$:
$$
A = \big(M^{(1)}\big)^{-1}\big(M^{(2)}\big)^{-1}U
$$
$$
L = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 3 & 1 \end{bmatrix}
= \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{bmatrix}
$$
The multipliers dropped into place with no mixing:
$$
L = \begin{bmatrix} 1 & & \\ m_{21} & 1 & \\ m_{31} & m_{32} & 1 \end{bmatrix}
$$

> [!warning] Order matters
> The product in the other order, $\big(M^{(2)}\big)^{-1}\big(M^{(1)}\big)^{-1}$, has entry $(3, 1)$ equal to $4 + 3 \cdot 2 = 10$. That mixing happens for $M^{(2)}M^{(1)}$ itself, which is why we never form it. $L$ is the product of the inverses in the order $(1)(2)$.

**Verify $LU = A$** row by row. Row $i$ of $LU$ is $\sum_k l_{ik}\,(\text{row } k \text{ of } U)$:
$$
\begin{align*}
\text{row 1} &= 1\cdot(2, 1, 1) = (2, 1, 1) \\
\text{row 2} &= 2(2, 1, 1) + 1(0, 1, 1) = (4, 3, 3) \\
\text{row 3} &= 4(2, 1, 1) + 3(0, 1, 1) + 1(0, 0, 2) = (8, 7, 9) \quad\checkmark
\end{align*}
$$

**(c) Two right-hand sides, one factorization**

*For $\mathbf{b}_1 = (4, 10, 24)^{\top}$.* Forward, $L\mathbf{y} = \mathbf{b}_1$:
$$
y_1 = 4, \qquad y_2 = 10 - 2(4) = 2, \qquad y_3 = 24 - 4(4) - 3(2) = 2
$$
Back, $U\mathbf{x} = \mathbf{y}$:
$$
x_3 = \frac{2}{2} = 1, \qquad x_2 = \frac{2 - 1(1)}{1} = 1, \qquad x_1 = \frac{4 - 1(1) - 1(1)}{2} = 1
$$
$$
\boxed{\,\mathbf{x} = (1, 1, 1)^{\top}\,}
$$

*For $\mathbf{b}_2 = (1, 1, -1)^{\top}$.* No refactoring is needed. Forward:
$$
y_1 = 1, \qquad y_2 = 1 - 2(1) = -1, \qquad y_3 = -1 - 4(1) - 3(-1) = -2
$$
Back:
$$
x_3 = \frac{-2}{2} = -1, \qquad x_2 = \frac{-1 - (-1)}{1} = 0, \qquad x_1 = \frac{1 - 0 - (-1)}{2} = 1
$$
$$
\boxed{\,\mathbf{x} = (1, 0, -1)^{\top}\,}
$$

Check $\mathbf{b}_2$: $A\mathbf{x} = (2 - 1,\ 4 - 3,\ 8 - 9) = (1, 1, -1)$. $\checkmark$

**(d) Determinant**
$$
\det(A) = \underbrace{\det(L)}_{1}\det(U) = 2 \cdot 1 \cdot 2 = \boxed{\,4\,}
$$
Check by cofactor expansion along row 1:
$$
2(27 - 21) - 1(36 - 24) + 1(28 - 24) = 12 - 12 + 4 = 4 \quad\checkmark
$$

## Cost comparison for $n = 3$
| Work | Formula | Flops |
|---|---|---|
| Factor (A only) | $\sum_{k=1}^{n-1} k(1 + 2k)$ | $1\cdot3 + 2\cdot5 = 13$ |
| $L\mathbf{y} = \mathbf{b}$ (unit $L$) | $n^2 - n$ | 6 |
| $U\mathbf{x} = \mathbf{y}$ | $n^2$ | 9 |

The second right-hand side cost only $6 + 9 = 15$ flops, with no new factorization. For large $n$ the gap is $\tfrac23 n^3$ against $2n^2$.

## Takeaways
- $L$ is the table of multipliers. It costs nothing extra to build.
- Factor once and solve many times.
- $\det(A)$ is the product of the pivots.

## Related topics
- [[Gaussian Elimination]]
- [[LU Decomposition]]
- [[Determinants via LU]]

---
tags: [math-315, exploration, lecture-3]
source: Lecture 3 handout, p. 6 (Exploration 3.2.12)
topics: ["[[LU Decomposition]]", "[[Gaussian Elimination]]", "[[Partial Pivoting]]"]
---
# Exploration 3.2.12 — A Matrix with No LU Decomposition
Back to [Index](../Index.md)

> [!question] Problem
> Prove that
> $$
> A = \begin{bmatrix} -1 & 2 & 5 \\ 2 & -4 & 5 \\ -1 & 0 & 5 \end{bmatrix}
> $$
> does not have an LU decomposition, without actually trying to compute it.

## Setup
- **Matrix type:** general $3 \times 3$
- **Claim:** there are no $L$ (unit lower triangular) and $U$ (upper triangular) with $A = LU$
- **Tools:** zero-pivot test, leading principal minors, and a direct proof by contradiction

## Strategy
1. Run one step of elimination and look at the next pivot.
2. Explain why a zero pivot rules out LU: the leading $2 \times 2$ minor is zero.
3. Make it airtight with a contradiction argument that assumes $A = LU$ and matches entries.
4. Show that $A$ is still invertible, so a row swap ($PA = LU$) fixes it.

## Solution
**Step 1: Gaussian elimination.** The pivot is $a_{11} = -1$.
$$
m_{21} = \frac{2}{-1} = -2, \qquad m_{31} = \frac{-1}{-1} = 1
$$
$$
\begin{align*}
R_2 - (-2)R_1 = R_2 + 2R_1 &= (2, -4, 5) + 2(-1, 2, 5) = (0, 0, 15) \\
R_3 - (1)R_1 &= (-1, 0, 5) - (-1, 2, 5) = (0, -2, 0)
\end{align*}
$$
$$
A^{(2)} = \begin{bmatrix} -1 & 2 & 5 \\ 0 & \boxed{0} & 15 \\ 0 & -2 & 0 \end{bmatrix}
$$
The handout shows only the $R_2$ update and leaves row 3 as it was. Either way the $(2, 2)$ entry is what matters.

**Step 2: the pivot at $(2, 2)$ is zero.** Computing $m_{32} = a_{32}^{(2)}/a_{22}^{(2)} = -2/0$ is impossible, so elimination cannot continue without a row swap.

**Why this rules out LU, via leading minors.** Row replacements with $i > j$ never change a leading principal minor $\Delta_k = \det A_{1:k,1:k}$. They only add multiples of earlier rows within the same leading block. So
$$
\Delta_2 = \det\begin{bmatrix} -1 & 2 \\ 2 & -4 \end{bmatrix} = (-1)(-4) - (2)(2) = 0
= \det\begin{bmatrix} -1 & 2 \\ 0 & 0 \end{bmatrix} = u_{11}\,u_{22}
$$
If $A = LU$ existed, then taking the leading $2\times2$ blocks gives $A_{1:2,1:2} = L_{1:2,1:2}\,U_{1:2,1:2}$, and
$$
\Delta_2 = \underbrace{1 \cdot 1}_{\det L_{1:2,1:2}} \cdot\ u_{11}u_{22} \implies u_{22} = \frac{\Delta_2}{u_{11}} = \frac{0}{-1} = 0
$$
So any LU factorization would be forced to have $u_{22} = 0$. The next argument shows that leads to a contradiction.

**Step 3: direct contradiction.** Suppose
$$
\begin{bmatrix} -1 & 2 & 5 \\ 2 & -4 & 5 \\ -1 & 0 & 5 \end{bmatrix}
= \begin{bmatrix} 1 & 0 & 0 \\ l_{21} & 1 & 0 \\ l_{31} & l_{32} & 1 \end{bmatrix}
\begin{bmatrix} u_{11} & u_{12} & u_{13} \\ 0 & u_{22} & u_{23} \\ 0 & 0 & u_{33} \end{bmatrix}
$$
Match entries in the order that determines each unknown:
$$
\begin{align*}
(1,1):&\quad u_{11} = -1 \\
(1,2):&\quad u_{12} = 2 \\
(2,1):&\quad l_{21}u_{11} = 2 \implies l_{21} = -2 \\
(2,2):&\quad l_{21}u_{12} + u_{22} = -4 \implies -4 + u_{22} = -4 \implies u_{22} = 0 \\
(3,1):&\quad l_{31}u_{11} = -1 \implies l_{31} = 1 \\
(3,2):&\quad l_{31}u_{12} + l_{32}u_{22} = 0 \implies 2 + l_{32}\cdot 0 = 0 \implies 2 = 0 \quad\text{⚡}
\end{align*}
$$
Entry $(3, 2)$ cannot be satisfied for any choice of $l_{32}$, because $u_{22} = 0$ removes $l_{32}$ from the equation. **Therefore no LU decomposition exists.** $\blacksquare$

**Step 4: $A$ is still invertible.** Cofactor expansion along row 1:
$$
\det A = -1\big((-4)(5) - (5)(0)\big) - 2\big((2)(5) - (5)(-1)\big) + 5\big((2)(0) - (-4)(-1)\big)
= 20 - 30 - 20 = -30 \neq 0
$$
So the obstruction is the **ordering of the rows**, not singularity.

**Fix: swap rows 2 and 3 up front.**
$$
P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \qquad
PA = \begin{bmatrix} -1 & 2 & 5 \\ -1 & 0 & 5 \\ 2 & -4 & 5 \end{bmatrix}
$$
Eliminate with $m_{21} = 1$ and $m_{31} = -2$:
$$
\begin{align*}
R_2 - R_1 &= (0, -2, 0) \\
R_3 + 2R_1 &= (0, 0, 15)
\end{align*}
\qquad m_{32} = \frac{0}{-2} = 0
$$
$$
PA = \underbrace{\begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ -2 & 0 & 1 \end{bmatrix}}_{L}
\underbrace{\begin{bmatrix} -1 & 2 & 5 \\ 0 & -2 & 0 \\ 0 & 0 & 15 \end{bmatrix}}_{U}
$$
Check row 3: $-2(-1, 2, 5) + (0, 0, 15) = (2, -4, 5)$. $\checkmark$

Determinant check with one swap:
$$
\det A = (-1)^1(-1)(-2)(15) = -30 \quad\checkmark
$$

> [!note] With true partial pivoting
> The rule "largest $|a_{i1}|$ goes on top" would pick row 2 (entry $2$) as the first pivot. That also produces a valid $PA = LU$. The swap above is just the smallest change that works.

## Result
- $A$ has **no** LU decomposition, because $\Delta_2 = 0$ forces $u_{22} = 0$, which makes entry $(3,2)$ inconsistent.
- $A$ is nonsingular ($\det A = -30$), and $PA = LU$ exists with $P$ swapping rows 2 and 3.

## Takeaways
- LU without pivoting exists iff every leading minor $\Delta_1, \dots, \Delta_{n-1}$ is nonzero.
- A zero pivot is a **row-order** problem, not an invertibility problem. That is the reason for [Partial Pivoting](../Topics/Partial%20Pivoting.md).

## Related topics
- [LU Decomposition](../Topics/LU%20Decomposition.md)
- [Gaussian Elimination](../Topics/Gaussian%20Elimination.md)
- [Partial Pivoting](../Topics/Partial%20Pivoting.md)

---
tags: [math-315, exploration, lecture-3]
source: Lecture 3 handout, p. 11 (Section 3.3.2 Example)
topics: ["[[LDLT Factorization]]", "[[Cholesky Factorization]]"]
---
# EX07 — LDLT Factorization of a 2×2 Symmetric Matrix
Back to [Index](../Index.md)

> [!question] Problem
> Factor the symmetric matrix
> $$
> S = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix}
> $$
> first as $S = LU$, then as $S = LDL^{\top}$. Explain why applying the row operation as a column operation too restores the symmetry.

## Setup
- **Matrix type:** symmetric ($s_{12} = s_{21} = 2$)
- **Goal:** $L$ unit lower triangular, $D$ diagonal, and the same $L$ on both sides

## Strategy
1. Do one elimination step to get $LU$.
2. Factor the pivots out of $U$: $U = D\,(D^{-1}U)$.
3. Check that $D^{-1}U = L^{\top}$.
4. Reinterpret: the same operation on the columns turns $U$ into $D$.

## Solution
**Step 1: $S = LU$.** One row operation, "subtract half of row 1 from row 2":
$$
m_{21} = \frac{2}{4} = \frac12, \qquad
R_2 - \tfrac12R_1 = (2, 3) - (2, 1) = (0, 2)
$$
$$
S = \underbrace{\begin{bmatrix} 1 & 0 \\ \tfrac12 & 1 \end{bmatrix}}_{L}
\underbrace{\begin{bmatrix} 4 & 2 \\ 0 & 2 \end{bmatrix}}_{U}
$$
This factorization is **not** symmetric: $L$ has $\tfrac12$ below the diagonal, while $U$ has $2$ above it.

**Step 2: pull out the pivots.**
$$
D = \operatorname{diag}(u_{11}, u_{22}) = \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix}, \qquad
D^{-1}U = \begin{bmatrix} \tfrac14 & 0 \\ 0 & \tfrac12 \end{bmatrix}\begin{bmatrix} 4 & 2 \\ 0 & 2 \end{bmatrix}
= \begin{bmatrix} 1 & \tfrac12 \\ 0 & 1 \end{bmatrix}
$$
Entry by entry, $(D^{-1}U)_{ij} = u_{ij}/u_{ii}$, so $(D^{-1}U)_{12} = 2/4 = \tfrac12$.

**Step 3: compare with $L^{\top}$.**
$$
L^{\top} = \begin{bmatrix} 1 & \tfrac12 \\ 0 & 1 \end{bmatrix} = D^{-1}U \quad\checkmark
$$
So $U = DL^{\top}$ and
$$
\boxed{\,S = LDL^{\top} = \begin{bmatrix} 1 & 0 \\ \tfrac12 & 1 \end{bmatrix}\begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} 1 & \tfrac12 \\ 0 & 1 \end{bmatrix}\,}
$$

This matches the general proof. There, $A = LDM^{\top}$ with $M^{\top} = D^{-1}U$, and symmetry forces $M = L$. Here we can see $M = L$ directly.

**Step 4: the column-operation view.** The row operation is $M_{21}S$ with $M_{21} = \begin{bmatrix} 1 & 0 \\ -\tfrac12 & 1 \end{bmatrix}$. Doing the same operation on the **columns** means right-multiplying by $M_{21}^{\top}$ ($C_2 \leftarrow C_2 - \tfrac12C_1$):
$$
M_{21}\,S\,M_{21}^{\top}
= \begin{bmatrix} 4 & 2 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} 1 & -\tfrac12 \\ 0 & 1 \end{bmatrix}
= \begin{bmatrix} 4 & 2 - 2 \\ 0 & 2 \end{bmatrix}
= \begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix} = D
$$
Inverting both sides gives $S = M_{21}^{-1}D\,M_{21}^{-\top} = LDL^{\top}$, which is the same answer.

**Verify:**
$$
LD = \begin{bmatrix} 4 & 0 \\ 2 & 2 \end{bmatrix}, \qquad
(LD)L^{\top} = \begin{bmatrix} 4 & 0 \\ 2 & 2 \end{bmatrix}\begin{bmatrix} 1 & \tfrac12 \\ 0 & 1 \end{bmatrix}
= \begin{bmatrix} 4 & 2 \\ 2 & 1 + 2 \end{bmatrix} = S \quad\checkmark
$$

**Bonus: Cholesky.** Both pivots are positive ($4, 2 > 0$), so $S$ is SPD, and $G = LD^{1/2}$:
$$
G = \begin{bmatrix} 1 & 0 \\ \tfrac12 & 1 \end{bmatrix}\begin{bmatrix} 2 & 0 \\ 0 & \sqrt2 \end{bmatrix}
= \begin{bmatrix} 2 & 0 \\ 1 & \sqrt2 \end{bmatrix}, \qquad
GG^{\top} = \begin{bmatrix} 4 & 2 \\ 2 & 1 + 2 \end{bmatrix} = S \quad\checkmark
$$

## Storage
| Factorization | Numbers stored |
|---|---|
| $LU$ | $l_{21}$, $u_{11}$, $u_{12}$, $u_{22}$: 4 |
| $LDL^{\top}$ | $l_{21}$, $d_1$, $d_2$: 3 $= n(n+1)/2$ |

## Takeaways
- For symmetric $A$, the upper factor is $DL^{\top}$, so it carries no new information.
- Row operation plus matching column operation gives $D$. That is the symmetric version of elimination.
- Positive $D$ leads to [Cholesky Factorization](../Topics/Cholesky%20Factorization.md).

## Related topics
- [LDLT Factorization](../Topics/LDLT%20Factorization.md)
- [Cholesky Factorization](../Topics/Cholesky%20Factorization.md)

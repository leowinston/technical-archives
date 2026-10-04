---
tags: [math-315, exploration, lecture-3]
source: Lecture 3 handout, pp. 13–14 (Section 3.3.3 Example)
topics: ["[[Cholesky Factorization]]", "[[Symmetric Positive Definite Matrices]]", "[[LDLT Factorization]]"]
---
# EX08 — Cholesky Factorization of a 3×3 SPD Matrix
Back to [Index](../Index.md)

> [!question] Problem
> Determine the Cholesky factorization $GG^{\top}$ of
> $$
> A = \begin{bmatrix} 4 & -1 & 1 \\ -1 & 4.25 & 2.75 \\ 1 & 2.75 & 3.5 \end{bmatrix}
> $$
> then use it to solve $A\mathbf{x} = \mathbf{b}$ with $\mathbf{b} = (4, 6, 7.25)^{\top}$.

## Setup
- **Matrix type:** symmetric. The diagonal $4, 4.25, 3.5$ is positive and the largest entry is on the diagonal, which is consistent with SPD.
- **Unknown:** lower triangular $G$ with $g_{kk} > 0$
- **Method:** match the entries of $A$ with those of $GG^{\top}$, column by column

## Strategy
1. Write $GG^{\top}$ symbolically.
2. Match the lower-triangle entries in the order $a_{11}, a_{21}, a_{31}, a_{22}, a_{32}, a_{33}$. Each one introduces exactly one new unknown.
3. Take positive square roots on the diagonal.
4. Solve $G\mathbf{y} = \mathbf{b}$, then $G^{\top}\mathbf{x} = \mathbf{y}$.

## Solution
**Symbolic product.**
$$
GG^{\top} =
\begin{bmatrix} g_{11} & 0 & 0 \\ g_{21} & g_{22} & 0 \\ g_{31} & g_{32} & g_{33} \end{bmatrix}
\begin{bmatrix} g_{11} & g_{21} & g_{31} \\ 0 & g_{22} & g_{32} \\ 0 & 0 & g_{33} \end{bmatrix}
=
\begin{bmatrix}
g_{11}^2 & g_{11}g_{21} & g_{11}g_{31} \\
g_{11}g_{21} & g_{21}^2 + g_{22}^2 & g_{21}g_{31} + g_{22}g_{32} \\
g_{11}g_{31} & g_{21}g_{31} + g_{22}g_{32} & g_{31}^2 + g_{32}^2 + g_{33}^2
\end{bmatrix}
$$
Each entry is $a_{ik} = \sum_{j=1}^{k} g_{ij}g_{kj}$ (row $i$ of $G$ dotted with row $k$ of $G$). The matrix is symmetric, so only the lower triangle needs matching.

**Column 1.**
$$
\begin{align*}
a_{11}:&\quad 4 = g_{11}^2 &&\implies g_{11} = 2 \quad (\text{not } -2\text{, since } g_{11} > 0) \\
a_{21}:&\quad -1 = g_{11}g_{21} = 2g_{21} &&\implies g_{21} = -0.5 \\
a_{31}:&\quad 1 = g_{11}g_{31} = 2g_{31} &&\implies g_{31} = 0.5
\end{align*}
$$
In general, column 1 of $G$ is column 1 of $A$ divided by $\sqrt{a_{11}}$.

**Column 2.**
$$
\begin{align*}
a_{22}:&\quad 4.25 = g_{21}^2 + g_{22}^2 = 0.25 + g_{22}^2 &&\implies g_{22}^2 = 4 \implies g_{22} = 2 \\
a_{32}:&\quad 2.75 = g_{21}g_{31} + g_{22}g_{32} = (-0.5)(0.5) + 2g_{32} &&\implies 2g_{32} = 3 \implies g_{32} = 1.5
\end{align*}
$$

**Column 3.**
$$
\begin{align*}
a_{33}:&\quad 3.5 = g_{31}^2 + g_{32}^2 + g_{33}^2 = 0.25 + 2.25 + g_{33}^2 \\
&\implies g_{33}^2 = 1 \implies g_{33} = 1
\end{align*}
$$
$$
\boxed{\,G = \begin{bmatrix} 2 & 0 & 0 \\ -0.5 & 2 & 0 \\ 0.5 & 1.5 & 1 \end{bmatrix}\,}
$$
Every quantity under a square root ($4$, $4$, $1$) was positive. That confirms $A$ is **SPD**. If any had been $\le 0$, the algorithm would stop and report "not SPD".

### Same computation as pseudocode
```
k = 1: g11 = sqrt(4)                            = 2
       g21 = -1 / 2                             = -0.5
       g31 =  1 / 2                             = 0.5
k = 2: g22 = sqrt(4.25 - (-0.5)^2)              = sqrt(4) = 2
       g32 = (2.75 - (0.5)(-0.5)) / 2           = 3 / 2   = 1.5
k = 3: g33 = sqrt(3.5 - 0.5^2 - 1.5^2)          = sqrt(1) = 1
```

### Connection to $LDL^{\top}$
$G = LD^{1/2}$, so $D^{1/2} = \operatorname{diag}(g_{kk}) = \operatorname{diag}(2, 2, 1)$ and $L = GD^{-1/2}$ (divide each column of $G$ by its diagonal entry):
$$
D = \operatorname{diag}(4, 4, 1), \qquad
L = \begin{bmatrix} 1 & 0 & 0 \\ -0.25 & 1 & 0 \\ 0.25 & 0.75 & 1 \end{bmatrix}
$$
The pivots of Gaussian elimination on $A$ are $4, 4, 1$, all positive, as SPD requires.

**Verify $GG^{\top} = A$.** Take rows of $G$ as vectors $\mathbf{r}_1 = (2, 0, 0)$, $\mathbf{r}_2 = (-0.5, 2, 0)$, $\mathbf{r}_3 = (0.5, 1.5, 1)$:
$$
\begin{align*}
\mathbf{r}_2\cdot\mathbf{r}_2 &= 0.25 + 4 = 4.25 \quad\checkmark \\
\mathbf{r}_2\cdot\mathbf{r}_3 &= -0.25 + 3 = 2.75 \quad\checkmark \\
\mathbf{r}_3\cdot\mathbf{r}_3 &= 0.25 + 2.25 + 1 = 3.5 \quad\checkmark
\end{align*}
$$

### Solving $A\mathbf{x} = \mathbf{b}$
Forward, $G\mathbf{y} = \mathbf{b}$:
$$
\begin{align*}
y_1 &= \frac{4}{2} = 2 \\
y_2 &= \frac{6 - (-0.5)(2)}{2} = \frac{7}{2} = 3.5 \\
y_3 &= \frac{7.25 - (0.5)(2) - (1.5)(3.5)}{1} = 7.25 - 1 - 5.25 = 1
\end{align*}
$$
Back, $G^{\top}\mathbf{x} = \mathbf{y}$ with $G^{\top} = \begin{bmatrix} 2 & -0.5 & 0.5 \\ 0 & 2 & 1.5 \\ 0 & 0 & 1 \end{bmatrix}$:
$$
\begin{align*}
x_3 &= \frac{1}{1} = 1 \\
x_2 &= \frac{3.5 - 1.5(1)}{2} = 1 \\
x_1 &= \frac{2 - (-0.5)(1) - 0.5(1)}{2} = 1
\end{align*}
$$
$$
\boxed{\,\mathbf{x} = (1, 1, 1)^{\top}\,}
$$
Check: the row sums of $A$ are $4$, $6$, $7.25$, which is $\mathbf{b}$. $\checkmark$

## Cost
| Method | Flops for large $n$ |
|---|---|
| $LU$ | $\tfrac23 n^3$ |
| Cholesky | $\tfrac13 n^3$ |

Cholesky does half the work because it only computes the lower triangle. Symmetry gives the other half for free.

## Takeaways
- Each entry equation introduces **one** new $g$. Work column by column, top to bottom.
- Choosing the positive roots makes $G$ unique.
- A failed square root is a free test that $A$ is **not** SPD.

## Related topics
- [Cholesky Factorization](../Topics/Cholesky%20Factorization.md)
- [Symmetric Positive Definite Matrices](../Topics/Symmetric%20Positive%20Definite%20Matrices.md)
- [LDLT Factorization](../Topics/LDLT%20Factorization.md)

---
tags: [math-315, exploration, lecture-3, appendix-b]
source: Lecture 3 handout, p. 19 (B.13.2 Matrix Norms, Part 3)
topics: ["[[Matrix Norms]]", "[[Vector Norms]]"]
---
# EX11 — ℓ1 Norm of a 3×2 Matrix
Back to [Index](../Index.md)

> [!question] Problem
> Let
> $$
> A = \begin{bmatrix} 1 & -2 \\ 3 & 0 \\ -1 & 4 \end{bmatrix} \in \mathbb{R}^{3\times2}
> $$
> (a) Compute $\|A\mathbf{x}\|_1$ for $\mathbf{x} = (1, 1)^{\top}$, for its normalized version, and for $\mathbf{e}_2$.
> (b) Prove that $\|A\|_1$ is the maximum column sum, and find it for this $A$.
> (c) Also find $\|A\|_\infty$ and $\|A\|_F$.

## Setup
- **Definition:** $\|A\|_1 = \max_{\|\mathbf{x}\|_1 = 1}\|A\mathbf{x}\|_1$
- **Candidates:** only unit vectors count, so $\mathbf{x}$ must be normalized before comparing

## Strategy
1. Evaluate the trial vectors. Note that $(1, 1)$ is **not** a unit vector in $\ell_1$.
2. Bound $\|A\mathbf{x}\|_1$ for every unit $\mathbf{x}$ using the triangle inequality.
3. Find the $\mathbf{x}$ that reaches the bound.

## Solution
**(a) Trial vectors**

*$\mathbf{x} = (1, 1)^{\top}$:*
$$
A\mathbf{x} = \begin{bmatrix} 1 - 2 \\ 3 + 0 \\ -1 + 4 \end{bmatrix} = \begin{bmatrix} -1 \\ 3 \\ 3 \end{bmatrix}, \qquad \|A\mathbf{x}\|_1 = 1 + 3 + 3 = 7
$$
This does **not** show $\|A\|_1 \ge 7$, because $\|\mathbf{x}\|_1 = 2$.

*Normalized, $\mathbf{x}_{\text{norm}} = \mathbf{x}/2 = \big(\tfrac12, \tfrac12\big)^{\top}$:*
$$
A\mathbf{x}_{\text{norm}} = \begin{bmatrix} -\tfrac12 \\ \tfrac32 \\ \tfrac32 \end{bmatrix}, \qquad \|A\mathbf{x}_{\text{norm}}\|_1 = \frac12 + \frac32 + \frac32 = 3.5
$$
By homogeneity this is just $7/2$.

*$\mathbf{e}_2 = (0, 1)^{\top}$, already a unit vector:*
$$
A\mathbf{e}_2 = \begin{bmatrix} -2 \\ 0 \\ 4 \end{bmatrix}, \qquad \|A\mathbf{e}_2\|_1 = 2 + 0 + 4 = 6
$$
*And $\mathbf{e}_1$:*
$$
A\mathbf{e}_1 = (1, 3, -1)^{\top}, \qquad \|A\mathbf{e}_1\|_1 = 5
$$

| Unit $\mathbf{x}$ | $\lVert A\mathbf{x}\rVert_1$ |
|---|---|
| $(\tfrac12, \tfrac12)$ | 3.5 |
| $(1, 0)$ | 5 |
| $(0, 1)$ | **6** |

**(b) Proof: $\|A\|_1 = \max_j \sum_i |a_{ij}|$**

Let $\|\mathbf{x}\|_1 = 1$ and write $c_j = \sum_{i=1}^{m}|a_{ij}|$ for the $j$-th column sum.
$$
\begin{align*}
\|A\mathbf{x}\|_1 &= \sum_{i=1}^{m}\Big|\sum_{j=1}^{n} a_{ij}x_j\Big| && \text{definition} \\
&\le \sum_{i=1}^{m}\sum_{j=1}^{n}|a_{ij}|\,|x_j| && \text{triangle inequality} \\
&= \sum_{j=1}^{n}|x_j|\sum_{i=1}^{m}|a_{ij}| = \sum_{j=1}^{n}|x_j|\,c_j && \text{swap the sums} \\
&\le \Big(\max_j c_j\Big)\sum_{j=1}^{n}|x_j| = \max_j c_j && \text{since } \|\mathbf{x}\|_1 = 1
\end{align*}
$$
So $\|A\|_1 \le \max_j c_j$. **Equality:** take $\mathbf{x} = \mathbf{e}_J$, where column $J$ has the largest sum. Then $A\mathbf{e}_J$ is column $J$, and $\|A\mathbf{e}_J\|_1 = c_J$. $\blacksquare$

*Here:* $c_1 = 1 + 3 + 1 = 5$ and $c_2 = 2 + 0 + 4 = 6$, so
$$
\boxed{\,\|A\|_1 = 6\,}, \qquad \text{attained at } \mathbf{e}_2
$$
The proof also explains the table: $\|A\mathbf{x}\|_1 \le 5|x_1| + 6|x_2|$ is a weighted average of $5$ and $6$, so no unit vector can beat $6$.

**(c) $\infty$-norm and Frobenius norm**

*$\infty$-norm = max row sum.* The same argument with rows gives
$$
|(A\mathbf{x})_i| \le \sum_j |a_{ij}|\,|x_j| \le \|\mathbf{x}\|_\infty\sum_j|a_{ij}|
$$
$$
\text{row sums: } 1 + 2 = 3, \quad 3 + 0 = 3, \quad 1 + 4 = 5 \implies \boxed{\,\|A\|_\infty = 5\,}
$$
It is attained at the **sign vector** of row 3, $\mathbf{x} = (\operatorname{sign}(-1), \operatorname{sign}(4)) = (-1, 1)$, which has $\|\mathbf{x}\|_\infty = 1$:
$$
A\mathbf{x} = \begin{bmatrix} -1 - 2 \\ -3 \\ 1 + 4 \end{bmatrix} = \begin{bmatrix} -3 \\ -3 \\ 5 \end{bmatrix}, \qquad \|A\mathbf{x}\|_\infty = 5 \quad\checkmark
$$

*Frobenius norm* (not induced):
$$
\|A\|_F = \sqrt{1 + 4 + 9 + 0 + 1 + 16} = \boxed{\,\sqrt{31} \approx 5.568\,}
$$

```
# induced 1-norm and inf-norm
norm_1   = max(sum(abs(a[i][j]) for i in rows) for j in cols)   # max column sum
norm_inf = max(sum(abs(a[i][j]) for j in cols) for i in rows)   # max row sum
norm_fro = sqrt(sum(a[i][j]^2 for all i, j))
```

## Takeaways
- Normalize before comparing. $\|A\mathbf{x}\|_1 = 7$ with $\|\mathbf{x}\|_1 = 2$ only gives a ratio of $3.5$.
- The 1-norm is the max **column** sum, attained at a standard basis vector.
- The $\infty$-norm is the max **row** sum, attained at a vector of $\pm1$ entries.

## Related topics
- [Matrix Norms](../Topics/Matrix%20Norms.md)
- [Vector Norms](../Topics/Vector%20Norms.md)

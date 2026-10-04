---
tags: [math-315, exploration, lecture-3]
source: Lecture 3 handout, p. 23 (Section 3.4.1 Condition Number, Part 5)
topics: ["[[Condition Number]]", "[[Determinants via LU]]", "[[Singular Value Decomposition]]"]
---
# EX14 — Determinant Versus Condition Number
Back to [Index](../Index.md)

> [!question] Problem
> Let $A \in \mathbb{R}^{10\times10}$ be upper triangular with $1$ on the diagonal and $-1$ everywhere above it:
> $$
> A = \begin{bmatrix}
> 1 & -1 & -1 & \cdots & -1 \\
> 0 & 1 & -1 & \cdots & -1 \\
> 0 & 0 & 1 & \cdots & -1 \\
> \vdots & & & \ddots & \vdots \\
> 0 & 0 & 0 & \cdots & 1
> \end{bmatrix}
> $$
> (a) Show $\det A = 1$.
> (b) Find $A^{-1}$ exactly and compute $\kappa_1(A)$.
> (c) Find an explicit small perturbation that makes $A$ singular.
> (d) Conclude that $\det A$ does not measure closeness to singularity.

## Setup
- **Size:** $n = 10$, but the derivation works for any $n$
- **Handout values:** $\kappa_2(A) \approx 1918$ and $\min\|A - \tilde A\|_2 \approx 0.0029$ over singular $\tilde A$

## Strategy
1. Triangular matrix, so $\det$ is the product of the diagonal.
2. Guess $A^{-1}$ from small cases, then verify $AB = I$ with a geometric sum.
3. Column sums give $\|A\|_1$ and $\|A^{-1}\|_1$.
4. Use the last column of $A^{-1}$ to build a null vector for a perturbed matrix.

## Solution
**(a) Determinant**
$$
\det A = \prod_{i=1}^{10} a_{ii} = 1^{10} = \boxed{\,1\,}
$$
By this measure $A$ looks as far from singular as the identity.

**(b) The inverse**

*Small cases.* Back substitution on $A\mathbf{x} = \mathbf{e}_n$ for $n = 4$ gives
$$
x_4 = 1, \qquad x_3 = x_4 = 1, \qquad x_2 = x_3 + x_4 = 2, \qquad x_1 = x_2 + x_3 + x_4 = 4
$$
Row $i$ reads $x_i - \sum_{j>i}x_j = 0$, so each entry is the sum of all the entries below it. That doubles each time.

*Claim.*
$$
\big(A^{-1}\big)_{ij} = \begin{cases} 1 & i = j \\ 2^{\,j-i-1} & j > i \\ 0 & j < i \end{cases}
$$

*Proof.* Call this matrix $B$ and take $j > i$:
$$
\begin{align*}
(AB)_{ij} &= \sum_{k} a_{ik}b_{kj} = b_{ij} - \sum_{k=i+1}^{j} b_{kj} \\
&= 2^{\,j-i-1} - \Big(\underbrace{\sum_{k=i+1}^{j-1}2^{\,j-k-1}}_{1 + 2 + \cdots + 2^{\,j-i-2}} + \underbrace{b_{jj}}_{1}\Big) \\
&= 2^{\,j-i-1} - \big(2^{\,j-i-1} - 1 + 1\big) = 0
\end{align*}
$$
For $i = j$, $(AB)_{ii} = a_{ii}b_{ii} = 1$. For $j < i$ both factors are upper triangular, so the entry is $0$. Hence $AB = I$. $\blacksquare$

For $n = 10$, the first row of $A^{-1}$ is
$$
(1,\ 1,\ 2,\ 4,\ 8,\ 16,\ 32,\ 64,\ 128,\ 256)
$$
The entries grow **exponentially** with $n$.

*Norms.*
$$
\begin{align*}
\|A\|_1 &= \max_j(\text{column } j \text{ sum}) = \max_j\big(1 + (j-1)\big) = n = 10 \\
\text{column } j \text{ of } A^{-1} &: 1 + \sum_{i<j}2^{\,j-i-1} = 1 + \big(2^{\,j-1} - 1\big) = 2^{\,j-1} \\
\|A^{-1}\|_1 &= 2^{\,n-1} = 2^9 = 512
\end{align*}
$$
$$
\boxed{\,\kappa_1(A) = 10 \times 512 = 5120\,}
$$
$\|A\|_\infty$ and $\|A^{-1}\|_\infty$ are the same (row 1 in each case), so $\kappa_\infty = 5120$ too. The 2-norm value is $\kappa_2 \approx 1918.5$, smaller but the same order of magnitude.

**(c) An explicit singular neighbor**

Let $\mathbf{v}$ be the last column of $A^{-1}$:
$$
\mathbf{v} = A^{-1}\mathbf{e}_n = (256,\ 128,\ 64,\ \dots,\ 2,\ 1,\ 1)^{\top}, \qquad A\mathbf{v} = \mathbf{e}_n
$$
Now subtract $\delta$ from entry $(n, 1)$ only:
$$
\tilde A = A - \delta\,\mathbf{e}_n\mathbf{e}_1^{\top}
\implies \tilde A\mathbf{v} = \mathbf{e}_n - \delta\,v_1\mathbf{e}_n = (1 - 256\,\delta)\,\mathbf{e}_n
$$
Choose $\delta = 1/256 = 2^{-(n-2)}$. Then $\tilde A\mathbf{v} = \mathbf{0}$ with $\mathbf{v} \neq \mathbf{0}$, so **$\tilde A$ is singular**:
$$
\|A - \tilde A\|_2 = \|\delta\,\mathbf{e}_n\mathbf{e}_1^{\top}\|_2 = \delta = \frac{1}{256} \approx 0.0039
$$
Changing a single entry by $0.4\%$ makes the matrix singular. The **optimal** 2-norm perturbation has size $\sigma_{10} \approx 0.00293$, which is the handout's $0.0029$. It is obtained by removing the last SVD term, as in [EX10](EX10%20-%20SVD%20and%20Condition%20Number%20of%20a%202x2%20Matrix.md).

*Kahan check:*
$$
\frac{\sigma_{10}}{\|A\|_2} = \frac{0.00293}{5.620} \approx 5.2 \times 10^{-4} \approx \frac{1}{1918.5} = \frac{1}{\kappa_2(A)} \quad\checkmark
$$

**(d) The contrast**

| Matrix | $\det$ | $\kappa_2$ | Nearly singular? |
|---|---|---|---|
| $A$ above | $1$ | $\approx 1918$ | **yes** (distance $0.0029$) |
| $0.1\,I_{10}$ | $10^{-10}$ | $1$ | **no** (perfectly conditioned) |

Scaling shows why the determinant fails. $\det(cA) = c^n\det A$ changes enormously with $c$, but $\kappa(cA) = \kappa(A)$ does not change at all. Closeness to singularity should not depend on units, so $\kappa$ is the right measure.

## Result
- $\det A = 1$, yet $\kappa_1 = 5120$ and $\kappa_2 \approx 1918$.
- A single-entry change of $1/256$ makes $A$ singular. The optimal change is $\sigma_{\min} \approx 0.0029$.
- There is no direct relationship between $\det(A)$ and $\kappa(A)$.

## Takeaways
- Use $\kappa(A)$, or $\sigma_{\min}$ relative to $\sigma_{\max}$, to judge near-singularity, never $\det A$.
- Innocent-looking triangular matrices can have exponentially large inverses.

## Related topics
- [Condition Number](../Topics/Condition%20Number.md)
- [Determinants via LU](../Topics/Determinants%20via%20LU.md)
- [Singular Value Decomposition](../Topics/Singular%20Value%20Decomposition.md)

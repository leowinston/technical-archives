---
tags: [math-315, exploration, lecture-3, appendix-b]
source: Lecture 3 handout, p. 20 (Matrix Norms in Python Example)
topics: ["[[Matrix Norms]]", "[[Singular Value Decomposition]]"]
---
# EX12 — Four Norms of a 3×3 Matrix
Back to [Index](../Index.md)

> [!question] Problem
> By hand, compute $\|A\|_1$, $\|A\|_\infty$, $\|A\|_F$ and $\|A\|_2$ for
> $$
> A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}
> $$
> and confirm the handout's values $18$, $24$, $16.8819$ and $16.8481$.

## Setup
- **Formulas:** max column sum, max row sum, root of the sum of squares, and $\sqrt{\lambda_{\max}(A^{\top}A)}$
- **Observation:** $R_3 = 2R_2 - R_1$, so $A$ is **singular** and one singular value will be $0$

## Strategy
1. Read off the 1-norm and $\infty$-norm from the absolute sums.
2. Add up the squares for the Frobenius norm.
3. For the 2-norm, find the characteristic polynomial of $A^{\top}A$ using its trace and principal minors, then take the largest root.

## Solution
**$\ell_1$ (max column sum)**
$$
\begin{align*}
\text{col 1} &: 1 + 4 + 7 = 12 \\
\text{col 2} &: 2 + 5 + 8 = 15 \\
\text{col 3} &: 3 + 6 + 9 = 18
\end{align*}
\qquad\implies \boxed{\,\|A\|_1 = 18\,}
$$

**$\ell_\infty$ (max row sum)**
$$
\begin{align*}
\text{row 1} &: 1 + 2 + 3 = 6 \\
\text{row 2} &: 4 + 5 + 6 = 15 \\
\text{row 3} &: 7 + 8 + 9 = 24
\end{align*}
\qquad\implies \boxed{\,\|A\|_\infty = 24\,}
$$

**Frobenius**
$$
\sum_{i,j}a_{ij}^2 = \sum_{k=1}^{9}k^2 = \frac{9 \cdot 10 \cdot 19}{6} = 285
\implies \boxed{\,\|A\|_F = \sqrt{285} \approx 16.8819\,}
$$

**$\ell_2$ (spectral norm)**

*Why $\lambda_{\max}$:* for $\|\mathbf{x}\|_2 = 1$,
$$
\|A\mathbf{x}\|_2^2 = \mathbf{x}^{\top}\big(A^{\top}A\big)\mathbf{x}
$$
Diagonalize the symmetric matrix $A^{\top}A = V\Lambda V^{\top}$ and set $\mathbf{z} = V^{\top}\mathbf{x}$, which is still a unit vector. Then
$$
\mathbf{x}^{\top}\big(A^{\top}A\big)\mathbf{x} = \sum_i \lambda_i z_i^2 \le \lambda_{\max}
$$
with equality at the top eigenvector. So $\|A\|_2 = \sqrt{\lambda_{\max}(A^{\top}A)}$.

*Form $A^{\top}A$.* Entry $(i, j)$ is column $i$ dotted with column $j$:
$$
A^{\top}A = \begin{bmatrix}
1 + 16 + 49 & 2 + 20 + 56 & 3 + 24 + 63 \\
\cdot & 4 + 25 + 64 & 6 + 30 + 72 \\
\cdot & \cdot & 9 + 36 + 81
\end{bmatrix}
= \begin{bmatrix} 66 & 78 & 90 \\ 78 & 93 & 108 \\ 90 & 108 & 126 \end{bmatrix}
$$

*Characteristic polynomial.* For a $3\times3$ matrix $B$,
$$
p(\lambda) = \lambda^3 - (\operatorname{tr}B)\lambda^2 + (E_2)\lambda - \det B
$$
where $E_2$ is the sum of the principal $2\times2$ minors.
$$
\begin{align*}
\operatorname{tr} &= 66 + 93 + 126 = 285 \quad (= \|A\|_F^2) \\
E_2 &= \underbrace{(66)(93) - 78^2}_{6138 - 6084 = 54} + \underbrace{(66)(126) - 90^2}_{8316 - 8100 = 216} + \underbrace{(93)(126) - 108^2}_{11718 - 11664 = 54} = 324 \\
\det &= \det(A)^2 = 0 \quad (A \text{ is singular})
\end{align*}
$$
$$
p(\lambda) = \lambda^3 - 285\lambda^2 + 324\lambda = \lambda\big(\lambda^2 - 285\lambda + 324\big)
$$
*Roots:*
$$
\lambda = 0, \qquad \lambda = \frac{285 \pm \sqrt{285^2 - 4(324)}}{2} = \frac{285 \pm \sqrt{81225 - 1296}}{2} = \frac{285 \pm \sqrt{79929}}{2}
$$
With $\sqrt{79929} \approx 282.7172$:
$$
\lambda_{\max} \approx \frac{567.7172}{2} = 283.8586, \qquad \lambda_{\text{mid}} \approx 1.1414, \qquad \lambda_{\min} = 0
$$
$$
\boxed{\,\|A\|_2 = \sqrt{283.8586} \approx 16.8481\,}
$$
The singular values are $\sigma \approx 16.848,\ 1.068,\ 0$.

## Consistency checks
- $\|A\|_F^2 = \sum\sigma_i^2 = \operatorname{tr}(A^{\top}A)$: $283.8586 + 1.1414 + 0 = 285$. $\checkmark$
- $\|A\|_2 \le \|A\|_F$: $16.848 \le 16.882$. They are close because $A$ is nearly rank 1 ($\sigma_2 \ll \sigma_1$).
- $\|A\|_2 \le \sqrt{\|A\|_1\|A\|_\infty} = \sqrt{432} \approx 20.78$. $\checkmark$
- $\sigma_3 = 0$ means $\kappa_2(A) = \sigma_1/\sigma_3 = \infty$. You cannot reliably solve $A\mathbf{x} = \mathbf{b}$ with this matrix.

## Summary
| Norm | Value | Library call |
|---|---|---|
| $\lVert A\rVert_1$ | $18$ | `norm(A, 1)` |
| $\lVert A\rVert_\infty$ | $24$ | `norm(A, inf)` |
| $\lVert A\rVert_F$ | $\sqrt{285} \approx 16.8819$ | `norm(A, "fro")` |
| $\lVert A\rVert_2$ | $\approx 16.8481$ | `norm(A, 2)` |

## Takeaways
- The 1-, $\infty$- and Frobenius norms are cheap, $O(n^2)$. The 2-norm needs an eigenvalue or SVD computation.
- $\|A\|_F^2 = \sum\sigma_i^2$, and $\|A\|_2 = \sigma_1$.

## Related topics
- [Matrix Norms](../Topics/Matrix%20Norms.md)
- [Singular Value Decomposition](../Topics/Singular%20Value%20Decomposition.md)

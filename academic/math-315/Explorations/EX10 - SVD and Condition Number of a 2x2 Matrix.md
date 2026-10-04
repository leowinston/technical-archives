---
tags: [math-315, exploration, lecture-3]
source: Constructed example for Sections 3.3 (SVD) and 3.4.1 (Condition Number, Parts 5–7)
topics: ["[[Singular Value Decomposition]]", "[[Condition Number]]", "[[Matrix Norms]]"]
---
# EX10 — SVD and Condition Number of a 2×2 Matrix
Back to [Index](../Index.md)

> [!question] Problem
> Let $A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}$ (the same matrix as [EX09](EX09%20-%20QR%20Factorization%20and%20Solve%20of%20a%202x2%20System.md)).
> (a) Compute the full SVD $A = U\Sigma V^{\top}$.
> (b) Prove $\kappa_2(A) = \sigma_1/\sigma_n$ in general, then evaluate it here.
> (c) Compare with $\kappa_1$ and $\kappa_\infty$.
> (d) Find the nearest singular matrix in the 2-norm and check Kahan's formula $1/\kappa_2 = \min\|\Delta A\|_2/\|A\|_2$.

## Setup
- **Recipe:** $\sigma_i = \sqrt{\lambda_i(A^{\top}A)}$, $\mathbf{v}_i$ = eigenvectors of $A^{\top}A$, $\mathbf{u}_i = A\mathbf{v}_i/\sigma_i$
- **Facts used:** orthogonal matrices preserve the 2-norm; $\|A\|_2 = \sigma_1$

## Strategy
1. Form $A^{\top}A$ and find its eigenvalues and eigenvectors.
2. Build $\Sigma$, $V$ and $U$, then verify by reconstructing $A$.
3. Derive $\|A^{-1}\|_2 = 1/\sigma_n$ from the SVD.
4. Remove the smallest singular term to get the nearest singular matrix.

## Solution
**(a) The SVD**

*Step 1: $A^{\top}A$.*
$$
A^{\top}A = \begin{bmatrix} 3 & 4 \\ 0 & 5 \end{bmatrix}\begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}
= \begin{bmatrix} 9 + 16 & 20 \\ 20 & 25 \end{bmatrix}
= \begin{bmatrix} 25 & 20 \\ 20 & 25 \end{bmatrix}
$$

*Step 2: eigenvalues.*
$$
\det\big(A^{\top}A - \lambda I\big) = (25 - \lambda)^2 - 400 = 0 \implies 25 - \lambda = \pm 20 \implies \lambda_1 = 45,\ \lambda_2 = 5
$$
$$
\sigma_1 = \sqrt{45} = 3\sqrt5 \approx 6.708, \qquad \sigma_2 = \sqrt5 \approx 2.236
$$
Check: $\sigma_1\sigma_2 = \sqrt{225} = 15 = |\det A|$. $\checkmark$

*Step 3: right singular vectors, the eigenvectors of $A^{\top}A$.*
$$
\begin{align*}
\lambda = 45:&\quad \begin{bmatrix} -20 & 20 \\ 20 & -20 \end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_1 = \tfrac{1}{\sqrt2}(1, 1)^{\top} \\
\lambda = 5:&\quad \begin{bmatrix} 20 & 20 \\ 20 & 20 \end{bmatrix}\mathbf{v} = \mathbf{0} \implies \mathbf{v}_2 = \tfrac{1}{\sqrt2}(1, -1)^{\top}
\end{align*}
$$

*Step 4: left singular vectors, from $A\mathbf{v}_i = \sigma_i\mathbf{u}_i$.*
$$
\begin{align*}
\mathbf{u}_1 &= \frac{A\mathbf{v}_1}{\sigma_1} = \frac{1}{3\sqrt5}\cdot\frac{1}{\sqrt2}\begin{bmatrix} 3 \\ 9 \end{bmatrix} = \frac{1}{\sqrt{10}}\begin{bmatrix} 1 \\ 3 \end{bmatrix} \\
\mathbf{u}_2 &= \frac{A\mathbf{v}_2}{\sigma_2} = \frac{1}{\sqrt5}\cdot\frac{1}{\sqrt2}\begin{bmatrix} 3 \\ -1 \end{bmatrix} = \frac{1}{\sqrt{10}}\begin{bmatrix} 3 \\ -1 \end{bmatrix}
\end{align*}
$$
Check: $\mathbf{u}_1^{\top}\mathbf{u}_2 = \tfrac{1}{10}(3 - 3) = 0$, and $\|\mathbf{u}_i\|_2 = 1$. $\checkmark$

$$
\boxed{\,
A = \underbrace{\frac{1}{\sqrt{10}}\begin{bmatrix} 1 & 3 \\ 3 & -1 \end{bmatrix}}_{U}
\underbrace{\begin{bmatrix} 3\sqrt5 & 0 \\ 0 & \sqrt5 \end{bmatrix}}_{\Sigma}
\underbrace{\frac{1}{\sqrt2}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}}_{V^{\top}}
\,}
$$

*Verify* with the outer-product form $A = \sigma_1\mathbf{u}_1\mathbf{v}_1^{\top} + \sigma_2\mathbf{u}_2\mathbf{v}_2^{\top}$:
$$
\begin{align*}
\sigma_1\mathbf{u}_1\mathbf{v}_1^{\top} &= \frac{3\sqrt5}{\sqrt{20}}\begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix} = \frac32\begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix} \\
\sigma_2\mathbf{u}_2\mathbf{v}_2^{\top} &= \frac{\sqrt5}{\sqrt{20}}\begin{bmatrix} 3 & -3 \\ -1 & 1 \end{bmatrix} = \frac12\begin{bmatrix} 3 & -3 \\ -1 & 1 \end{bmatrix} \\
\text{sum} &= \begin{bmatrix} 1.5 + 1.5 & 1.5 - 1.5 \\ 4.5 - 0.5 & 4.5 + 0.5 \end{bmatrix} = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix} \quad\checkmark
\end{align*}
$$

**(b) $\kappa_2 = \sigma_1/\sigma_n$, the general proof**

*Orthogonal factors don't change the 2-norm.* For orthogonal $W$ and any $B$:
$$
\|WB\mathbf{x}\|_2 = \|B\mathbf{x}\|_2 \implies \|WB\|_2 = \|B\|_2
$$
Also $\|BW\|_2 = \max_{\|\mathbf{x}\|=1}\|BW\mathbf{x}\|_2 = \max_{\|\mathbf{z}\|=1}\|B\mathbf{z}\|_2 = \|B\|_2$, because $\mathbf{z} = W\mathbf{x}$ ranges over the whole unit sphere. This gives an **equality**, which is stronger than the handout's submultiplicative bound.

*Norm of a diagonal matrix.*
$$
\|\Sigma\mathbf{x}\|_2^2 = \sum_i \sigma_i^2x_i^2 \le \sigma_1^2\sum_i x_i^2
$$
Equality holds at $\mathbf{x} = \mathbf{e}_1$, so $\|\Sigma\|_2 = \sigma_1$. In the same way, $\Sigma^{-1} = \operatorname{diag}(1/\sigma_i)$ has largest entry $1/\sigma_n$, so $\|\Sigma^{-1}\|_2 = 1/\sigma_n$.

*Combine.*
$$
\begin{align*}
\|A\|_2 &= \|U\Sigma V^{\top}\|_2 = \|\Sigma\|_2 = \sigma_1 \\
A^{-1} &= \big(U\Sigma V^{\top}\big)^{-1} = V\Sigma^{-1}U^{\top} \implies \|A^{-1}\|_2 = \|\Sigma^{-1}\|_2 = \frac{1}{\sigma_n} \\
\kappa_2(A) &= \|A\|_2\|A^{-1}\|_2 = \frac{\sigma_1}{\sigma_n}
\end{align*}
$$
*Here:*
$$
\kappa_2(A) = \frac{3\sqrt5}{\sqrt5} = \boxed{\,3\,}
$$
The matrix is well-conditioned.

**(c) Other norms**
$$
A^{-1} = \frac{1}{15}\begin{bmatrix} 5 & 0 \\ -4 & 3 \end{bmatrix}
$$
$$
\begin{align*}
\|A\|_1 &= \max(3 + 4,\ 0 + 5) = 7, & \|A^{-1}\|_1 &= \max\!\left(\tfrac{9}{15},\ \tfrac{3}{15}\right) = 0.6, & \kappa_1 &= 4.2 \\
\|A\|_\infty &= \max(3,\ 9) = 9, & \|A^{-1}\|_\infty &= \max\!\left(\tfrac{5}{15},\ \tfrac{7}{15}\right) = \tfrac{7}{15}, & \kappa_\infty &= 4.2
\end{align*}
$$
The different norms give numbers of the same size ($3$ against $4.2$). The condition number depends on the norm, but only by modest constant factors.

**(d) Nearest singular matrix**

Drop the smallest singular term:
$$
\tilde A = A - \sigma_2\mathbf{u}_2\mathbf{v}_2^{\top} = \frac32\begin{bmatrix} 1 & 1 \\ 3 & 3 \end{bmatrix}
= \begin{bmatrix} 1.5 & 1.5 \\ 4.5 & 4.5 \end{bmatrix}
$$
This has rank 1, so it is singular. The size of the change is
$$
\|\Delta A\|_2 = \big\|\sigma_2\mathbf{u}_2\mathbf{v}_2^{\top}\big\|_2 = \sigma_2 = \sqrt5
$$
$$
\frac{\|\Delta A\|_2}{\|A\|_2} = \frac{\sqrt5}{3\sqrt5} = \frac13 = \frac{1}{\kappa_2(A)} \quad\checkmark
$$
No smaller perturbation works. If $\|\Delta A\|_2 < \sigma_n$, then for every unit $\mathbf{x}$, $\|(A + \Delta A)\mathbf{x}\|_2 \ge \|A\mathbf{x}\|_2 - \|\Delta A\mathbf{x}\|_2 \ge \sigma_n - \|\Delta A\|_2 > 0$, so $A + \Delta A$ is still nonsingular.

## Takeaways
- The SVD gives $\|A\|_2$, $\|A^{-1}\|_2$, $\kappa_2$ and the distance to singularity all at once.
- $\sigma_n$ is exactly how far $A$ is from being singular in the 2-norm.
- $\kappa_2 = 1$ exactly for orthogonal matrices, since all $\sigma_i = 1$.

## Related topics
- [Singular Value Decomposition](../Topics/Singular%20Value%20Decomposition.md)
- [Condition Number](../Topics/Condition%20Number.md)
- [Matrix Norms](../Topics/Matrix%20Norms.md)

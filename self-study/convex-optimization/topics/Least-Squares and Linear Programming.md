---
tags: [convex-optimization, topic, ch-1]
source: Boyd & Vandenberghe §1.2 (pp. 4–7)
---
# Least-Squares and Linear Programming
Back to [[self-study/convex-optimization/Index|Index]] · Section 1.2

## Least-squares
No constraints, and the objective is a sum of squares:
$$
\text{minimize } \lVert Ax - b \rVert_2^2 = \sum_{i=1}^{k} (a_i^{\top}x - b_i)^2
$$
Setting the gradient to zero gives the **normal equations**
$$
\boxed{\,A^{\top}A\,x = A^{\top}b\,} \quad\Rightarrow\quad x^\star = (A^{\top}A)^{-1}A^{\top}b.
$$
Cost is about $n^2k$ flops. Weighted and regularized ($+\rho\lVert x\rVert_2^2$) versions are still least-squares.

## Linear programming
Objective and constraints are all affine:
$$
\begin{array}{ll}
\text{minimize} & c^{\top}x \\
\text{subject to} & a_i^{\top}x \le b_i, \quad i = 1, \dots, m
\end{array}
$$
No closed form, but interior-point methods solve it in about $n^2m$ flops per iteration. **Chebyshev approximation** $\min_x \max_i \lvert a_i^{\top}x - b_i\rvert$ becomes an LP with one extra variable $t$.

## Explorations
- [[EX08 - Least Squares by Gradient Descent]]

See also: [[Least Squares by Gradient Descent]], [[Linear Programs]]

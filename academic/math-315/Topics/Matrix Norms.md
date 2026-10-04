---
tags: [math-315, topic, lecture-3, appendix-b]
---
# Matrix Norms
Back to [Index](../Index.md) · Appendix B.13.2

## Definition
A matrix norm satisfies the three vector-norm properties. It is **submultiplicative** if also
$$
\|AB\| \le \|A\|\,\|B\|
$$

## Induced norms
Every vector norm induces a matrix norm:
$$
\|A\| = \sup_{\mathbf{x} \neq \mathbf{0}} \frac{\|A\mathbf{x}\|}{\|\mathbf{x}\|} = \max_{\|\mathbf{x}\| = 1}\|A\mathbf{x}\|
$$
By construction, $\|A\mathbf{x}\| \le \|A\|\,\|\mathbf{x}\|$.

## Formulas
| Norm | Formula | Attained at |
|---|---|---|
| $\lVert A\rVert_1$ | max column sum $\max_j \sum_i \lvert a_{ij}\rvert$ | $\mathbf{e}_J$ |
| $\lVert A\rVert_\infty$ | max row sum $\max_i \sum_j \lvert a_{ij}\rvert$ | sign vector of row $I$ |
| $\lVert A\rVert_2$ | $\sqrt{\lambda_{\max}(A^{\top}A)} = \sigma_1$ | top right singular vector |
| $\lVert A\rVert_F$ | $\big(\sum_{i,j} a_{ij}^2\big)^{1/2}$ | not induced |

## Why the 1-norm is the column sum
For $\|\mathbf{x}\|_1 = 1$:
$$
\|A\mathbf{x}\|_1 \le \sum_j |x_j|\sum_i |a_{ij}| \le \max_j \sum_i |a_{ij}|
$$
Equality holds at $\mathbf{x} = \mathbf{e}_J$, where $J$ is the largest column.

## Example
$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}: \quad
\|A\|_1 = 18,\ \ \|A\|_\infty = 24,\ \ \|A\|_F = \sqrt{285},\ \ \|A\|_2 \approx 16.848
$$

## Explorations
- [EX11 - l1 Norm of a 3x2 Matrix](../Explorations/EX11%20-%20l1%20Norm%20of%20a%203x2%20Matrix.md)
- [EX12 - Four Norms of a 3x3 Matrix](../Explorations/EX12%20-%20Four%20Norms%20of%20a%203x3%20Matrix.md)

See also: [Vector Norms](Vector%20Norms.md), [Condition Number](Condition%20Number.md)

---
tags: [math-315, topic, lecture-3]
---
# Condition Number
Back to [[academic/math-315/Index|Index]] · Section 3.4.1

## Definition
$$
\kappa(A) = \|A\|\,\|A^{-1}\|
$$
It depends on the induced norm used.

## Error bound
$$
\frac{\|\mathbf{x} - \hat{\mathbf{x}}\|}{\|\mathbf{x}\|} \le \kappa(A)\,\frac{\|\mathbf{b} - A\hat{\mathbf{x}}\|}{\|\mathbf{b}\|}
$$
**Proof.** $\mathbf{x} - \hat{\mathbf{x}} = A^{-1}\mathbf{r}$, so $\|\mathbf{x} - \hat{\mathbf{x}}\| \le \|A^{-1}\|\,\|\mathbf{r}\|$. Also $\|\mathbf{b}\| \le \|A\|\,\|\mathbf{x}\|$, so $1/\|\mathbf{x}\| \le \|A\|/\|\mathbf{b}\|$. Multiply the two.

## Properties
- $\kappa(A) \ge 1$, since $1 = \|I\| = \|AA^{-1}\| \le \|A\|\,\|A^{-1}\|$.
- $\kappa_2(A) = \sigma_1/\sigma_n$, since orthogonal factors don't change the 2-norm.
- $\kappa_2(Q) = 1$ for orthogonal $Q$.
- $1/\kappa_p(A) = \min\big\{\|\Delta A\|_p/\|A\|_p : A + \Delta A \text{ singular}\big\}$ (Kahan).
- $\det(A)$ says **nothing** about $\kappa(A)$.

## Interpretation
When $\kappa$ is large, $A$ is ill-conditioned, or nearly singular, and a small residual may hide a large error. When $\kappa \approx 1$, a small residual means a small error. Libraries provide it as `cond(A, p)`.

## Example
$$
\kappa_1\begin{bmatrix} 0.913 & 0.659 \\ 0.457 & 0.330 \end{bmatrix} \approx 1.70 \times 10^4
$$

## Explorations
- [[EX10 - SVD and Condition Number of a 2x2 Matrix]]
- [[EX13 - Small Residual, Large Error]]
- [[EX14 - Determinant Versus Condition Number]]

See also: [[Forward and Backward Error]], [[Singular Value Decomposition]], [[Matrix Norms]]

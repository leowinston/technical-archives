---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §10.3, Lemma 10.2
---
# Levenberg-Marquardt Method
Back to [Index](../Index.md) · Nocedal & Wright §10.3

[Gauss-Newton](Gauss-Newton%20Method.md) with a [trust region](Trust-Region%20Methods.md) instead of a line search.

## Subproblem
$$
\min_p\; \tfrac12\lVert J_k\,p + r_k\rVert_2^2 \qquad \text{subject to}\qquad \lVert p\rVert \le \Delta_k
$$
The model Hessian is $B_k = J_k^{\top}J_k$.

## Solution
$p^{LM}$ solves it if and only if there is $\lambda \ge 0$ with
$$
\boxed{\,(J^{\top}J + \lambda I)\,p^{LM} = -J^{\top}r, \qquad \lambda\,(\Delta - \lVert p^{LM}\rVert) = 0\,}
$$
- Gauss-Newton step inside the region: $\lambda = 0$.
- Otherwise $\lambda > 0$ and $\lVert p^{LM}\rVert = \Delta$.

## Between two methods
- $\lambda \to 0$: the Gauss-Newton step.
- $\lambda \to \infty$: $p \approx -\tfrac1\lambda J^{\top}r$, a short steepest descent step.

$J^{\top}J + \lambda I$ is positive definite for every $\lambda > 0$, so the step exists even when $J$ is **rank deficient**, which is exactly where Gauss-Newton breaks.

## It is a linear least-squares problem
The equations above are the [normal equations](../../../academic/math-315/Topics%202/Normal%20Equations.md) of
$$
\min_p\; \frac12\left\lVert\begin{bmatrix} J \\ \sqrt{\lambda}\,I \end{bmatrix}p + \begin{bmatrix} r \\ 0 \end{bmatrix}\right\rVert_2^2
$$
so they can be solved by [QR](../../../academic/math-315/Topics%202/Least%20Squares%20via%20QR.md) without forming $J^{\top}J$. This is ridge regression on the linearized problem: $\lambda$ is the regularization weight in the [Bias-Variance Tradeoff](../ml-notebook/Bias-Variance%20Tradeoff.md).

## Convergence
- **Global:** if each step reduces the model at least as much as [The Cauchy Point](The%20Cauchy%20Point.md), then $J_k^{\top}r_k \to 0$.
- **Local:** near a solution where $J^{\top}J$ dominates the Hessian, the trust region becomes inactive and the method takes Gauss-Newton steps, with their fast rate.

See also: [Newton's Method with Hessian Modification](Newton's%20Method%20with%20Hessian%20Modification.md), the same $+\lambda I$ shift for general $f$

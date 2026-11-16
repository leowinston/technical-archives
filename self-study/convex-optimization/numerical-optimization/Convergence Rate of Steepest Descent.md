---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §3.3, Theorems 3.3 and 3.4
---
# Convergence Rate of Steepest Descent
Back to [Index](../Index.md) · Nocedal & Wright §3.3

Steepest descent always converges ([Zoutendijk's Theorem](Zoutendijk's%20Theorem.md)), and it can be painfully slow. The [condition number](../../../academic/math-315/Topics%201/Condition%20Number.md) decides.

## Model problem
$$
f(x) = \tfrac12x^{\top}Qx - b^{\top}x, \qquad Q \text{ symmetric positive definite}
$$
$\nabla f = Qx - b$, and the minimizer solves $Qx^* = b$. The exact line search step along $-\nabla f_k$ is
$$
\alpha_k = \frac{\nabla f_k^{\top}\nabla f_k}{\nabla f_k^{\top}Q\,\nabla f_k}
$$

## Theorem
With eigenvalues $0 < \lambda_1 \le \cdots \le \lambda_n$ of $Q$ and $\lVert x\rVert_Q^2 = x^{\top}Qx$:
$$
\boxed{\,\lVert x_{k+1} - x^*\rVert_Q^2 \le \left(\frac{\lambda_n - \lambda_1}{\lambda_n + \lambda_1}\right)^{2}\lVert x_k - x^*\rVert_Q^2 = \left(\frac{\kappa - 1}{\kappa + 1}\right)^{2}\lVert x_k - x^*\rVert_Q^2\,}
$$
with $\kappa = \lambda_n/\lambda_1$.

## Reading it
- [Linear convergence](../../../academic/math-315/Topics%204/Order%20of%20Convergence.md), with a constant that depends only on $\kappa$.
- $\kappa = 1$: circular contours, the gradient points at $x^*$, one step.
- $\kappa = 800$: the factor is $0.995$. After $500$ steps $f - f^*$ is still $8\%$ of where it started.
- Geometrically the contours are long ellipses and the iterates zigzag across the valley.

## General $f$
The same bound holds near a minimizer $x^*$ with $\nabla^2 f(x^*)$ positive definite, using its eigenvalues. Exact line searches do not help: an inexact search can only be slower.

## The fix
Change the metric. [Newton's method](Newton's%20Method%20for%20Optimization.md) uses $B_k = \nabla^2 f_k$, which turns the ellipses back into circles.

See also: [Gradient Descent as a Fixed Point Iteration](Gradient%20Descent%20as%20a%20Fixed%20Point%20Iteration.md), where the same factor $\tfrac{\kappa-1}{\kappa+1}$ appears as a contraction constant · [EX08 - Least Squares by Gradient Descent](../explorations/EX08%20-%20Least%20Squares%20by%20Gradient%20Descent.md)

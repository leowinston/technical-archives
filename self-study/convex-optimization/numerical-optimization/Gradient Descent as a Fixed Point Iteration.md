---
tags: [convex-optimization, topic, numerical-optimization]
source: connects Nocedal & Wright §3.3 with Math 315 Lecture 7 and my Banach proof
---
# Gradient Descent as a Fixed Point Iteration
Back to [Index](../Index.md) · Connection note

Gradient descent with a fixed step $\alpha$ is [fixed point iteration](../../../academic/math-315/Topics%204/Fixed%20Point%20Iteration.md) in $\R^n$:
$$
x_{k+1} = g(x_k), \qquad g(x) = x - \alpha\,\nabla f(x)
$$
Fixed points of $g$ are exactly the stationary points $\nabla f(x^*) = 0$.

## When $g$ is a contraction
Suppose $m\,I \preceq \nabla^2 f(x) \preceq L\,I$ for all $x$, with $m > 0$. Then
$$
g(x) - g(y) = (I - \alpha H)(x - y), \qquad H = \int_0^1\nabla^2 f\big(y + t(x - y)\big)\,dt
$$
The eigenvalues of $I - \alpha H$ lie in $[1 - \alpha L,\ 1 - \alpha m]$, so
$$
\boxed{\,\lVert g(x) - g(y)\rVert_2 \le q\,\lVert x - y\rVert_2, \qquad q = \max\{\lvert 1 - \alpha m\rvert,\ \lvert 1 - \alpha L\rvert\}\,}
$$
and $q < 1$ exactly when $0 < \alpha < 2/L$.

## What Banach gives
$\R^n$ is complete, so [Banach's Fixed Point Theorem](../../../archive/proofs/Explorations/Banach's%20Fixed%20Point%20Theorem.md) applies:
- a minimizer $x^*$ **exists and is unique**;
- gradient descent converges to it from **every** $x_0$;
- $\lVert x_k - x^*\rVert \le q^k\,\lVert x_0 - x^*\rVert$, and from Step 2 of the proof, $\lVert x_k - x^*\rVert \le \dfrac{q^k}{1 - q}\lVert x_1 - x_0\rVert$, a bound computable after one step.

## Best step
$q$ is smallest when $1 - \alpha m = -(1 - \alpha L)$:
$$
\alpha = \frac{2}{m + L}, \qquad q = \frac{L - m}{L + m} = \frac{\kappa - 1}{\kappa + 1}
$$
the same factor as in [Convergence Rate of Steepest Descent](Convergence%20Rate%20of%20Steepest%20Descent.md).

## Same theorem, three places
| Space | Map | Fixed point |
|---|---|---|
| $\R$ | $g(x)$ with $\lvert g'\rvert \le G < 1$ | root of $x - g(x)$ ([Math 315](../../../academic/math-315/Topics%204/Fixed%20Point%20Iteration.md)) |
| $\R^n$ | $x - \alpha\nabla f(x)$ | minimizer of $f$ |
| continuous functions | $\phi \mapsto y_0 + \int F(s, \phi)\,ds$ | solution of an ODE ([Math 212](../../../academic/math-212/Topics%201/Existence%20and%20Uniqueness%20Theorems.md)) |

[Newton's method](Newton's%20Method%20for%20Optimization.md) is also a fixed point iteration, with the derivative of $g$ equal to zero at $x^*$. That is why it is quadratic instead of linear.

## Explorations
- [EX12 - Gradient Descent as a Contraction](../explorations/EX12%20-%20Gradient%20Descent%20as%20a%20Contraction.md)

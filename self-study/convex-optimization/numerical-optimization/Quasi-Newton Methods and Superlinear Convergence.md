---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §3.3, Theorems 3.6 and 3.7
---
# Quasi-Newton Methods and Superlinear Convergence
Back to [Index](../Index.md) · Nocedal & Wright §3.3

Get most of [Newton's](Newton's%20Method%20for%20Optimization.md) speed without ever forming the Hessian.

## The step
$$
p_k = -B_k^{-1}\,\nabla f_k
$$
where $B_k$ is a symmetric positive definite approximation to $\nabla^2 f_k$, updated after every step using only gradients.

## The secant equation
With $s_k = x_{k+1} - x_k$ and $y_k = \nabla f_{k+1} - \nabla f_k$, the new matrix is required to satisfy
$$
B_{k+1}\,s_k = y_k
$$
In one dimension this reads $B_{k+1} = \dfrac{f'(x_{k+1}) - f'(x_k)}{x_{k+1} - x_k}$, which is the [secant method](../../../academic/math-315/Topics%204/Secant%20Method.md) applied to $f'$. In $n$ dimensions the equation leaves freedom, and BFGS fills it with a rank-two update.

## When is it superlinear?
**Theorem (Dennis–Moré).** Suppose $x_k \to x^*$ with $\nabla f(x^*) = 0$ and $\nabla^2 f(x^*)$ positive definite, and the steps are $x_{k+1} = x_k + p_k$. Then the convergence is superlinear **if and only if**
$$
\boxed{\,\lim_{k\to\infty}\frac{\lVert(B_k - \nabla^2 f(x^*))\,p_k\rVert}{\lVert p_k\rVert} = 0\,}
$$
$B_k$ does not have to converge to the Hessian. It only has to act like the Hessian **along the search directions**.

Under the same condition, the unit step $\alpha_k = 1$ is accepted by the [Wolfe Conditions](Wolfe%20Conditions.md) for all large $k$ (with $c_1 \le \tfrac12$), so a line search should always try $\alpha = 1$ first.

## The three rates
| Method | Per-step cost | [Order](../../../academic/math-315/Topics%204/Order%20of%20Convergence.md) |
|---|---|---|
| Steepest descent | gradient | linear, factor $\left(\tfrac{\kappa-1}{\kappa+1}\right)^2$ |
| Quasi-Newton | gradient + $O(n^2)$ update | superlinear |
| Newton | gradient + Hessian + $O(n^3)$ solve | quadratic |

The pattern is the one-dimensional one: bisection, secant, Newton.

See also: [Line Search Methods](Line%20Search%20Methods.md), [Convergence Rate of Steepest Descent](Convergence%20Rate%20of%20Steepest%20Descent.md)

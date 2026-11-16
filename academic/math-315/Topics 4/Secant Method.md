---
tags: [math-315, topic, lecture-7]
---
# Secant Method
Back to [Index](../Index.md) · Lecture 7

[Newton's method](Newton's%20Method.md) without the derivative: replace the tangent with the line through the last two iterates.

## Iteration
Approximate $f'(x_n)$ by a [finite difference](../Topics%202/Finite%20Difference%20Formulas.md):
$$
f'(x_n) \approx \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}
$$
$$
\boxed{\,x_{n+1} = x_n - f(x_n)\,\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}\,}
$$
It needs two starting guesses $x_0, x_1$ and one new function value per step.

## Convergence
Near a simple root the errors satisfy $e_{n+1} \approx C\,e_n\,e_{n-1}$. Trying $e_{n+1} \approx k\,e_n^{p}$ gives $p^2 = p + 1$, so
$$
p = \frac{1 + \sqrt5}{2} \approx 1.618
$$
**Superlinear**, and local like Newton: it needs $x_0$ and $x_1$ close to $x^*$.

## Versus Newton
Newton costs one $f$ and one $f'$ per step. Two secant steps cost the same two evaluations and give order $1.618^2 \approx 2.62$, so per function evaluation the secant method is often the faster one.

## As interpolation
$x_{n+1}$ is the root of the degree-1 [interpolating polynomial](../Topics%202/Polynomial%20Interpolation.md) through the last two points. Using three points and a quadratic gives [Inverse Quadratic Interpolation](Inverse%20Quadratic%20Interpolation.md).

The quasi-Newton methods of optimization are this idea in $n$ dimensions: build the derivative from differences of past gradients ([Quasi-Newton Methods and Superlinear Convergence](../../../self-study/convex-optimization/numerical-optimization/Quasi-Newton%20Methods%20and%20Superlinear%20Convergence.md)).

See also: [False Position Method](False%20Position%20Method.md), [Order of Convergence](Order%20of%20Convergence.md)

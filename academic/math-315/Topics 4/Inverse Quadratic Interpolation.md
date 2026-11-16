---
tags: [math-315, topic, lecture-7]
---
# Inverse Quadratic Interpolation
Back to [Index](../Index.md) · Lecture 7

Use the last three iterates instead of two.

## The problem with a quadratic in $x$
Fit a parabola through $(x_{n-2}, f_{n-2})$, $(x_{n-1}, f_{n-1})$, $(x_n, f_n)$ and take its root. But a parabola has two roots, or none that are real, so there is a choice to make each step.

## Flip the axes
If $f$ has an inverse near the root, then $x^* = f^{-1}(0)$. Interpolate $x$ as a function of $y$ through
$$
(f_{n-2},\, x_{n-2}), \quad (f_{n-1},\, x_{n-1}), \quad (f_n,\, x_n)
$$
to get a quadratic $p(y) \approx f^{-1}(y)$, and evaluate it at $y = 0$:
$$
\boxed{\,x_{n+1} = p(0)\,}
$$
There is no root to choose: $p(0)$ is a single number. In [Lagrange form](../Topics%202/Lagrange%20Form.md),
$$
x_{n+1} = \frac{f_{n-1}f_n}{(f_{n-2}-f_{n-1})(f_{n-2}-f_n)}x_{n-2} + \frac{f_{n-2}f_n}{(f_{n-1}-f_{n-2})(f_{n-1}-f_n)}x_{n-1} + \frac{f_{n-2}f_{n-1}}{(f_n-f_{n-2})(f_n-f_{n-1})}x_n
$$

## Convergence
Local and superlinear:
$$
e_{n+1} \approx K\,e_n^{p}, \qquad p \approx 1.839
$$
Slower than [Newton](Newton's%20Method.md), slightly faster than [secant](Secant%20Method.md), still one function evaluation per step. It breaks down if two of the three $f$ values are equal.

## In practice
Brent's method combines it with secant and [bisection](Bisection%20Method.md): take the fast step when it stays inside the bracket, bisect when it does not. That is what [Root Finding in Python](Root%20Finding%20in%20Python.md) uses.

See also: [Order of Convergence](Order%20of%20Convergence.md), [Quadratic Interpolation Search](Quadratic%20Interpolation%20Search.md) for the minimization version

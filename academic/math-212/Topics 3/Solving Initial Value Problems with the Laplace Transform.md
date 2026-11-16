---
tags:
  - math-212
  - topic
  - chapter-6
---
# Solving Initial Value Problems with the Laplace Transform
Back to [Index](../Index.md) · Chapter 6.2 · Enrichment handout, Parts IV–V

Three steps: transform the equation (calculus), solve for $Y(s)$ (algebra), invert (table lookup).

## First order
$y' + 2y = 1$, $y(0) = 0$. Transform with $\mathcal{L}\{y'\} = sY - y(0)$:
$$
(s+2)Y = \frac1s \quad\Longrightarrow\quad Y = \frac{1}{s(s+2)} = \frac{1/2}{s} - \frac{1/2}{s+2}
$$
$$
y(t) = \tfrac12\left(1 - e^{-2t}\right)
$$

## Second order
$y'' + 3y' + 2y = 0$, $y(0) = 1$, $y'(0) = 0$:
$$
\left(s^2Y - s\right) + 3\left(sY - 1\right) + 2Y = 0 \quad\Longrightarrow\quad Y = \frac{s+3}{(s+1)(s+2)} = \frac{2}{s+1} - \frac{1}{s+2}
$$
$$
y(t) = 2e^{-t} - e^{-2t}
$$
Check: $y(0) = 1$ and $y'(0) = -2 + 2 = 0$.

## The pattern
For $ay'' + by' + cy = g(t)$ with $y(0) = y_0$, $y'(0) = y_0'$:
$$
Y(s) = \frac{(as + b)\,y_0 + a\,y_0' + G(s)}{as^2 + bs + c}
$$
The denominator is the characteristic polynomial. Its roots, the **poles** of $Y$, are the exponents in the solution, so the transform finds the same $e^{rt}$ as [variation of parameters](../Topics%202/Variation%20of%20Parameters.md) or undetermined coefficients, with the initial conditions already applied.

See also: [Transforms of Derivatives](Transforms%20of%20Derivatives.md), [Inverse Transforms and Partial Fractions](Inverse%20Transforms%20and%20Partial%20Fractions.md)

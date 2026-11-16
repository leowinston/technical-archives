---
tags: [math-315, topic, lecture-7]
---
# Order of Convergence
Back to [Index](../Index.md) · Lecture 7

How fast the error shrinks once the iteration is close.

## Definition
Suppose $x_n \to x^*$ with $x_n \neq x^*$. If there are $\alpha > 0$ and $\lambda > 0$ with
$$
\lim_{n\to\infty}\frac{\lvert x_{n+1} - x^*\rvert}{\lvert x_n - x^*\rvert^{\alpha}} = \lambda
$$
then the sequence converges with **order** $\alpha$ and **asymptotic error constant** $\lambda$. For large $n$, $e_{n+1} \approx \lambda\,e_n^{\alpha}$.

## What the order means
- $\alpha = 1$ (linear, needs $\lambda < 1$): a fixed number of correct digits is added per step.
- $1 < \alpha < 2$ (superlinear): the number of new digits grows each step.
- $\alpha = 2$ (quadratic): the number of correct digits roughly doubles each step.

## The methods
| Method | Order $\alpha$ | Constant | Cost per step |
|---|---|---|---|
| [Bisection Method](Bisection%20Method.md) | $1$ | $\tfrac12$ | 1 $f$ |
| [False Position Method](False%20Position%20Method.md) | $1$ | problem dependent | 1 $f$ |
| [Fixed Point Iteration](Fixed%20Point%20Iteration.md) | $1$ | $\lvert g'(x^*)\rvert$ | 1 $g$ |
| [Secant Method](Secant%20Method.md) | $\tfrac{1+\sqrt5}{2} \approx 1.618$ | | 1 $f$ |
| [Inverse Quadratic Interpolation](Inverse%20Quadratic%20Interpolation.md) | $\approx 1.839$ | | 1 $f$ |
| [Newton's Method](Newton's%20Method.md) | $2$ | $\left\lvert\tfrac{f''(x^*)}{2f'(x^*)}\right\rvert$ | 1 $f$ + 1 $f'$ |

## Measuring it
From three consecutive errors, $\alpha \approx \dfrac{\ln(e_{n+1}/e_n)}{\ln(e_n/e_{n-1})}$.

The same vocabulary describes optimization methods: steepest descent is linear, quasi-Newton is superlinear, and Newton is quadratic ([Convergence Rate of Steepest Descent](../../../self-study/convex-optimization/numerical-optimization/Convergence%20Rate%20of%20Steepest%20Descent.md), [Newton's Method for Optimization](../../../self-study/convex-optimization/numerical-optimization/Newton's%20Method%20for%20Optimization.md)).

## Explorations
- [EX53 - Bisection, Secant, and Newton on the Same Root](../Explorations%204/EX53%20-%20Bisection,%20Secant,%20and%20Newton%20on%20the%20Same%20Root.md)

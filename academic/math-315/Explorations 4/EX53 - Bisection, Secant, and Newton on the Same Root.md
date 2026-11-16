---
tags:
  - math-315
  - exploration
  - lecture-7
source: Lecture 7 handout, pp. 22–23 (Newton example), extended
topics:
  - "[[../Topics 4/Order of Convergence]]"
  - "[[../Topics 4/Newton's Method]]"
  - "[[../Topics 4/Secant Method]]"
  - "[[../Topics 4/Bisection Method]]"
---
# EX53 — Bisection, Secant, and Newton on the Same Root
Back to [Index](../Index.md)

> [!question] Problem
> $f(x) = 2\cosh(x/4) - x$ has a root $x^* = 2.357551053877402$.
> (a) Find it by bisection on $[0, 4]$, secant from $x_0 = 0$, $x_1 = 4$, and Newton from $x_0 = 0$.
> (b) Measure each method's order of convergence.
> (c) Repeat Newton on $f(x) = (x - 1)^2$ from $x_0 = 2$. What changes?

## Setup
- $f'(x) = \tfrac12\sinh(x/4) - 1$ and $f''(x) = \tfrac18\cosh(x/4)$.
- $f(0) = 2 > 0$ and $f(4) = 2\cosh(1) - 4 = -0.914 < 0$, so $[0, 4]$ is a bracket.

## Solution
**(a) Newton**, $x_{n+1} = x_n - f(x_n)/f'(x_n)$:

| $n$ | $x_n$ | $\lvert e_n\rvert$ |
|---|---|---|
| 1 | 2.000000000000000 | 3.58e-01 |
| 2 | 2.345190506678295 | 1.24e-02 |
| 3 | 2.357534752954785 | 1.63e-05 |
| 4 | 2.357551053848945 | 2.85e-11 |
| 5 | 2.357551053877402 | 0 |

**Secant**:

| $n$ | $x_n$ | $\lvert e_n\rvert$ |
|---|---|---|
| 2 | 2.745519138248772 | 3.88e-01 |
| 3 | 2.258358411337213 | 9.92e-02 |
| 4 | 2.361863449344380 | 4.31e-03 |
| 5 | 2.357596216891594 | 4.52e-05 |
| 6 | 2.357551033006328 | 2.09e-08 |
| 7 | 2.357551053877503 | 1.01e-13 |
| 8 | 2.357551053877402 | 0 |

**Bisection** needs $35$ halvings to bring the bound $(b-a)/2^n$ below $10^{-10}$, since $\log_2(4/10^{-10}) = 35.2$.

**(b)** Newton: $e_{n+1}/e_n^2$ should approach $\left\lvert\dfrac{f''(x^*)}{2f'(x^*)}\right\rvert = \dfrac{0.1474}{2(0.6880)} = 0.1071$.

| $n$ | $e_{n+1}/e_n^2$ |
|---|---|
| 1 | 0.097 |
| 2 | 0.106 |
| 3 | 0.107 |

The exponents of the errors go $-2, -5, -11$: the digits double. Secant: the estimate $\ln(e_{n+1}/e_n)/\ln(e_n/e_{n-1})$ gives $1.45,\ 1.68,\ 1.59$, scattered around $1.618$. Bisection: exactly $\tfrac12$ per step by construction.

| Method | Function evaluations to full precision |
|---|---|
| Bisection | 35 (to $10^{-10}$ only) |
| Secant | 8 |
| Newton | 5 of $f$ and 5 of $f'$ |

**(c)** For $(x-1)^2$ the Newton step is $x_{n+1} = x_n - \tfrac12(x_n - 1)$:

| $n$ | $x_n$ | $\lvert e_n\rvert$ |
|---|---|---|
| 1 | 1.5 | 0.5 |
| 2 | 1.25 | 0.25 |
| 3 | 1.125 | 0.125 |
| 4 | 1.0625 | 0.0625 |

The error halves each step. Newton has become as slow as bisection, because $f'(x^*) = 0$ and so $g'(x^*) = \tfrac12 \neq 0$.

## Takeaways
- Quadratic convergence is visible in the table: $10^{-2} \to 10^{-5} \to 10^{-11}$.
- Per function evaluation, secant ($8$) beats Newton ($10$) on this problem.
- At a double root Newton is only linear with rate $\tfrac12$. Simple roots are what make it fast.

## Related topics
- [Order of Convergence](../Topics%204/Order%20of%20Convergence.md)
- [Newton's Method](../Topics%204/Newton's%20Method.md)
- [Secant Method](../Topics%204/Secant%20Method.md)
- [Bisection Method](../Topics%204/Bisection%20Method.md)

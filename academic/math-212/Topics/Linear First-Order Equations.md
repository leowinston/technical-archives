---
tags: [math-212, topic, chapter-2]
---
# Linear First-Order Equations
Back to [[academic/math-212/Index|Index]] · Chapter 2.1

## Standard form
$$
\frac{dy}{dt} + p(t)y = g(t)
$$
Divide by the coefficient of $y'$ first, so the equation starts with $y'$ alone.

## Method of integrating factors
$$
\begin{align*}
\mu(t) &= \exp\left(\int p(t)\,dt\right) \\
\frac{d}{dt}\big[\mu(t)y\big] &= \mu(t)g(t) \\
y(t) &= \frac{1}{\mu(t)}\left[\int \mu(t)g(t)\,dt + c\right]
\end{align*}
$$

### Strategy
1. Put the equation in standard form and read off $p$ and $g$.
2. Compute $\mu = e^{\int p}$. You don't need a constant of integration here.
3. Multiply through. The left side becomes $(\mu y)'$.
4. Integrate both sides, remembering $+c$, then divide by $\mu$.

## Homogeneous case ($g = 0$)
$$
y = c\,e^{-\int p(t)\,dt}
$$

## Workbook problems
- [[WB1 P01 - Car Slowing Down to a Stop]]
- [[WB1 P05 - The Equation y' - ay = 0]]
- [[WB1 P06 - General Solution of the Homogeneous Linear Equation]]
- [[WB1 P07 - Linear Equation with an Exact Left Side]]
- [[WB1 P08 - Linear Equation y' - 2y = 4 - x]]
- [[WB1 P09 - Deriving the Integrating Factor]]
- [[WB1 P10 - Linear Equation with Exponential Forcing]]
- [[WB1 P22 - Rewriting as a Linear Equation]]

See also: [[Variation of Parameters]], [[Existence and Uniqueness Theorems]]

---
tags: [math-212, topic, chapter-2]
---
# Linear First-Order Equations
Back to [Index](../Index.md) · Chapter 2.1

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
- [WB1 P01 - Car Slowing Down to a Stop](../Workbook%201/WB1%20P01%20-%20Car%20Slowing%20Down%20to%20a%20Stop.md)
- [WB1 P05 - The Equation y' - ay = 0](../Workbook%201/WB1%20P05%20-%20The%20Equation%20y%27%20-%20ay%20%3D%200.md)
- [WB1 P06 - General Solution of the Homogeneous Linear Equation](../Workbook%201/WB1%20P06%20-%20General%20Solution%20of%20the%20Homogeneous%20Linear%20Equation.md)
- [WB1 P07 - Linear Equation with an Exact Left Side](../Workbook%201/WB1%20P07%20-%20Linear%20Equation%20with%20an%20Exact%20Left%20Side.md)
- [WB1 P08 - Linear Equation y' - 2y = 4 - x](../Workbook%201/WB1%20P08%20-%20Linear%20Equation%20y%27%20-%202y%20%3D%204%20-%20x.md)
- [WB1 P09 - Deriving the Integrating Factor](../Workbook%201/WB1%20P09%20-%20Deriving%20the%20Integrating%20Factor.md)
- [WB1 P10 - Linear Equation with Exponential Forcing](../Workbook%201/WB1%20P10%20-%20Linear%20Equation%20with%20Exponential%20Forcing.md)
- [WB1 P22 - Rewriting as a Linear Equation](../Workbook%201/WB1%20P22%20-%20Rewriting%20as%20a%20Linear%20Equation.md)

See also: [Variation of Parameters](Variation%20of%20Parameters.md), [Existence and Uniqueness Theorems](Existence%20and%20Uniqueness%20Theorems.md)

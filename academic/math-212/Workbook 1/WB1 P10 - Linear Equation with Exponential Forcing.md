---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 10 (p. 7)
topics: ["[[Linear First-Order Equations]]"]
---
# Problem 10 — $y' + 2y = x^3e^{-2x}$
Back to [Index](../Index.md)

> [!question] Problem
> Given $y' + 2y = x^3e^{-2x}$:
> (a) Classify the equation.
> (b) Find the general solution $y = y(x, c)$.

## Classification
- **Type:** ODE, first order
- **Linearity:** **linear, nonhomogeneous**
- **Coefficients:** constant, $p = 2$

## Strategy
1. $\mu = e^{\int 2\,dx} = e^{2x}$.
2. Multiplying by $\mu$ cancels the $e^{-2x}$ on the right, leaving the polynomial $x^3$.
3. Integrate and divide by $\mu$.

## Solution
$$
\begin{align*}
\mu &= e^{2x} \\
\left(e^{2x}y\right)' &= e^{2x}\cdot x^3e^{-2x} = x^3 \\
e^{2x}y &= \frac{x^4}{4} + c \\
y &= \left(\frac{x^4}{4} + c\right)e^{-2x}
\end{align*}
$$
Every solution tends to $0$ as $x \to \infty$, because the exponential dominates.

## Solution set
- **General solution:** $y(x) = \left(\dfrac{x^4}{4} + C\right)e^{-2x}$, $C \in \mathbb{R}$, $x \in \mathbb{R}$.
- **Constant solutions:** none. $y \equiv k$ would need $2k = x^3e^{-2x}$ for all $x$.

## Graph
```desmos-graph
left=-1.5; right=6; top=3; bottom=-2
---
y=\left(\frac{x^{4}}{4}+c\right)e^{-2x}
c=[-1,0,1,2]
```

## Related topics
- [Linear First-Order Equations](../Topics/Linear%20First-Order%20Equations.md)
- [WB1 P12 - Problem 10 by Variation of Parameters](WB1%20P12%20-%20Problem%2010%20by%20Variation%20of%20Parameters.md) (the same equation solved another way)

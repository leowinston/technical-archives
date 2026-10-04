---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 12 (p. 8)
topics: ["[[Variation of Parameters]]", "[[Linear First-Order Equations]]"]
---
# Problem 12 — Problem 10 by Variation of Parameters
Back to [Index](../Index.md)

> [!question] Problem
> Solve [Problem 10](WB1%20P10%20-%20Linear%20Equation%20with%20Exponential%20Forcing.md), $y' + 2y = x^3e^{-2x}$, using variation of parameters.

## Classification
- **Type:** ODE, first order, **linear, nonhomogeneous**, constant coefficient

## Strategy
1. Complementary equation $y' + 2y = 0$ gives $y_1 = e^{-2x}$.
2. Look for $y = ue^{-2x}$. Then $u' = f/y_1$.
3. Integrate to get $u$ and multiply by $y_1$.

## Solution
$$
\begin{align*}
y_1 &= e^{-2x} \\
u' &= \frac{x^3e^{-2x}}{e^{-2x}} = x^3 \\
u &= \frac{x^4}{4} + c \\
y &= uy_1 = \left(\frac{x^4}{4} + c\right)e^{-2x}
\end{align*}
$$
This agrees with the integrating factor answer in Problem 10.

## Solution set
- **General solution:** $y(x) = \left(\dfrac{x^4}{4} + C\right)e^{-2x}$, $C \in \mathbb{R}$, $x \in \mathbb{R}$ (same as [Problem 10](WB1%20P10%20-%20Linear%20Equation%20with%20Exponential%20Forcing.md)).
- **Constant solutions:** none.

## Graph
The particular solution $y_p = \tfrac{x^4}{4}e^{-2x}$ is black, and the complementary terms $ce^{-2x}$ are dashed.
```desmos-graph
left=-1.5; right=6; top=3; bottom=-2
---
y=\frac{x^{4}}{4}e^{-2x}|#000000
y=ce^{-2x}|dashed
c=[-1,1,2]
```

## Related topics
- [Variation of Parameters](../Topics/Variation%20of%20Parameters.md)
- [Linear First-Order Equations](../Topics/Linear%20First-Order%20Equations.md)

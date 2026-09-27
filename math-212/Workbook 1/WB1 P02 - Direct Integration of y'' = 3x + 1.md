---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 2 (p. 3)
topics: ["[[Solutions and Direction Fields]]", "[[Classification of Differential Equations]]"]
---
# Problem 2 — Solve $y'' = 3x + 1$
Back to [[Index]]

> [!question] Problem
> Solve $y'' = 3x + 1$.

## Classification
- **Type:** ODE
- **Order:** second
- **Linearity:** linear, **nonhomogeneous**
- **Special structure:** the right side depends only on $x$, so the equation can be solved by direct integration

## Strategy
1. Integrate once to get $y'$, adding a constant $c_1$.
2. Integrate again to get $y$, adding a constant $c_2$.
3. A second-order equation should give **two** arbitrary constants.

## Solution
$$
\begin{align*}
y'' &= 3x + 1 \\
y' &= \frac{3}{2}x^2 + x + c_1 \\
y &= \frac{1}{2}x^3 + \frac{1}{2}x^2 + c_1x + c_2
\end{align*}
$$

## Solution set
- **General solution:** $y(x) = \tfrac{1}{2}x^3 + \tfrac{1}{2}x^2 + C_1x + C_2$, $C_1, C_2 \in \mathbb{R}$, $x \in \mathbb{R}$.
- **Constant solutions:** none, since $y'' = 0 \neq 3x + 1$.

## Graph
Members of the solution family with $c_2 = 0$ and several values of $c_1$:
```desmos-graph
left=-4; right=4; top=6; bottom=-6
---
y=\frac{1}{2}x^{3}+\frac{1}{2}x^{2}+c_{1}x
c_{1}=[-3,-1,0,1,3]
```

## Related topics
- [[Solutions and Direction Fields]]
- [[Classification of Differential Equations]]

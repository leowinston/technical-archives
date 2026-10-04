---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 3 (p. 3)
topics: ["[[Classification of Differential Equations]]"]
---
# Problem 3 — Classify as Linear or Nonlinear
Back to [Index](../Index.md)

> [!question] Problem
> Classify each equation as linear or nonlinear. If it is linear, say whether it is homogeneous or nonhomogeneous.

## Strategy
1. Try to write the equation as $a_1(x)y' + a_0(x)y = g(x)$.
2. If that fails because $y$ appears in a power, a product like $yy'$, or a function like $e^y$ or $\ln y$, the equation is **nonlinear**.
3. If it is linear, it is **homogeneous** when $g(x) \equiv 0$ and **nonhomogeneous** otherwise.

## Classification

| | Equation | Linear form / reason | Classification |
|---|---|---|---|
| (a) | $x^2y' + 3xy = x^2$ | $a_1 = x^2$, $a_0 = 3x$, $g = x^2$ | **Linear, nonhomogeneous** |
| (b) | $xy' + 3y^2 = 2x$ | contains $y^2$ | **Nonlinear** |
| (c) | $xy' - 8x^2y = \sin x$ | $a_1 = x$, $a_0 = -8x^2$, $g = \sin x$ | **Linear, nonhomogeneous** |
| (d) | $xy' + \ln y = 0$ | contains $\ln y$ | **Nonlinear** |
| (e) | $yy' = 3$ | contains the product $yy'$ | **Nonlinear** |
| (f) | $y' + xe^y = 12$ | contains $e^y$ | **Nonlinear** |
| (g) | $y' = x^2y - 2$ | $y' - x^2y = -2$ | **Linear, nonhomogeneous** |

Variable coefficients like $x^2$ or $\sin x$ do **not** make an equation nonlinear. Only nonlinear dependence on $y$ does.

## Solution
Standard forms of the linear equations (divide by the leading coefficient):
$$
\begin{align*}
\text{(a)}\quad & y' + \frac{3}{x}y = 1 \\
\text{(c)}\quad & y' - 8xy = \frac{\sin x}{x} \\
\text{(g)}\quad & y' - x^2y = -2
\end{align*}
$$

## Graph
Classification needs no graph. For comparison, here is the linear equation (a) solved: $y = \dfrac{x}{4} + \dfrac{c}{x^3}$.
```desmos-graph
left=-4; right=4; top=4; bottom=-4
---
y=\frac{x}{4}+\frac{c}{x^{3}}
c=[-1,0,1]
```

## Related topics
- [Classification of Differential Equations](../Topics/Classification%20of%20Differential%20Equations.md)
- [Linear First-Order Equations](../Topics/Linear%20First-Order%20Equations.md)

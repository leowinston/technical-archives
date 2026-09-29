---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 22 (p. 17)
topics: ["[[Linear First-Order Equations]]"]
---
# Problem 22 — $y' = e^{2x} + y - 1$
Back to [[academic/math-212/Index|Index]]

> [!question] Problem
> Find the general solution of $y' = e^{2x} + y - 1$.

## Classification
- **Type:** ODE, first order
- **Linearity:** **linear, nonhomogeneous**. In standard form it is $y' - y = e^{2x} - 1$.
- **Not separable:** the right side is a sum, not a product $g(x)h(y)$

## Strategy
1. Move the $y$ term to the left to get standard form.
2. $\mu = e^{\int -1\,dx} = e^{-x}$.
3. Multiply through, integrate, and divide by $\mu$.

## Solution
$$
\begin{align*}
y' - y &= e^{2x} - 1 \\
\mu &= e^{-x} \\
\left(e^{-x}y\right)' &= e^{x} - e^{-x} \\
e^{-x}y &= e^{x} + e^{-x} + c \\
\boxed{\,y = e^{2x} + 1 + ce^{x}\,}
\end{align*}
$$
**Check:** $y' = 2e^{2x} + ce^{x}$ and $e^{2x} + y - 1 = 2e^{2x} + ce^{x} \checkmark$

## Solution set
- **General solution:** $y(x) = e^{2x} + 1 + Ce^{x}$, $C \in \mathbb{R}$, $x \in \mathbb{R}$.
- **Constant solutions:** none. $y \equiv k$ would need $e^{2x} + k - 1 = 0$ for all $x$.

## Graph
As $x \to -\infty$, every solution approaches $y = 1$. This is not an equilibrium, because $y \equiv 1$ does not solve the equation.
```desmos-graph
left=-5; right=2; top=6; bottom=-4
---
y=e^{2x}+1+ce^{x}
c=[-6,-3,-1,0,1,3]
y=1|dashed|#000000
```

## Related topics
- [[Linear First-Order Equations]]

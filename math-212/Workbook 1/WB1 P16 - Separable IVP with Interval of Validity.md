---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 16 (p. 11)
topics: ["[[Separable Equations]]", "[[Existence and Uniqueness Theorems]]"]
---
# Problem 16 — $y' = \dfrac{3x^2 + 4x + 2}{2(y - 1)}$, $y(0) = -1$
Back to [[Index]]

> [!question] Problem
> Classify the equation $y' = \dfrac{3x^2 + 4x + 2}{2(y - 1)}$ and find its general solution. Then solve the IVP with $y(0) = -1$.

## Classification
- **Type:** ODE, first order
- **Linearity:** **nonlinear**
- **Method:** **separable**
- **Singular line:** $y = 1$, where $f$ is undefined and solutions have vertical tangents

## Strategy
1. Separate the variables and integrate to get the general implicit solution.
2. Substitute $(0, -1)$ to find $c$.
3. Complete the square in $y$ and solve. Pick the **sign of the square root** that matches $y(0) = -1$.
4. The interval of validity is where the radicand is **positive**. Factor the cubic to find it.

## Solution
General solution:
$$
\begin{align*}
2(y - 1)\,dy &= (3x^2 + 4x + 2)\,dx \\
y^2 - 2y &= x^3 + 2x^2 + 2x + c
\end{align*}
$$
Initial condition $y(0) = -1$:
$$
(-1)^2 - 2(-1) = 3 = c
$$
Solve for $y$:
$$
\begin{align*}
(y - 1)^2 &= x^3 + 2x^2 + 2x + 4 \\
y &= 1 \pm \sqrt{x^3 + 2x^2 + 2x + 4} \\
y(0) = 1 \pm 2 = -1 &\implies \text{choose } - \\
\boxed{\,y = 1 - \sqrt{x^3 + 2x^2 + 2x + 4}\,}
\end{align*}
$$
**Interval of validity:**
$$
x^3 + 2x^2 + 2x + 4 = x^2(x + 2) + 2(x + 2) = (x^2 + 2)(x + 2) > 0 \iff x > -2
$$
So the solution is valid on $(-2, \infty)$. At $x = -2$, $y = 1$ and the tangent is vertical.

## Solution set
- **General solution (implicit):** $y^2 - 2y = x^3 + 2x^2 + 2x + C$, $C \in \mathbb{R}$.
- **Explicit:** $y(x) = 1 \pm \sqrt{x^3 + 2x^2 + 2x + C + 1}$, valid where the radicand is **positive**. Each sign is a separate family.
- **IVP:** $C = 3$, minus sign, $x \in (-2, \infty)$.
- **Constant solutions:** none. $3x^2 + 4x + 2$ has negative discriminant, so it is never $0$. $y = 1$ is where $f$ is undefined, not a solution.

## Graph
The IVP solution is blue and the discarded $+$ branch is dashed. The point $(-2, 1)$ marks the vertical tangent.
```desmos-graph
left=-3; right=3; top=6; bottom=-5
---
y=1-\sqrt{x^{3}+2x^{2}+2x+4}|#2d70b3
y=1+\sqrt{x^{3}+2x^{2}+2x+4}|dashed|#c74440
(0,-1)|#2d70b3
(-2,1)|open|#000000
x=-2|dotted|#000000
```

## Related topics
- [[Separable Equations]]
- [[Existence and Uniqueness Theorems]] (the interval of existence depends on the initial condition)

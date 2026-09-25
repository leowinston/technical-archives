---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 13 (p. 9)
topics: ["[[Separable Equations]]"]
---
# Problem 13 — $y' = \dfrac{x^2}{1 - y^2}$
Back to [[Index]]

> [!question] Problem
> Classify the equation $y' = \dfrac{x^2}{1 - y^2}$ and find its general solution.

## Classification
- **Type:** ODE, first order
- **Linearity:** **nonlinear** ($y^2$ in the denominator)
- **Method:** **separable**, $\dfrac{dy}{dx} = g(x)h(y)$ with $g = x^2$ and $h = \dfrac{1}{1 - y^2}$
- **Note:** there are no equilibria, since $x^2/(1 - y^2)$ is never identically $0$

## Strategy
1. Multiply by $(1 - y^2)$ and by $dx$ to separate the variables.
2. Integrate both sides.
3. Solving the cubic in $y$ is not practical, so leave the answer in **implicit** form.
4. Integral curves have vertical tangents where $1 - y^2 = 0$, that is, at $y = \pm 1$.

## Solution
$$
\begin{align*}
(1 - y^2)\,dy &= x^2\,dx \\
\int (1 - y^2)\,dy &= \int x^2\,dx \\
y - \frac{y^3}{3} &= \frac{x^3}{3} + c \\
\boxed{\,3y - y^3 - x^3 = C\,}
\end{align*}
$$

## Graph
Implicit level curves $3y - y^3 - x^3 = C$. The lines $y = \pm 1$ (dashed) mark where solutions have vertical tangents.
```desmos-graph
left=-4; right=4; top=3; bottom=-3
---
3y-y^{3}-x^{3}=C
C=[-4,-2,0,2,4]
y=1|dashed|#000000
y=-1|dashed|#000000
```

## Related topics
- [[Separable Equations]]
- [[Existence and Uniqueness Theorems]] ($\partial f/\partial y$ is discontinuous at $y = \pm 1$)

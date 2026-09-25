---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 15 (p. 10)
topics: ["[[Separable Equations]]", "[[Existence and Uniqueness Theorems]]"]
---
# Problem 15 — $y' = \tfrac{1}{2}x(1 - y^2)$
Back to [[Index]]

> [!question] Problem
> Classify the equation $y' = \tfrac{1}{2}x(1 - y^2)$ and find its general solution in explicit form.

## Classification
- **Type:** ODE, first order
- **Linearity:** **nonlinear** ($y^2$)
- **Method:** **separable**, $g(x) = \tfrac{x}{2}$ and $h(y) = 1 - y^2$
- **Equilibria:** $y \equiv 1$ and $y \equiv -1$

## Strategy
1. Record the equilibria $y = \pm 1$ before dividing by $1 - y^2$.
2. Separate the variables and use partial fractions: $\dfrac{1}{1 - y^2} = \dfrac{1}{2}\left(\dfrac{1}{1 + y} + \dfrac{1}{1 - y}\right)$.
3. Exponentiate, absorb $\pm e^{c}$ into a single constant $C$, and solve for $y$ algebraically.
4. Check which equilibria the formula includes. One of them is a **singular solution**.

## Solution
$$
\begin{align*}
\frac{dy}{1 - y^2} &= \frac{x}{2}\,dx \\
\frac{1}{2}\ln\left\lvert\frac{1 + y}{1 - y}\right\rvert &= \frac{x^2}{4} + c_1 \\
\frac{1 + y}{1 - y} &= Ce^{x^2/2}
\end{align*}
$$
Solve for $y$:
$$
\begin{align*}
1 + y &= Ce^{x^2/2}(1 - y) \\
y\left(1 + Ce^{x^2/2}\right) &= Ce^{x^2/2} - 1 \\
\boxed{\,y = \frac{Ce^{x^2/2} - 1}{Ce^{x^2/2} + 1}\,}
\end{align*}
$$
- $C = 0$ gives $y = -1$.
- No value of $C$ gives $y = 1$ (it corresponds to $C \to \infty$). So $y \equiv 1$ is a **singular solution** that the general formula misses.
- For $C > 0$, the formula equals $y = \tanh\left(\dfrac{x^2}{4} + k\right)$ with $C = e^{2k}$.

## Graph
Solutions with $C > 0$ approach $y = 1$. Solutions with $C < 0$ blow up at finite $x$.
```desmos-graph
left=-5; right=5; top=4; bottom=-4
---
y=\frac{Ce^{\frac{x^{2}}{2}}-1}{Ce^{\frac{x^{2}}{2}}+1}
C=[-3,-0.5,0,0.05,0.5,3]
y=1|dashed|#000000
y=-1|dashed|#000000
```

## Related topics
- [[Separable Equations]]
- [[Existence and Uniqueness Theorems]] (singular solutions of nonlinear equations)

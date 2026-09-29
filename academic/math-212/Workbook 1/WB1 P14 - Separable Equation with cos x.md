---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 14 (p. 9)
topics: ["[[Separable Equations]]"]
---
# Problem 14 — $y' = \dfrac{(y - 3)\cos x}{1 + 2y^2}$
Back to [[academic/math-212/Index|Index]]

> [!question] Problem
> Classify the equation $y' = \dfrac{(y - 3)\cos x}{1 + 2y^2}$ and find its general solution.

## Classification
- **Type:** ODE, first order
- **Linearity:** **nonlinear**
- **Method:** **separable**, $g(x) = \cos x$ and $h(y) = \dfrac{y - 3}{1 + 2y^2}$
- **Equilibrium:** $y \equiv 3$, the root of $h(y) = 0$

## Strategy
1. **Before dividing** by $y - 3$, record the constant solution $y = 3$.
2. Separate the variables: $\dfrac{1 + 2y^2}{y - 3}\,dy = \cos x\,dx$.
3. The fraction on the left is improper, so use polynomial long division.
4. Integrate. The answer stays implicit.

## Solution
Long division:
$$
\frac{2y^2 + 1}{y - 3} = 2y + 6 + \frac{19}{y - 3}
$$
Integrate:
$$
\begin{align*}
\int \left(2y + 6 + \frac{19}{y - 3}\right)dy &= \int \cos x\,dx \\
\boxed{\,y^2 + 6y + 19\ln\lvert y - 3\rvert = \sin x + c\,}
\end{align*}
$$
together with the equilibrium solution $y \equiv 3$.

## Solution set
- **General solution (implicit):** $y^2 + 6y + 19\ln\lvert y - 3\rvert = \sin x + C$, $C \in \mathbb{R}$.
- **Constant solutions:** $y \equiv 3$. No $C$ gives it ($\ln 0$ is undefined), so it is listed separately.
- **Note:** $f$ is smooth, so no solution crosses $y = 3$. Each solution stays above or below it for all $x \in \mathbb{R}$ ($\lvert y'\rvert$ is bounded, so there is no blow-up).

## Graph
Implicit solutions for several values of $c$, with the equilibrium $y = 3$ dashed. Solutions never cross $y = 3$. The graph writes $\ln\lvert y - 3\rvert$ as $\tfrac{1}{2}\ln\left((y - 3)^2\right)$ because the plugin treats `|` as a separator.
```desmos-graph
left=-7; right=7; top=7; bottom=-8
---
y^{2}+6y+\frac{19}{2}\ln\left(\left(y-3\right)^{2}\right)=\sin\left(x\right)+c
c=[-20,0,20,30,40,50]
y=3|dashed|#000000
```

## Related topics
- [[Separable Equations]]
- [[Autonomous Equations and Phase Lines]] (equilibrium solutions)

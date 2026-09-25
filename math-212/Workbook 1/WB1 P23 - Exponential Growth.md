---
tags: [math-212, problem, workbook-1, population-model]
source: Workbook Part 1, Problem 23 (p. 18)
topics: ["[[Exponential Growth]]", "[[Autonomous Equations and Phase Lines]]"]
---
# Problem 23 — Exponential Growth
Back to [[Index]]

> [!question] Problem
> Let $y = \phi(t)$ be the population of a species at time $t$. Assume the rate of change of the population is proportional to $y$, with constant of proportionality $r$: a growth rate ($r > 0$) or decline rate ($r < 0$).
> (a) Write the differential equation.
> (b) Given $y(0) = y_0$, solve the IVP.
> (c) Sketch several solutions of the IVP.

## Classification
- **Type:** ODE, first order, **linear, homogeneous**, constant coefficient
- **Also:** **autonomous** and separable
- **Equilibrium:** $y = 0$. It is unstable for $r > 0$ and asymptotically stable for $r < 0$.

## Strategy
1. Translate "rate of change proportional to $y$" into $\dfrac{dy}{dt} = ry$.
2. Separate the variables, or use the result of [[WB1 P05 - The Equation y' - ay = 0|Problem 5]].
3. Apply $y(0) = y_0$.
4. Sketch separate cases for $r > 0$ and $r < 0$.

## Solution
**(a)**
$$
\frac{dy}{dt} = ry
$$
**(b)**
$$
\begin{align*}
\frac{dy}{y} &= r\,dt \\
\ln\lvert y\rvert &= rt + c \\
y &= Ce^{rt}, \qquad y(0) = y_0 \implies C = y_0 \\
\boxed{\,y(t) = y_0e^{rt}\,}
\end{align*}
$$
**(c)**
- If $r > 0$, every solution with $y_0 > 0$ grows without bound. The doubling time is $\dfrac{\ln 2}{r}$.
- If $r < 0$, every solution decays to $0$. The half-life is $\dfrac{\ln 2}{\lvert r\rvert}$.

## Graph
Growth with $r = 0.5$ in blue and decline with $r = -0.5$ in red, for $y_0 \in \{0.5, 1, 2, 3\}$:
```desmos-graph
left=-0.5; right=6; top=8; bottom=-0.5
xAxisLabel=t; yAxisLabel=y
---
y=y_{0}e^{0.5x}|x>=0|#2d70b3
y=y_{0}e^{-0.5x}|x>=0|#c74440
y_{0}=[0.5,1,2,3]
```

## Related topics
- [[Exponential Growth]]
- [[Autonomous Equations and Phase Lines]]
- [[Logistic Growth]] (adds a carrying capacity)

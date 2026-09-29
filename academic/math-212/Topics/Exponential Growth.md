---
tags: [math-212, topic, chapter-2, population-model]
---
# Exponential Growth
Back to [[academic/math-212/Index|Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

This is the Malthusian model. The rate of change is proportional to the current population.
$$
\begin{align*}
\frac{dy}{dt} &= ry \\
y(t) &= y_0 e^{rt}
\end{align*}
$$
- If $r > 0$, the population grows without bound.
- If $r < 0$, it decays to $0$.
- The only equilibrium is $y = 0$. It is unstable when $r > 0$ and stable when $r < 0$.

```desmos-graph
left=-0.5; right=6; top=8; bottom=-8
xAxisLabel=t; yAxisLabel=y
---
y=y_{0}e^{r_0 x}|x>=0|#2d70b3
y_{0}=[-3,-2,-1,-0.5,0.25,0.5,1,2,3]
y=y_{0}e^{-r_0 x}|x>=0|#c74440|dashed
r_0=0.5
```
Solid curves have rate $r$, and dashed curves have rate $-r$.

## Workbook problems
- [[WB1 P05 - The Equation y' - ay = 0]]
- [[WB1 P23 - Exponential Growth]]

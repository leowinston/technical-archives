---
tags: [math-212, topic, chapter-2]
---
# Bifurcations
Back to [[academic/math-212/Index|Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

A **bifurcation** happens when changing a parameter $a$ in $\dfrac{dy}{dt} = f(a, y)$ changes the number or stability of the equilibria.

| Type          | Equation                     | Equilibria                                     |
| ------------- | ---------------------------- | ---------------------------------------------- |
| Saddle-node   | $y' = a - y^2$               | none for $a < 0$; $y = \pm\sqrt a$ for $a > 0$ |
| Pitchfork     | $y' = ay - y^3 = y(a - y^2)$ | $0$; plus $\pm\sqrt a$ for $a > 0$             |
| Transcritical | $y' = ay - y^2 = y(a - y)$   | $0$ and $a$, which swap stability at $a = 0$   |

The graph below is the saddle-node bifurcation diagram for $y' = a - y^2$: equilibria plotted against the parameter $a$. Solid curves are stable and dashed curves are unstable.
```desmos-graph
left=-3; right=3; top=2.5; bottom=-2.5
xAxisLabel=a; yAxisLabel=y*
---
y=\sqrt{x}|x>=0|#2d70b3
y=-\sqrt{x}|x>=0|dashed|#2d70b3
```

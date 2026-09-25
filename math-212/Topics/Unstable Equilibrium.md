---
tags: [math-212, topic, chapter-2, stability]
---
# Unstable Equilibrium
Back to [[Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

An equilibrium $y_1$ of $y' = f(y)$ is **unstable** if solutions that start near $y_1$ (on either side) move away from it.
- Test: $f'(y_1) > 0$. Equivalently, $f < 0$ just below $y_1$ and $f > 0$ just above.
- On the phase line both arrows point **away** from $y_1$ (a source).
- Example: $y = 0$ in [[Logistic Growth]] and $y = T$ in [[Threshold Growth]].

Example $y' = y - 1$ with $y_1 = 1$. Solution curves peel away from the dashed line.
```desmos-graph
left=-0.5; right=3; top=3; bottom=-1
xAxisLabel=t; yAxisLabel=y
---
y=1+\left(a-1\right)e^{x}|x>=0|#2d70b3
a=[0.6,0.8,0.95,1.05,1.2,1.4]
y=1|dashed|#c74440
```

Phase plot $f(y) = y - 1$. The graph crosses zero going **up**.
```desmos-graph
left=-1; right=3; top=2; bottom=-2
xAxisLabel=y; yAxisLabel=f(y)
---
y=x-1|#6042a6
(1,0)|open|#c74440
```

See also: [[Stable Equilibrium]], [[Semistable Equilibrium]]

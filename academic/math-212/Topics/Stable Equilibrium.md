---
tags: [math-212, topic, chapter-2, stability]
---
# Stable Equilibrium
Back to [[academic/math-212/Index|Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

An equilibrium $y_1$ of $y' = f(y)$ (so $f(y_1) = 0$) is **asymptotically stable** if every solution that starts near $y_1$ approaches $y_1$ as $t \to \infty$.
- Test: $f'(y_1) < 0$. Equivalently, $f > 0$ just below $y_1$ and $f < 0$ just above.
- On the phase line both arrows point **toward** $y_1$ (a sink).
- Example: $y = K$ in [[Logistic Growth]] and $y = 0$ in [[Threshold Growth]].

Example $y' = -(y - 1)$ with $y_1 = 1$. Every solution curve converges to the dashed line.
```desmos-graph
left=-0.5; right=6; top=3; bottom=-1
xAxisLabel=t; yAxisLabel=y
---
y=1+\left(a-1\right)e^{-x}|x>=0|#2d70b3
a=[-0.8,-0.2,0.4,1.6,2.2,2.8]
y=1|dashed|#388c46
```

Phase plot $f(y) = -(y - 1)$. The graph crosses zero going **down**.
```desmos-graph
left=-1; right=3; top=2; bottom=-2
xAxisLabel=y; yAxisLabel=f(y)
---
y=-\left(x-1\right)|#6042a6
(1,0)|#388c46
```

See also: [[Unstable Equilibrium]], [[Semistable Equilibrium]]

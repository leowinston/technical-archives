---
tags: [math-212, topic, chapter-2, stability]
---
# Semistable Equilibrium
Back to [[Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

An equilibrium $y_1$ of $y' = f(y)$ is **semistable** if solutions approach it from one side and move away on the other.
- Test: $f$ has the **same sign** on both sides of $y_1$. Then $f'(y_1) = 0$, so the derivative test is inconclusive.
- On the phase line one arrow points toward $y_1$ and the other points away.
- Typical form: a repeated root, as in $f(y) = (y - 1)^2$. Semistable points appear at a saddle-node [[Bifurcations|bifurcation]].

Example $y' = (y - 1)^2$ with $y_1 = 1$. Solutions below rise toward $1$. Solutions above blow up.
```desmos-graph
left=-0.5; right=5; top=3; bottom=-1
xAxisLabel=t; yAxisLabel=y
---
y=1+\frac{a-1}{1-\left(a-1\right)x}|x>=0|#2d70b3
a=[-1,0,0.5]
y=1+\frac{b-1}{1-\left(b-1\right)x}|x>=0|x<1/(b-1)|#c74440
b=[1.3,1.6]
y=1|dashed|#fa7e19
```

Phase plot $f(y) = (y - 1)^2$. The graph touches zero without crossing.
```desmos-graph
left=-1; right=3; top=2; bottom=-1
xAxisLabel=y; yAxisLabel=f(y)
---
y=\left(x-1\right)^{2}|#6042a6
(1,0)|#fa7e19
```

See also: [[Stable Equilibrium]], [[Unstable Equilibrium]]

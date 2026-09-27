---
tags: [math-212, topic, chapter-2, population-model]
---
# Threshold Growth
Back to [[Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

This is the critical-threshold model. $r > 0$ is a rate constant and $T > 0$ is the threshold level.
$$
\begin{align*}
\frac{dy}{dt} &= -r\left(1 - \frac{y}{T}\right)y \\
y(t) &= \frac{y_0 T}{y_0 + (T - y_0)e^{rt}}
\end{align*}
$$
- $y = 0$ is [[Stable Equilibrium|asymptotically stable]] and $y = T$ is [[Unstable Equilibrium|unstable]].
- Solutions starting below $T$ decay to $0$. Solutions between $T/2$ and $T$ have an inflection point at $y = T/2$.
- Solutions starting above $T$ blow up in finite time at $t^* = \frac{1}{r}\ln\frac{y_0}{y_0 - T}$.

```desmos-graph
left=-0.5; right=6; top=5; bottom=-0.5
xAxisLabel=t; yAxisLabel=y
---
y=\frac{y_{0}T}{y_{0}+\left(T-y_{0}\right)e^{r_0 x}}|x>=0|#2d70b3
y_{0}=[0.1,0.3,0.6,0.8,1,1.2,1.4,1.6,1.8,1.95]
y=\frac{2.5T}{2.5+\left(T-2.5\right)e^{r_0 x}}|x>=0|x<1.6|#c74440
y=\frac{2.2T}{2.2+\left(T-2.2\right)e^{r_0 x}}|x>=0|x<2.39|#c74440
y=\frac{3T}{3+\left(T-3\right)e^{r_0 x}}|x>=0|x<1.09|#c74440
y=\frac{4T}{4+\left(T-4\right)e^{r_0 x}}|x>=0|x<0.69|#c74440
T=2
r_0=1
y=T|dashed|#c74440
y=T/2|dotted|#fa7e19
```

## Workbook problems
- [[WB1 P25 - A Critical Threshold]]
- [[WB1 P26 - Critical Threshold Blow-Up]]

See also: [[Logistic Growth]], [[Logistic Growth with a Threshold]]

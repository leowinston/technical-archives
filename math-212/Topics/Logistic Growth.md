---
tags: [math-212, topic, chapter-2, population-model]
---
# Logistic Growth
Back to [[Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

This is the Verhulst model. $r > 0$ is the intrinsic growth rate and $K > 0$ is the environmental carrying capacity.
$$
\begin{align*}
\frac{dy}{dt} &= r\left(1 - \frac{y}{K}\right)y \\
y(t) &= \frac{y_0 K}{y_0 + (K - y_0)e^{-rt}}
\end{align*}
$$
- $y = 0$ is **unstable** and $y = K$ is **asymptotically stable**.
- Solutions starting between $0$ and $K/2$ have an inflection point at $y = K/2$, where growth is fastest.

```desmos-graph
left=-0.5; right=8; top=8; bottom=-0.5
xAxisLabel=t; yAxisLabel=y
---
y=\frac{y_{0}K}{y_{0}+\left(K-y_{0}\right)e^{-r_0 x}}|x>=0|#2d70b3
y_{0}=[0.1,0.3,0.7,1.2,2,3,3.6,5,6,7]
K=4
r_0=1
y=K|dashed|#c74440
y=K/2|dotted|#fa7e19
```

## Workbook problems
- [[WB1 P24 - Logistic Growth]]

See also: [[Logistic Growth with a Threshold]], [[Harvesting]], [[Bernoulli Equations]]

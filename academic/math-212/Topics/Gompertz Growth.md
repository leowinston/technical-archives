---
tags: [math-212, topic, chapter-2, population-model]
---
# Gompertz Growth
Back to [[academic/math-212/Index|Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

$$
\begin{align*}
\frac{dy}{dt} &= ry\ln\left(\frac{K}{y}\right) \\
y(t) &= K\exp\left[\ln\left(\frac{y_0}{K}\right)e^{-rt}\right]
\end{align*}
$$
- $y = K$ is asymptotically stable.
- The inflection point is at $y = K/e$, compared with $K/2$ for the logistic model.

```desmos-graph
left=-0.5; right=8; top=2.5; bottom=-0.3
xAxisLabel=t; yAxisLabel=y
---
y=K\exp\left(\ln\left(\frac{a}{K}\right)e^{-r_0x}\right)|x>=0
a=[0.1,0.5,1,1.5,2.2]
K=1.5
r_0=0.8
y=K|dashed|#388c46
y=K/e|dotted|#fa7e19
```

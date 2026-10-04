---
tags: [math-212, topic, chapter-2, population-model]
---
# Harvesting
Back to [Index](../Index.md) · Chapter 2.5 · [Autonomous Equations and Phase Lines](Autonomous%20Equations%20and%20Phase%20Lines.md)

## Schaefer model (effort harvesting)
$$
\frac{dy}{dt} = r\left(1 - \frac{y}{K}\right)y - Ey
$$
- Equilibria are $y_1 = 0$ and $y_2 = K\left(1 - \dfrac{E}{r}\right)$. When $E < r$, $y_2$ is stable.
- The sustainable yield is $Y = Ey_2 = KE\left(1 - \dfrac{E}{r}\right)$. It is largest at $E = r/2$, giving $Y_{\max} = rK/4$.

The harvested model is logistic with rate $r - E$ and capacity $K(1 - E/r)$. Below, $r = 1$, $K = 4$, $E = 0.4$, so solutions approach $y_2 = 2.4$ instead of $K$.

```desmos-graph
left=-0.5; right=10; top=6; bottom=-0.5
xAxisLabel=t; yAxisLabel=y
---
y=\frac{y_{0}M}{y_{0}+\left(M-y_{0}\right)e^{-\left(r_0-E\right)x}}|x>=0|#2d70b3
y_{0}=[0.1,0.3,0.6,1,1.5,2,3,4,5,5.8]
M=K\left(1-E/r_0\right)
K=4
r_0=1
E=0.4
y=M|dashed|#388c46
y=K|dotted|#c74440
```

## Constant-yield harvesting
$$
\frac{dy}{dt} = r\left(1 - \frac{y}{K}\right)y - h
$$
If $h > rK/4$, there are no equilibria and the population collapses (see [saddle-node bifurcation](Bifurcations.md)).

When $h < rK/4$, the equilibria $a < b$ are the roots of $r\left(1 - \frac{y}{K}\right)y = h$. Writing $k = r(b-a)/K$ and $C = \frac{y_0 - b}{y_0 - a}$, the solution is
$$
y(t) = \frac{b - aCe^{-kt}}{1 - Ce^{-kt}}
$$
$b$ is stable and $a$ is unstable, so a population that starts below $a$ is harvested to extinction in finite time. Below, $r = 1$, $K = 4$, $h = 0.75$, so $a = 1$ and $b = 3$.

```desmos-graph
left=-0.5; right=10; top=6; bottom=-0.5
xAxisLabel=t; yAxisLabel=y
---
y=\frac{3-\frac{y_{0}-3}{y_{0}-1}e^{-0.5x}}{1-\frac{y_{0}-3}{y_{0}-1}e^{-0.5x}}|x>=0|#2d70b3
y_{0}=[1.05,1.3,1.7,2.2,2.7,3.3,4,5,5.8]
y=\frac{3-5e^{-0.5x}}{1-5e^{-0.5x}}|x>=0|x<2|y>=0|#c74440
y=\frac{3-11e^{-0.5x}}{1-11e^{-0.5x}}|x>=0|x<4|y>=0|#c74440
y=\frac{3-41e^{-0.5x}}{1-41e^{-0.5x}}|x>=0|x<6|y>=0|#c74440
y=1|dashed|#fa7e19
y=3|dashed|#388c46
```

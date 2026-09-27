---
tags: [math-212, topic, chapter-2, population-model]
---
# Logistic Growth with a Threshold
Back to [[Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

This model combines [[Threshold Growth]] with [[Logistic Growth]].
$$
\frac{dy}{dt} = -r\left(1 - \frac{y}{T}\right)\left(1 - \frac{y}{K}\right)y, \qquad r > 0,\ 0 < T < K
$$
- $y = 0$ and $y = K$ are **asymptotically stable**. $y = T$ is **unstable** and acts as the threshold.
- A population that starts below $T$ dies out. One that starts above $T$ approaches the carrying capacity $K$.

The solution is implicit. Separating variables with partial fractions gives $t = \frac{1}{r}\left[F(y_0) - F(y)\right]$, where
$$
F(y) = \ln|y| - \frac{K}{K-T}\ln\left|1 - \frac{y}{T}\right| + \frac{T}{K-T}\ln\left|1 - \frac{y}{K}\right|
$$
The graph plots $t$ as a function of $y$ in each region.

```desmos-graph
left=-0.5; right=6; top=8; bottom=-0.5
xAxisLabel=t; yAxisLabel=y
---
x=\frac{\left(\frac{1}{2}\ln\left(a_{0}^{2}\right)-\frac{K}{2\left(K-T\right)}\ln\left(\left(1-\frac{a_{0}}{T}\right)^{2}\right)+\frac{T}{2\left(K-T\right)}\ln\left(\left(1-\frac{a_{0}}{K}\right)^{2}\right)\right)-\left(\frac{1}{2}\ln\left(y^{2}\right)-\frac{K}{2\left(K-T\right)}\ln\left(\left(1-\frac{y}{T}\right)^{2}\right)+\frac{T}{2\left(K-T\right)}\ln\left(\left(1-\frac{y}{K}\right)^{2}\right)\right)}{r_0}|x>=0|y>0|y<T|#2d70b3
a_0=[0.3,0.8,1.3,1.7,1.9]
x=\frac{\left(\frac{1}{2}\ln\left(b_{0}^{2}\right)-\frac{K}{2\left(K-T\right)}\ln\left(\left(1-\frac{b_{0}}{T}\right)^{2}\right)+\frac{T}{2\left(K-T\right)}\ln\left(\left(1-\frac{b_{0}}{K}\right)^{2}\right)\right)-\left(\frac{1}{2}\ln\left(y^{2}\right)-\frac{K}{2\left(K-T\right)}\ln\left(\left(1-\frac{y}{T}\right)^{2}\right)+\frac{T}{2\left(K-T\right)}\ln\left(\left(1-\frac{y}{K}\right)^{2}\right)\right)}{r_0}|x>=0|y>T|y<K|#388c46
b_0=[2.1,2.4,3,4,5,5.8]
x=\frac{\left(\frac{1}{2}\ln\left(c_{0}^{2}\right)-\frac{K}{2\left(K-T\right)}\ln\left(\left(1-\frac{c_{0}}{T}\right)^{2}\right)+\frac{T}{2\left(K-T\right)}\ln\left(\left(1-\frac{c_{0}}{K}\right)^{2}\right)\right)-\left(\frac{1}{2}\ln\left(y^{2}\right)-\frac{K}{2\left(K-T\right)}\ln\left(\left(1-\frac{y}{T}\right)^{2}\right)+\frac{T}{2\left(K-T\right)}\ln\left(\left(1-\frac{y}{K}\right)^{2}\right)\right)}{r_0}|x>=0|y>K|#6042a6
c_0=[6.5,7,7.8]
T=2
K=6
r_0=1
y=T|dashed|#fa7e19
y=K|dashed|#c74440
```

## Workbook problems
- [[WB1 P27 - Logistic Growth with a Threshold]]

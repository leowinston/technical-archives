---
tags: [math-212, problem, workbook-1, population-model]
source: Workbook Part 1, Problem 24 (pp. 19–20)
topics: ["[[Logistic Growth]]", "[[Autonomous Equations and Phase Lines]]"]
---
# Problem 24 — Logistic Growth
Back to [[Index]]

> [!question] Problem
> Given $y' = r\left(1 - \dfrac{y}{K}\right)y$, where $r > 0$ is the intrinsic growth rate and $K > 0$ is the carrying capacity:
> (a) Find the equilibrium solutions (critical points).
> (b) Find where solutions increase and decrease.
> (c) Sketch the phase line.
> (d) Study the concavity of the solutions.
> (e) Sketch many solutions in the $ty$-plane.
> (f) Classify the equilibria.
> (g) **Homework:** find the general solution.

## Classification
- **Type:** ODE, first order, **nonlinear** ($y^2$ term)
- **Also:** **autonomous** ($y' = f(y)$), separable, and a Bernoulli equation with $n = 2$
- **Method:** qualitative phase-line analysis for (a)–(f), separation with partial fractions for (g)

## Strategy
1. Let $f(y) = ry - \dfrac{r}{K}y^2$. Equilibria are the roots of $f$.
2. Make a sign chart of $f$ to get increasing and decreasing regions and the phase-line arrows.
3. Use $y'' = f'(y)f(y)$ and a sign chart of the product for concavity.
4. Classify each equilibrium from the arrows or the sign of $f'(y_i)$.
5. For (g), separate the variables, use partial fractions, and solve for $y$.

## Solution
**(a) Equilibria**
$$
f(y) = r\left(1 - \frac{y}{K}\right)y = 0 \implies y = 0,\quad y = K
$$

**(b) Increasing and decreasing**

| Interval | $y$ | $1 - y/K$ | $f(y)$ | Solutions |
|---|---|---|---|---|
| $y < 0$ | $-$ | $+$ | $-$ | decreasing |
| $0 < y < K$ | $+$ | $+$ | $+$ | **increasing** |
| $y > K$ | $+$ | $-$ | $-$ | decreasing |

**(c) Phase line**
- Below $0$ the arrows point **down**, away from $0$.
- Between $0$ and $K$ they point **up**, toward $K$.
- Above $K$ they point **down**, toward $K$.

**(d) Concavity**
$$
\begin{align*}
f'(y) &= r\left(1 - \frac{2y}{K}\right) = 0 \iff y = \frac{K}{2} \\
y'' &= f'(y)f(y)
\end{align*}
$$

| Interval | $f$ | $f'$ | $y''$ | Concavity |
|---|---|---|---|---|
| $y < 0$ | $-$ | $+$ | $-$ | down |
| $0 < y < K/2$ | $+$ | $+$ | $+$ | up |
| $K/2 < y < K$ | $+$ | $-$ | $-$ | down |
| $y > K$ | $-$ | $-$ | $+$ | up |

Solutions starting in $(0, K/2)$ have an **inflection point** at $y = K/2$, where the growth rate is largest ($f(K/2) = rK/4$).

**(e)** See the graphs below.

**(f) Classification**
$$
\begin{align*}
f'(0) &= r > 0 &&\implies y = 0 \text{ is unstable} \\
f'(K) &= -r < 0 &&\implies y = K \text{ is asymptotically stable}
\end{align*}
$$

**(g) General solution**
$$
\begin{align*}
\frac{dy}{y\left(1 - y/K\right)} &= r\,dt \\
\int \left(\frac{1}{y} + \frac{1/K}{1 - y/K}\right)dy &= \int r\,dt \\
\ln\lvert y\rvert - \ln\left\lvert 1 - \frac{y}{K}\right\rvert &= rt + c \\
\frac{y}{1 - y/K} &= Ce^{rt}, \qquad C = \frac{y_0}{1 - y_0/K} \\
\boxed{\,y(t) = \frac{y_0K}{y_0 + (K - y_0)e^{-rt}}\,}
\end{align*}
$$
Check: $y(0) = y_0$, and for $y_0 > 0$, $y \to K$ as $t \to \infty$.

## Graph
**Solutions in the $ty$-plane** with $K = 4$ and $r = 1$. The equilibria $y = 0$ and $y = K$ are dashed, and the inflection level $y = K/2$ is dotted.
```desmos-graph
left=-0.5; right=8; top=7; bottom=-0.5
xAxisLabel=t; yAxisLabel=y
---
y=\frac{y_{0}K}{y_{0}+\left(K-y_{0}\right)e^{-r_{0}x}}|x>=0
y_{0}=[0.1,0.5,1,2,3,5,6]
K=4
r_0=1
y=K|dashed|#388c46
y=0|dashed|#c74440
y=K/2|dotted|#fa7e19
```

**Phase diagram:** $f(y)$ plotted against $y$. Solutions increase where the curve is above the axis.
```desmos-graph
left=-1; right=5; top=1.5; bottom=-1.5
xAxisLabel=y; yAxisLabel=f(y)
---
y=r_{0}\left(1-\frac{x}{K}\right)x|#6042a6
K=4
r_0=1
(0,0)|open|#c74440
(K,0)|#388c46
```

## Related topics
- [[Logistic Growth]]
- [[Autonomous Equations and Phase Lines]]
- [[Bernoulli Equations]]

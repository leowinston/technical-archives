---
tags: [math-212, problem, workbook-1, population-model]
source: Workbook Part 1, Problem 25 (p. 21)
topics: ["[[Threshold Growth]]", "[[Autonomous Equations and Phase Lines]]"]
---
# Problem 25 — A Critical Threshold
Back to [[Index]]

> [!question] Problem
> Given $y' = -r\left(1 - \dfrac{y}{T}\right)y$, where $r > 0$ is the intrinsic growth rate and $T > 0$ is the threshold level:
> (a) Find the equilibrium solutions (critical points).
> (b) Find where solutions increase and decrease.
> (c) Sketch the phase line.
> (d) Study the concavity of the solutions.
> (e) Sketch many solutions in the $ty$-plane.
> (f) Classify the equilibria.

## Classification
- **Type:** ODE, first order, **nonlinear**
- **Also:** **autonomous** and separable
- **Method:** qualitative phase-line analysis. This is the [[Logistic Growth|logistic equation]] with the sign reversed.

## Strategy
1. Let $f(y) = -ry + \dfrac{r}{T}y^2$ and find its roots.
2. Sign chart of $f$. Because of the minus sign, every arrow is the **reverse** of the logistic case.
3. Concavity from $y'' = f'(y)f(y)$ with $f'(y) = -r\left(1 - \dfrac{2y}{T}\right)$.
4. Classify from the sign of $f'$ at each equilibrium.

## Solution
**(a) Equilibria**
$$
f(y) = -r\left(1 - \frac{y}{T}\right)y = 0 \implies y = 0,\quad y = T
$$

**(b) Increasing and decreasing**

| Interval | $f(y)$ | Solutions |
|---|---|---|
| $y < 0$ | $+$ | increasing |
| $0 < y < T$ | $-$ | **decreasing** (population dies out) |
| $y > T$ | $+$ | **increasing** (grows without bound) |

**(c) Phase line**
- Below $0$ the arrows point **up**, toward $0$.
- Between $0$ and $T$ they point **down**, toward $0$.
- Above $T$ they point **up**, away from $T$.

**(d) Concavity**
$$
\begin{align*}
f'(y) &= -r\left(1 - \frac{2y}{T}\right) = 0 \iff y = \frac{T}{2} \\
y'' &= f'(y)f(y)
\end{align*}
$$

| Interval | $f$ | $f'$ | $y''$ | Concavity |
|---|---|---|---|---|
| $y < 0$ | $+$ | $-$ | $-$ | down |
| $0 < y < T/2$ | $-$ | $-$ | $+$ | up |
| $T/2 < y < T$ | $-$ | $+$ | $-$ | down |
| $y > T$ | $+$ | $+$ | $+$ | up |

Solutions starting in $(T/2, T)$ have an inflection point as they cross $y = T/2$ on the way down.

**(e)** See the graphs below.

**(f) Classification**
$$
\begin{align*}
f'(0) &= -r < 0 &&\implies y = 0 \text{ is asymptotically stable} \\
f'(T) &= r > 0 &&\implies y = T \text{ is unstable (the threshold)}
\end{align*}
$$
A population that starts below $T$ goes extinct. One that starts above $T$ grows without bound, reaching infinity in finite time (see [[WB1 P26 - Critical Threshold Blow-Up|Problem 26]]).

## Graph
**Solutions in the $ty$-plane** with $T = 2$ and $r = 1$. Starting values below $T$ are blue. The value $y_0 = 2.5$ is red and blows up near $t^\star = \ln 5 \approx 1.61$.
```desmos-graph
left=-0.5; right=6; top=5; bottom=-0.5
xAxisLabel=t; yAxisLabel=y
---
y=\frac{y_{0}T}{y_{0}+\left(T-y_{0}\right)e^{r_{0}x}}|x>=0|#2d70b3
y_{0}=[0.3,0.8,1.2,1.6,1.9]
y=\frac{2.5T}{2.5+\left(T-2.5\right)e^{r_{0}x}}|x>=0|x<1.6|#c74440
T=2
r_0=1
y=T|dashed|#c74440
y=T/2|dotted|#fa7e19
```

**Phase diagram:** $f(y)$ against $y$.
```desmos-graph
left=-1; right=3; top=1; bottom=-1
xAxisLabel=y; yAxisLabel=f(y)
---
y=-r_{0}\left(1-\frac{x}{T}\right)x|#6042a6
T=2
r_0=1
(0,0)|#388c46
(T,0)|open|#c74440
```

## Related topics
- [[Threshold Growth]]
- [[Autonomous Equations and Phase Lines]]
- [[Logistic Growth with a Threshold]]

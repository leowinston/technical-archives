---
tags: [math-212, problem, workbook-1, population-model]
source: Workbook Part 1, Problem 27 (p. 23)
topics: ["[[Logistic Growth with a Threshold]]", "[[Autonomous Equations and Phase Lines]]"]
---
# Problem 27 — Logistic Growth with a Threshold
Back to [[Index]]

> [!question] Problem
> Given $y' = -r\left(1 - \dfrac{y}{T}\right)\left(1 - \dfrac{y}{K}\right)y$, where $r > 0$ and $0 < T < K$:
> (a) Find the equilibrium solutions (critical points).
> (b) Find where solutions increase and decrease.
> (c) Sketch the phase line.
> (d) Study the concavity of the solutions.
> (e) Sketch many solutions in the $ty$-plane.
> (f) Classify the equilibria.

## Classification
- **Type:** ODE, first order, **nonlinear** (cubic in $y$)
- **Also:** **autonomous** and separable
- **Method:** qualitative phase-line analysis. The model combines [[Threshold Growth]] (below $K$) with [[Logistic Growth]] (above $T$).

## Strategy
1. Find the roots of the cubic $f(y)$: $0$, $T$, and $K$.
2. Sign chart of $f$. It has four factors: $-r$, $(1 - y/T)$, $(1 - y/K)$, and $y$.
3. For concavity, $f'$ is a quadratic. Find its two roots $y_1, y_2$ and use Rolle's theorem to place them: $0 < y_1 < T < y_2 < K$.
4. Build a sign chart for $y'' = f'(y)f(y)$ across all six intervals.
5. Classify the equilibria with $f'(0)$, $f'(T)$, and $f'(K)$.

## Solution
**(a) Equilibria**
$$
f(y) = -r\left(1 - \frac{y}{T}\right)\left(1 - \frac{y}{K}\right)y = 0 \implies y = 0,\quad y = T,\quad y = K
$$

**(b) Increasing and decreasing**

| Interval | $1 - \frac{y}{T}$ | $1 - \frac{y}{K}$ | $y$ | $f(y)$ | Solutions |
|---|---|---|---|---|---|
| $y < 0$ | $+$ | $+$ | $-$ | $+$ | increasing |
| $0 < y < T$ | $+$ | $+$ | $+$ | $-$ | **decreasing** (extinction) |
| $T < y < K$ | $-$ | $+$ | $+$ | $+$ | **increasing** (toward $K$) |
| $y > K$ | $-$ | $-$ | $+$ | $-$ | decreasing |

**(c) Phase line** (reading upward): $\uparrow\ \mathbf{0}\ \downarrow\ \mathbf{T}\ \uparrow\ \mathbf{K}\ \downarrow$
- Arrows point **into** $0$ and **into** $K$.
- Arrows point **away** from $T$.

**(d) Concavity.** Expand $f$ and differentiate:
$$
\begin{align*}
f(y) &= -r\left[y - \left(\frac{1}{T} + \frac{1}{K}\right)y^2 + \frac{y^3}{TK}\right] \\
f'(y) &= -\frac{r}{TK}\left[3y^2 - 2(T + K)y + TK\right]
\end{align*}
$$
The roots of $f'$ are
$$
y_{1,2} = \frac{(T + K) \mp \sqrt{T^2 - TK + K^2}}{3}, \qquad 0 < y_1 < T < y_2 < K
$$
The bracket is $TK > 0$ at $y = 0$, $T(T - K) < 0$ at $y = T$, and $K(K - T) > 0$ at $y = K$. So $f' < 0$ outside $[y_1, y_2]$ and $f' > 0$ inside.

| Interval | $f$ | $f'$ | $y'' = f'f$ | Concavity |
|---|---|---|---|---|
| $y < 0$ | $+$ | $-$ | $-$ | down |
| $0 < y < y_1$ | $-$ | $-$ | $+$ | up |
| $y_1 < y < T$ | $-$ | $+$ | $-$ | down |
| $T < y < y_2$ | $+$ | $+$ | $+$ | up |
| $y_2 < y < K$ | $+$ | $-$ | $-$ | down |
| $y > K$ | $-$ | $-$ | $+$ | up |

Inflection points occur where solutions cross $y = y_1$ or $y = y_2$.

**(e)** See the graphs below.

**(f) Classification**
$$
\begin{align*}
f'(0) &= -r < 0 &&\implies y = 0 \text{ is asymptotically stable} \\
f'(T) &= r\left(1 - \frac{T}{K}\right) > 0 &&\implies y = T \text{ is unstable (threshold)} \\
f'(K) &= -r\left(\frac{K}{T} - 1\right) < 0 &&\implies y = K \text{ is asymptotically stable}
\end{align*}
$$

## Solution set
- **Constant solutions:** $y \equiv 0$, $y \equiv T$, $y \equiv K$.
- **General solution (implicit, not asked):** with partial fractions,
$$
\frac{\lvert y\rvert^{K - T}\,\lvert y - K\rvert^{T}}{\lvert y - T\rvert^{K}} = Ce^{-r(K - T)t}, \qquad C > 0
$$
- **Note:** $C = e^{c} > 0$ here, and the absolute values can't be dropped because the exponents need not be integers. $y \equiv 0$ and $y \equiv K$ would need $C = 0$, and $y \equiv T$ would need "$C = \infty$", so all three equilibria are listed separately.

## Graph
Parameters: $T = 1$, $K = 3$, $r = 1$. Then $y_{1,2} = \frac{4 \mp \sqrt 7}{3} \approx 0.45,\ 2.22$.

**Solutions in the $ty$-plane.** Separating the variables with partial fractions gives the implicit solution
$$
\ln\lvert y\rvert - \frac{K}{K - T}\ln\left\lvert 1 - \frac{y}{T}\right\rvert + \frac{T}{K - T}\ln\left\lvert 1 - \frac{y}{K}\right\rvert = -rt + c
$$
The graph plots its level curves. Equilibria are dashed and inflection levels are dotted.
```desmos-graph
left=-0.5; right=6; top=4; bottom=-0.3
xAxisLabel=t; yAxisLabel=y
---
\frac{1}{2}\ln\left(y^{2}\right)-\frac{K}{2\left(K-T\right)}\ln\left(\left(1-\frac{y}{T}\right)^{2}\right)+\frac{T}{2\left(K-T\right)}\ln\left(\left(1-\frac{y}{K}\right)^{2}\right)=-r_{0}x+c|x>=0
c=[-3,-1.5,0,1.5,3]
T=1
K=3
r_0=1
y=0|dashed|#388c46
y=T|dashed|#c74440
y=K|dashed|#388c46
y=\frac{T+K-\sqrt{T^{2}-TK+K^{2}}}{3}|dotted|#fa7e19
y=\frac{T+K+\sqrt{T^{2}-TK+K^{2}}}{3}|dotted|#fa7e19
```

**Phase diagram:** $f(y)$ against $y$. Stable equilibria are filled points and the unstable one is open.
```desmos-graph
left=-0.5; right=3.5; top=1; bottom=-1
xAxisLabel=y; yAxisLabel=f(y)
---
y=-r_{0}\left(1-\frac{x}{T}\right)\left(1-\frac{x}{K}\right)x|#6042a6
T=1
K=3
r_0=1
(0,0)|#388c46
(T,0)|open|#c74440
(K,0)|#388c46
```

## Related topics
- [[Logistic Growth with a Threshold]]
- [[Autonomous Equations and Phase Lines]]
- [[Threshold Growth]]
- [[Logistic Growth]]

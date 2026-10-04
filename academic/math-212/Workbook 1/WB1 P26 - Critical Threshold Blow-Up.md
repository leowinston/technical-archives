---
tags: [math-212, problem, workbook-1, population-model]
source: Workbook Part 1, Problem 26 (p. 22)
topics: ["[[Threshold Growth]]", "[[Existence and Uniqueness Theorems]]"]
---
# Problem 26 — A Critical Threshold (continued)
Back to [Index](../Index.md)

> [!question] Problem
> Consider the IVP $y' = -r\left(1 - \dfrac{y}{T}\right)y$, $y(0) = y_0$ (from [Problem 25](WB1%20P25%20-%20A%20Critical%20Threshold.md)).
> (a) Verify that
> $$y = \frac{y_0T}{y_0 + (T - y_0)e^{rt}}$$
> is the solution of the IVP. Observe that the population becomes unbounded in finite time.
> (b) Find the vertical asymptote $t = t^\star$ where $y \to +\infty$.

## Classification
- **Type:** ODE, first order, **nonlinear**, autonomous. This is an **IVP**.
- **Key phenomenon:** **blow-up in finite time**. The interval of existence depends on $y_0$, which is typical of nonlinear equations.

## Strategy
1. **Verify:** check the initial condition, then differentiate $y$ and compare with the right side. Writing the denominator as $D(t)$ keeps the algebra short.
2. **Blow-up:** $y \to \infty$ when the denominator reaches $0$. Solve $D(t^\star) = 0$ for $t^\star$.
3. Find which $y_0$ make $t^\star > 0$. That happens only when $y_0 > T$.

## Solution
**(a)** Let $D(t) = y_0 + (T - y_0)e^{rt}$, so $y = \dfrac{y_0T}{D}$ and $D' = r(T - y_0)e^{rt} = r(D - y_0)$.

Initial condition:
$$
y(0) = \frac{y_0T}{y_0 + T - y_0} = y_0 \checkmark
$$
Left side:
$$
y' = -\frac{y_0T\,D'}{D^2} = -\frac{r\,y_0T\,(D - y_0)}{D^2}
$$
Right side:
$$
\begin{align*}
-r\left(1 - \frac{y}{T}\right)y &= -r\left(1 - \frac{y_0}{D}\right)\frac{y_0T}{D} \\
&= -\frac{r\,y_0T\,(D - y_0)}{D^2} \checkmark
\end{align*}
$$

**(b)** $y \to +\infty$ when $D(t^\star) = 0$:
$$
\begin{align*}
y_0 + (T - y_0)e^{rt^\star} &= 0 \\
e^{rt^\star} &= \frac{y_0}{y_0 - T} \\
\boxed{\,t^\star = \frac{1}{r}\ln\left(\frac{y_0}{y_0 - T}\right)\,}
\end{align*}
$$
- $t^\star > 0$ exactly when $\dfrac{y_0}{y_0 - T} > 1$, which means $y_0 > T$.
- When $0 < y_0 < T$, the denominator stays positive and $y \to 0$.
- The closer $y_0$ is to $T$ from above, the later the blow-up.

## Solution set
- **Solution set:** $y(t) = \dfrac{y_0T}{y_0 + (T - y_0)e^{rt}}$, $y_0 \in \mathbb{R}$.
- **Constant solutions:** $y \equiv 0$ ($y_0 = 0$) and $y \equiv T$ ($y_0 = T$). Both are included.
- **Interval of existence:**
  - $0 \leq y_0 \leq T$: all $t \in \mathbb{R}$.
  - $y_0 > T$: $t < t^\star$ (blow-up forward in time).
  - $y_0 < 0$: $t > t^\star$, where now $t^\star < 0$ (blow-up backward in time); $y \to 0$ as $t \to \infty$.

## Graph
Solutions with $T = 2$, $r = 1$, and $y_0 \in \{2.5, 3, 4\}$. The//ir vertical asymptotes $t^\star = \ln\frac{y_0}{y_0 - 2} \approx 1.61, 1.10, 0.69$ are dashed.
```desmos-graph
left=-0.5; right=3; top=12; bottom=-0.5
xAxisLabel=t; yAxisLabel=y
---
y=\frac{aT}{a+\left(T-a\right)e^{r_{0}x}}|x>=0|x<t_s|#c74440
a=[2.5,3,4]
t_s=\frac{1}{r_{0}}\ln\left(\frac{a}{a-T}\right)
x=t_s|dashed|#000000
T=2
r_0=1
y=T|dotted|#2d70b3
```

## Related topics
- [WB1 P25 - A Critical Threshold](WB1%20P25%20-%20A%20Critical%20Threshold.md)
- [Existence and Uniqueness Theorems](../Topics/Existence%20and%20Uniqueness%20Theorems.md) (the interval of existence depends on the initial value)
- [Autonomous Equations and Phase Lines](../Topics/Autonomous%20Equations%20and%20Phase%20Lines.md)

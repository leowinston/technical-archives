---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 4 (p. 4)
topics: ["[[Solutions and Direction Fields]]"]
---
# Problem 4 — Solve $y' = 1$ and $y' = \frac{1}{x^2}$
Back to [[Index]]

> [!question] Problem
> Solve (a) $y' = 1$ and (b) $y' = \dfrac{1}{x^2}$.

## Classification
- **Type:** ODE, first order, linear, nonhomogeneous
- **Special structure:** $y' = f(x)$, so direct integration works

## Strategy
1. Integrate the right side and add $c$.
2. In (b), $f(x) = 1/x^2$ is undefined at $x = 0$. Solutions live on $(-\infty, 0)$ **or** $(0, \infty)$, and the constant can differ on each interval.

## Solution
**(a)**
$$
\begin{align*}
y &= \int 1\,dx = x + c
\end{align*}
$$

**(b)**
$$
\begin{align*}
y &= \int x^{-2}\,dx = -\frac{1}{x} + c, \qquad x \neq 0
\end{align*}
$$

## Graph
Family (a) in blue and family (b) in red:
```desmos-graph
left=-5; right=5; top=5; bottom=-5
---
y=x+c|#2d70b3
y=-\frac{1}{x}+c|#c74440
c=[-2,0,2]
```

## Related topics
- [[Solutions and Direction Fields]]

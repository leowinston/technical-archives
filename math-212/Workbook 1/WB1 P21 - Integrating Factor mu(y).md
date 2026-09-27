---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 21 (p. 16)
topics: ["[[Integrating Factors for Exact Equations]]", "[[Exact Equations]]"]
---
# Problem 21 — $2xy^3\,dx + (3x^2y^2 + x^2y^3 + 1)\,dy = 0$
Back to [[Index]]

> [!question] Problem
> Find the general solution of $2xy^3\,dx + (3x^2y^2 + x^2y^3 + 1)\,dy = 0$.

## Classification
- **Type:** ODE, first order, **nonlinear**
- **Method:** **not exact**. $\dfrac{N_x - M_y}{M}$ depends only on $y$, so an **integrating factor $\mu(y)$** works.

## Strategy
1. Compute $M_y - N_x$. Dividing by $N$ does **not** give a function of $x$ alone.
2. Divide $N_x - M_y$ by $M$ instead. That gives a function of $y$ alone.
3. $\mu(y) = e^{\int P(y)\,dy}$.
4. Multiply through, integrate $\tilde M$ with respect to $x$, and match $\psi_y$ with $\tilde N$.

## Solution
Exactness test:
$$
\begin{align*}
M_y &= 6xy^2, \qquad N_x = 6xy^2 + 2xy^3 \\
N_x - M_y &= 2xy^3
\end{align*}
$$
Integrating factor:
$$
\begin{align*}
\frac{N_x - M_y}{M} &= \frac{2xy^3}{2xy^3} = 1 = P(y) \\
\mu(y) &= e^{\int 1\,dy} = e^{y}
\end{align*}
$$
Potential function:
$$
\begin{align*}
\psi &= \int 2xy^3e^{y}\,dx = x^2y^3e^{y} + h(y) \\
\psi_y &= x^2\left(3y^2 + y^3\right)e^{y} + h'(y) \\
&\overset{!}{=} \left(3x^2y^2 + x^2y^3 + 1\right)e^{y} \\
h'(y) &= e^{y} \implies h(y) = e^{y}
\end{align*}
$$
$$
\boxed{\,e^{y}\left(x^2y^3 + 1\right) = c\,}
$$

## Solution set
- **General solution (implicit):** $e^{y}\left(x^2y^3 + 1\right) = C$, $C \in \mathbb{R}$.
- **Explicit in $x$:** $x = \pm\sqrt{\dfrac{Ce^{-y} - 1}{y^3}}$ where the radicand is $\geq 0$.
- **Constant solutions:** $y \equiv 0$ ($M = 2xy^3 = 0$ and $dy = 0$). It lies on the level set $C = 1$.
- **Note:** $\mu = e^{y}$ is never $0$, so nothing is added or lost.

## Graph
```desmos-graph
left=-4; right=4; top=3; bottom=-4
---
e^{y}\left(x^{2}y^{3}+1\right)=c
c=[-2,-0.5,0.5,1,3]
```

## Related topics
- [[Integrating Factors for Exact Equations]]
- [[Exact Equations]]

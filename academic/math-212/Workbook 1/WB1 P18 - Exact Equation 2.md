---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 18 (p. 13)
topics: ["[[Exact Equations]]", "[[Separable Equations]]"]
---
# Problem 18 — $6x^2y^2\,dx + 4x^3y\,dy = 0$
Back to [[academic/math-212/Index|Index]]

> [!question] Problem
> Find the general solution of $6x^2y^2\,dx + 4x^3y\,dy = 0$.

## Classification
- **Type:** ODE, first order, **nonlinear**
- **Method:** **exact** ($M_y = N_x$). It is also **separable**: dividing by $x^3y^2$ gives $\frac{6}{x}dx + \frac{4}{y}dy = 0$.

## Strategy
1. Check exactness.
2. Integrate $M$ with respect to $x$, then match $\psi_y$ with $N$.
3. Optionally, confirm with the separable approach.

## Solution
$$
\begin{align*}
M_y &= 12x^2y = N_x \quad\checkmark \\
\psi &= \int 6x^2y^2\,dx = 2x^3y^2 + h(y) \\
\psi_y &= 4x^3y + h'(y) = 4x^3y \implies h' = 0
\end{align*}
$$
$$
\boxed{\,x^3y^2 = C\,}
$$
**Check by separation:** $6\ln\lvert x\rvert + 4\ln\lvert y\rvert = c$ gives $x^6y^4 = C'$, which is the same family.

## Solution set
- **General solution (implicit):** $x^3y^2 = C$, $C \in \mathbb{R}$.
- **Explicit:** as $y' = -\dfrac{3y}{2x}$ (linear), $y(x) = K\lvert x\rvert^{-3/2}$, $K \in \mathbb{R}$, on $(0, \infty)$ **or** $(-\infty, 0)$.
- **Constant solutions:** $y \equiv 0$, included at $C = 0$ ($K = 0$).
- **Note:** in the separable check, $C' = e^{c} > 0$ at first, and $y \equiv 0$ was lost when dividing by $y^2$. It returns as $C' = 0$. Also $x \equiv 0$ solves the differential form, but it is not a function $y(x)$.

## Graph
```desmos-graph
left=-4; right=4; top=4; bottom=-4
---
x^{3}y^{2}=C
C=[-4,-1,1,4]
```

## Related topics
- [[Exact Equations]]
- [[Separable Equations]]

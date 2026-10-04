---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 17 (p. 12)
topics: ["[[Exact Equations]]"]
---
# Problem 17 — $(4x^3y^3 + 3x^2)\,dx + (3x^4y^2 + 6y^2)\,dy = 0$
Back to [Index](../Index.md)

> [!question] Problem
> Find the general solution of $(4x^3y^3 + 3x^2)\,dx + (3x^4y^2 + 6y^2)\,dy = 0$.

## Classification
- **Type:** ODE, first order, **nonlinear**
- **Form:** differential form $M\,dx + N\,dy = 0$
- **Method:** **exact**, since $M_y = N_x$ (checked below)

## Strategy
1. Identify $M$ and $N$ and check $M_y = N_x$.
2. $\psi = \int M\,dx + h(y)$.
3. Set $\psi_y = N$ to find $h'(y)$.
4. Write $\psi(x, y) = c$.

## Solution
$$
\begin{align*}
M &= 4x^3y^3 + 3x^2, & N &= 3x^4y^2 + 6y^2 \\
M_y &= 12x^3y^2, & N_x &= 12x^3y^2 \quad\checkmark\ \text{exact}
\end{align*}
$$
$$
\begin{align*}
\psi &= \int (4x^3y^3 + 3x^2)\,dx = x^4y^3 + x^3 + h(y) \\
\psi_y &= 3x^4y^2 + h'(y) = 3x^4y^2 + 6y^2 \\
h'(y) &= 6y^2 \implies h(y) = 2y^3
\end{align*}
$$
$$
\boxed{\,x^4y^3 + x^3 + 2y^3 = c\,}
$$

## Solution set
- **General solution (implicit):** $x^4y^3 + x^3 + 2y^3 = C$, $C \in \mathbb{R}$.
- **Explicit:** $y(x) = \sqrt[3]{\dfrac{C - x^3}{x^4 + 2}}$ (real cube root), $C \in \mathbb{R}$.
- **Constant solutions:** none. $y \equiv k$ would need $4x^3k^3 + 3x^2 = 0$ for all $x$.
- **Note:** $N = 3y^2(x^4 + 2) = 0$ when $y = 0$, that is at $x = \sqrt[3]{C}$. The tangent is vertical there, so each curve gives a solution $y(x)$ on $(-\infty, \sqrt[3]{C})$ and another on $(\sqrt[3]{C}, \infty)$.

## Graph
Level curves of $\psi(x, y) = x^4y^3 + x^3 + 2y^3$:
```desmos-graph
left=-3; right=3; top=3; bottom=-3
---
x^{4}y^{3}+x^{3}+2y^{3}=c
c=[-4,-1,0,1,4]
```

## Related topics
- [Exact Equations](../Topics/Exact%20Equations.md)

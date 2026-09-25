---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 17 (p. 12)
topics: ["[[Exact Equations]]"]
---
# Problem 17 — $(4x^3y^3 + 3x^2)\,dx + (3x^4y^2 + 6y^2)\,dy = 0$
Back to [[Index]]

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

## Graph
Level curves of $\psi(x, y) = x^4y^3 + x^3 + 2y^3$:
```desmos-graph
left=-3; right=3; top=3; bottom=-3
---
x^{4}y^{3}+x^{3}+2y^{3}=c
c=[-4,-1,0,1,4]
```

## Related topics
- [[Exact Equations]]

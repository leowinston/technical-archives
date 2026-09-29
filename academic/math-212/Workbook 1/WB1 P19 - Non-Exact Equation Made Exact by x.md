---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 19 (pp. 13–14)
topics: ["[[Exact Equations]]", "[[Integrating Factors for Exact Equations]]"]
---
# Problem 19 — $(3x + 2y^2)\,dx + 2xy\,dy = 0$
Back to [[academic/math-212/Index|Index]]

> [!question] Problem
> Given $(3x + 2y^2)\,dx + 2xy\,dy = 0$:
> (a) Show that the equation is not exact.
> (b) Attempt to find the general solution.
> (c) Multiply the equation by $x$ and find the general solution.

## Classification
- **Type:** ODE, first order, **nonlinear**
- **Method:** **not exact**. It becomes exact after multiplying by the integrating factor $\mu(x) = x$.

## Strategy
1. Compare $M_y$ and $N_x$.
2. Run the exact-equation procedure anyway and watch it fail: $h'$ will depend on $x$.
3. Multiply by $x$, check exactness again, and solve.
4. (Where does $\mu = x$ come from? $\dfrac{M_y - N_x}{N} = \dfrac{1}{x}$, so $\mu = e^{\int dx/x} = x$.)

## Solution
**(a)**
$$
\begin{align*}
M_y &= 4y, \qquad N_x = 2y \\
M_y &\neq N_x \implies \text{not exact}
\end{align*}
$$

**(b)** Try the procedure anyway:
$$
\begin{align*}
\psi &= \int (3x + 2y^2)\,dx = \frac{3}{2}x^2 + 2xy^2 + h(y) \\
\psi_y &= 4xy + h'(y) \overset{?}{=} 2xy \\
h'(y) &= -2xy
\end{align*}
$$
This fails: $h'$ must depend only on $y$, but it depends on $x$. No potential function $\psi$ exists.

**(c)** Multiply by $x$:
$$
\begin{align*}
(3x^2 + 2xy^2)\,dx + 2x^2y\,dy &= 0 \\
\tilde M_y = 4xy, \quad \tilde N_x &= 4xy \quad\checkmark\ \text{exact} \\
\psi &= \int (3x^2 + 2xy^2)\,dx = x^3 + x^2y^2 + h(y) \\
\psi_y &= 2x^2y + h'(y) = 2x^2y \implies h' = 0
\end{align*}
$$
$$
\boxed{\,x^3 + x^2y^2 = c\,}
$$
Solving for $y$ (for $x \neq 0$): $y = \pm\sqrt{\dfrac{c - x^3}{x^2}}$.

## Solution set
- **General solution (implicit):** $x^3 + x^2y^2 = C$, $C \in \mathbb{R}$.
- **Explicit:** $y(x) = \pm\dfrac{\sqrt{C - x^3}}{\lvert x\rvert}$, valid for $x < \sqrt[3]{C}$, $x \neq 0$. Each sign and each side of $x = 0$ is a separate solution.
- **Constant solutions:** none. $y \equiv k$ would need $3x + 2k^2 = 0$ for all $x$.
- **Note:** multiplying by $\mu = x$ can add the curve $x = 0$ (it sits inside $C = 0$). $x \equiv 0$ does solve the original differential form, but it is not a function $y(x)$.

## Graph
```desmos-graph
left=-4; right=4; top=4; bottom=-4
---
x^{3}+x^{2}y^{2}=c
c=[-4,-1,1,4,8]
```

## Related topics
- [[Exact Equations]]
- [[Integrating Factors for Exact Equations]]

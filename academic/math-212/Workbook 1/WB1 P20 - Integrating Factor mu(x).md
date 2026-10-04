---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 20 (p. 15)
topics: ["[[Integrating Factors for Exact Equations]]", "[[Exact Equations]]"]
---
# Problem 20 — $(2xy^3 - 2x^3y^3 - 4xy^2 + 2x)\,dx + (3x^2y^2 + 4y)\,dy = 0$
Back to [Index](../Index.md)

> [!question] Problem
> Find the general solution of $(2xy^3 - 2x^3y^3 - 4xy^2 + 2x)\,dx + (3x^2y^2 + 4y)\,dy = 0$.

## Classification
- **Type:** ODE, first order, **nonlinear**
- **Method:** **not exact**. $\dfrac{M_y - N_x}{N}$ depends only on $x$, so an **integrating factor $\mu(x)$** works.

## Strategy
1. Compute $M_y - N_x$.
2. Divide by $N$ and look for a common factor that cancels, leaving a function of $x$ alone.
3. $\mu(x) = e^{\int Q(x)\,dx}$.
4. Multiply through. Start $\psi$ from $\int \tilde N\,dy$, because $\tilde N$ is simpler.
5. Match $\psi_x$ with $\tilde M$ to find $g(x)$.

## Solution
Exactness test:
$$
\begin{align*}
M_y &= 6xy^2 - 6x^3y^2 - 8xy \\
N_x &= 6xy^2 \\
M_y - N_x &= -6x^3y^2 - 8xy = -2x\left(3x^2y^2 + 4y\right)
\end{align*}
$$
Integrating factor:
$$
\begin{align*}
\frac{M_y - N_x}{N} &= \frac{-2x\left(3x^2y^2 + 4y\right)}{3x^2y^2 + 4y} = -2x \\
\mu(x) &= e^{\int -2x\,dx} = e^{-x^2}
\end{align*}
$$
Potential function, starting from $\tilde N = e^{-x^2}(3x^2y^2 + 4y)$:
$$
\begin{align*}
\psi &= \int e^{-x^2}\left(3x^2y^2 + 4y\right)dy = e^{-x^2}\left(x^2y^3 + 2y^2\right) + g(x) \\
\psi_x &= -2xe^{-x^2}\left(x^2y^3 + 2y^2\right) + e^{-x^2}\left(2xy^3\right) + g'(x) \\
&= e^{-x^2}\left(2xy^3 - 2x^3y^3 - 4xy^2\right) + g'(x)
\end{align*}
$$
Setting $\psi_x = \tilde M = e^{-x^2}\left(2xy^3 - 2x^3y^3 - 4xy^2 + 2x\right)$:
$$
\begin{align*}
g'(x) &= 2xe^{-x^2} \implies g(x) = -e^{-x^2}
\end{align*}
$$
$$
\boxed{\,e^{-x^2}\left(x^2y^3 + 2y^2 - 1\right) = c\,}
$$

## Solution set
- **General solution (implicit):** $e^{-x^2}\left(x^2y^3 + 2y^2 - 1\right) = C$, $C \in \mathbb{R}$.
- **Constant solutions:** none. $y \equiv k$ would need $M = 0$ for all $x$. The $x^3$ coefficient forces $k = 0$, but then $M = 2x \neq 0$.
- **Note:** $\mu = e^{-x^2}$ is never $0$, so multiplying by it neither adds nor removes solutions.

## Graph
```desmos-graph
left=-3; right=3; top=3; bottom=-3
---
e^{-x^{2}}\left(x^{2}y^{3}+2y^{2}-1\right)=c
c=[-0.8,-0.3,0,0.5,2]
```

## Related topics
- [Integrating Factors for Exact Equations](../Topics/Integrating%20Factors%20for%20Exact%20Equations.md)
- [Exact Equations](../Topics/Exact%20Equations.md)

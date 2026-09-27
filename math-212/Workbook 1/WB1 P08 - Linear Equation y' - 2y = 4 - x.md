---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 8 (p. 6)
topics: ["[[Linear First-Order Equations]]"]
---
# Problem 8 — $y' - 2y = 4 - x$
Back to [[Index]]

> [!question] Problem
> Given $y' - 2y = 4 - x$:
> (a) Classify the equation.
> (b) Find the general solution $y = y(x, c)$.

## Classification
- **Type:** ODE, first order
- **Linearity:** **linear, nonhomogeneous**
- **Coefficients:** constant ($p = -2$), with a polynomial right side $g = 4 - x$
- **Standard form:** already $y' + p y = g$ with $p(x) = -2$

## Strategy
1. Integrating factor: $\mu = e^{\int -2\,dx} = e^{-2x}$.
2. Multiply through so the left side becomes $\left(e^{-2x}y\right)'$.
3. Integrate $(4 - x)e^{-2x}$ **by parts**.
4. Divide by $\mu$ and check the answer.

## Solution
$$
\begin{align*}
\mu &= e^{-2x} \\
\left(e^{-2x}y\right)' &= (4 - x)e^{-2x} \\
e^{-2x}y &= \int (4 - x)e^{-2x}\,dx
\end{align*}
$$
By parts, with $u = 4 - x$ and $dv = e^{-2x}dx$:
$$
\begin{align*}
\int (4 - x)e^{-2x}\,dx &= -\frac{1}{2}(4 - x)e^{-2x} - \frac{1}{2}\int e^{-2x}\,dx \\
&= -\frac{1}{2}(4 - x)e^{-2x} + \frac{1}{4}e^{-2x} + c
\end{align*}
$$
Divide by $e^{-2x}$:
$$
\begin{align*}
y &= -2 + \frac{x}{2} + \frac{1}{4} + ce^{2x} \\
\boxed{\,y = \frac{x}{2} - \frac{7}{4} + ce^{2x}\,}
\end{align*}
$$
**Check:** $y' - 2y = \tfrac{1}{2} + 2ce^{2x} - x + \tfrac{7}{2} - 2ce^{2x} = 4 - x \checkmark$

Only $c = 0$ gives a bounded solution as $x \to \infty$: the line $y = \tfrac{x}{2} - \tfrac{7}{4}$. Every other solution moves away from it.

## Solution set
- **General solution:** $y(x) = \dfrac{x}{2} - \dfrac{7}{4} + Ce^{2x}$, $C \in \mathbb{R}$, $x \in \mathbb{R}$.
- **Constant solutions:** none. $y \equiv k$ would need $-2k = 4 - x$ for all $x$.

## Graph
```desmos-graph
left=-6; right=4; top=4; bottom=-6
---
y=\frac{x}{2}-\frac{7}{4}+ce^{2x}
c=[-0.1,-0.01,0.01,0.1]
y=\frac{x}{2}-\frac{7}{4}|dashed|#000000
```

## Related topics
- [[Linear First-Order Equations]]

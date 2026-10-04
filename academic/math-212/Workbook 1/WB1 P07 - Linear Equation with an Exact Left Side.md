---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 7 (p. 6)
topics: ["[[Linear First-Order Equations]]"]
---
# Problem 7 — $(4 + x^2)y' + 2xy = 4x$
Back to [Index](../Index.md)

> [!question] Problem
> Given $(4 + x^2)y' + 2xy = 4x$:
> (a) Classify the equation.
> (b) Find the general solution $y = y(x, c)$.

## Classification
- **Type:** ODE, first order
- **Linearity:** **linear, nonhomogeneous** ($g = 4x \neq 0$)
- **Coefficients:** variable
- **Standard form:** $y' + \dfrac{2x}{4 + x^2}y = \dfrac{4x}{4 + x^2}$, with $p$ and $g$ continuous for all $x$

## Strategy
1. Notice that the left side is already a derivative: $\dfrac{d}{dx}(4 + x^2) = 2x$. So $(4 + x^2)y' + 2xy = \left[(4 + x^2)y\right]'$.
2. Integrate both sides directly.
3. (The integrating factor method gives the same result: $\mu = e^{\int \frac{2x}{4 + x^2}dx} = 4 + x^2$.)

## Solution
$$
\begin{align*}
\frac{d}{dx}\left[(4 + x^2)y\right] &= 4x \\
(4 + x^2)y &= 2x^2 + c \\
y &= \frac{2x^2 + c}{4 + x^2}
\end{align*}
$$
Every solution tends to $2$ as $x \to \pm\infty$. By Theorem 2.4.1, each solution exists on all of $\mathbb{R}$.

## Solution set
- **General solution:** $y(x) = \dfrac{2x^2 + C}{4 + x^2}$, $C \in \mathbb{R}$, $x \in \mathbb{R}$.
- **Constant solutions:** $y \equiv k$ requires $2xk = 4x$ for all $x$, so $k = 2$. It is included at $C = 8$: $\dfrac{2x^2 + 8}{4 + x^2} = 2$.

## Graph
```desmos-graph
left=-8; right=8; top=4; bottom=-3
---
y=\frac{2x^{2}+c}{4+x^{2}}
c=[-8,-4,0,4,8,12]
y=2|dashed|#000000
```

## Related topics
- [Linear First-Order Equations](../Topics/Linear%20First-Order%20Equations.md)
- [Existence and Uniqueness Theorems](../Topics/Existence%20and%20Uniqueness%20Theorems.md)

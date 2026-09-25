---
tags: [math-212, topic, chapter-2]
---
# Homogeneous Substitution
Back to [[Index]] · Chapter 2.2

> [!warning] Two meanings of "homogeneous"
> This note uses **homogeneous** to mean $f(x, y)$ depends only on $y/x$. That is different from a homogeneous *linear* equation, where $g = 0$ (see [[Classification of Differential Equations]]).

$$
\frac{dy}{dx} = F\!\left(\frac{y}{x}\right)
$$

Substitute $y = xv(x)$, so $y' = v + xv'$:
$$
\begin{align*}
v + x\frac{dv}{dx} &= F(v) \\
\frac{dv}{F(v) - v} &= \frac{dx}{x}
\end{align*}
$$
The result is separable (see [[Separable Equations]]). Solve for $v$, then substitute back $v = y/x$.

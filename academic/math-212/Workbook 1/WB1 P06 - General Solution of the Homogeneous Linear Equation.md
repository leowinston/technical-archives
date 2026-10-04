---
tags: [math-212, problem, workbook-1, proof]
source: Workbook Part 1, Problem 6 (p. 5)
topics: ["[[Linear First-Order Equations]]", "[[Existence and Uniqueness Theorems]]"]
---
# Problem 6 — General Solution of $y' + p(x)y = 0$
Back to [Index](../Index.md)

> [!question] Problem
> Prove: if $p$ is continuous on $(a, b)$, then the general solution of the homogeneous equation $y' + p(x)y = 0$ on $(a, b)$ is
> $$y = ce^{-\int p(x)\,dx}$$
> *Hints:* (a) show that it is a solution for any $c$; (b) show that **any** solution can be written in this form.

## Classification
- **Type:** ODE, first order, **linear, homogeneous**, variable coefficient
- **Kind of problem:** proof. There are two directions: the formula gives solutions, and every solution has this form.

## Strategy
1. Let $P(x)$ be an antiderivative of $p$. It exists because $p$ is continuous, and $P' = p$.
2. **(a)** Differentiate $ce^{-P}$ and substitute it into the equation.
3. **(b)** Take an arbitrary solution $y$ and look at $u = ye^{P}$. Show $u' = 0$, so $u$ is constant.
4. Use the fact that $(a, b)$ is an **interval**: a function with zero derivative on an interval is constant, by the Mean Value Theorem.

## Solution
Let $P(x) = \int p(x)\,dx$, so $P'(x) = p(x)$ on $(a, b)$.

**(a) Every function of the form $y = ce^{-P}$ is a solution.**
$$
\begin{align*}
y' &= c\cdot\left(-P'(x)\right)e^{-P(x)} = -p(x)\,ce^{-P(x)} = -p(x)y \\
\implies y' + p(x)y &= 0 \checkmark
\end{align*}
$$

**(b) Every solution has this form.** Let $y$ be any solution on $(a, b)$ and set $u(x) = y(x)e^{P(x)}$:
$$
\begin{align*}
u' &= y'e^{P} + y\,p\,e^{P} \\
&= e^{P}\left(y' + p(x)y\right) \\
&= e^{P}\cdot 0 = 0
\end{align*}
$$
So $u \equiv c$ on $(a, b)$ by the Mean Value Theorem, and therefore
$$
y = ce^{-P(x)} = ce^{-\int p(x)\,dx} \qquad \blacksquare
$$

## Solution set
- **General solution:** $y(x) = Ce^{-\int p(x)\,dx}$, $C \in \mathbb{R}$, $x \in (a, b)$.
- **Constant solutions:** $y \equiv 0$ ($C = 0$). A nonzero constant works only where $p \equiv 0$.
- **Note:** here $C$ comes from $u' = 0$, so $C \in \mathbb{R}$ directly. Part (b) proves nothing is missing, unlike the separable case.

## Graph
An example with $p(x) = x$, so $y = ce^{-x^2/2}$:
```desmos-graph
left=-4; right=4; top=3; bottom=-3
---
y=ce^{-\frac{x^{2}}{2}}
c=[-2,-1,0,1,2]
```

## Related topics
- [Linear First-Order Equations](../Topics/Linear%20First-Order%20Equations.md)
- [Existence and Uniqueness Theorems](../Topics/Existence%20and%20Uniqueness%20Theorems.md)
- [Variation of Parameters](../Topics/Variation%20of%20Parameters.md) (uses this result as $y_1$)

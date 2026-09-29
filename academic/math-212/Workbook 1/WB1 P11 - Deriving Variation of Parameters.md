---
tags: [math-212, problem, workbook-1, derivation]
source: Workbook Part 1, Problem 11 (p. 8)
topics: ["[[Variation of Parameters]]"]
---
# Problem 11 — Method of Variation of Parameters
Back to [[academic/math-212/Index|Index]]

> [!question] Problem
> Given $y' + p(x)y = f(x)$, find the general solution in the form $y = y_1u$, where $y_1$ is a solution of the complementary equation.

## Classification
- **Type:** ODE, first order, **linear, nonhomogeneous**
- **Kind of problem:** derivation

## Strategy
1. Solve the complementary equation $y_1' + py_1 = 0$ (see [[WB1 P06 - General Solution of the Homogeneous Linear Equation|Problem 6]]).
2. Replace the constant $c$ in $cy_1$ by a function $u(x)$.
3. Substitute $y = uy_1$. The $u$ terms cancel because $y_1$ solves the homogeneous equation.
4. Solve the simple equation left over for $u'$ and integrate.

## Solution
Complementary solution:
$$
y_1 = e^{-\int p(x)\,dx}, \qquad y_1' + py_1 = 0
$$
Substitute $y = uy_1$:
$$
\begin{align*}
y' + py &= u'y_1 + uy_1' + puy_1 \\
&= u'y_1 + u\underbrace{\left(y_1' + py_1\right)}_{=0} \\
&= u'y_1 = f
\end{align*}
$$
So:
$$
\begin{align*}
u' &= \frac{f(x)}{y_1(x)} \\
u &= \int \frac{f(x)}{y_1(x)}\,dx + c \\
y &= y_1(x)\left[\int \frac{f(x)}{y_1(x)}\,dx + c\right]
\end{align*}
$$
Since $1/y_1 = e^{\int p} = \mu$, this matches the integrating factor formula from [[WB1 P09 - Deriving the Integrating Factor|Problem 9]].

## Solution set
- **General solution:** $y(x) = y_1(x)\left[\displaystyle\int \dfrac{f(x)}{y_1(x)}\,dx + C\right]$, $C \in \mathbb{R}$, with $y_1 = e^{-\int p\,dx}$.
- **Note:** $y_1$ is **one** fixed nonzero solution of the complementary equation, so its own constant is set to $1$. The free constant is the $C$ from integrating $u'$.

## Graph
The general solution splits as $y = cy_1 + y_p$. For example, with $y' + y = 1$: $y_1 = e^{-x}$ and $y = 1 + ce^{-x}$. The complementary part is dashed and the particular solution $y_p = 1$ is black.
```desmos-graph
left=-2; right=5; top=4; bottom=-3
---
y=1+ce^{-x}
c=[-2,-1,1,2]
y=ce^{-x}|dashed
y=1|#000000
```

## Related topics
- [[Variation of Parameters]]
- [[Linear First-Order Equations]]

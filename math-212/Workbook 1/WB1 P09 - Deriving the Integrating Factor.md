---
tags: [math-212, problem, workbook-1, derivation]
source: Workbook Part 1, Problem 9 (p. 7)
topics: ["[[Linear First-Order Equations]]"]
---
# Problem 9 — Method of Integrating Factors
Back to [[Index]]

> [!question] Problem
> Given $y' + p(x)y = f(x)$, find a general formula for an integrating factor $\mu(x)$.

## Classification
- **Type:** ODE, first order, **linear**, in standard form
- **Kind of problem:** derivation

## Strategy
1. Multiply both sides by an unknown $\mu(x)$.
2. **Require** that the left side equal $(\mu y)'$ by the product rule.
3. Compare the two expressions. That gives a separable equation for $\mu$.
4. Solve for $\mu$. Any nonzero multiple works, so drop the constant.

## Solution
Multiply through by $\mu$:
$$
\mu y' + \mu p y = \mu f
$$
We want the left side to equal $(\mu y)' = \mu y' + \mu' y$. Comparing:
$$
\begin{align*}
\mu' y &= \mu p y \\
\frac{\mu'}{\mu} &= p(x) \\
\ln\mu &= \int p(x)\,dx \\
\mu(x) &= e^{\int p(x)\,dx}
\end{align*}
$$
The equation becomes $(\mu y)' = \mu f$, so
$$
y = \frac{1}{\mu(x)}\left[\int \mu(x)f(x)\,dx + c\right]
$$

## Graph
An example: $y' + 2xy = 2x$ gives $\mu = e^{x^2}$, so $(e^{x^2}y)' = 2xe^{x^2}$ and $y = 1 + ce^{-x^2}$.
```desmos-graph
left=-4; right=4; top=4; bottom=-2
---
y=1+ce^{-x^{2}}
c=[-2,-1,0,1,2]
```

## Related topics
- [[Linear First-Order Equations]]
- [[Variation of Parameters]]
- [[Integrating Factors for Exact Equations]] (the same idea for exact equations)

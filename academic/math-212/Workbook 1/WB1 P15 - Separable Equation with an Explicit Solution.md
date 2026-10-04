---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 15 (p. 10)
topics: ["[[Separable Equations]]", "[[Existence and Uniqueness Theorems]]"]
---
# Problem 15 — $y' = \tfrac{1}{2}x(1 - y^2)$
Back to [Index](../Index.md)

> [!question] Problem
> Classify the equation $y' = \tfrac{1}{2}x(1 - y^2)$ and find its general solution in explicit form.

## Classification
- **Type:** ODE, first order
- **Linearity:** **nonlinear** ($y^2$)
- **Method:** **separable**, $g(x) = \tfrac{x}{2}$ and $h(y) = 1 - y^2$
- **Equilibria:** $y \equiv 1$ and $y \equiv -1$

## Strategy
1. Record the equilibria $y = \pm 1$ before dividing by $1 - y^2$.
2. Separate the variables and use partial fractions: $\dfrac{1}{1 - y^2} = \dfrac{1}{2}\left(\dfrac{1}{1 + y} + \dfrac{1}{1 - y}\right)$.
3. Exponentiate, absorb $\pm e^{c}$ into a single constant $C$, and solve for $y$ algebraically.
4. Check which equilibria the formula includes. List any it misses separately.

## Solution
$$
\begin{align*}
\frac{dy}{1 - y^2} &= \frac{x}{2}\,dx \\
\frac{1}{2}\ln\left\lvert\frac{1 + y}{1 - y}\right\rvert &= \frac{x^2}{4} + c_1 \\
\frac{1 + y}{1 - y} &= Ce^{x^2/2}
\end{align*}
$$
Solve for $y$:
$$
\begin{align*}
1 + y &= Ce^{x^2/2}(1 - y) \\
y\left(1 + Ce^{x^2/2}\right) &= Ce^{x^2/2} - 1 \\
\boxed{\,y = \frac{Ce^{x^2/2} - 1}{Ce^{x^2/2} + 1}\,}
\end{align*}
$$
- **Range of $C$.** From the derivation, $C = \pm e^{2c_1}$, so $C \neq 0$. Dividing by $1 - y^2$ assumed $y \neq \pm 1$, so the derivation only produces the non-constant solutions.
- **$y \equiv -1$.** Found separately as an equilibrium, not from the derivation. It happens to match the formula at $C = 0$, so we extend the range to $C \in \mathbb{R}$ to cover it. $C = 0$ is not reached by any $c_1$, and nothing about $x \to -\infty$ is involved.
- **$y \equiv 1$.** Also an equilibrium. No real $C$ gives it, so the formula misses it and we list it separately. The "$C \to \infty$" limit is only a heuristic for why it's missing.
- Which equilibrium gets missed depends on the parametrization. With $D = 1/C$, $y = \dfrac{1 - De^{-x^2/2}}{1 + De^{-x^2/2}}$: now $D = 0$ gives $y = 1$ and $y = -1$ is the missing one. Since $f(x,y) = \tfrac{1}{2}x(1-y^2)$ is smooth, uniqueness holds everywhere, so neither is a singular solution in the strict sense (a solution where uniqueness fails).
- For $C > 0$, the formula equals $y = \tanh\left(\dfrac{x^2}{4} + k\right)$ with $C = e^{2k}$.

## Solution set
- **General solution:** $y(x) = \dfrac{Ce^{x^2/2} - 1}{Ce^{x^2/2} + 1}$, $C \in \mathbb{R}$.
- **Constant solutions:** $y \equiv -1$ (included at $C = 0$) and $y \equiv 1$ (not included; list separately).
- **Interval of existence** (where $Ce^{x^2/2} + 1 \neq 0$):
  - $C \geq 0$: all $x \in \mathbb{R}$, with $-1 \leq y < 1$.
  - $-1 < C < 0$: the denominator vanishes at $x = \pm x^\star$, $x^\star = \sqrt{2\ln(-1/C)}$. The solution through $x = 0$ lives on $(-x^\star, x^\star)$ with $y < -1$. The pieces on $x > x^\star$ and $x < -x^\star$ are separate solutions with $y > 1$.
  - $C = -1$: blows up at $x = 0$, giving one solution on $(-\infty, 0)$ and one on $(0, \infty)$, both with $y > 1$.
  - $C < -1$: the denominator is always negative, so the solution exists on all of $\mathbb{R}$, with $y > 1$ and $y \to 1$ as $x \to \pm\infty$.

## Graph
Solutions with $C \geq 0$ stay between $-1$ and $1$. Solutions with $-1 \leq C < 0$ blow up at finite $x$. Solutions with $C < -1$ stay above $y = 1$.
```desmos-graph
left=-5; right=5; top=4; bottom=-4
---
y=\frac{Ce^{\frac{x^{2}}{2}}-1}{Ce^{\frac{x^{2}}{2}}+1}
C=[-3,-0.5,0,0.05,0.5,3]
y=1|dashed|#000000
y=-1|dashed|#000000
```

## Related topics
- [Separable Equations](../Topics/Separable%20Equations.md)
- [Existence and Uniqueness Theorems](../Topics/Existence%20and%20Uniqueness%20Theorems.md)

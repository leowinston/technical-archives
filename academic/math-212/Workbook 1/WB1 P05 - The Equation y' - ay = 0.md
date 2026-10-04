---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 5 (p. 4)
topics: ["[[Linear First-Order Equations]]", "[[Exponential Growth]]"]
---
# Problem 5 — The Equation $y' - ay = 0$
Back to [Index](../Index.md)

> [!question] Problem
> Let $a$ be a constant.
> (a) Guess the general solution of $y' - ay = 0$.
> (b) Solve the initial value problem with $y(x_0) = y_0$.

## Classification
- **Type:** ODE, first order, **linear, homogeneous**, constant coefficient
- **Also:** autonomous and separable

## Strategy
1. The equation says $y' = ay$: the derivative is proportional to the function, so guess $y = e^{ax}$.
2. Multiplying a solution by a constant still gives a solution, so the general solution is $y = ce^{ax}$.
3. Use $y(x_0) = y_0$ to find $c$.

## Solution
**(a)**
$$
\begin{align*}
y &= ce^{ax} \\
\text{check: } y' - ay &= ace^{ax} - ace^{ax} = 0 \checkmark
\end{align*}
$$

**(b)**
$$
\begin{align*}
y_0 &= ce^{ax_0} \implies c = y_0e^{-ax_0} \\
y &= y_0e^{a(x - x_0)}
\end{align*}
$$

## Solution set
- **General solution:** $y(x) = Ce^{ax}$, $C \in \mathbb{R}$, $x \in \mathbb{R}$.
- **IVP:** $C = y_0e^{-ax_0}$, which can be any real number, so every IVP is covered.
- **Constant solutions:** $y \equiv 0$, included at $C = 0$. If $a = 0$, every constant $y \equiv C$ is a solution.
- **Note:** solving by separation instead gives $C = \pm e^{c} \neq 0$ at first. $y \equiv 0$ is lost when dividing by $y$ and put back as $C = 0$ (same situation as [Problem 15](WB1%20P15%20-%20Separable%20Equation%20with%20an%20Explicit%20Solution.md)).

## Graph
Solutions through $(x_0, y_0) = (1, 1)$ for $a \in \{-1, -0.5, 0, 0.5, 1\}$:
```desmos-graph
left=-3; right=4; top=6; bottom=-1
---
y=y_{0}e^{a\left(x-x_{0}\right)}
a=[-1,-0.5,0,0.5,1]
x_{0}=1
y_{0}=1
(x_{0},y_{0})|#000000
```

## Related topics
- [Linear First-Order Equations](../Topics/Linear%20First-Order%20Equations.md)
- [Exponential Growth](../Topics/Exponential%20Growth.md)

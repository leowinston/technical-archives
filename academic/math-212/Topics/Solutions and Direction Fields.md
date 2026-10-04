---
tags: [math-212, topic, chapter-1]
---
# Solutions and Direction Fields
Back to [Index](../Index.md) · Chapter 1.2

- A **solution** of $y' = f(t, y)$ on an interval $I$ is a differentiable function $y = \phi(t)$ with $\phi'(t) = f(t, \phi(t))$ for every $t \in I$.
- The **general solution** is a family of solutions with an arbitrary constant $c$. An initial condition $y(t_0) = y_0$ picks one member of the family.
- An **integral curve** is the graph of a solution.
- A **direction field** draws a short segment with slope $f(t, y)$ at each grid point. Integral curves are tangent to these segments everywhere.

## Direct integration
When the right side depends only on the independent variable, integrate:
$$
\begin{align*}
y' = f(x) \implies y = \int f(x)\,dx + c
\end{align*}
$$
An $n$-th order equation $y^{(n)} = f(x)$ needs $n$ integrations and has $n$ arbitrary constants.

## Workbook problems
- [WB1 P02 - Direct Integration of y'' = 3x + 1](../Workbook%201/WB1%20P02%20-%20Direct%20Integration%20of%20y%27%27%20%3D%203x%20%2B%201.md)
- [WB1 P04 - Direct Integration of First-Order Equations](../Workbook%201/WB1%20P04%20-%20Direct%20Integration%20of%20First-Order%20Equations.md)

---
tags: [convex-optimization, topic, ch-1]
source: Boyd & Vandenberghe §1.1 (pp. 1–3)
---
# Mathematical Optimization
Back to [[self-study/convex-optimization/Index|Index]] · Section 1.1

## Standard problem
$$
\begin{array}{ll}
\text{minimize} & f_0(x) \\
\text{subject to} & f_i(x) \le b_i, \quad i = 1, \dots, m
\end{array}
$$
$x \in \R^n$ is the **optimization variable**, $f_0$ the **objective**, $f_i$ the **constraints**. $x^\star$ is **optimal** if it has the smallest objective value among all feasible $x$.

## Problem classes
The class is set by the form of the $f_i$. It is **linear** when
$$
f_i(\alpha x + \beta y) = \alpha f_i(x) + \beta f_i(y),
$$
and **convex** when this only has to hold as $\le$ for $\alpha + \beta = 1$, $\alpha, \beta \ge 0$.

## Solvability
> [!important] ✎ Highlighted: "exceptions"
> The general problem is **hard**. Methods either take a very long time or may not find the solution. The *exceptions* are a few classes that can be solved reliably and efficiently: least-squares, linear programs, and convex problems.

See also: [[Least-Squares and Linear Programming]], [[Convex Optimization Overview]]
